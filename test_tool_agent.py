from agents.tool_agent import ToolAgent

agent = ToolAgent()

print("=== TEST 1: Simple chat ===")
response = agent.run("Hello, how are you?")
print(f"Response: {response}\n")

print("=== TEST 2: Web search ===")
response = agent.run("Search for information about machine learning")
print(f"Response: {response}\n")

print("=== TEST 3: Save a note ===")
response = agent.run("Save this note: Remember to study Python decorators")
print(f"Response: {response}\n")

print("=== TEST 4: List files ===")
response = agent.run("What files do I have saved?")
print(f"Response: {response}\n")