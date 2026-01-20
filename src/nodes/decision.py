from src.state.schema import AgentState
import yaml
from pathlib import Path

def decision_node(state: AgentState) -> AgentState:
    """
    Accrording to the state['decision_result'], decide the next action.
    """
    print(state["conversation"]['current_intent'])
    # waiting for manual review
    if state.get("system", {}).get("manual_review_status") == "pending":
        if "conversation" in state and "messages" in state["conversation"]:
            state["conversation"]["messages"].append({
                "role": "assistant",
                "content": "請稍候，人工審核中，審核完成後會自動通知您。"
            })
        state["next_action"] = "finalizer"
        return state

    # manual review logic
    if state.get("next_action") == "manual_review":
        state["next_action"] = "finalizer"
        return state
    
    # error_handle_node logic
    error_msg = state.get("system", {}).get("error_message", "")
    if error_msg:
        if "已超過最大重試次數" in error_msg:
            state['next_action'] = 'finalizer'
            state["system"]["current_node"] = "decision"
            return state
        else:
            state["next_action"] = "conversation"
        state["system"]["error_message"] = ""
        return state
    
    # Load configiuration
    config_path = Path("config/config.yaml")
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        max_turn = config.get("conversation", {}).get("max_turn_count", 3)
    
    else:
        max_turn = 3
    
    # if job_state is empty, end workflow directly
    if state["job_state"].get("status") == "empty":
        state["next_action"] = "finalizer"
        return state
    
    if (
        state["user_profile"].get("parsed_at")
        and state["job_state"].get("matched_jobs")
        and not state.get("decision_result")
    ):
        print("Entering decision agent...")
        from src.decision.decision_agent import run_decision_agent
        raw_scores = {
            "skill_match": state["user_profile"].get("skill_score", 60),
            "experience_match": state["user_profile"].get("exp_score", 70),
            "preference_match": state["user_profile"].get("pref_score", 65)
        }
        weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
        from src.decision.decision_agent import run_decision_agent
        decision_result = run_decision_agent(
            case_id=state.get("session_id", "default"),
            raw_scores=raw_scores,
            weights=weights,
            normalization_method="min-max"
        )
        state["decision_result"] = decision_result
        state["system"]["decision_result"] = decision_result
        if decision_result["final_score"] > 0.8:
            state["next_action"] = "skill_analyzer"
        elif decision_result["final_score"] > 0.6:
            state["next_action"] = "recommendation"
        else:
            state["next_action"] = "finalizer"
        print(f"Decision result: {decision_result}, next action: {state['next_action']}")
        return state

    # manual decision logic
    if state.get("system", {}).get("need_manual_review", False):
        state["next_action"] = "manual_review"
        return state

    # 僅在尚未解析履歷或尚未匹配職缺時才分流
    if not state["user_profile"].get("parsed_at"):
        state["conversation"]["current_intent"] = "general"
        state["next_action"] = "resume_parser"
        return state
    if not state["job_state"].get("matched_jobs"):
        state["conversation"]["current_intent"] = "job_search"
        state["next_action"] = "job_matcher"
        return state

    # 其他情境
    if state["conversation"]["current_intent"] == "skill_analysis":
        state["next_action"] = "conversation"
        return state
    if state["conversation"].get("turn_count", 0) < max_turn:
        state["conversation"]["current_intent"] = "general"
        state["next_action"] = "conversation"
        return state

    # 預設推進到 finalizer
    state["next_action"] = "finalizer"
    return state
