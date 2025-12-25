"""LangGraph 工作流程定義 - Phase 5 架構設計 (@ARCH)"""

from langgraph.graph import StateGraph, END
from src.state.schema import AgentState
from src.nodes import (
    resume_parser_node,
    job_matcher_node,
    skill_analyzer_node,
    recommendation_node,
    conversation_node,
    router_node,
    error_handler_node,
    finalizer_node,
)

from typing import Any

def create_workflow() -> Any:
    """
    建立完整的 LangGraph 工作流程，並編譯為可執行 Graph 實例

    Returns:
        CompiledGraph: 編譯後的工作流程圖
    """
    workflow = StateGraph(AgentState)

    # 加入所有 Nodes
    workflow.add_node("resume_parser", resume_parser_node)
    workflow.add_node("job_matcher", job_matcher_node)
    workflow.add_node("skill_analyzer", skill_analyzer_node)
    workflow.add_node("recommendation", recommendation_node)
    workflow.add_node("conversation", conversation_node)
    workflow.add_node("router", router_node)
    workflow.add_node("error_handler", error_handler_node)
    workflow.add_node("finalizer", finalizer_node)

    # 固定 Edges
    workflow.add_edge("resume_parser", "router")
    workflow.add_edge("job_matcher", "recommendation")
    workflow.add_edge("recommendation", "router")
    workflow.add_edge("conversation", "router")
    workflow.add_edge("error_handler", "router")
    workflow.add_edge("finalizer", END)

    # 條件路由 (router_node)
    workflow.add_conditional_edges(
        "router",
        lambda state: router_node(state)["next_action"],
        {
            "resume_parser": "resume_parser",
            "job_matcher": "job_matcher",
            "conversation": "conversation",
            "__end__": "finalizer"
        }
    )

    # 設定入口點
    workflow.set_entry_point("resume_parser")

    # 編譯 Graph
    app = workflow.compile()
    return app

# 全域實例
graph_app = create_workflow()
