"""LLM 整合測試"""

import pytest
from src.langgraph.state import AgentState
from src.langgraph.nodes import (
    identify_intent_node,
    decompose_tasks_node,
    load_context_node,
    update_memory_node
)

def test_identify_intent_with_llm(monkeypatch):
    """測試 LLM 意圖識別"""
    # Mock LLMClient.generate
    from src.llm.llm_client import LLMClient
    monkeypatch.setattr(LLMClient, "generate", lambda self, prompt: '{"intents": ["search_job", "analyze_salary"]}')

    state = AgentState(
        messages=[],
        query="我想找台北的 AI 工程師工作，薪水 80 萬以上",
        session_id="test_session",
        user_id="test_user",
        intents=[],
        tasks=[],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
    result_state = identify_intent_node(state)
    assert "search_job" in result_state["intents"]
    assert "analyze_salary" in result_state["intents"]

def test_decompose_tasks_with_llm(monkeypatch):
    """測試 LLM 任務拆解"""
    from src.llm.llm_client import LLMClient
    monkeypatch.setattr(LLMClient, "generate", lambda self, prompt: '{"location": "台北", "skill": "AI", "salary_range": "80萬以上"}')

    state = AgentState(
        messages=[],
        query="我想找台北的 AI 工程師工作，薪水 80 萬以上",
        session_id="test_session",
        user_id="test_user",
        intents=["search_job", "analyze_salary"],
        tasks=[],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
    result_state = decompose_tasks_node(state)
    assert len(result_state["tasks"]) == 2
    for task in result_state["tasks"]:
        assert "location" in task["params"]
        assert "skill" in task["params"]
        assert "salary_range" in task["params"]

def test_load_context_node(monkeypatch):
    """測試 Memory 載入"""
    from src.memory.conversation_memory import ConversationMemory
    class MockMemory:
        def get_history(self, session_id, limit):
            return [{"query": "A", "response": "B"}]
        def get_user_preferences(self, user_id):
            return {"preferred_location": "台北"}
    monkeypatch.setattr("src.memory.conversation_memory.ConversationMemory", lambda: MockMemory())

    state = AgentState(
        messages=[],
        query="test",
        session_id="test_session",
        user_id="test_user",
        intents=[],
        tasks=[],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
    result_state = load_context_node(state)
    assert "history" in result_state["context"]
    assert "user_preferences" in result_state["context"]
    assert result_state["context"]["user_preferences"]["preferred_location"] == "台北"

def test_update_memory_node(monkeypatch):
    """測試 Memory 儲存"""
    from src.memory.conversation_memory import ConversationMemory
    class MockMemory:
        def save_conversation(self, **kwargs):
            return True
    monkeypatch.setattr("src.memory.conversation_memory.ConversationMemory", lambda: MockMemory())

    state = AgentState(
        messages=[],
        query="test",
        session_id="test_session",
        user_id="test_user",
        intents=["search_job"],
        tasks=[],
        current_agent="",
        results=[{"agent": "JobSearchAgent", "result": "找到 5 個職缺"}],
        context={},
        final_response="這是回應",
        error="",
        retry_count=0
    )
    result_state = update_memory_node(state)
    assert "error" not in result_state or result_state["error"] == ""
