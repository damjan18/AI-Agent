from planner_agent import PlannerAgent
from researcher_agent import ResearcherAgent
from writer_agent import WriterAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()
        self.workflow_log = []
        
    def log(self, agent_name: str, input_text: str, output_text: str):
        self.workflow_log.append({
            "agent": agent_name,
            "input": input_text,
            "output": output_text
        })
        
    def run_workflow(self, user_task: str) -> dict:
        print(f"\n{'='*50}")
        print(f"TASK: {user_task}")
        print(f"{'='*50}\n")
        
        # Step 1: Planner breaks down the tasks
        print(">>> Planner is working...")
        plan = self.planner.run(user_task)
        self.log("Planner", user_task, plan)
        print(f"Plan created:\n{plan}\n")
        
        # Step 2: Researcher gathers information
        print(">>> Researcher is working...")
        research_prompt = f"Research information needed for this task: {user_task}"
        research = self.researcher.run(research_prompt)
        self.log("Researcher", research_prompt, research)
        print(f"Research done: \n{research}\n")
        
        #Step 3: Writer creates final output
        print(">>> Writer is working...")
        writer_prompt = f"""Create the final output for this task: {user_task}
        
        Use this plan:
        {plan}
        
        Use this research:
        {research}
        
        Write complete final output."""
        
        final_output = self.writer.run(writer_prompt)
        self.log("Writer", writer_prompt, final_output)
        print(f"Final output:\n{final_output}\n")
        
        return {
            "task": user_task,
            "plan": plan,
            "research": research,
            "final_output": final_output,
            "workflow_log": self.workflow_log
        }
        
    def reset_all(self):
        self.planner.reset()
        self.writer.reset()
        self.researcher.reset()
        self.workflow_log = []