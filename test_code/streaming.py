import requests
import json
import os

def get_api_key(file_path="together_ai"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
    else:
        raise FileNotFoundError(f"Credentials file '{file_path}' not found.")
    return api_key

with open("prompt/generate_prompt.txt", 'r', encoding='utf-8') as f:
    file_content = f.read()

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
  "Authorization": f"Bearer {get_api_key('usage/openrouter')}",
  "Content-Type": "application/json"
}

payload = {
  "model": "meta-llama/llama-3-8b-instruct",
  "messages": [
     {"role": "system", "content": file_content},
     {"role": "user", "content": "What is the result of 1+1?"}
     ],
  "stream": True
}

buffer = ""
with requests.post(url, headers=headers, json=payload, stream=True) as r:
  for chunk in r.iter_content(chunk_size=1024, decode_unicode=True):
    buffer += chunk
    while True:
      try:
        # Find the next complete SSE line
        line_end = buffer.find('\n')
        if line_end == -1:
          break

        line = buffer[:line_end].strip()
        buffer = buffer[line_end + 1:]

        if line.startswith('data: '):
          data = line[6:]
          if data == '[DONE]':
            break

          try:
            data_obj = json.loads(data)
            content = data_obj["choices"][0]["delta"].get("content")
            if content:
              print(content, end="", flush=True)
          except json.JSONDecodeError:
            pass
      except Exception:
        break
