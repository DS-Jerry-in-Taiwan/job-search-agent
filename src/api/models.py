from pydantic import BaseModel
from typing import Any, Dict, List, Optional

# 對話請求
class ChatRequest(BaseModel):
    session_id: str
    message: str
    context: Optional[Dict[str, Any]] = None

# 對話回應
class ChatResponse(BaseModel):
    reply: str
    state: Dict[str, Any]
    trace: List[Any]

# 健康檢查回應
class HealthResponse(BaseModel):
    status: str
    version: str

# StateGraph 可視化回應
class GraphVisualizeResponse(BaseModel):
    graph_svg: str
    nodes: List[Any]
    edges: List[Any]

# Session 歷史回應
class SessionHistoryResponse(BaseModel):
    session_id: str
    history: List[Any]
