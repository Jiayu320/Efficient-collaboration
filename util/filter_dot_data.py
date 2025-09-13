import json
import re
import os
from datetime import datetime

def is_plan_valid(plan_text):
    """
    检查计划中的所有Task是否都以问号结尾
    
    Args:
        plan_text (str): 包含XML计划的文本
        
    Returns:
        bool: 如果所有Task都以问号结尾，返回True，否则返回False
    """
    # 使用正则表达式查找所有Task属性
    task_pattern = r'Task="([^"]+)"'
    tasks = re.findall(task_pattern, plan_text)
    tasks_num = len(tasks)
    count = 0
    '''
    # 检查每个Task是否以问号结尾
    for task in tasks:
        if not task.strip().endswith('?'):
            count += 1
    if count == tasks_num:
        return False
    '''
    for task in tasks:
        if not task.strip().endswith('?'):
            return False
    return True

def filter_dot_training_data(input_file, output_file):
    """
    过滤不符合要求的数据（Task不以问号结尾）
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径
    """
    try:
        # 读取原始JSON文件
        print(f"正在读取文件: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        original_count = len(data)
        print(f"原始数据条数: {original_count}")
        
        # 过滤数据
        filtered_data = []
        removed_count = 0
        
        for item in data:
            output = item.get('output', '')
            
            # 检查是否包含XML计划且所有Task都以问号结尾
            if '<Plan>' in output and '</Plan>' in output and is_plan_valid(output):
                filtered_data.append(item)
            else:
                removed_count += 1
        
        # 保存过滤后的数据
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=2)
        
        print(f"过滤后数据条数: {len(filtered_data)}")
        print(f"移除数据条数: {removed_count}")
        print(f"过滤后的数据已保存到: {output_file}")
        
    except Exception as e:
        print(f"处理文件时出错: {str(e)}")

if __name__ == "__main__":
    # 输入和输出文件路径
    input_file = 'D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration\\dataset\\llama_factory\\limo_training_llama_817.json'
    
    # 创建带有时间戳的输出文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration\\dataset\\llama_factory\\limo_training_llama_{timestamp}.json'

    # 执行过滤
    filter_dot_training_data(input_file, output_file)