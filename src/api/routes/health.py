from fastapi import APIRouter
from src.api.models import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    """
    健康檢查端點，回傳服務狀態與版本
    """
    return HealthResponse(status="ok", version="0.1.0")
