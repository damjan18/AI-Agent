from agents.base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Researcher",
            role="information gathering specialist",
            instructions="""You research and gather information on topics.
            
            
            When given a topic or question:
            1. Provide key facts and information
            2. Include relevant details
            3. Be accurate and concise
            4. Organize information clearly
            
            Focus only on factual information."""
            )