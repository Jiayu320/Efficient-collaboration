import json
import os

import concurrent.futures
import traceback
import time

from util.io_file import read_json, write_json

from openai import OpenAI
import tqdm as tqdm

def generate_cot_summary(question, sentence_groups, api_key=None, analysis_model="gpt-4"):
    """
    调用API对拼接后的CoT生成简短总结
    
    参数:
        question: 问题文本
        sentence_groups: 分句后的CoT文本
        api_key: API密钥（可选）
    
    返回:
        对CoT的一句话总结
    """
    # 总结模板
    system_message = """
    You are an assistant that converts a chain-of-thought (CoT) breakdown into a concise planning document.  
    Task rules  
    1. The user will give you several numbered “groups” of CoT sentences (typically JSON-like).  
    2. For each group, output exactly one bullet beginning with “* Group k: ”.  
    3. Each bullet must state only the actions / subtasks that need to be carried out in that group.  
    4. Do NOT include any conclusions, results, or answers.  
    5. Present the bullets as a single “To-Do List”.  
    6. Preserve the original group numbering order.  
    7. Write in clear, concise English.
    8. Make sure groups numbers are complete and sequential, starting from 1.

    Example (for few-shot in-context learning – keep it verbatim):

    Summarize each group of CoT steps by listing only the actions or tasks to be done, without including any final results. Format the output as a to-do list for planning purposes.  
    Query: Find the last three digits of the product of the positive roots of $\\sqrt{1995}x^{\\log_{1995}x}=x^2.$.
    CoT steps:  
    {
    "group1": [
    "Okay, so I need to find the last three digits of the product of the positive roots of the equation √(1995) * x^(log_{1995} x) = x².",
    "Hmm, let's see. First, let me try to understand the equation and figure out how to solve it.",
    "The equation is given as √(1995) * x^(log_{1995} x) = x². That looks a bit complicated with the logarithm in the exponent."
    ],
    "group2": [
    "Maybe I can take logarithms on both sides to simplify it? Or perhaps rewrite the equation using properties of exponents and logarithms.",
    "Let me recall that log_b a = (ln a)/(ln b), so log_{1995} x is equal to (ln x)/(ln 1995).",
    "Also, x raised to log_{1995} x can be rewritten using exponentials.",
    "Wait, maybe I can express x^(log_{1995} x) as e^{(ln x) * (log_{1995} x)}. But that might not be helpful. Let me think differently."
    ],
    "group3": [
    "Alternatively, since the equation has x in the exponent and also x squared, maybe substituting t = log_{1995} x would help.",
    "Let me try that. Let's set t = log_{1995} x, which means that x = 1995^t.",
    "Then substituting back into the equation: √(1995) * (1995^t)^{t} = (1995^t)^2"
    ],
    "group4": [
    "Simplify both sides:",
    "Left side: √(1995) * 1995^{t^2}",
    "Right side: 1995^{2t}"
    ],
    "group5": [
    "Since 1995 is a positive real number, we can equate the exponents on both sides, but first, let's express √(1995) as 1995^{1/2}.",
    "So the left side becomes 1995^{1/2} * 1995^{t^2} = 1995^{t^2 + 1/2}",
    "The right side is 1995^{2t}",
    "Therefore, since the bases are the same and positive, we can set the exponents equal: t^2 + 1/2 = 2t"
    ],
    "group6": [
    "That simplifies to t^2 - 2t + 1/2 = 0. Hmm, quadratic equation. Let's solve for t:",
    "t = [2 ± sqrt(4 - 2)] / 2 = [2 ± sqrt(2)] / 2 = 1 ± (sqrt(2)/2)",
    "So t = 1 + (√2)/2 or t = 1 - (√2)/2"
    ]
    }

    Summarized to-do list:
    * Group 1: Examine and interpret the original equation to decide on an overall solving strategy.  
    * Group 2: Use logarithmic and exponential laws to simplify the equation algebraically.  
    * Group 3: Introduce the substitution t = log₁₉₉₅ x and rewrite the entire equation in terms of t.  
    * Group 4: Simplify both sides of the substituted equation to express them as comparable powers of 1995.  
    * Group 5: Convert √1995 to an exponent form, equate the resulting exponents, and obtain a quadratic in t.  
    * Group 6: Solve the derived quadratic equation for t.  

    End of example.

    Now is your turn. Please summarize the following CoT steps into a concise to-do list for planning purposes:
    """
    user_content = """
    Query: {Question}
    CoT steps: 
    {CoT}
    Summarized to-do list:
    """
    
    try:
        # 初始化OpenAI客户端
        # client = OpenAI(base_url="https://api.bianxie.ai/v1", api_key=api_key)
        client = OpenAI(base_url="https://api.deepseek.com", api_key=api_key)

        # 调用API
        response = client.chat.completions.create(
            model=analysis_model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_content.format(Question=question, CoT=sentence_groups)}
            ]
        )
        
        # 提取并返回总结
        summary = response.choices[0].message.content.strip()
        # print(f"生成的总结: {summary}")
        return summary
    
    except Exception as e:
        return f"生成总结时出错: {str(e)}"

def rate_cot_difficulty(question, sentence_groups, api_key=None, analysis_model="gpt-4"):
    """
    调用API根据CoT判断步骤的难度，1-10打分
    
    参数:
        sentence_groups: 分句后的CoT文本
        api_key: API密钥
    
    返回:
        难度评分（1-10）
    """
    system_content = """
    You are an assistant whose job is to assign a difficulty score (integer 1 – 10) to each numbered group of chain-of-thought (CoT) steps the user provides.

    Scoring rubric
    1  = Very trivial; can be done almost mechanically with no conceptual hurdle.  
    2 – 3 = Straight-forward; basic recall or routine algebra.  
    4 – 5 = Moderate; requires several connected ideas or non-obvious algebraic manipulations.  
    6 – 7 = Challenging; involves multi-step reasoning, substitutions, or non-standard tricks.  
    8 – 9 = Very hard; demands deep insight, advanced theory, or creative leaps.  
    10 = Extremely difficult; research-level or exceptionally intricate reasoning.

    Task rules
    1. Keep the original group numbering order.  
    2. Output one line per group in the form: “Group k: <score>”.  
    3. Do not justify or explain the score; supply only the integer.  
    4. Use plain digits 1-10 (no decimals).  
    5. Place the list under the heading “Difficulty Scores”.
    6. Make sure groups numbers are complete and sequential, starting from 1.

    Example (few-shot, keep exactly as is)
    Query: Find the last three digits of the product of $\\sqrt{1995}x^{\\log_{1995}x}=x^2.$.
    CoT steps:
    {
    "group1": [
    "Okay, so I need to find the last three digits of the product of the positive roots of the equation √(1995) * x^(log_{1995} x) = x².",
    "Hmm, let's see. First, let me try to understand the equation and figure out how to solve it.",
    "The equation is given as √(1995) * x^(log_{1995} x) = x². That looks a bit complicated with the logarithm in the exponent."
    ],
    "group2": [
    "Maybe I can take logarithms on both sides to simplify it? Or perhaps rewrite the equation using properties of exponents and logarithms.",
    "Let me recall that log_b a = (ln a)/(ln b), so log_{1995} x is equal to (ln x)/(ln 1995).",
    "Also, x raised to log_{1995} x can be rewritten using exponentials.",
    "Wait, maybe I can express x^(log_{1995} x) as e^{(ln x) * (log_{1995} x)}. But that might not be helpful. Let me think differently."
    ],
    "group3": [
    "Alternatively, since the equation has x in the exponent and also x squared, maybe substituting t = log_{1995} x would help.",
    "Let me try that. Let's set t = log_{1995} x, which means that x = 1995^t.",
    "Then substituting back into the equation: √(1995) * (1995^t)^{t} = (1995^t)^2"
    ],
    "group4": [
    "Simplify both sides:",
    "Left side: √(1995) * 1995^{t^2}",
    "Right side: 1995^{2t}"
    ],
    "group5": [
    "Since 1995 is a positive real number, we can equate the exponents on both sides, but first, let's express √(1995) as 1995^{1/2}.",
    "So the left side becomes 1995^{1/2} * 1995^{t^2} = 1995^{t^2 + 1/2}",
    "The right side is 1995^{2t}",
    "Therefore, since the bases are the same and positive, we can set the exponents equal: t^2 + 1/2 = 2t"
    ],
    "group6": [
    "That simplifies to t^2 - 2t + 1/2 = 0. Hmm, quadratic equation. Let's solve for t:",
    "t = [2 ± sqrt(4 - 2)] / 2 = [2 ± sqrt(2)] / 2 = 1 ± (sqrt(2)/2)",
    "So t = 1 + (√2)/2 or t = 1 - (√2)/2"
    ]
    }

    Assistant:  
    Group 1: 2  
    Group 2: 4  
    Group 3: 5  
    Group 4: 3  
    Group 5: 6  
    Group 6: 5  

    End of example.
    """
    rating_template = """
    Now it is your turn. Please evaluate the difficulty of the following groups on a 1-10 scale, using the rubric provided above. Do not explain or justify your scores, just follow the format exactly.
    Query: {Question}
    CoT steps:
    {CoT}
    Assistant:  
    """
    
    try:
        # 初始化OpenAI客户端
        # client = OpenAI(base_url="https://api.bianxie.ai/v1", api_key=api_key)
        client = OpenAI(base_url="https://api.deepseek.com", api_key=api_key)

        # 调用API
        response = client.chat.completions.create(
            model=analysis_model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": rating_template.format(Question=question, CoT=sentence_groups)}
            ],
        )
        
        # 提取并返回评分
        scores = response.choices[0].message.content.strip()
        # print(f"生成的评分: {scores}")
        return scores
    
    except Exception as e:
        return f"评分时出错: {str(e)}"

def analyzing_step_dependencies(question, sentence_groups, api_key=None, analysis_model="gpt-4"):
    """
    分析每个步骤的依赖关系

    参数:
        question: 问题文本
        sentence_groups: 各步骤的句子组
        api_key: API密钥（可选）
        analysis_model: 模型的版本号（可选）

    返回:
        依赖关系的字典
    """
    system_content = """
    You are an assistant specialized in analyzing dependency relations among solution-step groups in a math explanation.
    Your job: determine which earlier step-groups each group relies on.
    Task rules:
    1. A group may depend only on groups with smaller numbers.
    2. A dependency exists if a group directly uses a previous group’s result, concept, or method.
    3. A dependency exists if logically the later group needs the earlier group’s conclusion in order to proceed.
    4. If a group has no dependencies, its value is an empty array [].
    5. Favor parallelism: include only the minimal, truly necessary dependencies so that independent groups can be processed concurrently; avoid long serial chains whenever possible.
    6. Directly output the result without any additional words or explanations.
    7. Make sure groups numbers are complete and sequential.
    Example (few-shot, keep exactly as is)
    Query: Find the last three digits of the product of the positive roots of √(1995) x^{log_{1995} x} = x².
    CoT steps:
    {
    "group1": [
    "Okay, so I need to find the last three digits of the product of the positive roots of the equation √(1995) * x^(log_{1995} x) = x².",
    "Hmm, let's see. First, let me try to understand the equation and figure out how to solve it.",
    "The equation is given as √(1995) * x^(log_{1995} x) = x². That looks a bit complicated with the logarithm in the exponent."
    ],
    "group2": [
    "Maybe I can take logarithms on both sides to simplify it? Or perhaps rewrite the equation using properties of exponents and logarithms.",
    "Let me recall that log_b a = (ln a)/(ln b), so log_{1995} x is equal to (ln x)/(ln 1995).",
    "Also, x raised to log_{1995} x can be rewritten using exponentials.",
    "Wait, maybe I can express x^(log_{1995} x) as e^{(ln x) * (log_{1995} x)}. But that might not be helpful. Let me think differently."
    ],
    "group3": [
    "Alternatively, since the equation has x in the exponent and also x squared, maybe substituting t = log_{1995} x would help.",
    "Let me try that. Let's set t = log_{1995} x, which means that x = 1995^t.",
    "Then substituting back into the equation: √(1995) * (1995^t)^{t} = (1995^t)^2"
    ],
    "group4": [
    "Simplify both sides:",
    "Left side: √(1995) * 1995^{t^2}",
    "Right side: 1995^{2t}"
    ],
    "group5": [
    "Since 1995 is a positive real number, we can equate the exponents on both sides, but first, let's express √(1995) as 1995^{1/2}.",
    "So the left side becomes 1995^{1/2} * 1995^{t^2} = 1995^{t^2 + 1/2}",
    "The right side is 1995^{2t}",
    "Therefore, since the bases are the same and positive, we can set the exponents equal: t^2 + 1/2 = 2t"
    ],
    "group6": [
    "That simplifies to t^2 - 2t + 1/2 = 0. Hmm, quadratic equation. Let's solve for t:",
    "t = [2 ± sqrt(4 - 2)] / 2 = [2 ± sqrt(2)] / 2 = 1 ± (sqrt(2)/2)",
    "So t = 1 + (√2)/2 or t = 1 - (√2)/2"
    ]
    }

    Dependency mapping:
    Group 1: []
    Group 2: ["group1"]
    Group 3: ["group1"]
    Group 4: ["group3"]
    Group 5: ["group4"]
    Group 6: ["group5"]

    End of example.    
    """
    
    user_template = """
    
    Query: {Question}
    CoT steps:
    {CoT}
    Assistant:  
    """
    
    try:
        # 初始化OpenAI客户端
        # client = OpenAI(base_url="https://api.bianxie.ai/v1", api_key=api_key)
        client = OpenAI(base_url="https://api.deepseek.com", api_key=api_key)
        # 调用API
        response = client.chat.completions.create(
            model=analysis_model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_template.format(Question=question, CoT=sentence_groups)}
            ]
            # response_format={"type": "json_object"}
        )
        
        # 获取API返回的依赖关系并解析为字典
        dependencies_json = response.choices[0].message.content.strip()
        # print(f"生成的依赖关系: {dependencies_json}")
        dependencies = json.loads(dependencies_json)
        
        # 标准化依赖关系格式
        normalized_dependencies = {}
        for key, value in dependencies.items():
            # 确保键名使用正确的"group"前缀
            if key.startswith("Group "):
                normalized_key = f"group{key[6:]}"
            elif not key.startswith("group"):
                normalized_key = f"group{key}"
            else:
                normalized_key = key
            
            normalized_dependencies[normalized_key] = value
            
        return normalized_dependencies
    
    except Exception as e:
        error_msg = f"分析步骤依赖关系时出错: {str(e)}"
        return {"error": error_msg}

def analyze_group_results(group_summary, group_difficulty):
    """
    解析所有组别的summary和difficulty并返回数组
    
    参数:
        group_summary: 各组别的总结字符串
        group_difficulty: 各组别的难度字符串
    
    返回:
        包含所有组别summary和difficulty的数组
    """
    results = []
    
    # 提取所有组别的summary
    summary_lines = group_summary.split('\n')
    summaries = {}
    for line in summary_lines:
        line = line.strip()
        if line.startswith("* Group "):
            parts = line.split(":", 1)
            if len(parts) == 2:
                group_num = parts[0].replace("* Group ", "").strip()
                summary = parts[1].strip()
                summaries[group_num] = summary
    
    # 提取所有组别的difficulty
    difficulty_lines = group_difficulty.split('\n')
    difficulties = {}
    for line in difficulty_lines:
        line = line.strip()
        if line.startswith("Group "):
            parts = line.split(":", 1)
            if len(parts) == 2:
                group_num = parts[0].replace("Group ", "").strip()
                try:
                    difficulty = int(parts[1].strip())
                except ValueError:
                    difficulty = parts[1].strip()
                difficulties[group_num] = difficulty
    
    # 合并数据到结果数组
    all_group_nums = sorted(set(list(summaries.keys()) + list(difficulties.keys())), 
                         key=lambda x: int(x) if x.isdigit() else float('inf'))
    
    for group_num in all_group_nums:
        results.append({
            "group_num": group_num,
            "summary": summaries.get(group_num),
            "difficulty": difficulties.get(group_num)
        })
    
    return results

def convert_group_results_to_dict(group_results, group_relations):
    """
    将group_results数组转换为按格式组织的字典
    
    参数:
        group_results: analyze_group_results函数的返回结果
        group_relations: 步骤依赖关系字典
    
    返回:
        summaries、difficulties和relations的字典，格式为{"group1": value, "group2": value, ...}
    """
    summaries = {}
    difficulties = {}
    relations = {}
    
    for item in group_results:
        group_num = item.get("group_num")
        summary = item.get("summary")
        difficulty = item.get("difficulty")
        
        if group_num:
            group_key = f"group{group_num}"
            if summary is not None:
                summaries[group_key] = summary
            if difficulty is not None:
                difficulties[group_key] = difficulty
    
    # 处理依赖关系字典，确保键名格式正确
    if group_relations and isinstance(group_relations, dict):
        relations = {}
        for key, value in group_relations.items():
            if key.startswith("groupgroup"):
                fixed_key = key.replace("groupgroup", "group")
            elif not key.startswith("group"):
                fixed_key = f"group{key}"
            else:
                fixed_key = key
            relations[fixed_key] = value
    else:
        relations = group_relations
    
    result = {
        "summaries": summaries,
        "difficulties": difficulties
    }
    
    if relations:
        result["relations"] = relations
    
    return result

def call_api_with_retry(api_call, *args, **kwargs):
    max_retries = 5
    for i in range(max_retries):
        try:
            # 调用API
            result = api_call(*args, **kwargs)
            return result
        except Exception as e:
            if "负载已饱和" in str(e) or "rate limit" in str(e).lower():
                wait_time = 2 ** i
                print(f"API限流，等待{wait_time}秒后重试...")
                time.sleep(wait_time)
            else:
                raise
    raise RuntimeError("API多次重试后仍然失败")

def process_file(file_path, output_dir=None, api_key=None, analysis_model="gpt-4"):
    """
    处理单个文件:拼接CoT，生成总结，评估难度，分析步骤依赖关系
    
    参数:
        file_path: JSON文件路径
        output_dir: 输出目录（可选）
        api_key: API密钥（可选）
        analysis_model: 模型的版本号（可选）

    返回:
        处理结果字典
    """
    try:
        data = read_json(file_path)[0] # 原始数据
        # data = read_json(file_path)
        question = data.get("question", "")
        sentence_groups = data.get("analysis", {}).get("sentence_groups", {})

        # 使用重试机制调用API
        group_summary = call_api_with_retry(generate_cot_summary, question, sentence_groups, api_key, analysis_model)
        if not group_summary:
            raise ValueError("生成CoT总结失败，可能是API调用出错或返回空结果。")
        time.sleep(1)
        group_difficulty = call_api_with_retry(rate_cot_difficulty, question, sentence_groups, api_key, analysis_model)
        if not group_difficulty:
            raise ValueError("生成CoT难度评分失败，可能是API调用出错或返回空结果。")
        time.sleep(1)
        # 分析步骤依赖关系
        group_relations = call_api_with_retry(analyzing_step_dependencies, question, sentence_groups, api_key, analysis_model)
        if not group_relations:
            raise ValueError("分析步骤依赖关系失败，可能是API调用出错或返回空结果。")
        time.sleep(1)

        # 分析结果并生成分组数据
        group_results = analyze_group_results(group_summary, group_difficulty)
        
        # 将group_results转换为所需格式
        formatted_results = convert_group_results_to_dict(group_results, group_relations)

        # 将结果添加到原始数据的analysis字段中
        if "analysis" not in data:
            data["analysis"] = {}
        
        data["analysis"]["summaries"] = formatted_results["summaries"]
        data["analysis"]["difficulties"] = formatted_results["difficulties"]
        if "relations" in formatted_results:
            data["analysis"]["relations"] = formatted_results["relations"]
        
        data["analysis_model_new"] = analysis_model
        # 将更新后的原始数据写回到原文件
        original_data = read_json(file_path)
        original_data[0] = data
        write_json(file_path, original_data)
        
        # 如果指定了输出目录，保存处理结果到新文件
        if output_dir:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            # analysis中只保留必要的字段
            data["analysis"] = {
                "sentence_groups": data["analysis"].get("sentence_groups", {}),
                "summaries": data["analysis"].get("summaries", {}),
                "difficulties": data["analysis"].get("difficulties", {}),
                "relations": data["analysis"].get("relations", {})
            }
            result = {
                "id": data.get("id", ""),
                "question": question,
                "answer": data.get("answer", ""),
                "solution": data.get("solution", ""),
                "analysis": data.get("analysis", {}),
                "original_token_count": data.get("original_token_count", 0),
                "analysis_model_new": analysis_model
            }
            output_path = os.path.join(output_dir, os.path.basename(file_path))
            write_json(output_path, result)

            return result
        
        else:
            result = {
                "id": data.get("id", ""),
                "question": question,
                "answer": data.get("answer", ""),
                "solution": data.get("solution", ""),
                "analysis": data.get("analysis", {}),
                "original_token_count": data.get("original_token_count", 0)
            }
            return result
        
    except Exception as e:
        error_msg = f"处理文件 {file_path} 时出错: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return {"error": error_msg}

def process_directory(input_dir, output_dir, api_key=None, max_workers=4, analysis_model=None):
    """
    处理目录中的所有JSON文件，如果输出目录中已存在处理好的文件则跳过
    
    参数:
        input_dir: 输入目录路径
        output_dir: 输出目录路径
        api_key: API密钥（可选）
        max_workers: 最大并行处理线程数
        analysis_model: 模型的版本号（可选）
    
    返回:
        处理成功和失败的文件列表
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取所有JSON文件
    json_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) 
                 if os.path.isfile(os.path.join(input_dir, f)) and f.endswith('.json')]
    
    # 获取已处理的文件列表
    processed_files = set()
    if os.path.exists(output_dir):
        processed_files = {os.path.basename(f) for f in os.listdir(output_dir) 
                          if os.path.isfile(os.path.join(output_dir, f)) and f.endswith('.json')}
    
    # 筛选未处理的文件
    files_to_process = [f for f in json_files if os.path.basename(f) not in processed_files]
    
    print(f"找到 {len(json_files)} 个文件，其中 {len(json_files) - len(files_to_process)} 个已处理，{len(files_to_process)} 个待处理")
    
    successful_files = []
    failed_files = []
    
    # 将已处理的文件添加到成功列表中
    for file_path in json_files:
        if os.path.basename(file_path) in processed_files:
            successful_files.append(file_path)
    
    # 并行处理文件
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(process_file, file_path, output_dir, api_key, analysis_model): file_path for file_path in files_to_process}
        
        for future in tqdm.tqdm(concurrent.futures.as_completed(future_to_file), total=len(files_to_process), desc="Processing files"):
            file_path = future_to_file[future]
            try:
                result = future.result()
                if "error" in result:
                    failed_files.append(file_path)
                else:
                    successful_files.append(file_path)
                    # 添加延迟以避免API速率限制
                    time.sleep(0.5)
            except Exception as e:
                failed_files.append(file_path)
                print(f"处理文件 {file_path} 时出错: {str(e)}")
    
    # 保存处理结果统计
    stats = {
        "total_files": len(json_files),
        "successful_files": len(successful_files),
        "failed_files": len(failed_files),
        "failed_file_paths": failed_files
    }
    write_json(os.path.join(output_dir, "processing_stats.json"), stats)
    
    return successful_files, failed_files

def get_api_key(file_path="together_ai"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
    else:
        raise FileNotFoundError(f"Credentials file '{file_path}' not found.")
    return api_key

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="处理JSON文件中的思维链（CoT）数据")
    # parser.add_argument("--input", default="data\\structure\\limo\\583.json", help="输入文件或目录路径")
    parser.add_argument("--input", default="data\\structure\\fix", help="输入文件或目录路径")
    parser.add_argument("--output", default="data\\structure\\limo_out", help="输出目录路径，默认为None（直接修改原文件）")
    # parser.add_argument("--output", default=None, help="输出目录路径，默认为None（直接修改原文件）")
    parser.add_argument("--api_key", default=get_api_key("deepseek"), help="API密钥")
    parser.add_argument("--workers", type=int, default=4, help="并行处理的最大线程数")
    parser.add_argument("--analysis_model", default="deepseek-reasoner", help="模型的版本号") # gpt-4.1, deepseek-ai/DeepSeek-R1,o3-mini-high, claude-3-7-sonnet-latest
    args = parser.parse_args()

    if os.path.isfile(args.input):
        # 处理单个文件
        result = process_file(args.input, args.output, args.api_key, args.analysis_model)
        print(f"处理完成: {args.input}")
    elif os.path.isdir(args.input):
        # 处理整个目录
        successful, failed = process_directory(args.input, args.output, args.api_key, args.workers, args.analysis_model)
        print(f"处理完成。成功: {len(successful)}，失败: {len(failed)}")
    else:
        print(f"错误:输入路径不存在 {args.input}")

