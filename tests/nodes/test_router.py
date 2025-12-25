import pytest
from src.state.operations import create_initial_state
from src.nodes.router import router_node

def test_router_resume_parser():
    """履歷未解析時應進入 resume_parser"""
    state = create_initial_state()
    state["user_profile"]["parsed_at"] = None
    node = router_node(state)
    assert node["next_action"] == "resume_parser"
    assert state["conversation"]["current_intent"] == "general"

def test_router_job_matcher():
    """履歷已解析但未匹配職缺時應進入 job_matcher"""
    state = create_initial_state()
    state["user_profile"]["parsed_at"] = "2025-01-01"
    state["job_state"]["matched_jobs"] = []
    node = router_node(state)
    assert node["next_action"] == "job_matcher"
    assert state["conversation"]["current_intent"] == "job_search"

def test_router_conversation_skill_analysis():
    """意圖為 skill_analysis 時應進入 conversation"""
    state = create_initial_state()
    state["user_profile"]["parsed_at"] = "2025-01-01"
    state["job_state"]["matched_jobs"] = [{}]
    state["conversation"]["current_intent"] = "skill_analysis"
    node = router_node(state)
    assert node["next_action"] == "conversation"

def test_router_conversation_general():
    """turn_count < 3 時應進入 conversation 並設為 general"""
    state = create_initial_state()
    state["user_profile"]["parsed_at"] = "2025-01-01"
    state["job_state"]["matched_jobs"] = [{}]
    state["conversation"]["current_intent"] = "other"
    state["conversation"]["turn_count"] = 1
    node = router_node(state)
    assert node["next_action"] == "conversation"
    assert state["conversation"]["current_intent"] == "general"

def test_router_end():
    """turn_count >= 3 時流程結束"""
    state = create_initial_state()
    state["user_profile"]["parsed_at"] = "2025-01-01"
    state["job_state"]["matched_jobs"] = [{}]
    state["conversation"]["current_intent"] = "other"
    state["conversation"]["turn_count"] = 3
    node = router_node(state)
    assert node["next_action"] == "__end__"
