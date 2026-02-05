# TEST 1

# from base_agent import BaseAgent

# agent = BaseAgent(
#     name="TestBot",
#     role="helpful assistant",
#     instructions="Your answer questions briefly in 1-2 sentences."
# )
# reponse = agent.run("What is Python?")
# print(reponse)



# TEST 2

from planner_agent import PlannerAgent
from researcher_agent import ResearcherAgent
from writer_agent import WriterAgent


print("=== PLANNER ===")
planner = PlannerAgent()
plan = planner.run("Create a blog post about Python for beginners")
print(plan)

print("\n=== RESEARCHER ===")
researcher = ResearcherAgent()
research = researcher.run("What are the key features of Python for beginners?")
print(research)

print("\n=== WRITER ===")
writer = WriterAgent()
article = writer.run(f"Write a short blog intro using this info: {research}")
print(article)