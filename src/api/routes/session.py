from fastapi import APIRouter, HTTPException
from src.api.models import SessionHistoryResponse

router = APIRouter()

@router.get("/session/{session_id}/history", response_model=SessionHistoryResponse, tags=["Session"])
def get_session_history(session_id: str):
    """
    查詢指定 session 的對話歷史（此處為範例資料）
    """
    # TODO: 實作實際 session 歷史查詢邏輯
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID 不得為空")
    # 範例假資料
    return SessionHistoryResponse(
        session_id=session_id,
        history=[
            {"role": "user", "message": "你好"},
            {"role": "assistant", "message": "您好，有什麼可以幫忙的？"}
        ]
    )
