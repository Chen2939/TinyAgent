import json
import urllib.request

# Prepare request
data = json.dumps({
    "model": "gemma4:e4b",
    "messages": [{"role": "user", "content": "Hi, how is life?"}],
}).encode("utf-8")

# Post request
req = urllib.request.Request(
    url="http://localhost:11434/v1/chat/completions",
    data=data,
    headers={"Content-Type": "application/json"}
)

# Parse response
with urllib.request.urlopen(req) as response:
    result = json.loads(response.read())

# Print first choice of response
print(result["choices"][0])