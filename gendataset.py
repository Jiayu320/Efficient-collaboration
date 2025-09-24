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

# 使用 tqdm 提供优雅的进度条
from tqdm import tqdm

# *** MODIFIED: 回归到使用 openai 库 ***
try:
    from openai import OpenAI
except ImportError:
    print("OpenAI library not found. Please install it with: pip install openai")
    exit()


# --- 1. 配置模块 ---
ROUTER_MODEL = "qwen3-235b-a22b-thinking-2507"
ROUTER_KEY_PATHS = [
    "usage/qwen", "usage/qwen1", "usage/qwen2", "usage/qwen3", "usage/qwen4",
]
ROUTER_API_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
# MAX_WORKERS 将被动态设置为Key的数量
MAX_RETRIES = 3
RETRY_DELAY = 5
API_TIMEOUT = 300.0

SOURCE_DATA_PATH = "dataset/TestData/s1k1_data.json"
OUTPUT_DIR = "data_reports/dataset/s1k1_data/qwen3-235b-a22b-thinking-2507/gpt-4o/qwen2.5-3b-instruct/20250924_013352"
LOG_DIR = os.path.join(OUTPUT_DIR, "logs")

OUTPUT_W_THINKING_PATH = os.path.join(OUTPUT_DIR, "datasetTraining_w_thinking.json")
OUTPUT_WO_THINKING_PATH = os.path.join(OUTPUT_DIR, "datasetTraining_wo_thinking.json")

lock_w_thinking = Lock()
lock_wo_thinking = Lock()


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


# --- 3. API 调用模块 (回归 openai) ---
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
    """使用 openai 库调用API，返回完整的 completion 对象或 None。"""
    try:
        client = OpenAI(
            api_key=api_key,
            base_url=ROUTER_API_BASE_URL,
            timeout=API_TIMEOUT,
        )
        completion = client.chat.completions.create(
            model=ROUTER_MODEL,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ]
        )
        return completion
    except Exception as e:
        logger.error(f"API 调用时发生异常 (Key: ...{api_key[-4:]}): {e}")
        return None


# --- 4. 数据处理和文件操作模块 ---
def load_existing_data(filepath: str) -> Set:
    if not os.path.exists(filepath): return set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {item.get('instruction', '') for item in data}
    except (json.JSONDecodeError, FileNotFoundError):
        logger.warning(f"无法解析或找到文件 '{filepath}'，将视为空文件。")
        return set()

def append_to_json(filepath: str, data_item: Dict[str, Any], lock: Lock):
    with lock:
        try:
            if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
                with open(filepath, 'r+', encoding='utf-8') as f:
                    json_data = json.load(f)
                    json_data.append(data_item)
                    f.seek(0); json.dump(json_data, f, indent=4, ensure_ascii=False); f.truncate()
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump([data_item], f, indent=4, ensure_ascii=False)
        except Exception as e:
            logger.error(f"写入文件 '{filepath}' 失败: {e}")

def parse_model_output(text: str) -> Tuple[str, str]:
    think_content = ""; plan_content = ""
    think_match = re.search(r"<think>(.*?)</think>", text, re.DOTALL)
    if think_match: think_content = think_match.group(1).strip()
    else: logger.warning("在模型输出中未找到 <think> 标签。")
    plan_match = re.search(r"<Plan>(.*?)</Plan>", text, re.DOTALL)
    if plan_match: plan_content = f"<Plan>{plan_match.group(1).strip()}</Plan>"
    else:
        logger.warning("在模型输出中未找到 <Plan> 标签。")
        if not think_content and "<Plan>" in text: plan_content = text
    full_output = f"<think>\n{think_content}\n</think>\n{plan_content}" if think_content else plan_content
    return full_output, plan_content


# --- 5. 主逻辑模块 ---
def generate_prompts(query: str) -> Tuple[str, str]:
    # Prompt内容保持不变
    system_prompt = '''You are an expert **first-principles thinker and master strategist**. Your primary function is to deconstruct any complex problem into a clear, logical, and operational sequence of steps for a machine to execute.

Given a problem, your output must consist of two parts, in this exact order:

1.  A **`<think>` block**: Contains your high-level strategic analysis of the problem.
2.  A **`<Plan>` block**: Contains the XML-formatted, step-by-step operational plan.

**Part 1: The `<think>` Block**
Before generating the plan, you must first perform and explicitly state your strategic analysis within `<think>` tags. This analysis must be thorough and answer the following three questions:

  * **Core Principle Identification**: What are the fundamental principles, theorems, or formulas required to solve this problem? Be specific (e.g., "This requires the prime factorization of 20\!, followed by a combinatorial count using the number of distinct prime factors," not just "number theory").
  * **Pitfall Prediction**: What are the most likely traps? This includes:
      * *Conceptual Traps*: Misinterpreting definitions (e.g., confusing midsegment with area bisector), mixing up reference frames, making incorrect assumptions.
      * *Calculation Traps*: Overlooking special cases/exceptions (e.g., initial terms in a series), using the wrong formula (e.g., for error propagation or molecular speed), making unit conversion errors (e.g., g/mol vs kg/molecule).
      * *Completeness Traps*: Stopping the reasoning process too early and failing to perform the final calculation or count.
  * **Strategy Formulation**: Based on the principles and pitfalls, what is your high-level, step-by-step strategy? **This strategy must be concrete.** For any calculation step, explicitly state the formula or method you intend to use. (e.g., "First, find the prime factors of N. Second, count the number of distinct prime factors, let's say `k`. Third, the number of coprime factor pairs is `2^(k-1)`. Finally, calculate this value.").

**Part 2: The `<Plan>` Block**
After the `<think>` block, generate a solution plan that is a direct, operational implementation of your stated strategy. The plan must adhere to these strict constraints:

#### **XML Plan Constraints:**

1.  **Plan Length**: Must contain between 2 and 10 steps.
2.  **Actionable & Precise Steps**: Each `<Step>` `Task` must be a distinct and **unambiguous operational instruction**.
      * For conceptual steps, ask a precise question about a definition or property.
      * For calculation steps, **the task must specify the exact formula or method to be used** (e.g., "Using the formula for coprime factor pairs, `2^(k-1)`, calculate the total number where `k` is the number of distinct prime factors?").
3.  **Logical Flow & Completeness**: The plan must represent a clear logical progression from start to finish. **The final step must be the final numerical calculation or conclusive statement.**
4.  **Contextual Linking**: When a step `N` relies on a step `M`, the `Task` for step `N` should explicitly reference the output or variables from `M`.
5.  **Difficulty**: Mark steps requiring non-trivial synthesis with `Difficulty >= 5`.
6.  **Attribute Integrity**: All attributes must be correctly formatted. The `Task` must end with a question mark (?).
7.  **XML Format**: Output ONLY the `<think>` and `<Plan>` blocks as specified.

-----

### **Examples of Good vs. Flawed Plans**

#### **Good Example \#1: Correct Core Principle and Complete Plan**

**Question**: "For how many rational numbers between 0 and 1 will $20\!$ be the resulting product of their numerator and denominator in lowest terms?"

**Response**:
<think>
**Core Principle Identification**: The core principle is number theory, specifically concerning prime factorization and coprime numbers. A rational number `a/b` is in lowest terms if `gcd(a, b) = 1`. The condition `a*b = 20!` means `a` and `b` must be formed by partitioning the prime factors of `20!`. For `a` and `b` to be coprime, they cannot share any prime factors.
**Pitfall Prediction**: The primary trap is stopping after identifying the principle and failing to perform the final count. The second trap is miscounting; the number of ways to partition `k` distinct items into two groups is `2^k`, but since `a/b` must be between 0 and 1, `a` must be less than `b`. This means we must exclude the case `a=b` (if possible) and divide the remaining pairs by 2. For a number like `20!` which is not a perfect square, `a` can never equal `b`.
**Strategy Formulation**: 1. Find the prime factorization of 20\!. 2. Identify the number of *distinct* prime factors, let's call this `k`. 3. For `a` and `b` to be coprime, each distinct prime factor's entire power (e.g., `2^18`) must go entirely to either `a` or `b`. There are `2^k` ways to distribute these `k` distinct prime factors into two sets. 4. Since `a < b`, we divide the total number of pairs by 2. The case `a=b` is impossible as 20\! is not a perfect square. Thus the final answer is `2^k / 2 = 2^(k-1)`. 5. I will execute this final calculation.
</think>
<Plan>
<Step ID="1" Task="What are the distinct prime factors of 20\! ?" Difficulty="4" Token="50" Rely=""/>
<Step ID="2" Task="Count the number of distinct prime factors found in Step 1. Let this count be k. What is the value of k?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="3" Task="The number of pairs of coprime factors (a,b) of 20\! is 2^k. The number of rational numbers a/b between 0 and 1 is half of this. Using the formula N = 2^(k-1), what is the final number of such rational numbers?" Difficulty="4" Token="50" Rely="2"/>
</Plan>

-----

#### **Bad Example \#1: Flawed Geometric Model**

**Question**: "One base of a trapezoid is $100$ units longer than the other base. The segment that joins the midpoints of the legs divides the trapezoid into two regions whose areas are in the ratio $2:3$. Let $x$ be the length of the segment that divides the trapezoid into two regions of equal area. Find the greatest integer that does not exceed $x^2/100$."

**Flawed Plan**:
<Plan>
<Step ID="1" Task="If we denote the shorter base as 'a' and the longer base as 'a + 100', what is the length of the segment joining the midpoints of the legs?" Difficulty="2" Token="30" Rely=""/>
<Step ID="2" Task="Using the fact that the midpoint segment divides the trapezoid into regions with area ratio 2:3, what equation can we write relating a and the height h?" Difficulty="5" Token="60" Rely="1"/>
<Step ID="3" Task="What is the length x of the equal-area-dividing segment in terms of a?" Difficulty="4" Token="50" Rely=""/>
<Step ID="4" Task="Calculate x²/100 and find the greatest integer." Difficulty="3" Token="30" Rely="2,3"/>
</Plan>
**Justification for why this is flawed**: This plan is **conceptually flawed**. It incorrectly assumes that the information about the "midpoint segment" (midsegment) can be directly used to find the base `a`. The midsegment divides the trapezoid's height in half, creating two smaller trapezoids. The ratio of their areas is fixed by the lengths of the bases and does not depend on `h`. The plan fails to establish the correct geometric relationship (using similar trapezoids and area formulas) needed to find `a`.

-----

#### **Bad Example \#2: Ignoring Exceptions and Incomplete Plan**

**Question**: "Find the remainder when $9 \\times 99 \\times 999 \\times \\cdots \\times \\underbrace{99\\cdots9}\_{\\text{999 9's}}$ is divided by $1000$."

**Flawed Plan**:
<Plan>
<Step ID="1" Task="How can we express a number with n consecutive 9's in terms of powers of 10?" Difficulty="2" Token="20" Rely=""/>
<Step ID="2" Task="What are the remainders when 9, 99, and 999 are divided by 1000?" Difficulty="3" Token="30" Rely=""/>
<Step ID="3" Task="For numbers with 4 or more 9's, what is their remainder when divided by 1000?" Difficulty="4" Token="40" Rely="1"/>
<Step ID="4" Task="How many terms in our product have a remainder of 999?" Difficulty="3" Token="30" Rely=""/>
<Step ID="5" Task="What is the final remainder of the entire product?" Difficulty="4" Token="50" Rely="2,3,4"/>
</Plan>
**Justification for why this is flawed**: This plan is **incomplete and invites error**. While it correctly separates some cases, Step 5 is too vague. A good plan would have separate, explicit steps to: (a) calculate the product of the remainders of the special cases (`9 * 99`), (b) calculate the product of the remainders of the general cases (`999^997`), and (c) multiply the results from (a) and (b) together modulo 1000. Lumping these into one step caused the model to forget one of the terms in the final calculation.
'''
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
    logger.info("===== Prompt to Planner (openai) =====")
    logger.info(f"System Prompt: [Provided in definition]\nUser Prompt:\n{user_prompt}")

    completion = get_model_response(system_prompt, user_prompt, api_key)
    
    if not completion:
        logger.error(f"问题 '{problem_query[:80]}...' 的API调用失败或返回为空对象。")
        return

    # 提取所需信息
    request_id = None
    response_text = ""
    try:
        # 从响应头中获取 request_id
        if hasattr(completion, '_response') and hasattr(completion._response, 'headers'):
            request_id = completion._response.headers.get('x-request-id')

        if completion.choices:
            response_text = completion.choices[0].message.content or ""
        
    except Exception as e:
        logger.error(f"解析completion对象时出错: {e}")
        return
        
    # 如果响应内容为空，记录详细的调试信息
    if not response_text:
        log_msg = (
            f"问题 '{problem_query[:80]}...' 的模型响应内容为空，跳过此条目。 "
            f"Request ID: {request_id or 'N/A'}"
        )
        try:
            # 记录包含reasoning_content的完整响应体
            full_response_dump = completion.model_dump_json(indent=2)
            log_msg += f"\n----- Full Server Response -----\n{full_response_dump}\n--------------------------"
        except Exception as dump_error:
            log_msg += f"\n无法转储完整的响应对象: {dump_error}"
        
        logger.error(log_msg)
        return

    api_key_suffix = api_key[-4:] if api_key else "N/A"
    logger.info(f"===== Planner Response (Key: ...{api_key_suffix}) =====\n{response_text}")
    
    output_w_thinking, output_wo_thinking = parse_model_output(response_text)
    
    base_data = {"instruction": problem_query, "input": "", "system": system_prompt}
    data_w_thinking = {**base_data, "output": output_w_thinking}
    data_wo_thinking = {**base_data, "output": output_wo_thinking}

    append_to_json(OUTPUT_W_THINKING_PATH, data_w_thinking, lock_w_thinking)
    append_to_json(OUTPUT_WO_THINKING_PATH, data_wo_thinking, lock_wo_thinking)
    logger.info(f"已成功处理并保存问题: {problem_query[:80]}...")


def main():
    logger.info("===== 数据集生成脚本启动 (openai模式) =====")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    logger.info(f"所有输出将被保存到: {OUTPUT_DIR}")

    api_keys = [key for path in ROUTER_KEY_PATHS if (key := get_api_key(path)) is not None]
    if not api_keys:
        logger.error("未能加载任何有效的API Key，程序无法继续。")
        return
    logger.info(f"成功加载 {len(api_keys)} 个API Keys。")
    
    # *** NEW: 动态设置并行数为API Key的数量 ***
    max_workers = len(api_keys)
    logger.info(f"并行线程数将设置为: {max_workers}")
    
    key_cycler = itertools.cycle(api_keys)

    try:
        with open(SOURCE_DATA_PATH, 'r', encoding='utf-8') as f:
            source_data = json.load(f)
        logger.info(f"成功从 '{SOURCE_DATA_PATH}' 加载 {len(source_data)} 条源数据。")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"无法加载源数据文件 '{SOURCE_DATA_PATH}': {e}"); return

    processed_instructions = load_existing_data(OUTPUT_W_THINKING_PATH)
    if processed_instructions:
        logger.info(f"检测到 {len(processed_instructions)} 条已处理的数据，将跳过它们。")
    
    items_to_process = [item for item in source_data if item.get("problem") not in processed_instructions]

    if not items_to_process:
        logger.info("所有数据均已处理完毕，无需执行。"); return
        
    logger.info(f"总计需要处理 {len(items_to_process)} 条新数据。")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for item in items_to_process:
            current_api_key = next(key_cycler)
            futures.append(executor.submit(process_single_item, item, current_api_key))
        
        for future in tqdm(as_completed(futures), total=len(futures), desc=f"生成数据集(openai, {max_workers}个线程)"):
            try:
                future.result()
            except Exception as exc:
                logger.error(f"一个线程任务生成了异常: {exc}", exc_info=True)

    logger.info("===== 数据集生成任务完成 =====")
    logger.info(f"带有思考过程的数据集保存在: {OUTPUT_W_THINKING_PATH}")
    logger.info(f"不带思考过程的数据集保存在: {OUTPUT_WO_THINKING_PATH}")

if __name__ == "__main__":
    main()