"""邊界測試套件"""

import pytest
from src.graph import create_workflow
from src.state.operations import create_initial_state

def test_empty_skills():
    """測試空技能清單"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = []
    result = app.invoke(state)
    # 根據 mock provider，預設應有職缺資料
    assert isinstance(result["job_state"]["matched_jobs"], list)
    assert result["is_complete"] is True

def test_empty_jobs():
    """測試空職缺清單"""
    app = create_workflow()
    state = create_initial_state()
    state["job_state"]["jobs"] = []
    state["job_state"]["status"] = "empty"  # 必須加這行
    result = app.invoke(state)
    assert result["job_state"]["matched_jobs"] == []
    assert result["is_complete"] is True

def test_large_skills_list():
    """測試大量技能"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = [f"Skill{i}" for i in range(200)]
    result = app.invoke(state)
    assert isinstance(result["job_state"]["matched_jobs"], list)
    assert result["is_complete"] is True

def test_large_job_list():
    """測試大量職缺"""
    app = create_workflow()
    state = create_initial_state()
    state["job_state"]["jobs"] = [{"job_id": f"job_{i}", "title": f"Job {i}"} for i in range(1000)]
    result = app.invoke(state)
    assert isinstance(result["job_state"]["matched_jobs"], list)
    assert result["is_complete"] is True

def test_special_characters():
    """測試特殊字符處理"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = ["Python 🐍", "AI/ML", "C++"]
    result = app.invoke(state)
    assert result["is_complete"] is True

def test_unicode_handling():
    """測試 Unicode 處理"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = ["中文", "日本語", "Español"]
    result = app.invoke(state)
    assert result["is_complete"] is True

def test_null_values():
    """測試 Null 值處理"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = None
    result = app.invoke(state)
    assert result["is_complete"] is True

def test_invalid_state():
    """測試無效 State"""
    app = create_workflow()
    state = None
    with pytest.raises(Exception):
        app.invoke(state)

def test_max_iterations():
    """測試最大迭代次數"""
    app = create_workflow()
    state = create_initial_state()
    state["conversation"]["turn_count"] = 1000
    result = app.invoke(state)
    assert result["is_complete"] is True

def test_circular_routing():
    """測試循環路由檢測"""
    app = create_workflow()
    state = create_initial_state()
    # 模擬循環路由（此處僅驗證不會無限循環）
    state["conversation"]["turn_count"] = 0
    result = app.invoke(state)
    assert result["is_complete"] is True
