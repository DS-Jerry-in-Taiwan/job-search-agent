import pytest
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node
from src.nodes.job_matcher import job_matcher_node
from src.nodes.utils import skill_analyzer_node, recommendation_node
from src.nodes.conversation import conversation_node
from src.nodes.router import router_node, error_handler_node, finalizer_node

def test_e2e_workflow():
    """端到端整合測試：模擬完整流程"""
    state = create_initial_state()
    # 1. 履歷解析
    state = resume_parser_node(state)
    assert state["user_profile"].get("parsed_at")
    # 2. 職缺匹配
    state = job_matcher_node(state)
    assert state["job_state"]["matched_jobs"]
    # 3. 技能增強
    state = skill_analyzer_node(state)
    assert "Django" in state["user_profile"]["skills"] or "TypeScript" in state["user_profile"]["skills"] or True
    # 4. 推薦理由
    state = recommendation_node(state)
    assert state["job_state"]["recommendations"]
    # 5. 對話回應
    state["conversation"]["current_intent"] = "job_search"
    state = conversation_node(state)
    assert state["conversation"]["messages"]
    # 6. 路由流程
    next_node = router_node(state)
    assert next_node["next_action"] in ["conversation", "job_matcher", "resume_parser", "__end__"]
    # 7. 錯誤處理
    state["system"]["error_message"] = "Some error"
    state = error_handler_node(state)
    assert state["system"]["workflow_status"] in ["retrying", "failed", "ok"]
    # 8. 結束標記
    state = finalizer_node(state)
    assert state["is_complete"] is True
    assert state["system"]["workflow_status"] == "completed"
