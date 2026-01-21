from src.state.schema import AgentState
from typing import Dict, Optional

def conversation_node(state: AgentState) -> AgentState:
    """
    Conversation node: 僅負責流程調度，所有功能調用 conversation_service
    """
    from src.agent.services.conversation_service import process_conversation
    state = process_conversation(state)
    state["system"]["current_node"] = "conversation"
    return state
