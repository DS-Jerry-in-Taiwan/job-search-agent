"""StateGraph 測試
測試 StateGraph 的創建、編譯和執行
"""

import pytest
from src.langgraph.graph import create_workflow, route_to_agents
from src.langgraph.orchestrator import get_orchestrator
from src.langgraph.state import create_initial_state

def test_workflow_creation():
    """測試 StateGraph 創建"""
    workflow = create_workflow()
    assert workflow is not None

def test_workflow_compilation():
    """測試 StateGraph 編譯"""
    app = get_orchestrator()
    assert app is not None

def test_route_to_agents_search_job():
    """測試路由函數 - search_job"""
    state = create_initial_state("test")
    state["intents"] = ["search_job"]
    state["tasks"] = [{"intent": "search_job"}]
    result = route_to_agents(state)
    assert result == "job_search"

def test_route_to_agents_salary():
    """測試路由函數 - analyze_salary"""
    state = create_initial_state("test")
    state["intents"] = ["analyze_salary"]
    state["tasks"] = [{"intent": "analyze_salary"}]
    result = route_to_agents(state)
    assert result == "salary_analyze"

def test_route_to_agents_no_intent():
    """測試路由函數 - 無意圖"""
    state = create_initial_state("test")
    state["intents"] = []
    result = route_to_agents(state)
    assert result == "integrate_results"

def test_full_workflow_execution():
    """測試完整工作流程執行"""
    app = get_orchestrator()
    initial_state = create_initial_state("找台北 Python 工作")
    result = app.invoke(initial_state)
    assert result is not None
    assert "final_response" in result
    assert result["query"] == "找台北 Python 工作"
    assert len(result["intents"]) > 0
