import json
import os
import sys
import time
import random
import re
import argparse
from openai import OpenAI
from tqdm import tqdm
import xml.dom.minidom

# API配置
API_CONFIG = {
    "bianxie": {
        "base_url": "https://api.bianxie.ai/v1",
        "api_key": "sk-vKirQEe0vJmMN3X9UAENCCdheTHII81VCQm0NZHzG781H95Y",
        "models": ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
    },
    "openai": {
        "api_key": None,  # 需要从环境变量获取或手动输入
        "models": ["gpt-4o", "gpt-4", "gpt-3.5-turbo"]
    }
}

# 系统提示词 - 用于评估任务难度和token
DIFFICULTY_SYSTEM_PROMPT = """You are an AI specialized in evaluating task difficulty and estimating required token usage for mathematical problems.

For each given subtask from a problem decomposition, you will:
1. Rate its difficulty on a scale from 1 to 10 using this guide:
   - 1-2: Basic computation (arithmetic, simple formulas)
   - 3-4: Standard operations (algebra, basic calculus, standard formula application)
   - 5-6: Logical analysis (complex problem setup, multi-step reasoning)
   - 7-10: Advanced synthesis (requiring deep insight or complex techniques)
2. Estimate the number of tokens required to complete a subtask
3. Return ONLY the two numbers in this format: "Difficulty: X, Token: Y"
Remember that difficulty is subjective but should reflect relative complexity within the problem.
"""

# 输出数据中使用的系统提示词
OUTPUT_SYSTEM_PROMPT = "Generate a solution plan that breaks down the problem into logical steps, identifying dependencies, difficulty levels and token usage."

# 初始化API客户端
def init_client(api_provider="bianxie"):
    """初始化API客户端"""
    if api_provider == "bianxie":
        return OpenAI(
            base_url=API_CONFIG["bianxie"]["base_url"],
            api_key=API_CONFIG["bianxie"]["api_key"],
        )
    elif api_provider == "openai":
        # 从环境变量获取API密钥
        api_key = os.environ.get("OPENAI_API_KEY") or API_CONFIG["openai"]["api_key"]
        if not api_key:
            raise ValueError("OpenAI API密钥未设置，请设置OPENAI_API_KEY环境变量")
        return OpenAI(api_key=api_key)
    else:
        raise ValueError(f"不支持的API提供商: {api_provider}")


def estimate_difficulty_and_tokens(client, model, task, problem_text, retry=3):
    """使用LLM估计任务的难度和所需token数量"""
    for attempt in range(retry):
        try:
            # 构建提示
            user_prompt = f"""
Problem context: {problem_text}

Subtask: {task}

Rate the difficulty of this subtask and Estimate the number of tokens required to complete a subtask.
Return only: "Difficulty: X, Token: Y"
"""

            # 调用API
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": DIFFICULTY_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
            )
            
            # 提取结果
            result = response.choices[0].message.content.strip()
            
            # 使用正则表达式提取难度和token
            difficulty_match = re.search(r"Difficulty:\s*(\d+)", result)
            token_match = re.search(r"Token:\s*(\d+)", result)
            
            if difficulty_match and token_match:
                difficulty = int(difficulty_match.group(1))
                # 确保难度在1-7范围内
                difficulty = max(1, min(7, difficulty))
                
                token = int(token_match.group(1))
                return difficulty, token
            else:
                print(f"无法从响应中提取难度和token: {result}")
                if attempt == retry - 1:
                    # 最后一次尝试仍然失败，返回默认值
                    return random.randint(1, 5), random.randint(20, 50)
                    
        except Exception as e:
            print(f"调用API时出错: {e}")
            if attempt == retry - 1:
                # 最后一次尝试仍然失败，返回默认值
                return random.randint(1, 5), random.randint(20, 50)
            
        # 如果失败，等待一段时间后重试
        time.sleep(2)


def is_empty_task(task):
    """判断任务是否为空或只包含步骤号"""
    # 去除引号并修剪空白
    task = task.strip('"').strip()
    
    # 检查是否为空
    if not task:
        return True
    
    # 检查是否只包含"处理步骤 X:"格式
    if re.match(r'^处理步骤\s+\d+\s*:?\s*$', task):
        return True
    
    return False


def remap_dependencies(rely_dict, id_mapping):
    """重新映射依赖关系"""
    new_rely_dict = {}
    
    for old_id, relies in rely_dict.items():
        # 跳过已删除的步骤
        if old_id not in id_mapping:
            continue
            
        new_id = id_mapping[old_id]
        new_relies = []
        
        for rely_id in relies:
            # 如果依赖的步骤在新映射中存在
            if rely_id in id_mapping:
                new_relies.append(id_mapping[rely_id])
        
        # 保存新的依赖关系
        new_rely_dict[new_id] = new_relies
    
    return new_rely_dict


def generate_xml_plan(client, model, data_item, use_text_format=False):
    """从数据项生成XML格式的计划，处理空步骤并重新编号"""
    problem_text = data_item["problemText"]
    steps_dict = data_item["steps_dict"]
    int_edges = data_item["int_edges"]
    
    print(f"处理问题: {problem_text}")
    
    # 过滤空任务
    valid_steps = {}
    for step_id, task in steps_dict.items():
        if not is_empty_task(task):
            valid_steps[step_id] = task.strip('"').strip()
        else:
            print(f"  跳过空步骤 {step_id}")
    
    # 如果没有有效步骤
    if not valid_steps:
        print("  警告: 没有有效的步骤!")
        return "<Plan>\n</Plan>"
    
    # 创建新的ID映射关系
    old_to_new_id = {}
    new_id = 1
    for old_id in sorted(valid_steps.keys(), key=int):
        old_to_new_id[old_id] = str(new_id)
        new_id += 1
    
    # 创建依赖关系字典
    old_rely_dict = {step_id: [] for step_id in valid_steps.keys()}
    for edge in int_edges:
        from_step, to_step = edge
        from_step, to_step = str(from_step), str(to_step)
        # 只添加有效步骤间的依赖
        if from_step in valid_steps and to_step in valid_steps:
            old_rely_dict[to_step].append(from_step)
    
    # 重新映射依赖关系
    new_rely_dict = remap_dependencies(old_rely_dict, old_to_new_id)
    
    xml_steps = []
    
    # 处理每个有效步骤
    for old_id, task in valid_steps.items():
        new_id = old_to_new_id[old_id]
        print(f"  处理步骤 {old_id} -> {new_id}: {task}")
        
        # 获取难度和token估计
        difficulty, token = estimate_difficulty_and_tokens(client, model, task, problem_text)
        
        # 构建依赖字符串
        rely = ",".join(new_rely_dict[new_id]) if new_id in new_rely_dict and new_rely_dict[new_id] else ""
        
        # 创建XML步骤
        if use_text_format:
            xml_step = f'<Step ID="{new_id}" Task="{task}?" Difficulty="{difficulty}" Token="{token}" Rely="{rely}"/>'
        else:
            xml_step = f'<Step ID="{new_id}" Task="{task}" Difficulty="{difficulty}" Token="{token}" Rely="{rely}"/>'
        xml_steps.append(xml_step)
        
        # 防止API请求过快
        time.sleep(1)
    
    # 组合成完整的XML计划
    xml_plan = "<Plan>\n" + "\n".join(xml_steps) + "\n</Plan>"
    return xml_plan


def prettify_xml(xml_string):
    """美化XML字符串"""
    try:
        dom = xml.dom.minidom.parseString(xml_string)
        return dom.toprettyxml(indent="  ")
    except Exception as e:
        print(f"XML格式化错误: {e}")
        return xml_string


def load_existing_results(output_file):
    """加载已存在的处理结果"""
    if os.path.exists(output_file):
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"加载已有结果失败: {e}")
            return []
    return []


def get_processed_keys(results, input_file):
    """获取已处理的key列表"""
    processed_keys = set()
    
    # 提取输入文件名的基本部分，用于匹配
    input_base = os.path.basename(input_file).split(".")[0]
    
    # 记录问题文本到已处理key的映射
    problem_to_key = {}
    
    # 读取原始数据，建立问题文本到key的映射
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for key, item in data.items():
                problem_to_key[item["problemText"]] = key
    except Exception as e:
        print(f"读取原始数据失败: {e}")
        return processed_keys
    
    # 检查结果中哪些问题已处理
    for item in results:
        if item.get("instruction") in problem_to_key:
            processed_keys.add(problem_to_key[item["instruction"]])
    
    return processed_keys


def process_dot_dataset(client, model, input_file, output_file, sample_size=None, use_text_format=False):
    """处理DoT数据集文件并生成与training_data_new.json格式相同的数据，支持断点续传和增量保存"""
    print(f"处理文件: {input_file}")
    
    # 加载已存在的结果
    results = load_existing_results(output_file)
    print(f"已加载 {len(results)} 条已处理结果")
    
    # 获取已处理的key
    processed_keys = get_processed_keys(results, input_file)
    print(f"已处理 {len(processed_keys)} 条记录")
    
    # 读取输入数据
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 过滤已处理的项
    unprocessed_data = {k: v for k, v in data.items() if k not in processed_keys}
    print(f"待处理 {len(unprocessed_data)} 条记录")
    
    # 如果指定了样本大小，且未处理的数据量大于样本大小，随机选择样本
    if sample_size and sample_size > 0 and len(unprocessed_data) > sample_size:
        selected_keys = random.sample(list(unprocessed_data.keys()), sample_size)
        unprocessed_data = {k: unprocessed_data[k] for k in selected_keys}
        print(f"从未处理数据中选择 {len(unprocessed_data)} 条记录")
    
    # 如果没有未处理的数据
    if not unprocessed_data:
        print("没有新的数据需要处理")
        return results
    
    # 处理每个数据项
    for key, item in tqdm(unprocessed_data.items(), desc="处理数据"):
        try:
            # 生成XML计划
            xml_plan = generate_xml_plan(client, model, item, use_text_format)
            
            # 创建结果项，格式与training_data_new.json一致
            result_item = {
                "instruction": item["problemText"],
                "input": "",
                "output": xml_plan,
                "system": OUTPUT_SYSTEM_PROMPT
            }
            
            # 添加到结果列表
            results.append(result_item)
            
            # 增量保存
            save_dataset(results, output_file)
            
            print(f"完成项 {key} 并保存")
            
        except Exception as e:
            print(f"处理项 {key} 时出错: {e}")
    
    print(f"处理完成! 共生成 {len(results)} 个结果")
    return results


def save_dataset(results, output_file):
    """保存数据集到文件"""
    # 保存结果
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"保存完成! 已保存 {len(results)} 个结果到 {output_file}")


def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='处理DoT数据集并生成training_data_new.json格式的XML计划')
    
    parser.add_argument('--api', default='bianxie', choices=['bianxie', 'openai'], 
                        help='API提供商 (默认: bianxie)')
    parser.add_argument('--model', default='gpt-4o', 
                        help='模型名称 (默认: gpt-4o)')
    parser.add_argument('--input_dir', default='d:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/DoT_data',
                        help='DoT数据目录路径')
    parser.add_argument('--output_dir', default='d:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/processed',
                        help='输出目录路径')
    parser.add_argument('--output_file', default='dot_training_data.json',
                        help='输出文件名 (默认: dot_training_data.json)')
    parser.add_argument('--file_index', type=int, 
                        help='要处理的特定文件索引 (从0开始)')
    parser.add_argument('--sample_size', type=int, default=5,
                        help='每个文件要处理的样本数量 (默认: 5, 0表示处理所有数据)')
    parser.add_argument('--use_text_format', action='store_true',
                        help='将任务格式化为问题形式 (默认: False)')
    parser.add_argument('--resume', action='store_true',
                        help='从上次中断的地方继续处理 (默认: True)')
    
    return parser.parse_args()


def main():
    # 解析命令行参数
    args = parse_arguments()
    
    # 初始化API客户端
    client = init_client(args.api)
    
    # 确保输出目录存在
    os.makedirs(args.output_dir, exist_ok=True)
    
    # 输出文件路径
    output_file = os.path.join(args.output_dir, "dot_training_data.json")
    
    # 获取所有DoT数据文件
    dot_files = [f for f in os.listdir(args.input_dir) if f.endswith('.json')]
    
    # 如果指定了特定文件索引，只处理该文件
    if args.file_index is not None:
        if 0 <= args.file_index < len(dot_files):
            dot_files = [dot_files[args.file_index]]
        else:
            print(f"无效的文件索引: {args.file_index}, 应在0-{len(dot_files)-1}范围内")
            return
    
    # 处理所有文件，增量保存到同一个输出文件
    for dot_file in dot_files:
        input_path = os.path.join(args.input_dir, dot_file)
        
        print(f"\n开始处理文件: {dot_file}")
        process_dot_dataset(
            client, 
            args.model, 
            input_path, 
            output_file,
            args.sample_size, 
            args.use_text_format
        )
    
    print(f"所有处理完成! 结果已保存至 {output_file}")


if __name__ == "__main__":
    main()

'''
使用方法示例：

处理全部DoT数据（每个文件5个样本）：
python d:/JIAYU/Documents/GitHub/Efficient-collaboration/data/create_dot_dataset_advanced.py

处理全部DoT数据（每个文件10个样本）：
python d:/JIAYU/Documents/GitHub/Efficient-collaboration/data/create_dot_dataset_advanced.py --sample_size 10

处理全部DoT数据（每个文件全部样本）：
python d:/JIAYU/Documents/GitHub/Efficient-collaboration/data/create_dot_dataset_advanced.py --sample_size 0

处理特定文件：
python d:/JIAYU/Documents/GitHub/Efficient-collaboration/data/create_dot_dataset_advanced.py --file_index 0

指定输出文件名：
python d:/JIAYU/Documents/GitHub/Efficient-collaboration/data/create_dot_dataset_advanced.py --output_file custom_output.json

主要特性：
1. 支持断点续传 - 自动从上次中断的地方继续处理
2. 增量保存 - 每处理一条数据就保存到JSON文件
3. 删除空步骤 - 自动过滤空的子任务步骤并重新编号
'''