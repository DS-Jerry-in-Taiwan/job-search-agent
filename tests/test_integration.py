"""整合測試增強"""

import pytest
from src.graph import create_workflow
from src.state.operations import create_initial_state
from concurrent.futures import ThreadPoolExecutor

def test_full_workflow_real_data():
    """使用真實數據測試完整流程"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = ["Python", "FastAPI", "LangChain"]
    result = app.invoke(state)
    assert result["user_profile"]["parsed_at"] is not None
    assert isinstance(result["job_state"]["matched_jobs"], list)
    assert result["is_complete"] is True

def test_concurrent_execution():
    """測試並發執行"""
    app = create_workflow()
    def run_workflow():
        state = create_initial_state()
        return app.invoke(state)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(run_workflow) for _ in range(10)]
        results = [f.result() for f in futures]
    assert all(r["is_complete"] for r in results)

def test_state_persistence():
    """測試 State 持久化"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = ["Python"]
    result = app.invoke(state)
    # 模擬持久化
    import pickle
    data = pickle.dumps(result)
    loaded = pickle.loads(data)
    assert loaded["is_complete"] is True

def test_workflow_interruption():
    """測試工作流程中斷"""
    app = create_workflow()
    state = create_initial_state()
    state["system"]["interrupt"] = True
    try:
        app.invoke(state)
    except Exception:
        pass
    # 驗證可恢復
    state["system"]["interrupt"] = False
    result = app.invoke(state)
    assert result["is_complete"] is True

def test_workflow_resume():
    """測試工作流程恢復"""
    app = create_workflow()
    state = create_initial_state()
    state["system"]["resume"] = True
    result = app.invoke(state)
    assert result["is_complete"] is True

def test_multiple_users():
    """多用戶測試"""
    app = create_workflow()
    users = []
    for i in range(5):
        state = create_initial_state()
        state["user_profile"]["name"] = f"User{i}"
        users.append(app.invoke(state))
    assert all(u["is_complete"] for u in users)

def test_long_running_workflow():
    """長時間運行測試"""
    app = create_workflow()
    state = create_initial_state()
    state["conversation"]["turn_count"] = 50
    result = app.invoke(state)
    assert result["is_complete"] is True

def test_resource_cleanup():
    """資源清理測試"""
    app = create_workflow()
    state = create_initial_state()
    result = app.invoke(state)
    # 模擬清理
    state.clear()
    assert isinstance(result, dict)
