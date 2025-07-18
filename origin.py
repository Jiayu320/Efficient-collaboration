import requests
import json
import os
import re
from collections import defaultdict
from openai import OpenAI
import time

def get_api_key(file_path="together_ai"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
    else:
        raise FileNotFoundError(f"Credentials file '{file_path}' not found.")
    return api_key

with open("prompt/generate_prompt.txt", 'r', encoding='utf-8') as f:
    file_content = f.read()

# query = "What is the smallest positive integer with six positive odd integer divisors and twelve positive even integer divisors?"
query = "What is the result of 1+1?"

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {get_api_key('usage/openrouter')}",
    "Content-Type": "application/json"
}

payload = {
    "model": "qwen/qwen3-14b:free",
    "messages": [
        {"role": "system", "content": file_content},
        {"role": "user", "content": query}
    ],
    "stream": True
}

# 用于存储解析后的任务数据
tasks = defaultdict(dict)
current_step = None
xml_buffer = ""

def parse_step_attributes(attr_str):
    """解析属性字符串为字典"""
    attrs = {}
    # 使用正则匹配属性键值对
    pattern = r'(\w+)="(.*?)"'
    for match in re.finditer(pattern, attr_str):
        key, value = match.groups()
        attrs[key] = value
    return attrs

def process_xml_buffer():
    """处理XML缓冲区中的完整标签"""
    global xml_buffer, tasks, current_step
    
    # 查找完整的<Step>标签
    step_match = re.search(r'<Step\s+(.*?)/>', xml_buffer, re.DOTALL)
    if not step_match:
        # 检查是否有结束标签
        if '</Plan>' in xml_buffer:
            xml_buffer = ""
        return False
    
    full_tag = step_match.group(0)
    attr_str = step_match.group(1).strip()
    
    # 从缓冲区移除已处理的部分
    xml_buffer = xml_buffer[step_match.end():]
    
    # 解析属性
    attrs = parse_step_attributes(attr_str)
    if 'ID' not in attrs:
        return True
    
    # 添加到任务字典
    step_id = attrs['ID']
    tasks[step_id] = attrs
    tasks[step_id]['Result'] = None  # 添加Result字段
    
    # 设置当前步骤（用于后续结果收集）
    current_step = step_id
    return True

def generate_step_result(prompt, difficulty, threshold=2):
    difficulty = int(difficulty)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=get_api_key("usage/openrouter")
    )
    if difficulty < threshold:
        response = client.chat.completions.create(
            model="qwen/qwen3-14b:free",  # 或其他可用模型
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    else:
        response = client.chat.completions.create(
            model="qwen/qwen3-235b-a22b",  # 或其他可用模型
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    return response.choices[0].message.content

def build_step_prompt(current_step, tasks, query):
    """构建当前步骤的提示"""
    prompt_template = """
    You are a mathematical problem-solving assistant. I will provide you with a math problem and a specific step from my solution plan. Your task is to complete ONLY this specific step based on the description and token limit.

    PROBLEM:
    {Problem}

    CURRENT STEP:
    Task: {Task}
    Token Limit: {Token}
    Relied Results: {Relied_Results}

    INSTRUCTIONS:
    1. Focus ONLY on completing the specific task described above
    2. Keep your response within the token limit (approximately {Token} tokens)
    3. Use the results from previous steps as necessary
    4. Show your work clearly with mathematical reasoning
    5. Provide a concise conclusion for this step
    6. Do NOT attempt to solve other parts of the problem
    7. Format mathematical expressions properly

    Complete only the task described above within the token limit:
    """
    # 获得依赖的任务的具体结果
    relied_results = tasks[current_step].get('Rely', '')
    if relied_results:
        relied_results = [tasks[step_id]['Result'] for step_id in relied_results.split(',') if step_id in tasks]
    else:
        relied_results = []
    return prompt_template.format(
        Problem=query,
        Task=tasks[current_step].get('Task', ''),
        Token=tasks[current_step].get('Token', ''),
        Relied_Results=relied_results
    ), tasks[current_step].get('Difficulty', '')

import concurrent.futures

# Track completed steps
completed_steps = set()
# Create a thread pool executor
executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
# Store futures for each step
futures = {}

def is_step_ready(step_id, tasks):
    """Check if a step is ready to be processed (dependencies completed or none)"""
    rely_str = tasks[step_id].get('Rely', '')
    if not rely_str:
        return True
    
    rely_steps = rely_str.split(',')
    return all(step in completed_steps for step in rely_steps)

def process_step(step_id, tasks, query):
    """Process a single step"""
    prompt, difficulty = build_step_prompt(step_id, tasks, query)
    result = generate_step_result(prompt, difficulty)
    tasks[step_id]['Result'] = result
    completed_steps.add(step_id)
    return step_id

def router(tasks):
    """Schedule tasks for parallel execution when dependencies are met"""
    # Check for new tasks that can be started
    for step_id in tasks:
        if step_id not in futures and step_id not in completed_steps:
            if is_step_ready(step_id, tasks):
                print(f"Starting step {step_id}...")
                future = executor.submit(process_step, step_id, tasks, query)
                futures[step_id] = future
    
    # Check for completed tasks
    completed_futures = [f for step_id, f in list(futures.items()) if f.done()]
    for f in completed_futures:
        try:
            step_id = f.result()
            del futures[step_id]
        except Exception as e:
            print(f"Error in task execution: {e}")
    
    # If there are pending or running tasks, schedule another check soon
    if futures:
        time.sleep(0.1)  # Small delay to prevent CPU hogging
        return True  # Continue routing
    return False  # No more tasks to route

# 流式处理
with requests.post(url, headers=headers, json=payload, stream=True) as r:
    for chunk in r.iter_content(chunk_size=1024, decode_unicode=True):
        if not chunk:
            continue
            
        # 处理SSE格式
        for line in chunk.splitlines():
            line = line.strip()
            if not line or line == "data: [DONE]":
                continue
                
            if line.startswith('data: '):
                try:
                    data_obj = json.loads(line[6:])
                    content = data_obj["choices"][0]["delta"].get("content", "")
                    print(content, end="", flush=True)  # 实时输出
                    
                    # 添加到XML缓冲区
                    xml_buffer += content
                    
                    # 尝试解析缓冲区中的完整标签
                    while process_xml_buffer():
                        pass

                except json.JSONDecodeError:
                    pass

while process_xml_buffer():
    pass

'''
print("\n\nParsed Tasks:")
for step_id, attrs in sorted(tasks.items(), key=lambda x: int(x[0])):
    print(f"Step {step_id}:")
    for k, v in attrs.items():
        print(f"  {k}: {v}")
    print()
'''
