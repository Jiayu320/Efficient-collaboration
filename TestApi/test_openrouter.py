from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

# "meta-llama/llama-3-8b-instruct", "meta-llama/llama-3.2-3b-instruct:free"
# openai/gpt-4o
response = client.chat.completions.create(
            model="openai/gpt-4o",  # 或其他可用模型
            messages=[
                {"role": "user", "content": "What is the result of 1+1?"}
            ]
        )

print(response.choices[0].message.content)