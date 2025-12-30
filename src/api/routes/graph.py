from fastapi import APIRouter
from src.api.models import GraphVisualizeResponse

# 假設 StateGraph 物件定義於 src/langgraph/graph.py
from src.langgraph.graph import state_graph

router = APIRouter()

from fastapi import Query

@router.get("/graph/visualize", response_model=GraphVisualizeResponse, tags=["Graph"])
def graph_visualize(workflow_id: str = Query(default="default", description="指定 workflow id")):
    """
    StateGraph 可視化端點，回傳流程圖 SVG 及節點/邊資訊
    支援多 workflow，根據 workflow_id 回傳對應 StateGraph
    """
    # 根據 workflow_id 取得對應 StateGraph
    from src.langgraph.graph import get_state_graph_by_id, stategraph_to_mermaid
    state_graph_obj = get_state_graph_by_id(workflow_id)
    # 自動組裝 mermaid 代碼
    mermaid_str = stategraph_to_mermaid(state_graph_obj)
    nodes = list(getattr(state_graph_obj, "nodes", []))
    edges = list(getattr(state_graph_obj, "edges", []))
    return GraphVisualizeResponse(
        graph_svg=mermaid_str,
        nodes=nodes,
        edges=edges
    )
