import json
import os
import argparse
from xml.sax.saxutils import escape
from util.io_file import read_json, write_json
import tqdm

def convert_to_training_data(sample):
    """将单个样本转换为训练所需的input-target对"""
    plan_xml = "<Plan>\n"
    
    # 按group顺序构建XML
    for i in range(1, len(sample["analysis"]["summaries"]) + 1):
        group_key = f"group{i}"
        summary = sample["analysis"]["summaries"][group_key]
        difficulty = sample["analysis"]["difficulties"][group_key]
        relies = sample["analysis"]["relations"].get(group_key, [])
        token = sample["analysis"]["groups_token"][group_key]
        # 转义XML特殊字符
        escaped_summary = escape(summary)
        
        # 构建XML属性
        attributes = [
            f'ID="{i}"',
            f'Task="{escaped_summary}"',
            f'Difficulty="{difficulty}"',
            f'Token="{token}"'
        ]
        
        # 添加依赖关系
        if relies:
            rely_ids = ",".join([g[5:] for g in relies])
            attributes.append(f'Rely="{rely_ids}"')
        
        # 组合成XML元素
        plan_xml += f"<Step {' '.join(attributes)}/>\n"
    
    plan_xml += "</Plan>"
    
    return {
        "input": f"Question: {sample['question']}\nGenerate a solution plan:",
        "target": plan_xml
    }

def process_file(input_path):
    """处理单个文件并返回训练数据
    
    参数:
        input_path: 输入JSON文件路径
    
    返回:
        成功: 训练数据列表
        失败: None
    """
    try:
        # 读取JSON数据
        data = read_json(input_path)
        if not isinstance(data, list):
            data = [data]
        
        # 转换为训练数据
        training_data = [convert_to_training_data(item) for item in data]
        
        print(f"成功处理文件: {input_path}")
        return training_data
    except Exception as e:
        print(f"处理文件 {input_path} 时出错: {str(e)}")
        return None

def process_directory(input_dir, output_dir):
    """处理目录中的所有JSON文件，并将所有数据写入一个JSON文件中
    
    参数:
        input_dir: 输入目录路径
        output_dir: 输出目录路径
    
    返回:
        处理成功和失败的文件列表
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取所有JSON文件
    json_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) 
                 if os.path.isfile(os.path.join(input_dir, f)) and f.endswith('.json') and f[:-5].isdigit()]
    
    print(f"找到 {len(json_files)} 个文件需要处理")
    
    successful_files = []
    failed_files = []
    all_training_data = []
    
    # 处理所有文件并收集数据
    for file_path in tqdm.tqdm(json_files, desc="处理文件"):
        training_data = process_file(file_path)
        
        if training_data:
            all_training_data.extend(training_data)
            successful_files.append(file_path)
        else:
            failed_files.append(file_path)
    
    # 将所有数据写入单个输出文件
    output_path = os.path.join(output_dir, "all_training_data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        for item in all_training_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    print(f"所有数据已写入: {output_path}")
    print(f"共处理了 {len(all_training_data)} 条数据")
    
    # 保存处理结果统计
    stats = {
        "total_files": len(json_files),
        "successful_files": len(successful_files),
        "failed_files": len(failed_files),
        "total_records": len(all_training_data),
        "failed_file_paths": failed_files
    }
    write_json(os.path.join(output_dir, "processing_stats.json"), stats)
    
    return successful_files, failed_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将JSON文件转换为训练数据")
    parser.add_argument("--input", default="data/structure/limo_out", help="输入文件或目录路径")
    parser.add_argument("--output", default="data/training", help="输出目录路径")
    args = parser.parse_args()

    if os.path.isfile(args.input):
        # 处理单个文件
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        
        output_path = os.path.join(args.output, "all_training_data.json")
        training_data = process_file(args.input)
        
        if training_data:
            with open(output_path, "w", encoding="utf-8") as f:
                for item in training_data:
                    f.write(json.dumps(item, ensure_ascii=False) + "\n")
            print(f"处理完成: {args.input} -> {output_path}")
    elif os.path.isdir(args.input):
        # 处理整个目录
        successful, failed = process_directory(args.input, args.output)
        print(f"处理完成。成功: {len(successful)}，失败: {len(failed)}")
    else:
        print(f"错误: 输入路径不存在 {args.input}")