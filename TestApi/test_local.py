from openai import OpenAI
client = OpenAI(api_key="0", base_url="http://127.0.0.1:6006/v1")

messages = [
    {"role": "system", "content": "Generate a solution plan that breaks down the problem into logical steps, identifying dependencies, difficulty levels and token usage."},
    {"role": "user", "content": "What is the result of 1+1?"}]
# 启用流式输出
stream = client.chat.completions.create(
    messages=messages,
    # model="saves/Qwen3-1.7B-Instruct/full/sft",
    model="Qwen/Qwen2.5-3B-Instruct",
    stream=True  # 关键参数 [[9]]
)

# 逐块读取并输出
for chunk in stream:
    if chunk.choices[0].delta.content:  # 仅输出新增内容
        print(chunk.choices[0].delta.content, end="", flush=True)