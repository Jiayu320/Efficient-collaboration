# coding: utf-8
import os
import json
import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict, List, Any, Optional

from tqdm import tqdm

try:
    from openai import OpenAI
except ImportError:
    print("OpenAI 库未找到，请先安装: pip install openai")
    exit()

# --- 1. 配置模块 ---
# 请根据您的文件路径修改
SOURCE_DATA_PATH = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\MATH.json"
DATA_LIMIT = None  # 设置要处理的数据上限，设为 None 则不限制

# DeepSeek模型配置
MODEL_NAME = "qwen2.5-3b-instruct"
KEY_PATH = "usage/qwen"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 并行和重试配置
MAX_WORKERS = 10  # 可以根据您的API限制调整并行数
MAX_RETRIES = 3
RETRY_DELAY = 5  # 秒
API_TIMEOUT = 120.0  # API调用超时时间

# 日志配置
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


# --- 2. 日志模块 ---
def setup_logger() -> logging.Logger:
    """配置并返回一个日志记录器。"""
    log_filename = f"difficulty_rating_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_filepath = os.path.join(LOG_DIR, log_filename)
    
    logger = logging.getLogger("DifficultyRater")
    logger.setLevel(logging.INFO)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    # 文件处理器
    file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(
        "[%(levelname)s] %(asctime)s] (%(threadName)s) %(message)s", 
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(file_handler)
    
    # 控制台处理器
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(
        "[%(levelname)s] %(asctime)s] %(message)s", 
        datefmt="%H:%M:%S"
    ))
    logger.addHandler(stream_handler)
    
    return logger

logger = setup_logger()


# --- 3. API 调用模块 ---
def get_api_key(path: str) -> Optional[str]:
    """从指定路径读取API密钥。"""
    if not os.path.exists(path):
        logger.error(f"API密钥文件 '{path}' 未找到。")
        return None
    with open(path, 'r') as f:
        key = f.read().strip()
        if not key:
            logger.error(f"API密钥文件 '{path}' 为空。")
            return None
    return key

def get_difficulty_from_model(client: OpenAI, question: str) -> Optional[int]:
    """
    调用模型API以获取问题的难度等级。

    Args:
        client: OpenAI的客户端实例。
        question: 要评估的问题文本。

    Returns:
        返回一个整数形式的难度等级，如果失败则返回None。
    """
    prompt = f"""Please determine the difficulty of the following problem. 
Difficulty scale:
1-2: Basic computation
3-4: Standard operations 
5-6: Logical analysis 
7-10: Advanced synthesis
Problem: {question}
Please output only the difficulty level as a number. No other explanations or details are needed.
"""
    
    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{'role': 'user', 'content': prompt}],
                temperature=0,
                max_tokens=10,
                timeout=API_TIMEOUT,
            )
            content = response.choices[0].message.content
            
            # 使用正则表达式从返回内容中提取第一个数字
            match = re.search(r'\d+', content)
            if match:
                return int(match.group(0))
            else:
                logger.warning(f"未能从模型的响应中解析出数字: '{content}'")
                return None

        except Exception as e:
            logger.error(f"API调用失败 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                return None
    return None


# --- 4. 主逻辑模块 ---
def process_single_item(item: Dict[str, Any], client: OpenAI) -> Optional[Dict[str, Any]]:
    """
    处理单个JSON对象：获取问题，调用API，并更新对象。
    
    Returns:
        返回更新后的对象，如果处理失败则返回None。
    """
    question = item.get("problem")
    if not question:
        logger.warning("发现一个条目缺少 'problem' 字段，已跳过。")
        return None

    # 如果已经存在 'difficulty_level' 字段，则跳过
    if 'difficulty_level' in item:
        return item # 直接返回原始条目，以便重新写入

    difficulty = get_difficulty_from_model(client, question)

    if difficulty is not None:
        item['difficulty_level'] = difficulty
        logger.info(f"成功为问题 '{question[:50]}...' 评定难度: {difficulty}")
        return item
    else:
        logger.error(f"无法为问题 '{question[:50]}...' 获取难度等级，已跳过。")
        return None # 表示此条目处理失败

def main():
    """脚本主入口。"""
    logger.info("===== 开始执行问题难度评估脚本 =====")

    api_key = get_api_key(KEY_PATH)
    if not api_key:
        logger.error("无法加载API密钥，脚本终止。")
        return

    client = OpenAI(api_key=api_key, base_url=BASE_URL)

    try:
        with open(SOURCE_DATA_PATH, 'r', encoding='utf-8') as f:
            source_data = json.load(f)
        logger.info(f"成功从 '{SOURCE_DATA_PATH}' 加载 {len(source_data)} 条数据。")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"无法加载或解析源数据文件 '{SOURCE_DATA_PATH}': {e}")
        return

    # 确定要扫描以查找未处理项的数据范围
    data_to_scan = source_data
    if DATA_LIMIT is not None and DATA_LIMIT > 0 and len(source_data) > DATA_LIMIT:
        data_to_scan = source_data[:DATA_LIMIT]
        logger.info(f"根据 DATA_LIMIT={DATA_LIMIT} 的设置，将只在前 {len(data_to_scan)} 条数据中查找未处理项。")

    # 从指定的扫描范围筛选出需要处理的数据
    items_to_process = [item for item in data_to_scan if 'difficulty_level' not in item]
    
    if not items_to_process:
        logger.info("在指定范围内所有数据都已包含难度等级，无需处理。")
    else:
        logger.info(f"共发现 {len(items_to_process)} 条新数据需要处理。")
    
        updated_items = []
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS, thread_name_prefix='Worker') as executor:
            # 提交所有任务
            future_to_item = {executor.submit(process_single_item, item, client): item for item in items_to_process}
            
            # 使用tqdm显示进度条并处理结果
            for future in tqdm(as_completed(future_to_item), total=len(items_to_process), desc="评估问题难度"):
                original_item = future_to_item[future]
                try:
                    result_item = future.result()
                    if result_item:
                        updated_items.append(result_item)
                    else:
                        # 如果处理失败，仍然将原始条目加回去，以防数据丢失
                        updated_items.append(original_item)
                except Exception as exc:
                    logger.error(f"一个线程任务生成了异常: {exc}", exc_info=True)
                    updated_items.append(original_item) # 异常情况下也加回原始条目

        # 将已处理过的条目（带有difficulty_level）与本次更新的条目合并
        processed_items_map = {item['problem']: item for item in updated_items}
        final_data = []
        for item in source_data:
            # 优先使用更新后的条目，否则使用原始条目
            final_data.append(processed_items_map.get(item['problem'], item))
        source_data = final_data # 更新 source_data 以进行报告和保存

    # 将最终完整的数据写回原始文件
    try:
        with open(SOURCE_DATA_PATH, 'w', encoding='utf-8') as f:
            json.dump(source_data, f, indent=4, ensure_ascii=False)
        logger.info(f"处理完成！更新后的 {len(source_data)} 条数据已成功保存回 '{SOURCE_DATA_PATH}'。")
    except Exception as e:
        logger.error(f"写入最终结果到文件 '{SOURCE_DATA_PATH}' 时失败: {e}")

    # --- 5. 难度分布报告 ---
    logger.info("===== 生成难度分布报告 =====")
    difficulty_counts = {}
    unrated_count = 0

    for item in source_data:
        level = item.get('difficulty_level')
        # 确保level是整数
        if level is not None and isinstance(level, int):
            difficulty_counts[level] = difficulty_counts.get(level, 0) + 1
        else:
            unrated_count += 1

    # 在控制台打印格式化的报告
    print("\n" + "="*40)
    print("--- 问题难度等级分布报告 ---")
    print("="*40)

    if not difficulty_counts:
        print("没有找到已评级的项目。")
    else:
        # 按难度等级排序并打印
        for level in sorted(difficulty_counts.keys()):
            count = difficulty_counts[level]
            print(f"难度等级 {level:2d}: {count:3d} 个问题")

        # 分析分布均衡性
        print("-" * 20)
        print("分布摘要:")
        total_rated = sum(difficulty_counts.values())
        if total_rated > 0:
            max_count = max(difficulty_counts.values())
            min_count = min(difficulty_counts.values())
            # 使用一个简单的启发式规则来判断均衡性
            if len(difficulty_counts) > 3 and max_count > min_count * 3:
                print("数据分布不均衡，问题难度集中在某些特定级别。")
            else:
                print("数据分布相对均衡，问题难度较好地覆盖了多个级别。")

    if unrated_count > 0:
        print(f"\n注意：仍有 {unrated_count} 个问题未能成功评定难度。")
        print("您可以再次运行此脚本来重试这些失败的条目。")

    print("="*40 + "\n")


    logger.info("===== 脚本执行完毕 =====")


if __name__ == "__main__":
    main()

