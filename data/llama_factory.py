import os
import json
import argparse
from tqdm import tqdm

def read_json(file_path):
    """读取JSON文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data, file_path):
    """写入JSON文件"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def convert_to_llama_factory_format(input_dir, output_file, format_type="llama"):
    """
    将处理好的数据转换为LLaMA-Factory所需的格式
    
    参数:
        input_dir: 输入目录路径
        output_file: 输出文件路径
        format_type: 输出格式类型 ("llama" 或 "alpaca")
    """
    llama_factory_data = []
    
    # 获取所有JSON文件
    json_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) 
                 if os.path.isfile(os.path.join(input_dir, f)) and f.endswith('.json')]
    
    for file_path in tqdm(json_files, desc="处理文件"):
        try:
            file_data = read_json(file_path)
            
            # 检查数据是否是列表格式
            if isinstance(file_data, list):
                # 如果是列表，处理列表中的每个项目
                for data_item in file_data:
                    process_data_item(data_item, llama_factory_data, format_type)
            else:
                # 如果是字典，直接处理
                process_data_item(file_data, llama_factory_data, format_type)
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")
    
    # 写入结果
    write_json(llama_factory_data, output_file)
    print(f"已将 {len(llama_factory_data)} 条记录写入 {output_file}")

def process_data_item(data, llama_factory_data, format_type):
    """处理单个数据项"""
    # 从数据中提取所需字段
    question = data.get("question", "")
    
    # 首先检查是否有analysis中的summaries数据
    plan_data = data.get("analysis", {}).get("summaries", {})
    difficulties = data.get("analysis", {}).get("difficulties", {})
    relations = data.get("analysis", {}).get("relations", {})
    
    # 如果summaries不存在或为空，检查是否为training_data.json格式
    if not plan_data:
        # 检查training_data中的target格式
        target = data.get("target", "")
        input_text = data.get("input", "")
        if target and input_text:
            # 根据格式类型构建数据
            if format_type == "llama":
                llama_item = {
                    "instruction": input_text,
                    "input": "",
                    "output": target,
                    "system": "Generate a solution plan that breaks down the problem into logical steps, identifying dependencies and difficulty levels."
                }
            else:  # alpaca format
                # 提取问题部分，如果可以
                question_text = input_text
                if "Question:" in input_text:
                    question_text = input_text.split("Generate")[0].strip()
                    
                llama_item = {
                    "instruction": "Generate a solution plan for the following mathematical problem.",
                    "input": question_text,
                    "output": target
                }
            llama_factory_data.append(llama_item)
        return
    
    # 构建计划文本
    plan_steps = []
    
    # 尝试获取步骤ID列表
    if isinstance(plan_data, dict):
        # 如果是字典格式
        if all(k.startswith("group") for k in plan_data.keys()):
            # 获取组的键并排序 (group1, group2...)
            group_keys = sorted(plan_data.keys(), key=lambda x: int(x.replace("group", "")))
            
            for group_key in group_keys:
                step_id = group_key.replace("group", "")
                summary = plan_data[group_key]
                difficulty = difficulties.get(group_key, "1")
                relation = relations.get(group_key, []) if relations else []
                
                rely_text = ""
                if relation:
                    rely_ids = [r.replace("group", "") for r in relation]
                    if rely_ids:
                        rely_text = f" Rely=\"{','.join(rely_ids)}\""
                
                step = f"<Step ID=\"{step_id}\" Task=\"{summary}\" Difficulty=\"{difficulty}\" Token=\"\"" + rely_text + "/>"
                plan_steps.append(step)
        else:
            # 按照数字排序键
            step_ids = sorted(plan_data.keys(), key=lambda x: int(x))
            
            for step_id in step_ids:
                summary = plan_data[step_id]
                difficulty = difficulties.get(step_id, "1")
                relation = relations.get(step_id, []) if relations else []
                
                rely_text = ""
                if relation:
                    rely_text = f" Rely=\"{','.join(relation)}\""
                
                step = f"<Step ID=\"{step_id}\" Task=\"{summary}\" Difficulty=\"{difficulty}\" Token=\"\"" + rely_text + "/>"
                plan_steps.append(step)
    
    # 构建最终的计划
    plan = "<Plan>\n" + "\n".join(plan_steps) + "\n</Plan>"
    
    # 构建LLaMA-Factory格式的项
    if format_type == "llama":
        llama_item = {
            "instruction": f"Question: {question}\nGenerate a solution plan:",
            "input": "",
            "output": plan,
            "system": "Generate a solution plan that breaks down the problem into logical steps, identifying dependencies and difficulty levels."
        }
    else:  # alpaca format
        llama_item = {
            "instruction": "Generate a solution plan for the following mathematical problem.",
            "input": question,
            "output": plan
        }
    
    llama_factory_data.append(llama_item)

def main():
    # 参数解析
    parser = argparse.ArgumentParser(description="将处理好的数据转换为LLaMA-Factory格式")
    parser.add_argument("--input_dir", type=str, required=True, help="输入目录路径，包含处理好的JSON文件")
    parser.add_argument("--output_file", type=str, required=True, help="输出文件路径")
    parser.add_argument("--format", type=str, choices=["llama", "alpaca"], default="llama", help="输出格式类型")
    
    args = parser.parse_args()
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    
    # 执行转换
    convert_to_llama_factory_format(args.input_dir, args.output_file, args.format)

if __name__ == "__main__":
    main()
