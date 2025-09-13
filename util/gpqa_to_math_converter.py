#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import json
import pandas as pd
from pathlib import Path
import ast  # 用于安全地评估字符串表示的Python数据结构

def convert_gpqa_to_math_format(csv_file_path, output_file_path):
    """
    将GPQA的CSV数据转换为与math200.json格式一致的JSON数据
    
    Args:
        csv_file_path: GPQA CSV文件路径
        output_file_path: 输出JSON文件路径
    """
    print(f"正在处理: {csv_file_path}")
    file_name = Path(csv_file_path).stem
    
    # 读取CSV文件
    try:
        df = pd.read_csv(csv_file_path, encoding='utf-8')
    except UnicodeDecodeError:
        # 如果utf-8编码失败，尝试其他编码
        try:
            df = pd.read_csv(csv_file_path, encoding='latin-1')
        except Exception:
            # 如果还是失败，尝试更宽松的解析
            df = pd.read_csv(csv_file_path, encoding='latin-1', engine='python')
    
    # 打印列名，以便调试
    print(f"文件 {csv_file_path} 的列名: {list(df.columns)}")
    
    # 创建结果列表
    result = []
    
    # 针对不同的CSV文件使用不同的处理逻辑
    if file_name == "gpqa_experts":
        # 专家文件的特殊处理
        for _, row in df.iterrows():
            # 提取Expert Accuracy作为问题
            problem = str(row.get("Expert Accuracy", "")) if pd.notna(row.get("Expert Accuracy", "")) else ""
            
            # 提取Domain作为解决方案和类型
            domain = row.get("Domain", "") if pd.notna(row.get("Domain", "")) else ""
            
            # 如果Domain是字符串形式的列表，尝试转换为实际Python对象
            try:
                if isinstance(domain, str) and (domain.startswith('[') and domain.endswith(']')):
                    domain_list = ast.literal_eval(domain)
                else:
                    domain_list = domain
            except (SyntaxError, ValueError):
                domain_list = domain  # 如果转换失败，保持原样
            
            item = {
                "problem": problem,
                "solution": domain,
                "type": domain
            }
            
            # 添加其他有用的字段
            if "Name" in df.columns and pd.notna(row.get("Name")):
                item["name"] = str(row.get("Name"))
            
            if "Description of Expertise" in df.columns and pd.notna(row.get("Description of Expertise")):
                item["expertise"] = str(row.get("Description of Expertise"))
            
            if "Qualifications" in df.columns and pd.notna(row.get("Qualifications")):
                qual = row.get("Qualifications")
                try:
                    if isinstance(qual, str) and (qual.startswith('[') and qual.endswith(']')):
                        item["qualifications"] = ast.literal_eval(qual)
                    else:
                        item["qualifications"] = qual
                except (SyntaxError, ValueError):
                    item["qualifications"] = qual
            
            result.append(item)
    else:
        # 针对main、diamond等标准GPQA文件的处理
        # 检查必要的列是否存在
        question_col = None
        explanation_col = None
        
        # 根据文件类型选择适当的列
        if "Question" in df.columns:
            question_col = "Question"
        elif "Pre-Revision Question" in df.columns:
            question_col = "Pre-Revision Question"
        
        if "Explanation" in df.columns:
            explanation_col = "Explanation"
        elif "Pre-Revision Explanation" in df.columns:
            explanation_col = "Pre-Revision Explanation"
        
        # 如果标准列名不存在，尝试查找可能的替代列名
        if question_col is None:
            for col in df.columns:
                if "question" in col.lower():
                    question_col = col
                    print(f"使用替代问题列: {col}")
                    break
        
        if explanation_col is None:
            for col in df.columns:
                if "explanation" in col.lower() or "answer" in col.lower() or "solution" in col.lower():
                    explanation_col = col
                    print(f"使用替代答案/解释列: {col}")
                    break
        
        # 如果仍然找不到必要的列，报告错误
        if question_col is None:
            print(f"警告: 在文件 {csv_file_path} 中找不到问题列")
            if len(df.columns) > 0:
                question_col = df.columns[0]  # 使用第一列作为问题列
                print(f"使用第一列 '{question_col}' 作为问题列")
        
        if explanation_col is None:
            print(f"警告: 在文件 {csv_file_path} 中找不到解释/答案列")
            if len(df.columns) > 1:
                explanation_col = df.columns[1]  # 使用第二列作为解释列
                print(f"使用第二列 '{explanation_col}' 作为解释/答案列")
            else:
                explanation_col = question_col  # 最坏情况，使用问题列
        
        # 遍历CSV中的每一行
        for _, row in df.iterrows():
            # 创建与math200.json格式一致的对象
            item = {
                "problem": str(row.get(question_col, "")) if pd.notna(row.get(question_col, "")) else "",
                "solution": str(row.get(explanation_col, "")) if pd.notna(row.get(explanation_col, "")) else ""
            }
            
            # 添加其他有用的GPQA属性
            # 添加域（学科）信息
            domain_col = next((c for c in df.columns if "domain" in c.lower() and "high" in c.lower()), None)
            if domain_col and pd.notna(row.get(domain_col)):
                item["type"] = str(row.get(domain_col))
            
            # 添加难度信息
            difficulty_col = next((c for c in df.columns if "difficult" in c.lower() or "writer" in c.lower()), None)
            if difficulty_col and pd.notna(row.get(difficulty_col)):
                item["level"] = str(row.get(difficulty_col))
            
            # 添加正确答案
            answer_col = next((c for c in df.columns if "correct" in c.lower() and "answer" in c.lower()), None)
            if answer_col and pd.notna(row.get(answer_col)):
                item["answer"] = str(row.get(answer_col))
            
            # 添加不正确选项
            incorrect_answers = []
            for col in df.columns:
                if "incorrect" in col.lower() and "answer" in col.lower() and pd.notna(row.get(col)):
                    incorrect_answers.append(str(row.get(col)))
            if incorrect_answers:
                item["incorrect_answers"] = incorrect_answers
            
            # 添加子领域信息
            subdomain_col = next((c for c in df.columns if "subdomain" in c.lower()), None)
            if subdomain_col and pd.notna(row.get(subdomain_col)):
                item["subdomain"] = str(row.get(subdomain_col))
            
            # 添加记录ID
            id_col = next((c for c in df.columns if "id" in c.lower() and "record" in c.lower()), None)
            if id_col and pd.notna(row.get(id_col)):
                item["record_id"] = str(row.get(id_col))
            
            result.append(item)
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    # 过滤掉没有问题或解答的记录
    filtered_result = [item for item in result if item.get("problem") and item.get("solution")]
    
    if len(filtered_result) < len(result):
        print(f"警告: 过滤掉了 {len(result) - len(filtered_result)} 条没有问题或解答的记录")
    
    if not filtered_result:
        print(f"错误: 没有找到有效的记录，请检查文件格式和列名")
        return
    
    # 将结果写入JSON文件
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(filtered_result, f, ensure_ascii=False, indent=2)
    
    print(f"已保存到: {output_file_path}")
    print(f"转换了 {len(filtered_result)} 条记录")

def main():
    # 源文件夹和目标文件夹
    gpqa_folder = Path("D:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/original_data/GPQA")
    output_folder = Path("D:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/TestData")
    
    # 确保输出目录存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 记录转换情况的统计数据
    total_files = 0
    total_records = 0
    
    # 处理GPQA文件夹中的所有CSV文件
    csv_files = list(gpqa_folder.glob("*.csv"))
    if not csv_files:
        print(f"警告: 在 {gpqa_folder} 中没有找到CSV文件")
    
    for csv_file in csv_files:
        total_files += 1
        # 获取文件名（不带扩展名）
        file_name = csv_file.stem
        
        # 构建输出文件路径
        output_file = output_folder / f"{file_name}.json"
        
        try:
            # 转换文件
            convert_gpqa_to_math_format(csv_file, output_file)
            
            # 统计转换的记录数
            with open(output_file, 'r', encoding='utf-8') as f:
                records = json.load(f)
                total_records += len(records)
                
        except Exception as e:
            print(f"处理文件 {csv_file} 时出错: {str(e)}")
    
    print("\n转换摘要:")
    print(f"总共处理文件数: {total_files}")
    print(f"总共转换记录数: {total_records}")
    print(f"输出目录: {output_folder}")

if __name__ == "__main__":
    try:
        main()
        print("所有文件处理完成!")
    except Exception as e:
        print(f"运行过程中出现错误: {str(e)}")
        import traceback
        traceback.print_exc()