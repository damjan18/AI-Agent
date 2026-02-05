from fastapi import APIRouter, HTTPException
from api.schemas import (
    TaskRequest,
    TaskResponse,
    SingleAgentRequest,
    SingleAgentResponse,
    ToolAgentRequest,
    ToolAgentResponse,
    ValidatedAgentRequest,
    ValidatedAgentResponse
    
)
from agents.orchestrator import Orchestrator
from agents.planner_agent import PlannerAgent
from agents.researcher_agent import ResearcherAgent
from agents.writer_agent import WriterAgent
from agents.tool_agent import ToolAgent
from agents.validated_agent import ValidatedAgent
from agents.guardrails import Guardrails

router = APIRouter()
guardrails = Guardrails()

@router.post("/workflow", response_model=TaskResponse)
def run_workflow(request: TaskRequest):
    is_valid, message = guardrails.check_input(request.task)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)
    
    orchestrator = Orchestrator()
    result = orchestrator.run_workflow(request.task)
    return result

@router.post("/agent", response_model=SingleAgentResponse)
def run_single_agent(request: SingleAgentRequest):
    is_valid, message = guardrails.check_input(request.message)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)
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
    
    response = guardrails.sanitize_output(response)
    
    return {
        "agent": agent_name,
        "response": response
    }
    
@router.post("/tool-agent", response_model=ToolAgentResponse)
def run_tool_agent(request: ToolAgentRequest):
    is_valid, message = guardrails.check_input(request.message)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)
    
    agent = ToolAgent()
    response = agent.run(request.message)
    
    response = guardrails.sanitize_output(response)
    
    return {
        "message": request.message,
        "response": response
    }
    
@router.post("/validated-agent", response_model=ValidatedAgentResponse)
def run_validated_agent(request: ValidatedAgentRequest):
    agent = ValidatedAgent(
        name="SafeAssistant",
        role="helpful and safe assistant",
        instructions="You provide helpful answers while being safe and appropriate."
    )
    
    response = agent.run(request.message)
    
    validation_passed = not response.startswith("Input Error:") and not response.startswith("Output Error:")
    
    return {
        "message": request.message,
        "response": response,
        "validation_passed": validation_passed
    }
    
@router.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}