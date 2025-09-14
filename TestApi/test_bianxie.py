from openai import OpenAI

client = OpenAI(
  base_url="https://api.bianxie.ai/v1",
  api_key="sk-hyfoZxYog2I4WCJWO9tzZS92zmTfJN72KVkSeAtT9QWtNsF3",
)

response = client.chat.completions.create(
            model="gpt-4o",  # 或其他可用模型
            messages=[
                {"role": "user", "content": "What is the result of 1+1?"}
            ]
        )

print(response.choices[0].message.content)