"""LangGraph 工作流程測試 - Phase 5"""

import pytest
from src.graph.workflow import create_workflow
from src.state.operations import create_initial_state

def test_create_workflow():
    """測試 Graph 建立"""
    app = create_workflow()
    assert app is not None

def test_workflow_execution():
    """測試完整工作流程執行"""
    app = create_workflow()
    state = create_initial_state()
    result = app.invoke(state)
    assert result["user_profile"]["skills"]
    assert result["job_state"]["matched_jobs"]
    assert result["is_complete"] is True

def test_workflow_state_updates():
    """測試 State 更新"""
    app = create_workflow()
    state = create_initial_state()
    result = app.invoke(state)
    assert result["user_profile"].get("parsed_at") is not None
    assert result["job_state"].get("last_updated") is not None
    assert len(result["job_state"]["matched_jobs"]) > 0

def test_workflow_routing():
    """測試路由邏輯"""
    app = create_workflow()
    state = create_initial_state()
    result = app.invoke(state)
    assert result["system"]["workflow_status"] in ["completed", "finalizer", "conversation"]
