from openai import OpenAI
import os

def get_api_key(file_path="together_ai"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
    else:
        raise FileNotFoundError(f"Credentials file '{file_path}' not found.")
    return api_key

with open("usage/generate_prompt.txt", 'r', encoding='utf-8') as f:
    file_content = f.read()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=get_api_key("usage/openrouter"),
)

response = client.chat.completions.create(
            model="qwen/qwen3-14b:free",  # 或其他可用模型
            messages=[
                {"role": "system", "content": file_content},
                {"role": "user", "content": "What is the result of 1+1?"}
            ]
        )

print(response.choices[0].message.content)