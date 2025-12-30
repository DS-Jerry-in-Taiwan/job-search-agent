from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import chat, health, graph, session

app = FastAPI(
    title="LangGraph StateGraph API",
    description="提供 StateGraph 對話、健康檢查、流程圖、Session 歷史等端點",
    version="0.1.0"
)

# 加入 CORS 支援
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/metrics")
def metrics():
    # Prometheus 格式範例
    return Response(
        "app_up 1\nrequest_count_total 42\n",
        media_type="text/plain"
    )

app.include_router(chat.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")
app.include_router(graph.router, prefix="/api/v1")
app.include_router(session.router, prefix="/api/v1")
