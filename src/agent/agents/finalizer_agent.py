from typing import Dict, Any

class FinalizerAgent:
    """
    終結流程 Agent，標記狀態為完成
    """
    def finalize(self, state: Dict[str, Any]) -> Dict[str, Any]:
        state["system"]["workflow_status"] = "completed"
        state["system"]["current_node"] = "finalizer"
        state["system"]["final_message"] = "流程已完成，感謝使用！"
        return state
