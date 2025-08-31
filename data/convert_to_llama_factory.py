#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import argparse
from pathlib import Path

def convert_to_llama_factory(input_file, output_file):
    # 加载源数据
    with open(input_file, 'r', encoding='utf-8') as f:
        source_data = json.load(f)
    
    # 创建LLaMA Factory格式的数据
    llama_factory_data = []
    
    # 系统提示（固定）
    system_prompt = """
    You are an assistant whose job is to generate a solution plan. Given a math problem, generate a solution plan less than 10 steps in XML format with the following constraints:
    1. Plan must contain EXACTLY 1-10 steps (never more than 10)
    2. Each step must be distinct and non-redundant
    3. Merge trivial steps into logical units
    4. Focus on key insights and critical transitions
    5. Avoid step-by-step computations, focus on conceptual transitions
    6. Mark computational steps with Difficulty≥3
    7. Ensure all Rely attributes reference valid step IDs
    8. Make sure the Task is ended with a question mark (?)
    9. Format: 
    <Plan>
    <Step ID="1" Task="..." Difficulty="1-10" Token="Estimate the number of tokens required to complete a subtask" Rely="Output only relevant steps"/>
    ...
    </Plan>
    Make sure the format with paired tags is correct and all steps are properly nested within the <Plan> tag.

    Difficulty scale:
    1-2: Basic computation
    3-4: Standard operations 
    5-6: Logical analysis 
    7-10: Advanced synthesis

    Output ONLY the XML plan with no additional text.
    """
    
    # 转换每个问题
    for item in source_data:
        if "question" not in item:
            continue  # 跳过不包含问题的项
        
        # 提取所需字段
        question = item.get("question", "")
        plan = item.get("plan", "")
        
        # 创建LLaMA Factory格式的项目
        llama_item = {
            "instruction": question,
            "input": "",
            "output": plan,
            "system": system_prompt
        }
        
        llama_factory_data.append(llama_item)
    
    # 保存转换后的数据
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(llama_factory_data, f, ensure_ascii=False, indent=4)
    
    print(f"转换完成！共处理 {len(llama_factory_data)} 条记录。")
    return len(llama_factory_data)

def main():
    parser = argparse.ArgumentParser(description='将数据集转换为LLaMA Factory格式')
    parser.add_argument('--input', '-i', type=str, 
                        default='dataset/generated_data/s1k1_1_training.json',
                        help='输入文件路径')
    parser.add_argument('--output', '-o', type=str, 
                        default='dataset/llama_factory/s1k1_1_training_llama.json',
                        help='输出文件路径')
    
    args = parser.parse_args()
    
    # 确保输出目录存在
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 转换文件
    count = convert_to_llama_factory(args.input, args.output)
    print(f"成功将 {args.input} 转换为LLaMA Factory格式，保存至 {args.output}")
    print(f"共转换 {count} 条记录")

if __name__ == "__main__":
    main()
