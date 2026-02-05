import re
from typing import Tuple

class Guardrails:
    def __init__(self):
        self.blocked_words = [
            "password",
            "credit card",
            "social security",
            "api key",
            "secret key",
            "private key"
        ]
        self.max_output_length = 5000
        
    def check_input(self, user_input: str) -> Tuple[bool, str]:
        if not user_input or not user_input.strip():
            return False, "Input cannot be empty"
        

        if len(user_input) > 2000:
            return False, "Input too long. Maximum 2000 characters."
        
        return True, "Input is valid"
    
    def check_output(self, output:str) -> Tuple[bool, str]:
        if not output or not output.strip():
            return False, "Output is empty"
        
        if len (output) > self.max_output_length:
            return False, f"Output too long. Maximum {self.max_output_length} characters."
        
        
        output_lower = output.lower()
        for word in self.blocked_words:
            if word in output_lower:
                return False, f"Output contains sensitive term: {word}"
            
        return True, "Output is valid"
    
    def sanitize_output(self, output: str) -> str:
        # Remove email patterns
        output = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL REMOVED]', output)
        
        # Remove phone patterns
        output = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE REMOVED]', output)
        
        # Truncate if too long
        if len(output) > self.max_output_length:
            output = output[:self.max_output_length] + "... [TRUNCATED]"
            
        return output
    
    def validate_json_output(self, output: str) -> Tuple[bool, str]:
        import json
        try:
            json.loads(output)
            return True, "Valid JSON"
        except json.JSONDecodeError as e:
            return False, f"Invalid JSON: {str(e)}"
        