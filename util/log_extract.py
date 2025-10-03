import re
import json
import os

def extract_log_data(log_path):
    """
    从指定的日志文件中提取问题和Planner的输出。

    Args:
        log_path (str): 日志文件的完整路径。

    Returns:
        dict: 一个包含提取数据的字典，键是问题编号，值是包含问题和输出的字典。
              如果文件不存在或无法读取，则返回一个空字典。
    """
    if not os.path.exists(log_path):
        print(f"错误：文件不存在 -> {log_path}")
        return {}

    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            log_content = f.read()
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return {}

    # 使用正则表达式匹配每个问题块
    # re.DOTALL 标志让 '.' 可以匹配包括换行符在内的任意字符
    problem_blocks = re.findall(r'===== 开始处理问题 #(\d+) =====(.+?)(?===== 开始处理问题 #|\Z)', log_content, re.DOTALL)

    extracted_data = {}
    for problem_id, block_content in problem_blocks:
        # 提取问题
        question_match = re.search(r'问题: (.*?)\n', block_content)
        if not question_match:
            continue
        
        question = question_match.group(1).strip()

        # 提取Planner的输出
        # 我们从"===== 来自 Planner (Router) 的输出 ====="开始匹配
        # 直到下一个 "=====" 分隔符为止
        planner_output_match = re.search(r'===== 来自 Planner \(Router\) 的输出 =====\n(.*?)\n\[INFO\].*?=====', block_content, re.DOTALL)
        if not planner_output_match:
            continue
        
        raw_planner_output = planner_output_match.group(1).strip()
        
        # 清理每行前面的日志信息 (e.g., "[INFO] 10-02 14:51:30 execution.py:1197] ")
        cleaned_lines = []
        for line in raw_planner_output.split('\n'):
            # 找到']'后的第一个空格，并取其后的所有内容
            match = re.search(r'\] (.*)', line)
            if match:
                cleaned_lines.append(match.group(1))
            else:
                cleaned_lines.append(line)
        
        planner_output = '\n'.join(cleaned_lines).strip()

        # 存入字典
        extracted_data[problem_id] = {
            "question": question,
            "output": planner_output
        }

    return extracted_data

def save_to_json(data, output_path):
    """
    将提取的数据保存为JSON文件。

    Args:
        data (dict): 要保存的数据。
        output_path (str): JSON文件的输出路径。
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            # ensure_ascii=False 保证中文字符正确显示
            # indent=4 让JSON文件格式更美观
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"数据已成功提取并保存到: {output_path}")
    except Exception as e:
        print(f"保存JSON文件时出错: {e}")


if __name__ == "__main__":
    # 1. 请在这里设置您的日志文件路径
    # 注意：在Windows中，路径中的反斜杠'\'需要转义为'\\'或者使用正斜杠'/'
    log_file_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\data_reports\dataset\gpqa_main\gpt-4o\gpt-4o\gpt-4o\20251002_145122\run_details.log"

    # 2. 设置输出的JSON文件名
    output_json_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\data_reports\dataset\gpqa_main\gpt-4o\gpt-4o\gpt-4o\20251002_145122\extracted_planner_outputs.json"

    # 3. 执行提取和保存操作
    data = extract_log_data(log_file_path)
    if data:
        save_to_json(data, output_json_path)
    else:
        print("未能从日志中提取任何数据。")
