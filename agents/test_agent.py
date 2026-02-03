from base_agent import BaseAgent

agent = BaseAgent(
    name="TestBot",
    role="helpful assistant",
    instructions="Your answer questions briefly in 1-2 sentences."
)
reponse = agent.run("What is Python?")
print(reponse)