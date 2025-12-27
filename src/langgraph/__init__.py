"""LangGraph 模組
JobSearch Agent 的 LangGraph 實現

模組結構:
- state: AgentState 定義
- nodes: Node 函數實現
- graph: StateGraph 定義
- orchestrator: 主編排器
"""

from .state import AgentState, create_initial_state
from .graph import create_workflow, route_to_agents
from .orchestrator import get_orchestrator
from .nodes import (
    load_context_node,
    identify_intent_node,
    decompose_tasks_node,
    integrate_results_node,
    update_memory_node
)

__version__ = "0.1.0"

__all__ = [
    "AgentState",
    "create_initial_state",
    "create_workflow",
    "route_to_agents",
    "get_orchestrator",
    "load_context_node",
    "identify_intent_node",
    "decompose_tasks_node",
    "integrate_results_node",
    "update_memory_node",
]
