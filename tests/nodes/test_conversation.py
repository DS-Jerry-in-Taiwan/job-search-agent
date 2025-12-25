import pytest
from src.state.operations import create_initial_state
from src.nodes.conversation import conversation_node
from langchain_core.messages import AIMessage

def test_conversation_node_job_search():
    """測試 job_search 意圖回應"""
    state = create_initial_state()
    state["conversation"]["current_intent"] = "job_search"
    state["job_state"]["matched_jobs"] = [{}] * 3
    result = conversation_node(state)
    from langchain_core.messages import AIMessage
    assert isinstance(result["conversation"]["messages"][-1], AIMessage)
    assert getattr(result["conversation"]["messages"][-1], "content", None) is not None
    assert "3 個符合的職缺" in result["conversation"]["messages"][-1].content
    assert result["system"]["current_node"] == "conversation"

def test_conversation_node_skill_analysis():
    """測試 skill_analysis 意圖回應"""
    state = create_initial_state()
    state["conversation"]["current_intent"] = "skill_analysis"
    state["user_profile"]["skills"] = ["Python", "SQL"]
    result = conversation_node(state)
    msg = result["conversation"]["messages"][-1].content
    assert "Python" in msg and "SQL" in msg
    assert result["system"]["current_node"] == "conversation"

def test_conversation_node_general():
    """測試 general 意圖回應"""
    state = create_initial_state()
    state["conversation"]["current_intent"] = "general"
    result = conversation_node(state)
    msg = result["conversation"]["messages"][-1].content
    assert "職涯搜尋" in msg
    assert result["system"]["current_node"] == "conversation"
