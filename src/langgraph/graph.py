# StateGraph workflow registry for多 workflow支援

from langgraph.graph import StateGraph
from src.state.schema import AgentState

# 預設 workflow
state_graph = StateGraph(AgentState)  # 以主結構 AgentState 初始化

# 完整 workflow：參考 src/graph/workflow.py
from src.nodes import (
    resume_parser_node,
    router_node,
    job_matcher_node,
    skill_analyzer_node,
    recommendation_node,
    conversation_node,
)

state_graph.add_node("resume_parser", resume_parser_node)
state_graph.add_node("skill_analyzer", skill_analyzer_node)
state_graph.add_node("job_matcher", job_matcher_node)
state_graph.add_node("recommendation", recommendation_node)
state_graph.add_node("conversation", conversation_node)
state_graph.add_node("router", router_node)

state_graph.add_edge("resume_parser", "skill_analyzer")
state_graph.add_edge("skill_analyzer", "job_matcher")
state_graph.add_edge("job_matcher", "recommendation")
state_graph.add_edge("recommendation", "router")
state_graph.add_edge("conversation", "router")
state_graph.set_entry_point("resume_parser")

def stategraph_to_mermaid(graph_obj):
    """
    根據 StateGraph 結構自動組裝 mermaid 流程圖代碼
    """
    lines = ["graph TD"]
    # 不用引號，改用簡單節點名稱避免語法錯誤
    for edge in getattr(graph_obj, "edges", []):
        if isinstance(edge, tuple) and len(edge) == 2:
            lines.append(f"  {edge[0]}-->{edge[1]}")
    return "\n".join(lines)

# 其他 workflow 可依需求擴充
workflow_registry = {
    "default": state_graph,
    # "demo": demo_state_graph,
    # "custom": custom_state_graph,
}

# 官方建議：提供 workflow.app 供 langgraph.ui 掛載
try:
    from langgraph.ui import create_service
    app = state_graph.compile()
    service = create_service(app)
except ImportError:
    service = None

def get_state_graph_by_id(workflow_id: str):
    return workflow_registry.get(workflow_id, state_graph)
