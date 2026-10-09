from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1/", api_key="ollama")
resp = client.chat.completions.create(
    model="gemma3:12b",
    messages=[{"role": "user", "content": "你好"}],
)

print(resp.choices[0].message.content)