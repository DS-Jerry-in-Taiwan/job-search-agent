"""Node 函數測試
測試所有 Node 函數的基本功能
"""

import pytest
from src.langgraph.state import create_initial_state
from src.langgraph.nodes import (
    load_context_node,
    identify_intent_node,
    decompose_tasks_node,
    integrate_results_node,
    update_memory_node
)

def test_load_context_node():
    """測試 load_context_node"""
    state = create_initial_state("test")
    result = load_context_node(state)

    assert "context" in result
    assert isinstance(result["context"], dict)
    assert "history" in result["context"]
    assert "mentioned_jobs" in result["context"]
    assert "user_preferences" in result["context"]

def test_identify_intent_node():
    """測試 identify_intent_node"""
    # 測試案例 1: 搜尋工作
    state1 = create_initial_state("找台北 Python 工作")
    result1 = identify_intent_node(state1)
    assert "intents" in result1
    assert isinstance(result1["intents"], list)
    assert len(result1["intents"]) > 0
    assert "search_job" in result1["intents"]

    # 測試案例 2: 薪資分析
    state2 = create_initial_state("Python 工程師薪資多少")
    result2 = identify_intent_node(state2)
    assert "analyze_salary" in result2["intents"]

def test_decompose_tasks_node():
    """測試 decompose_tasks_node"""
    state = create_initial_state("test")
    state["intents"] = ["search_job", "analyze_salary"]
    result = decompose_tasks_node(state)
    assert "tasks" in result
    assert isinstance(result["tasks"], list)
    assert len(result["tasks"]) == 2
    for task in result["tasks"]:
        assert "intent" in task
        assert "query" in task
        assert "params" in task

def test_integrate_results_node_with_results():
    """測試 integrate_results_node（有結果）"""
    state = create_initial_state("test")
    state["results"] = [
        {"agent": "JobSearchAgent", "result": "找到 5 個職缺"},
        {"agent": "SalaryAnalyzerAgent", "result": "平均薪資 150 萬"}
    ]
    result = integrate_results_node(state)
    assert "final_response" in result
    assert result["final_response"] != ""
    assert "JobSearchAgent" in result["final_response"]
    assert "SalaryAnalyzerAgent" in result["final_response"]

def test_integrate_results_node_no_results():
    """測試 integrate_results_node（無結果）"""
    state = create_initial_state("test")
    state["results"] = []
    result = integrate_results_node(state)
    assert "final_response" in result
    assert result["final_response"] != ""

def test_update_memory_node():
    """測試 update_memory_node"""
    state = create_initial_state("test")
    result = update_memory_node(state)
    assert result is not None
    assert isinstance(result, dict)
