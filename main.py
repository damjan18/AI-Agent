from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from api.routes import router

app = FastAPI(
    title="AI Agent System",
    description="Multi-agent orchestration API with tools and guardrails",
    version="1.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http:''127.0.0.1:5173",
        "https://*.vercel.app"           
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return{
        "message": "AI Agent System API",
        "version": "1.1.0",
        "docs": "/docs",
        "endpoints": {
            "workflow": "/api/workflow",
            "single_agent": "/api/agent",
            "tool_agent": "/api/tool-agent",
            "validated_agent": "/api/validated_agent",
            "health": "/api/health"
        }
    }