from fastapi import APIRouter, HTTPException
from api.schemas import (
    TaskRequest,
    TaskResponse,
    SingleAgentRequest,
    SingleAgentResponse
)
from agents.orchestrator import Orchestrator
from agents.planner_agent import PlannerAgent
from agents.researcher_agent import ResearcherAgent
from agents.writer_agent import WriterAgent

router = APIRouter()

@router.post("/workflow", response_model=TaskResponse)
def run_workflow(request: TaskRequest):
    orchestrator = Orchestrator()
    result = orchestrator.run_workflow(request.task)
    return result

@router.post("/agent", response_model=SingleAgentResponse)
def run_single_agent(request: SingleAgentRequest):
    agents = {
        "planner": PlannerAgent,
        "researcher": ResearcherAgent,
        "writer": WriterAgent
    }
    
    agent_name = request.agent.lower()
    
    if agent_name not in agents:
        raise HTTPException(
            status_code=400,
            detail=f"Agent '{request.agent}' not found. Available: planner, researcher, writer"
        )
    
    agent = agents[agent_name]()
    response = agent.run(request.message)
    
    return {
        "agent": agent_name,
        "response": response
    }
    
@router.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}