from typing import Dict, Any

def process_error(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    統一錯誤處理邏輯
    - retry_flag=True 且 last_failed_node 存在且未超過最大重試次數：自動重試回原節點
    - 其他情境：回 decision node 由主流程判斷
    """
    retry_flag = state.get("system", {}).get("retry_flag", False)
    last_failed_node = state.get("system", {}).get("last_failed_node", None)
    max_retry = 3

    if retry_flag and last_failed_node:
        state["system"]["retry_count"] = state["system"].get("retry_count", 0) + 1
        state["system"]["retry_flag"] = False
        retry_count = state["system"]["retry_count"]
        if retry_count <= max_retry:
            state["next_action"] = last_failed_node
        else:
            state["system"]["error_message"] = (
                state["system"].get("error_message", "") +
                f"（已超過最大重試次數 {max_retry}）"
            )
            state["next_action"] = "decision"
    else:
        state["next_action"] = "decision"

    state["system"]["current_node"] = "error_handler"
    return state
