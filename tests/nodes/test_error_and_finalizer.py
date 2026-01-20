import pytest
from src.state.operations import create_initial_state
from src.nodes.error_handle_node import error_handler_node

def test_error_handler_retry_and_fail():
    """測試錯誤重試與失敗標記"""
    state = create_initial_state()
    state["system"]["error_message"] = "Some error"
    state["system"]["retry_flag"] = True
    state["system"]["last_failed_node"] = "decision"
    for i in range(4):
        state["system"]["retry_flag"] = True
        state = error_handler_node(state)
    assert state["system"]["retry_count"] == 4
    assert state["system"]["current_node"] == "error_handler"
    assert state["next_action"] == "decision"
    assert "已超過最大重試次數" in state["system"]["error_message"]

def test_error_handler_retrying():
    """測試重試未超過上限"""
    state = create_initial_state()
    state["system"]["error_message"] = "Some error"
    state["system"]["retry_flag"] = True
    state["system"]["last_failed_node"] = "decision"
    state["system"]["retry_count"] = 2
    state = error_handler_node(state)
    assert state["system"]["retry_count"] == 3
    assert state["system"]["current_node"] == "error_handler"
    assert state["next_action"] == "decision"

def test_error_handler_ok():
    """測試無錯誤時狀態為 ok"""
    state = create_initial_state()
    state["system"]["error_message"] = ""
    state = error_handler_node(state)
    assert state["system"]["current_node"] == "error_handler"
    assert state["next_action"] == "decision"
