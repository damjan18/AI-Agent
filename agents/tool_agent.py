import asyncio
import json
from groq import Groq
from dotenv import load_dotenv
import os
from tools.web_search import WebSearchTool
from tools.file_tool import FileTool


load_dotenv()

class ToolAgent:
    def __init__(self):
        self.name = "ToolAgent"
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.web_search = WebSearchTool()
        self.file_tool = FileTool()
        self.conversation = []
        
    def run(self, user_message: str) -> str:
        tool_decision = self._decide_tool(user_message)
        
        tool_result = None
        if tool_decision["use_tool"]:
            tool_result = self._execute_tool(
                tool_decision["tool"],
                tool_decision["tool_input"]
            )
        
        response = self._generate_response(user_message, tool_result)
        return response
    
    def _decide_tool(self, user_message: str) -> dict:
        system_prompt = """You decide which tool to use based on the user's request.
        
        Available tools:
        1. web_search - Search the web for current information
        2. file_read - Read a file from storage
        3. file_write - Save content to a file
        4. file_list - List all saved files
        5. none - No tool needed, just respond directly
        
        Respond in this exact JSON format:
        {"use_tool": true/false, "tool": "tool_name", "tool_input": "input for tool:}
        
        Examples:
        User: "Search information about Python"
        {"use_tool": true, "tool": "web_search", "tool_input": "Python programming"}
        
        User: "Save this note: Nuy groceries"
        {"use_tool": true, "tool": "file_write", "tool_input": "Buy groceries"}
        
        User: "What files do I have?"
        {"use_tool": true, "tool": "file_list", "tool_input": ""}
        
        User: "Hello, how are you?"
        {"use_tool": false, "tool": "none", "tool_input": ""}
        
        Only respond with JSON, nothing else."""
        
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=200
        )
        
        try:
            decision = json.loads(response.choices[0].message.content)
            return decision
        except:
            return {"use_tool": False, "tool": "none", "tool_input": ""}
        
    def _execute_tool(self, tool_name: str, tool_input: str) -> str:
        print(f">>> Using tool: {tool_name}")
        print(f">>> Input: {tool_input}")
        
        if tool_name == "web_search":
            result = asyncio.run(self.web_search.search(tool_input))
        elif tool_name == "file_read":
            result = self.file_tool.read_file(tool_input)
        elif tool_name == "file_write":
            filename = "note_" + str(len(os.listdir(self.file_tool.base_directory)))
            result = self.file_tool.write_file(filename, tool_input)
        elif tool_name == "file_list":
            result = self.file_tool.list_files()
        else:
            result = "Unknown tool"
            
        print(f">>> Tool result: {result}\n")
        return result
    
    def _generate_response(self, user_message: str, tool_result: str = None) -> str:
        system_prompt = """You are helpful assistant.
        If tool results are provided, use them to give an accurate response.
        Be concise and helpful."""
        
        messages = [{"role": "system", "content": system_prompt}]
        
        if tool_result:
            messages.append({
                "role": "user",
                "content": f"User asked: {user_message}\n\nTool result: {tool_result}\n\nProvide a helpful response based on this information."
            })
        else:
            messages.append({"role": "user", "content": user_message})
        
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            max_tokens=1024
        )
        
        return response.choices[0].message.content