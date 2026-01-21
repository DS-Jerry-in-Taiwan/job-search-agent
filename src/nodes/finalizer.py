def finalizer_node(state):
    """
    結束流程的收尾節點：僅負責流程調度，所有功能調用 finalizer_service
    """
    from src.agent.services.finalizer_service import finalize_state
    state = finalize_state(state)
    return state
