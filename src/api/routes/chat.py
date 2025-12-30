from fastapi import APIRouter, HTTPException
from src.api.models import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
def chat_endpoint(request: ChatRequest):
    """
    對話端點，接收訊息與上下文，回傳 AI 回應（此處為範例回傳）
    """
    # TODO: 實作 StateGraph 對話邏輯，串接 orchestrator
    if not request.message:
        raise HTTPException(status_code=400, detail="訊息不得為空")
    # 範例假資料
    return ChatResponse(
        reply=f"收到訊息：{request.message}",
        state={"dummy": True},
        trace=[{"step": "start"}, {"step": "end"}]
    )
