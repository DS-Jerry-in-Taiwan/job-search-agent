from src.state.schema import AgentState

def error_handler_node(state: AgentState) -> AgentState:
    """
    統一錯誤處理節點：僅負責流程調度，所有功能調用 error_handle_service
    """
    from src.agent.services.error_handle_service import process_error
    state = process_error(state)
    return state
