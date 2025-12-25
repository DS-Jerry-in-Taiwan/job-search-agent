import pytest
from src.state.operations import create_initial_state
from src.nodes.router import error_handler_node, finalizer_node

def test_error_handler_retry_and_fail():
    """測試錯誤重試與失敗標記"""
    state = create_initial_state()
    state["system"]["error_message"] = "Some error"
    for i in range(4):
        state = error_handler_node(state)
    assert state["system"]["workflow_status"] == "failed"
    assert state["system"]["retry_count"] == 4
    assert state["system"]["current_node"] == "error_handler"

def test_error_handler_retrying():
    """測試重試未超過上限"""
    state = create_initial_state()
    state["system"]["error_message"] = "Some error"
    state["system"]["retry_count"] = 2
    state = error_handler_node(state)
    assert state["system"]["workflow_status"] == "retrying"
    assert state["system"]["retry_count"] == 3

def test_error_handler_ok():
    """測試無錯誤時狀態為 ok"""
    state = create_initial_state()
    state["system"]["error_message"] = ""
    state = error_handler_node(state)
    assert state["system"]["workflow_status"] == "ok"

def test_finalizer_node():
    """測試流程結束標記"""
    state = create_initial_state()
    state = finalizer_node(state)
    assert state["is_complete"] is True
    assert state["system"]["workflow_status"] == "completed"
    assert state["system"]["current_node"] == "finalizer"
