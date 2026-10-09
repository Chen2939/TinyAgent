from LLM import LLM

# Reinitalize the LLM with the desired model and settings
llm = LLM(model="gemma4:e4b")

# Generate a `Response` dataclass
response = llm.generate(
    [{"role": "user",
      "content": "Hi, how is life?"}]
)
print(response)