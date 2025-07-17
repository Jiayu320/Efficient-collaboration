import json
import os

import concurrent.futures
import traceback
import time

from util.io_file import read_json, write_json

from openai import OpenAI
import tqdm as tqdm

def generate_step_plan(question, CoT, api_key=None, analysis_model="gpt-4"):
    system_content = """
    As a mathematical reasoning decomposition expert, generate an optimized step-by-step plan in XML format. Requirements:
    1. Steps ≤ 10 with maximized parallelism
    2. Difficulty scale: 1-10 (1=simplest, 10=hardest)
    3. Each step contains:
    - Task: Clear action description (no conclusions)
    - Difficulty: Differentiated score (1-10)
    - Token: Estimated token consumption
    - Rely: Prerequisite step IDs (if any)

    Output Example:
    <Plan>
    <Step ID="1" Task="Identify cases from condition 3∈{a,a²-2a}" Difficulty="3" Token="70"/>
    <Step ID="2" Task="Process case a=3: compute set and verify" Difficulty="2" Token="90" Rely="1"/>
    ...
    </Plan>

    Guidelines:
    - Difficulty must reflect: 
    1-2: Basic computation
    3-4: Standard operations 
    5-6: Logical analysis 
    7-10: Advanced synthesis
    - Minimize dependency chains
    - Token estimation based on GPT-4 tokenizer

    Example (few-shot, keep exactly as is)
    Query: "If $3 \\in \\{a, a^2 - 2a\\}$, then the value of the real number $a$ is ______."
    CoT steps: "Okay, so I've got this problem here: If 3 is an element of the set {a, a\u00b2 - 2a}, then what is the real number a? Hmm, let's try to figure this out step by step. I'm not too sure about this, but I think I can work it out.\n\nFirst off, the set is {a, a\u00b2 - 2a}, which means that either a is equal to 3, or a\u00b2 - 2a is equal to 3. Since sets don't care about order and don't allow duplicates, each element is unique. But since the problem mentions 3 is in the set, we just need to check both possibilities.\n\nLet me break it down into two cases:\n\n**Case 1: a = 3**\n\nWell, if a is 3, then let's check what the other element is. The other element is a\u00b2 - 2a, which would be 3\u00b2 - 2*3 = 9 - 6 = 3. So, both elements of the set would be 3, but wait, sets can't have duplicate elements, right? So, actually, the set would just be {3}. But the original set was given as {a, a\u00b2 - 2a}, which suggests it has two distinct elements. Hmm, does that mean that a\u00b2 - 2a can't also be 3? Or is it okay because sets remove duplicates?\n\nWait, actually, I think in set theory, duplicates are automatically removed, so {3, 3} is just {3}. So, in this case, does 3 still count as an element? Yes, but the set only has one element. So, in this problem, does the set have to have two elements? The problem doesn't specify, it just says 3 is in the set. So, even if the set becomes a singleton, 3 is still an element. So, a = 3 is a possible solution. But maybe the set is meant to have two elements? The problem isn't clear on that. Hmm, maybe I should consider that and move on to Case 2.\n\n**Case 2: a\u00b2 - 2a = 3**\n\nSo, if a\u00b2 - 2a is equal to 3, then let's set up the equation:\n\na\u00b2 - 2a = 3\n\nSubtract 3 from both sides to get a quadratic equation:\n\na\u00b2 - 2a - 3 = 0\n\nNow, let's try to factor this quadratic. Looking for two numbers that multiply to -3 and add to -2. Hmm, the factors of -3 are 1 and -3, or -1 and 3. 3 and -1 multiply to -3 and add to 2, which is not -2. Wait, 1 and -3 multiply to -3 and add to -2. Yes! So, the quadratic factors as:\n\n(a - 3)(a + 1) = 0\n\nSo, the solutions are a = 3 or a = -1.\n\nWait a second, so we have a = 3 or a = -1. But hold on, in Case 1, we considered a = 3, and now in Case 2, we get a = -1. So, are both solutions acceptable? Or do we have to check something?\n\nLet me check both solutions to see if they satisfy the original condition, that 3 is in the set {a, a\u00b2 - 2a}.\n\nFirst, check a = 3:\n\nAs before, the set becomes {3, 3\u00b2 - 2*3} = {3, 9 - 6} = {3, 3}, which is just {3}. So, 3 is an element. So, that's good.\n\nNow, check a = -1:\n\nThe set becomes {-1, (-1)\u00b2 - 2*(-1)} = {-1, 1 + 2} = {-1, 3}. So, 3 is in the set. Great, that works too.\n\nSo, both a = 3 and a = -1 satisfy the condition that 3 is in the set.\n\nWait, but the problem is asking for \"the value of the real number a\". So, are there two solutions? Or did I make a mistake?\n\nLooking back, in Case 1, a = 3 leads to the set {3}, which is still valid because sets can have one element. In Case 2, a = -1 gives the set {-1, 3}, which has two elements. So, both a = 3 and a = -1 are solutions.\n\nBut hold on, is a = 3 a valid solution? Because when a = 3, both elements become 3, so it's not a two-element set anymore. But the original problem doesn't specify that the set must have two elements, just that 3 is in it. So, I think both a = 3 and a = -1 are acceptable.\n\nBut wait, let me double-check a = 3:\n\nIf a = 3, then the set is {3, 3} which is {3}. Since 3 is in the set, that's okay. Similarly, for a = -1, the set is {-1, 3}, so 3 is in the set.\n\nSo, the solutions are a = 3 and a = -1.\n\nBut let me look at the problem again: \"If 3 \u2208 {a, a\u00b2 - 2a}, then the value of the real number a is ______.\" It's asking for the value of a. Hmm, so is there one value or multiple?\n\nWait, maybe I'm missing something. Because in a set, the elements are unique. So, when a = 3, it's still a valid set with one element, but does that count? Maybe in the problem's context, they expect a two-element set, so a\u00b2 - 2a must be different from a. So, a\u00b2 - 2a \u2260 a.\n\nLet's see: a\u00b2 - 2a \u2260 a implies a\u00b2 - 3a \u2260 0, which implies a \u2260 0 and a \u2260 3. So, if a is 3, then a\u00b2 - 2a is also 3, so that makes the set {3}, not {3, 3}. So, if the problem assumes that {a, a\u00b2 - 2a} has two distinct elements, then a cannot be 3. Therefore, a must be -1.\n\nSo, this is a bit ambiguous. The problem just states that 3 is an element of the set, without specifying whether the set is a singleton or a pair. If we consider the set as defined with two elements, then we must have a \u2260 3 because a\u00b2 - 2a = a when a = 3, making the set a singleton. Therefore, the only valid solution where the set has two elements is a = -1.\n\nSo, maybe the answer is a = -1. But I'm not 100% sure because the problem doesn't specify that the set must have two elements. Hmm, perhaps I should consider both cases.\n\nBut to reconcile, let me see the problem again: \"If 3 \u2208 {a, a\u00b2 - 2a}, then the value of the real number a is ______.\" So, it's just saying that 3 is in the set. Whether the set is singleton or pair, it doesn't matter, as long as 3 is in it.\n\nTherefore, both a = 3 and a = -1 satisfy 3 \u2208 {a, a\u00b2 - 2a}. So, why did I think of another possibility? Maybe it's just me overcomplicating.\n\nBut looking again, in the first case, when a = 3, the set is {3}, so 3 is there. In the second case, a = -1, the set is {-1, 3}, so 3 is there.\n\nSo, both are valid, right? So, the problem is asking for \"the value of the real number a\", so perhaps it's expecting multiple answers? Or is there something else?\n\nWait, the problem is written in a way that seems to expect a single answer. Hmm. Maybe I need to consider that if a = 3, then the set is {3}, which is just 3. So, does that count as 3 being in the set? Yes. So, perhaps both are correct, but maybe the problem expects two possible answers, but it's a fill-in-the-blank. So, maybe both are acceptable.\n\nWait, but looking back, in Chinese math problems, sometimes they expect all possible answers. Wait, no, the problem is in English. It says, \"the value of the real number a is ______.\" Hmm, maybe both 3 and -1.\n\nBut let me make sure. Let me plug in the values again:\n\na = 3:\n\nSet becomes {3, 3}, which is just {3}, and 3 is an element. So, 3 is included.\n\na = -1:\n\nSet becomes {-1, 1 + 2}, which is {-1, 3}, so 3 is an element. That works too.\n\nSo, both a = 3 and a = -1 are correct.\n\nBut the problem is a bit ambiguous in whether a is supposed to make the set have two distinct elements or not. If it's supposed to be a set with two elements, then only a = -1 is acceptable. If it's just that 3 is in the set, regardless of the number of elements, both are acceptable.\n\nWait, let me read the original problem again: \"If 3 \u2208 {a, a\u00b2 - 2a}, then the value of the real number a is ______.\"\n\nIt doesn't specify anything else, so just that 3 is in the set. So, a can be 3 or -1.\n\nBut the answer is a real number. So, is there a unique solution? Or is it multiple solutions? Since the problem is a fill-in-the-blank, maybe it's expecting both. But the original problem didn't specify, so perhaps I should consider the set to have two elements, hence a = -1.\n\nWait, but perhaps in the problem's original context, they are considering that the set has two elements, so when a = 3, you get a singleton, which is not a two-element set. So, that might be against the problem's expectation.\n\nTherefore, perhaps the intended answer is -1, and 3 is excluded because it leads to a singleton. So, the answer is -1.\n\nHmm, I think I'm overcomplicating it, but since I have two possible answers, I need to figure out which one is expected.\n\nWait, in set notation, if it's {a, a\u00b2 - 2a}, it's usually implying that it has two distinct elements. Otherwise, they would just write {a} or something else. So, perhaps they expect a = -1 as the solution because that gives a set with two distinct elements. So, maybe -1 is the answer they're looking for.\n\nBut then, technically, a = 3 also satisfies 3 \u2208 {a, a\u00b2 - 2a}, even if the set is a singleton. So, maybe both are acceptable. But the problem is a bit ambiguous. Since it's a fill-in-the-blank, maybe both? But perhaps, in the problem's source, the intended answer is -1.\n\nBut in any case, since we're solving it step by step, I think the safe answer is both 3 and -1. So, if the problem allows multiple solutions, both are correct. But if it's expecting a single answer, maybe -1. Hmm.\n\nWait, another thought: perhaps 3 is the other element, so when a is 3, the other element is also 3. So, if you consider that the set must have 3 as one element, then both possibilities a = 3 and a\u00b2 - 2a = 3 must be considered.\n\nBut when a = 3, the set is {3}. So, 3 is in the set, that's true. So, even if the other element is also 3, that's acceptable. So, 3 is still in the set.\n\nBut in the case of a = -1, the set is {-1, 3}, so both -1 and 3 are in the set.\n\nTherefore, both solutions are valid. So, I think both a = 3 and a = -1 are correct. So, maybe the answer is both? But the question is phrased as \"the value of the real number a\", singular. So, if they expect only one value, perhaps they expect both.\n\nBut in that case, how? Because \"the value\" is singular. Hmm.\n\nWait, if it's \"the value\", but it's a set, which could have multiple elements, but 3 is just one of them. So, if a can be either 3 or -1, maybe both. So, perhaps I need to write both.\n\nBut how would that look? If I have to write it as a numerical answer, separated by commas or something?\n\nBut in the original problem, it's in Chinese, but the translation is \"If 3 \u2208 {a, a\u00b2 - 2a}, then the value of the real number a is ______.\"\n\nIn Chinese math problems, sometimes they accept multiple answers if applicable. But in this case, as a fill-in-the-blank, unless they specify all possible answers, it's a bit unclear.\n\nWait, but let's think again. The problem says \"the value of the real number a\", but \"value\" is singular. So, maybe they expect only one. Hmm. So, which one is the answer?\n\nWait, perhaps let me check both. Maybe they consider that a must be different from 3? Because if a is 3, then the set is {3}, but it's a single element set, so 3 is still an element. But if a is -1, the set is two elements. So, maybe it's supposed to have two elements, and therefore, the answer is -1.\n\nAlternatively, maybe it's just a question expecting both, and the user can write both.\n\nBut in Chinese math problems, sometimes they prefer listing all solutions.\n\nBut the translation is given as \"the value of the real number a is ______.\" So, if they had two solutions, would they phrase it differently? Maybe \"the values\" or \"the possible values\"?\n\nSo, maybe only -1 is the answer. Because if a is 3, it's a bit of a trivial solution, just makes the set {3}, which doesn't provide a proper two-element set. So, perhaps they are expecting the non-trivial solution, which is -1.\n\nAlternatively, considering both, if I have to write both, then the answer is a is equal to 3 or -1. But again, it's not clear.\n\nWait, another thought: in sets, if you have {a, a\u00b2 - 2a}, it's implied that a and a\u00b2 - 2a are two different elements. So, if a is 3, then both elements become the same. So, the set is actually {3}, not {3, 3}. So, in the problem, if it's given as {a, a\u00b2 - 2a}, it's intended to be a two-element set, so a and a\u00b2 - 2a must be different.\n\nTherefore, to have a two-element set, a\u00b2 - 2a must be different from a, so:\n\na\u00b2 - 2a \u2260 a\n\nWhich simplifies to:\n\na\u00b2 - 3a \u2260 0\n\nSo, a(a - 3) \u2260 0\n\nWhich implies that a \u2260 0 and a \u2260 3.\n\nTherefore, if the problem expects the set to have two distinct elements, a can't be 3 or 0. So, a = 3 is not acceptable in that case.\n\nTherefore, the only solution is a = -1.\n\nHence, the answer is -1.\n\nYes, that makes sense. Because if a = 3, the set becomes a singleton, which is probably not the intended case, especially since the set is presented as having two elements: {a, a\u00b2 - 2a}.\n\nSo, I think the problem expects the set to have two distinct elements, hence a must not be equal to 3, so the answer is a = -1.\n\nOkay, so after all that thinking, I think the correct answer is a = -1.\n\n**Final Answer**\nThe value of the real number \\( a \\) is \\boxed{-1}"
    Assistant:
    <Plan><Step ID="1" Task="Identify the two cases from the condition: either a=3 or a²-2a=3" Difficulty="3" Token="70"/><Step ID="2" Task="Handle Case 1: Compute set elements when a=3 and verify 3∈set" Difficulty="2" Token="90" Rely="1"/><Step ID="3" Task="Handle Case 2: Solve quadratic equation a²-2a=3 for roots" Difficulty="4" Token="110" Rely="1"/><Step ID="4" Task="Analyze set representation {a, a²-2a} to determine if distinct elements are required" Difficulty="6" Token="130" Rely="1"/><Step ID="5" Task="Verify all candidate solutions by substitution into original set condition" Difficulty="3" Token="120" Rely="2,3"/><Step ID="6" Task="Apply distinctness condition to filter valid solutions" Difficulty="5" Token="100" Rely="4,5"/><Step ID="7" Task="Formulate final answer with mathematical notation" Difficulty="1" Token="40" Rely="6"/></Plan>
    End of example.
    """
    
    user_template = """
    Now it is your turn. Do not explain, just follow the format exactly.
    Query: {Question}
    CoT steps:{CoT}
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
                {"role": "user", "content": user_template.format(Question=question, CoT=CoT)}
            ]
        )

        plan = response.choices[0].message.content.strip()
        if not plan.startswith("<Plan>") or not plan.endswith("</Plan>"):
            raise ValueError("API返回的依赖关系格式不正确，必须以<Plan>开头并以</Plan>结尾。")
        else:
            return plan
    except Exception as e:
        error_msg = f"分析步骤依赖关系时出错: {str(e)}"
        return {"error": error_msg}

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
    try:
        data = read_json(file_path) # 原始数据
        # data = read_json(file_path)
        question = data.get("question", "")
        sentence_groups = data.get("analysis", {}).get("sentence_groups", {})

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

