from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.agent import SupervisorAgent
from src.agent.agents import JobSearchAgent, SalaryAnalyzerAgent, InterviewCoachAgent, ResumeOptimizerAgent
from src.models.database import Base, engine

app = FastAPI(title="JobSearch Agent API", version="1.0.0")

Base.metadata.create_all(bind=engine)

# 路由註冊
from api.routes import auth, users, favorites
app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api/users")
app.include_router(favorites.router, prefix="/api/favorites")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化 SupervisorAgent
supervisor = SupervisorAgent(agents=[
    JobSearchAgent(),
    SalaryAnalyzerAgent(),
    InterviewCoachAgent(),
    ResumeOptimizerAgent(),
])

class ChatRequest(BaseModel):
    message: str
    user_profile: dict = {}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        response = supervisor.run(request.message, context=request.user_profile)
        return {"response": response, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/search")
async def search(query: str):
    # JobSearchAgent 實現
    return {"jobs": [], "query": query}

from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    job_title: str
    experience: int

@app.post("/api/analyze")
async def analyze(request: AnalyzeRequest):
    # SalaryAnalyzerAgent 實現
    return {
        "salary_range": {},
        "advice": "",
        "job_title": request.job_title,
        "experience": request.experience
    }

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/metrics")
async def metrics():
    # Prometheus 格式範例
    content = (
        "# HELP app_up 1 if the app is up\n"
        "# TYPE app_up gauge\n"
        "app_up 1\n"
        "# HELP app_requests_total Total number of requests\n"
        "# TYPE app_requests_total counter\n"
        "app_requests_total 100\n"
    )
    from fastapi.responses import PlainTextResponse
    return PlainTextResponse(content, media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)
