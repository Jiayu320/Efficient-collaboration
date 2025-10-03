# -*- coding: utf-8 -*-
import json
import os

def convert_gpqa_format(input_path, output_path):
    """
    将原始 GPQA 数据集（JSON Lines 格式）转换为所需的目标 JSON 数组格式。

    转换规则：
    1.  从原始数据中读取 "Question", "options", 和 "answer" (索引)。
    2.  创建一个新的 "problem" 字段，该字段包含：
        - 原始的 "Question"。
        - 用 A, B, C, D... 标记的选项列表。
        - 一句英文提示，要求选择正确答案。 (新要求)
        - 在末尾明确指出正确答案的字母，格式为 "Answer: [字母]"。
    3.  创建一个新的 "answer" 字段，其值为正确选项的文本内容。
    4.  创建一个新的 "answer_id" 字段，其值为原始的正确答案索引。
    5.  保留原始数据中的所有其他字段（例如 "Canary String"）。
    6.  将所有转换后的记录保存到一个 JSON 数组中。

    Args:
        input_path (str): 原始 gpqa.json 文件的路径。
        output_path (str): 转换后要保存的 gpqa.json 文件的路径。
    """
    processed_data = []
    # 定义选项标签，以防有超过4个选项的问题
    option_labels = ['A', 'B', 'C', 'D', 'E', 'F']

    try:
        # 以 utf-8 编码读取输入文件
        with open(input_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                # 忽略文件中的空行
                if not line.strip():
                    continue
                
                try:
                    # 解析每一行的 JSON 对象
                    original_record = json.loads(line)

                    # 提取原始数据
                    question = original_record.get("Question", "")
                    options = original_record.get("options", [])
                    answer_index = original_record.get("answer") # 这是正确答案的索引

                    # 如果关键数据缺失，则跳过该行
                    if not question or not options or answer_index is None:
                        print(f"Warning: Skipping record due to missing data: {line.strip()}")
                        continue
                    
                    # --- 格式转换核心逻辑 ---

                    # 1. 将选项格式化为带 A, B, C... 标签的字符串
                    options_formatted_list = []
                    for i, option_text in enumerate(options):
                        if i < len(option_labels):
                            label = option_labels[i]
                            # 清理选项文本中可能存在的多余换行符
                            clean_option_text = option_text.strip()
                            options_formatted_list.append(f"{label}. {clean_option_text}")
                    
                    options_string = "\n".join(options_formatted_list)

                    # 2. 获取正确答案对应的标签和文本
                    correct_label = option_labels[answer_index]
                    correct_answer_text = options[answer_index].strip()

                    # 3. 构建新的 "problem" 字段
                    # 📌 新增：根据您的要求添加的英文指令
                    instruction_text = "Please select the correct answer and provide the final option letter and its corresponding content."
                    
                    # 📌 修改：将英文指令添加到 problem 字符串中
                    problem_string = f"{question.strip()}\n\n{options_string}\n\n{instruction_text}"
                    
                    # 4. 创建新的记录字典
                    new_record = {
                        "problem": problem_string,
                        "answer": correct_answer_text,
                        "answer_id": answer_index,
                    }

                    # 5. 保留原始数据中的其他字段
                    for key, value in original_record.items():
                        if key not in ["Question", "options", "answer"]:
                            new_record[key] = value
                    
                    processed_data.append(new_record)

                except json.JSONDecodeError:
                    print(f"Warning: Skipping a line that is not valid JSON: {line.strip()}")
                    continue

        # 确保输出目录存在，如果不存在则创建
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # 6. 将处理好的数据列表写入输出文件
        # 使用 indent=2 进行格式化，ensure_ascii=False 以正确处理非 ASCII 字符
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(processed_data, outfile, indent=2, ensure_ascii=False)
        
        print("✅ 数据转换成功！（已更新英文提示）")
        print(f"   输入文件: {input_path}")
        print(f"   输出文件: {output_path}")
        print(f"   总共处理了 {len(processed_data)} 条记录。")

    except FileNotFoundError:
        print(f"❌ 错误: 输入文件未找到: {input_path}")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")

# --- 脚本执行入口 ---
if __name__ == "__main__":
    # 📌 请确保以下路径是正确的
    input_file_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\gpqa.json"
    output_file_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\gpqa.json"
    
    # 执行转换函数
    convert_gpqa_format(input_file_path, output_file_path)