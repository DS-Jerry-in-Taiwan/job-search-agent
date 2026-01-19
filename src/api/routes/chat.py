from fastapi import APIRouter, HTTPException
from src.api.models import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
def chat_endpoint(request: ChatRequest):
    """
    對話端點，接收訊息與上下文，回傳 Decision Agent 決策建議與分數
    """
    from src.decision.decision_agent import run_decision_agent

    if not request.message:
        raise HTTPException(status_code=400, detail="訊息不得為空")

    # 簡易 NLP 規則：根據 message 內容產生模擬分數
    msg = request.message
    if "工程師" in msg and "專案經理" in msg:
        # 高分場景
        raw_scores = {"skill_match": 90, "experience_match": 80, "preference_match": 85}
    elif "行銷" in msg and "產品經理" in msg:
        # 中分場景
        raw_scores = {"skill_match": 65, "experience_match": 70, "preference_match": 60}
    elif "會計" in msg and "AI工程師" in msg:
        # 低分場景
        raw_scores = {"skill_match": 30, "experience_match": 40, "preference_match": 20}
    else:
        # 預設
        raw_scores = {"skill_match": 50, "experience_match": 50, "preference_match": 50}

    weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
    result = run_decision_agent(
        case_id=request.session_id or "default",
        raw_scores=raw_scores,
        weights=weights,
        normalization_method="min-max"
    )

    # 決策建議分級
    if result["final_score"] > 0.8:
        suggestion = "Highly Recommended"
    elif result["final_score"] > 0.6:
        suggestion = "Recommended"
    elif result["final_score"] < 0.4:
        suggestion = "Consider Alternative"
    else:
        suggestion = "Neutral"

    reply = (
        f"決策分數: {result['final_score']:.2f}\n"
        f"建議: {suggestion}\n"
        f"行動計畫: {[step['step'] for step in result['action_plan']]}"
    )

    return ChatResponse(
        reply=reply,
        state=result,
        trace=[{"step": "decision_agent", "score": result["final_score"]}]
    )
