from agents.base_agent import BaseAgent

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Writer",
            role="content writing specialist",
            instructions="""You write clear, polished content.
            
            When given information and a writing task:
            1. Write in clear, engaging style
            2. Structure content logically
            3. Keep it concise but complete
            4. Match the requested format
            
            Outpu only the final written content."""
                        )