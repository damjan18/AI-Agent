from agents.base_agent import BaseAgent
from agents.guardrails import Guardrails

class ValidatedAgent(BaseAgent):
    def __init__(self, name: str, role: str, instructions: str):
        super().__init__(name, role, instructions)
        self.guardrails = Guardrails()
        
    def run(self, user_message: str) -> str:
        is_valid, message = self.guardrails.check_input(user_message)
        if not is_valid:
            return f"Input Error: {message}" 
        
        response = super().run(user_message)
        
        is_valid, message = self.guardrails.check_output(response)
        if not is_valid:
            return f"Output Error: {message}"
        response = self.guardrails.sanitize_output(response)
        return response