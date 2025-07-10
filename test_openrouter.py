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
  api_key=get_api_key("bianxie"),
)

'''
completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
'''
response = client.chat.completions.create(
            model="gpt-4",  # 或其他可用模型
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the meaning of life?"}
            ]
        )
print(response.choices[0].message.content)