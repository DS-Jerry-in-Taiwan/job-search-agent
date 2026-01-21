from typing import Dict, Any

class RouterAgent:
    """
    路由 Agent，根據 state["next_action"] 分流
    """
    def route(self, state: Dict[str, Any]) -> Dict[str, Any]:
        next_action = state.get("next_action", "conversation")
        return {"next_node": next_action}
