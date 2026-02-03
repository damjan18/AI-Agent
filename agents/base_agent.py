from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class BaseAgent:
    def __init__(self, name: str, role: str, instructions: str):
        self.name = name
        self.role = role
        self.instructions = instructions
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.conversation_history = []
        
    def run(self, user_message: str) -> str:
        system_prompt = f"""You are {self.name}, a {self.role}.
        
        {self.instructions}
        
        Always respond in a helpful and structured way."""
        
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                *self.conversation_history
            ],
            max_tokens=1024
        )
        
        assistant_message = response.choices[0].message.content
        
        self.conversation_history.append({
            "role": "assistant", 
            "content": assistant_message
        })
        
        return assistant_message
    
    def reset(self):
        self.conversation_history = []
        