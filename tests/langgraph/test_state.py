"""AgentState 測試
測試 AgentState 的創建和欄位驗證
"""

import pytest
from src.langgraph.state import AgentState, create_initial_state

def test_agent_state_creation():
    """測試 AgentState 創建"""
    state = create_initial_state("測試查詢", "user123")

    assert state["query"] == "測試查詢"
    assert state["user_id"] == "user123"
    assert state["session_id"] != ""
    assert isinstance(state["session_id"], str)
    assert state["intents"] == []
    assert state["tasks"] == []
    assert state["results"] == []
    assert state["final_response"] == ""
    assert state["error"] == ""
    assert state["retry_count"] == 0

def test_agent_state_fields():
    """測試 AgentState 所有欄位"""
    state = create_initial_state("test")

    required_fields = [
        "messages", "query", "session_id", "user_id",
        "intents", "tasks", "current_agent", "results",
        "context", "final_response", "error", "retry_count"
    ]

    for field in required_fields:
        assert field in state, f"Missing required field: {field}"

def test_agent_state_types():
    """測試 AgentState 欄位類型"""
    state = create_initial_state("test")

    assert isinstance(state["messages"], list)
    assert isinstance(state["query"], str)
    assert isinstance(state["session_id"], str)
    assert isinstance(state["user_id"], str)
    assert isinstance(state["intents"], list)
    assert isinstance(state["tasks"], list)
    assert isinstance(state["current_agent"], str)
    assert isinstance(state["results"], list)
    assert isinstance(state["context"], dict)
    assert isinstance(state["final_response"], str)
    assert isinstance(state["error"], str)
    assert isinstance(state["retry_count"], int)
