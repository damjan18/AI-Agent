from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="AI Agent System",
    description="Multi-agent orchestration API",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return{
        "message": "AI Agent System API",
        "docs": "/docs",
        "endpoints": {
            "workflow": "/api/workflow",
            "single_agent": "/api/agent",
            "tool_agent": "/api/tool-agent",
            "health": "/api/health"
        }
    }