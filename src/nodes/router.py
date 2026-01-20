from src.state.schema import AgentState

def router_node(state: AgentState) -> dict:
    """
    根據 state["next_action"] 分流，回傳 dict: {"next_node": ...}
    """
    next_action = state.get("next_action", "conversation")
    return {"next_node": next_action}
