from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

response = client.chat.completions.create(
            model="meta-llama/llama-3.2-3b-instruct",  # 或其他可用模型
            messages=[
                {"role": "user", "content": "What is the result of 1+1?"}
            ]
        )

print(response.choices[0].message.content)