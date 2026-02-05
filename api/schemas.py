from pydantic import BaseModel
from typing import List, Optional

class TaskRequest(BaseModel):
    task: str
    
class AgentLog(BaseModel):
    agent: str
    input: str
    output: str
    
class TaskResponse(BaseModel):
    task: str
    plan: str
    research: str
    final_output: str
    workflow_log: List[AgentLog]
    
class SingleAgentRequest(BaseModel):
    agent: str
    message: str
    
class SingleAgentResponse(BaseModel):
    agent: str
    response: str
    
class ToolAgentRequest(BaseModel):
    message: str
    
class ToolAgentResponse(BaseModel):
    message: str
    response: str