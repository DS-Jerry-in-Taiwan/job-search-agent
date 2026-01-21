from typing import Dict, Any

def finalize_state(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    終結流程，標記狀態為完成
    """
    state["system"]["workflow_status"] = "completed"
    state["system"]["current_node"] = "finalizer"
    state["system"]["final_message"] = "流程已完成，感謝使用！"
    return state
