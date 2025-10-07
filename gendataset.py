# coding: utf-8

import os
import json
import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from threading import Lock
from typing import Dict, List, Tuple, Any, Optional, Set
import itertools

from tqdm import tqdm

try:
    from openai import OpenAI
except ImportError:
    print("OpenAI library not found. Please install it with: pip install openai")
    exit()


# --- 1. 配置模块 ---
ROUTER_MODEL = "qwen3-4b"
ROUTER_KEY_PATHS = [
    "usage/qwen", "usage/qwen1", "usage/qwen2", "usage/qwen3", "usage/qwen4",
]
ROUTER_API_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MAX_WORKERS = 5 # 并行数保持不变
MAX_RETRIES = 3
RETRY_DELAY = 5
API_TIMEOUT = 300.0

SOURCE_DATA_PATH = "dataset/TestData/training_data_2200.json"
OUTPUT_DIR = "data_reports/dataset/training_data_2200/qwen3-4b/gpt-4o/llama-3.2-3b-instruct/20251006_221702"
LOG_DIR = os.path.join(OUTPUT_DIR, "logs")

# 简化输出路径，只保留一个
OUTPUT_WO_THINKING_PATH = os.path.join(OUTPUT_DIR, "datasetTraining_wo_thinking.json")

# 只需要一个文件锁
file_lock = Lock()


# --- 2. 日志模块 ---
def setup_logger() -> logging.Logger:
    os.makedirs(LOG_DIR, exist_ok=True)
    log_filename = f"generation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_filepath = os.path.join(LOG_DIR, log_filename)
    logger = logging.getLogger("DatasetGenerator")
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s %(module)s:%(lineno)d] %(message)s", datefmt="%m-%d %H:%M:%S"))
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s] %(message)s", datefmt="%m-%d %H:%M:%S"))
    logger.addHandler(stream_handler)
    return logger

logger = setup_logger()


# --- 3. API 调用模块 (流式) ---
def get_api_key(path: str) -> Optional[str]:
    if not os.path.exists(path):
        logger.warning(f"API密钥文件 '{path}' 未找到，将跳过。")
        return None
    with open(path, 'r') as f:
        key = f.read().strip()
        if not key:
            logger.warning(f"API密钥文件 '{path}' 为空，将跳过。")
            return None
        return key

def get_model_response(system_prompt: str, user_prompt: str, api_key: str):
    """使用 openai 库以流式方式调用API，并处理数据流。"""
    try:
        client = OpenAI(
            api_key=api_key,
            base_url=ROUTER_API_BASE_URL,
            timeout=API_TIMEOUT,
        )
        
        # 切换为流式调用，并移除 enable_thinking
        stream = client.chat.completions.create(
            model=ROUTER_MODEL,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ],
            stream=True,
            temperature=1,
            extra_body={"enable_thinking": False}
        )

        full_content_parts = []
        request_id = None
        
        # 从响应头中获取 request_id
        if hasattr(stream, 'response') and hasattr(stream.response, 'headers'):
            request_id = stream.response.headers.get('x-request-id')

        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                full_content_parts.append(chunk.choices[0].delta.content)
        
        final_text = "".join(full_content_parts)
        
        return {
            "text": final_text,
            "request_id": request_id,
        }

    except Exception as e:
        logger.error(f"API 流式调用时发生异常 (Key: ...{api_key[-4:]}): {e}")
        return None


# --- 4. 数据处理和文件操作模块 ---
def load_existing_data(filepath: str) -> Set:
    if not os.path.exists(filepath): return set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 确保 instruction 字段存在
            return {item.get('instruction', '') for item in data if 'instruction' in item}
    except (json.JSONDecodeError, FileNotFoundError):
        logger.warning(f"无法解析或找到文件 '{filepath}'，将视为空文件。")
        return set()

def append_to_json(filepath: str, data_item: Dict[str, Any], lock: Lock):
    with lock:
        try:
            if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
                with open(filepath, 'r+', encoding='utf-8') as f:
                    # 读取现有数据，追加新项，然后重写文件
                    json_data = json.load(f)
                    json_data.append(data_item)
                    f.seek(0)
                    json.dump(json_data, f, indent=4, ensure_ascii=False)
                    f.truncate()
            else:
                # 文件不存在或为空，创建并写入新列表
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump([data_item], f, indent=4, ensure_ascii=False)
        except Exception as e:
            logger.error(f"写入文件 '{filepath}' 失败: {e}")

def parse_model_output(text: str) -> str:
    """仅解析并返回<Plan>标签及其内容"""
    plan_match = re.search(r"<Plan>(.*?)</Plan>", text, re.DOTALL)
    if plan_match:
        # 重新构建完整的<Plan>标签内容
        plan_content = f"<Plan>{plan_match.group(1).strip()}</Plan>"
        return plan_content
    else:
        logger.warning("在模型输出中未找到 <Plan> 标签，将返回原始输出。")
        # 如果没有找到<Plan>，返回原始文本以防数据丢失
        return text.strip()


# --- 5. 主逻辑模块 ---
def generate_prompts(query: str) -> Tuple[str, str]:
    system_prompt = """You are an expert AI cognitive scientist and systems architect. Your mission is to analyze a given problem and create a structured XML plan that follows the **Explain-Analyze-Generate (EAG)** framework.

The plan will be executed by a multi-threaded AI system using two distinct models. Your task decomposition and difficulty assignments must leverage the unique capabilities of these models.

### **Executor Model Profiles**
You will be assigning tasks to two available models. Use their profiles below to accurately estimate the `Difficulty` for each step:
  * **Small Model (Llama 3.2 3B): A highly capable and efficient small model. It excels at tasks requiring strong instruction-following, summarization, and rewriting. It is proficient in standard grade-school math (GSM8K) and common-sense reasoning (ARC Challenge). Use this model for well-defined, procedural, or structured tasks.
  * **Large Model (GPT-4o): A powerful, state-of-the-art large model with a vast knowledge base. It demonstrates superior performance in tasks requiring deep reasoning and expert-level knowledge, such as advanced scientific reasoning (GPQA Diamond, MMLU-Pro), competition-level math (AIME), and complex coding (LiveCodeBench). It is the preferred choice for tasks requiring synthesis, critical analysis, and solving problems in specialized domains.

### **Plan Structure: The EAG Framework**
Your generated `<Plan>` **must** be structured into three logical stages:

1.  **Step 1: The "Explain" Step**
      * The plan must begin with a single, foundational step (ID="1").
      * **Task:** The task for this step is directly inspired by the Explainer agent's role. It must be phrased as follows:
        > **"To assist the following agents, what is your understanding of the question after reviewing it, focusing only on essential information and filtering out all irrelevant details?"**

2.  **The "Analyze" Steps**
      * These are the intermediate steps that perform the core logical work.
      * **Task:** Break down the problem into the smallest possible, independent sub-tasks to solve the problem. These steps should rely on the "Explain" step (i.e., `Rely="1"`) or other completed analysis steps.
      * **Core Directives for Plan Generation**:
        1.  **Analyze the Problem**: Break down the problem into its core logical components.
        2.  **Strategic Milestones**: Focus on the high-level, conceptual milestones required to solve the problem.
        3.  **Maximize Parallelism**: Decompose into as many independent sub-tasks as possible.
        4.  **Formulate Actionable Questions**: The `Task` attribute must be a clear, self-contained question ending with a question mark (?). Do not leak answers in the task description.
        5.  **Delegate Knowledge Retrieval**: If a specific formula, theorem, or principle is required, your task is to create a step that **asks for that formula or principle** (e.g., "What is the formula for...?"). Delegate the retrieval of specific knowledge to the Executor.
      * **Goal:** Maximize parallelism. If multiple pieces of information can be processed independently, create a separate step for each.

3.  **The Final "Generate" Step**
      * The plan must conclude with a single aggregation step.
      * **Task:** The task for this step is directly inspired by the Generator agent's role. It must be phrased as follows:
        > **"After reviewing the original question and the thoughts of previous agents, what is the final answer to the question?"**
**Keep the plan Concise**: The final plan must contain **fewer than 7 steps**. Focus only on the most critical milestones needed to solve the problem.

### **XML Plan Constraints**
  * `ID`: A unique integer.
  * `Task`: The question for the executor AI. Must end with a question mark (?).
  * `Difficulty`: An integer from 1-9.
      * **1-4 (Small Model):** Procedural tasks, basic calculations, applying a known formula.
      * **5-9 (Large Model):** Complex reasoning, synthesis, or critical knowledge retrieval.
  * `Token`: An estimated integer for the answer's token count.
  * `Rely`: The `ID`(s) of prerequisite steps, separated by commas if multiple.

### Examples
**Problem**: Four years ago, Kody was only half as old as Mohamed. If Mohamed is currently twice 30 years old, how old is Kody?
**Output**:
<Plan>
<Step ID="1" Task="To assist the following agents, what is your understanding of the question after reviewing it, focusing only on essential information and filtering out all irrelevant details?" Difficulty="3" Token="60" Rely=""/>
<Step ID="2" Task="Based on the explanation in Step 1, what is Mohamed's current age?" Difficulty="2" Token="10" Rely="1"/>
<Step ID="3" Task="Using Mohamed's current age from Step 2, what was his age four years ago?" Difficulty="1" Token="10" Rely="2"/>
<Step ID="4" Task="Based on Mohamed's age four years ago, what was Kody's age four years ago?" Difficulty="2" Token="10" Rely="3"/>
<Step ID="5" Task="After reviewing the original question and the thoughts of previous agents, what is the final answer to the question?" Difficulty="2" Token="15" Rely="4"/>
</Plan>

**Question**: "Which of the following stars or stellar systems will appear the brightest in V magnitude when observed from Earth? Assume there is no extinction. [List of 6 options with apparent/absolute magnitudes and distances]"
**Output**:
<Plan>
<Step ID="1" Task="What is the formula for calculating the combined apparent magnitude of a multi-star system from the individual apparent magnitudes of its components?" Difficulty="2" Rely=""/>
<Step ID="2" Task="What is the distance modulus formula that relates a star's apparent magnitude (m), its absolute magnitude (M), and its distance in parsecs (d)?" Difficulty="2" Rely=""/>
<Step ID="3" Task="For each of the six options (a-f) provided in the problem, calculate its final apparent V magnitude as observed from Earth. Use the formulas from Step 1 and 2 where necessary. List the final apparent magnitude for each option." Difficulty="6" Rely="1,2"/>
<Step ID="4" Task="Based on the six apparent magnitude values calculated in Step 3, which star or stellar system is the brightest (i.e., has the numerically lowest magnitude value)?" Difficulty="2" Rely="3"/>
</Plan>

**Question**: "Identify the compound C9H11NO2 using the given data. IR: medium to strong intensity bands at 3420 cm-1, 3325 cm-1; strong band at 1720 cm-1. 1H NMR: 1.20 ppm (t, 3H); 4.0 ppm (bs, 2H); 4.5 ppm (q, 2H); 7.0 ppm (d, 2H), 8.0 ppm (d, 2H)."
**Output**:
<Plan>
<Step ID="1" Task="What functional group(s) are indicated by the IR absorption bands at 3420, 3325, and 1720 cm-1?" Difficulty="4" Rely=""/>
<Step ID="2" Task="In the 1H NMR spectrum, what structural fragment is suggested by the combination of a triplet signal at 1.20 ppm (3H) and a quartet signal at 4.5 ppm (2H)?" Difficulty="4" Rely=""/>
<Step ID="3" Task="In the 1H NMR spectrum, what structural feature is suggested by the presence of two distinct doublet signals at 7.0 ppm (2H) and 8.0 ppm (2H) in the aromatic region?" Difficulty="5" Rely=""/>
<Step ID="4" Task="What does the broad singlet signal at 4.0 ppm (2H) in the 1H NMR spectrum, combined with the IR data from Step 1, suggest about the functional group present?" Difficulty="5" Rely="1"/>
<Step ID="5" Task="Based on the fragments identified in the previous steps (a para-substituted aromatic ring, an ethyl group, and an amine/ester/amide functional group), assemble a complete molecular structure that matches the formula C9H11NO2." Difficulty="7" Rely="1,2,3,4"/>
<Step ID="6" Task="Compare the structure deduced in Step 5 with the provided options to identify the correct compound name." Difficulty="2" Rely="5"/>
</Plan>

**Problem**: Find the degree for the given field extension Q(sqrt(2), sqrt(3), sqrt(18)) over Q.\\n\\nA. 0\\nB. 4\\nC. 2\\nD. 6
**Output**:
<Plan>
<Step ID="1" Task="To assist the following agents, what is your understanding of the question after reviewing it, focusing only on essential information and filtering out all irrelevant details?" Difficulty="4" Token="50" Rely=""/>
<Step ID="2" Task="Is there a dependency between sqrt(2), sqrt(3), and sqrt(18)? Simplify the field extension Q(sqrt(2), sqrt(3), sqrt(18)) if possible." Difficulty="3" Token="30" Rely="1"/>
<Step ID="3" Task="Based on the simplified field extension from Step 2, what is the degree of this extension over Q?" Difficulty="5" Token="30" Rely="2"/>
<Step ID="4" Task="After reviewing the original question and the thoughts of previous agents, what is the final answer to the question?" Difficulty="2" Token="20" Rely="3"/>
</Plan>

**Problem**: The set of all real numbers under the usual multiplication operation is not a group since\\n\\nA. multiplication is not a binary operation\\nB. multiplication is not associative\\nC. identity element does not exist\\nD. zero has no inverse
**Output**:
<Plan>
<Step ID="1" Task="To assist the following agents, what is your understanding of the question after reviewing it, focusing only on essential information and filtering out all irrelevant details?" Difficulty="3" Token="50" Rely=""/>
<Step ID="2" Task="Check the closure property: Is multiplication a binary operation on the set of all real numbers?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="3" Task="Check the associative property: Is multiplication of real numbers associative?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="4" Task="Check the identity property: Is there an identity element for multiplication in the set of real numbers?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="5" Task="Check the inverse property: Does every element in the set of real numbers have a multiplicative inverse?" Difficulty="3" Token="30" Rely="1"/>
<Step ID="6" Task="After reviewing the original question and the thoughts of previous agents, what is the final answer to the question?" Difficulty="4" Token="30" Rely="2,3,4,5"/>
</Plan>

Now, based on the following Problem, generate a response that meets all the requirements above. The final plan must contain **fewer than 7 steps**. 
"""

    user_prompt = f'''
        **Question**: {query}
        **Plan**:
    '''
    return system_prompt, user_prompt

def process_single_item(item: Dict[str, Any], api_key: str):
    """处理单个数据项的工作线程函数"""
    problem_query = item.get("problem")
    if not problem_query:
        logger.warning(f"跳过一个没有 'problem' 字段的数据项: {item}")
        return

    system_prompt, user_prompt = generate_prompts(problem_query)
    
    logger.info(f"正在为问题构建数据集: {problem_query[:80]}...")
    logger.info("===== Prompt to Planner (openai-stream) =====")
    logger.info(f"System Prompt: [Provided in definition]\nUser Prompt:\n{user_prompt}")

    response_data = get_model_response(system_prompt, user_prompt, api_key)
    
    if not response_data:
        logger.error(f"问题 '{problem_query[:80]}...' 的API调用失败或返回为空对象。")
        return

    response_text = response_data["text"]
    request_id = response_data["request_id"]

    if not response_text or not response_text.strip():
        log_msg = (
            f"问题 '{problem_query[:80]}...' 的模型响应内容为空或仅含空白，跳过此条目。 "
            f"Request ID: {request_id or 'N/A'}"
        )
        logger.error(log_msg)
        return

    api_key_suffix = api_key[-4:] if api_key else "N/A"
    logger.info(f"===== Planner Response (Key: ...{api_key_suffix}) =====\n{response_text}")
    
    # 解析输出，现在只返回一个结果
    final_output = parse_model_output(response_text)
    
    # 构建要保存的数据
    data_to_save = {
        "instruction": problem_query,
        "input": "",
        "system": system_prompt,
        "output": final_output
    }

    # 写入单个JSON文件
    append_to_json(OUTPUT_WO_THINKING_PATH, data_to_save, file_lock)
    logger.info(f"已成功处理并保存问题: {problem_query[:80]}...")


def main():
    logger.info("===== 数据集生成脚本启动 (openai-stream模式) =====")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    logger.info(f"所有输出将被保存到: {OUTPUT_DIR}")

    api_keys = [key for path in ROUTER_KEY_PATHS if (key := get_api_key(path)) is not None]
    if not api_keys:
        logger.error("未能加载任何有效的API Key，程序无法继续。")
        return
    logger.info(f"成功加载 {len(api_keys)} 个API Keys。")
    
    # 使用API Key的数量作为并行数
    max_workers = len(api_keys)
    logger.info(f"并行线程数将设置为: {max_workers}")
    
    key_cycler = itertools.cycle(api_keys)

    try:
        with open(SOURCE_DATA_PATH, 'r', encoding='utf-8') as f:
            source_data = json.load(f)
        logger.info(f"成功从 '{SOURCE_DATA_PATH}' 加载 {len(source_data)} 条源数据。")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"无法加载源数据文件 '{SOURCE_DATA_PATH}': {e}"); return

    # 从目标输出文件加载已处理的数据
    processed_instructions = load_existing_data(OUTPUT_WO_THINKING_PATH)
    if processed_instructions:
        logger.info(f"检测到 {len(processed_instructions)} 条已处理的数据，将跳过它们。")
    
    items_to_process = [item for item in source_data if item.get("problem") not in processed_instructions]

    if not items_to_process:
        logger.info("所有数据均已处理完毕，无需执行。"); return
        
    logger.info(f"总计需要处理 {len(items_to_process)} 条新数据。")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_single_item, item, next(key_cycler)) for item in items_to_process]
        
        for future in tqdm(as_completed(futures), total=len(futures), desc=f"生成数据集(stream, {max_workers}个线程)"):
            try:
                future.result()
            except Exception as exc:
                logger.error(f"一个线程任务生成了异常: {exc}", exc_info=True)

    logger.info("===== 数据集生成任务完成 =====")
    logger.info(f"数据集保存在: {OUTPUT_WO_THINKING_PATH}")

if __name__ == "__main__":
    main()
