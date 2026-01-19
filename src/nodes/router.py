from src.state.schema import AgentState

import yaml
from pathlib import Path

from typing import Dict

def router_node(state: AgentState) -> AgentState:
    """
    工作流程路由器 → 決定下一步（Decision Agent 參與決策）

    輸入: state 整體狀態
    輸出: dict，包含 next node 名稱

    路由邏輯:
    - "resume_parser": 履歷未解析
    - "job_matcher": 履歷已解析但未匹配
    - "conversation": 需要對話回應
    - "decision_agent": 進入決策智能體
    - "__end__": 工作流程結束
    """
    config_path = Path("config/config.yaml")
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        max_turn = config.get("conversation", {}).get("max_turn_count", 3)
        end_status = config.get("workflow", {}).get("end_status", "__end__")
    else:
        max_turn = 3
        end_status = "__end__"

    # 決策智能體參與分流
    from src.decision.decision_agent import run_decision_agent

    if state["job_state"].get("status") == "empty":
        state["next_action"] = "finalizer"
        return state

    # 若已完成履歷解析與職缺匹配，進入 decision agent 決策
    if (
        state["user_profile"].get("parsed_at")
        and state["job_state"].get("matched_jobs")
        and not state.get("decision_result")
    ):
        # 模擬分數，可根據 state 實際內容設計
        raw_scores = {
            "skill_match": state["user_profile"].get("skill_score", 60),
            "experience_match": state["user_profile"].get("exp_score", 70),
            "preference_match": state["user_profile"].get("pref_score", 65)
        }
        weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
        decision_result = run_decision_agent(
            case_id=state.get("session_id", "default"),
            raw_scores=raw_scores,
            weights=weights,
            normalization_method="min-max"
        )
        state["decision_result"] = decision_result
        # 根據決策分數分流
        if decision_result["final_score"] > 0.8:
            state["next_action"] = "skill_analyzer"
        elif decision_result["final_score"] > 0.6:
            state["next_action"] = "recommendation"
        elif decision_result["final_score"] < 0.4:
            state["next_action"] = "conversation"
        else:
            state["next_action"] = "finalizer"
        return state

    if not state["user_profile"].get("parsed_at"):
        state["conversation"]["current_intent"] = "general"
        state["next_action"] = "resume_parser"
    elif not state["job_state"].get("matched_jobs"):
        state["conversation"]["current_intent"] = "job_search"
        state["next_action"] = "job_matcher"
    elif state["conversation"]["current_intent"] == "skill_analysis":
        state["next_action"] = "conversation"
    elif state["conversation"]["turn_count"] < max_turn:
        state["conversation"]["current_intent"] = "general"
        state["next_action"] = "conversation"
    else:
        state["next_action"] = "finalizer"
    return state

def error_handler_node(state: AgentState) -> AgentState:
    """
    錯誤處理與重試 → SystemState

    輸入: state["system"]["error_message"]
    輸出: 更新 retry_count, workflow_status

    處理流程:
    1. 檢查 error_message
    2. 判斷是否需要重試
    3. 超過3次則標記失敗

    重試策略:
    - 最多重試 3 次
    - 超過則 workflow_status = "failed"
    """
    if not state["system"].get("retry_count"):
        state["system"]["retry_count"] = 0
    if state["system"].get("error_message"):
        state["system"]["retry_count"] += 1
        if state["system"]["retry_count"] > 3:
            state["system"]["workflow_status"] = "failed"
        else:
            state["system"]["workflow_status"] = "retrying"
    else:
        state["system"]["workflow_status"] = "ok"
    state["system"]["current_node"] = "error_handler"
    return state

def finalizer_node(state: AgentState) -> AgentState:
    """
    工作流程結束 → is_complete=True

    輸入: state 整體狀態
    輸出: state["is_complete"] = True

    處理流程:
    1. 標記完成
    2. 更新 workflow_status
    """
    state["is_complete"] = True
    state["system"]["workflow_status"] = "completed"
    state["system"]["current_node"] = "finalizer"
    return state
