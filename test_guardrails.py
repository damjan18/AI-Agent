from agents.guardrails import Guardrails
from agents.validated_agent import ValidatedAgent

# Test Guardrails directly
print("=== TESTING GUARDRAILS ===\n")

guardrails = Guardrails()

# Test input validation
print("--- Input Validation ---")
tests = [
    "",
    "Hello",
    "A" * 3000
]

for test in tests:
    is_valid, message = guardrails.check_input(test)
    preview = test[:30] + "..." if len(test) > 30 else test
    print(f"Input: '{preview}' -> Valid: {is_valid}, Message: {message}")

# Test output sanitization
print("\n--- Output Sanitization ---")
test_output = "Contact me at john@email.com or call 123-456-7890"
sanitized = guardrails.sanitize_output(test_output)
print(f"Original: {test_output}")
print(f"Sanitized: {sanitized}")

# Test sensitive word detection
print("\n--- Sensitive Word Detection ---")
sensitive_output = "Your password is 12345"
is_valid, message = guardrails.check_output(sensitive_output)
print(f"Output: '{sensitive_output}' -> Valid: {is_valid}, Message: {message}")

# Test ValidatedAgent
print("\n=== TESTING VALIDATED AGENT ===\n")

agent = ValidatedAgent(
    name="SafeBot",
    role="helpful assistant",
    instructions="You answer questions briefly and safely."
)

# Normal request
print("--- Normal Request ---")
response = agent.run("What is Python?")
print(f"Response: {response}\n")

# Empty input
print("--- Empty Input ---")
response = agent.run("")
print(f"Response: {response}\n")