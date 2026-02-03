from base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Planner",
            role="task planning specialist", 
            instructions="""You break down complex tasks into clear, actionable steps.
            
            When given a task:
            1. Analyze what needs to be done
            2. Break it into 3-5 simple steps
            3. Number each step clearly
            4. Keep steps specific and actionable
            
            Only output the steps, nothing else."""
            )