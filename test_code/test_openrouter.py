from openai import OpenAI
import os

def get_api_key(file_path="together_ai"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
    else:
        raise FileNotFoundError(f"Credentials file '{file_path}' not found.")
    return api_key

client = OpenAI(
  base_url="https://api.bianxie.ai/v1",
  api_key="sk-vKirQEe0vJmMN3X9UAENCCdheTHII81VCQm0NZHzG781H95Y",
)

response = client.chat.completions.create(
            model="gpt-4o",  # 或其他可用模型
            messages=[
                {"role": "user", "content": "What is the result of 1+1?"}
            ]
        )

print(response.choices[0].message.content)