from orchestrator import Orchestrator

orchestrator = Orchestrator()

result = orchestrator.run_workflow(
    "Write a short email introducing our new AI product to customers"
)

print("\n" + "="*50)
print("WORKFLOW COMPLETE")
print("="*50)
print(f"\nFinal Output:\n{result['final_output']}")