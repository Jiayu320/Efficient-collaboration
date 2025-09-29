import json
import os

def process_json_file(input_path, output_path):
    """
    读取一个JSON文件，将选项添加到问题描述中，并保存到新文件。

    Args:
        input_path (str): 输入的JSON文件路径。
        output_path (str): 输出的JSON文件路径。
    """
    try:
        # 以UTF-8编码读取原始JSON文件
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 遍历数据中的每一个条目（字典）
        for item in data:
            # 检查'problem'和'choices'键是否存在
            if 'problem' in item and 'choices' in item:
                
                # 获取原始问题和选项
                original_problem = item['problem']
                choices = item['choices']

                # 生成选项字符串，格式为 "choice 1: A, choice 2: B, ..."
                options_str = ", ".join(
                    [f"choice {i+1}: {choice}" for i, choice in enumerate(choices)]
                )

                # 构建新的问题描述
                # instruction = " Select from the following options: {options}. And provide the answer. For example, if the answer is choice 2, your response should be 'The answer is choice 2.'".format(options=options_str)
                instruction = (
                    f" Select from the following options: {options_str}. "
                    "And provide the answer. For example, if the answer is choice 2, "
                    "your response should be 'The answer is choice 2.'"
                )

                # 更新问题描述
                item['problem'] = original_problem + instruction
        
        # 将修改后的数据以UTF-8编码写入新文件
        # indent=2 or 4 用于美化输出，ensure_ascii=False 确保中文字符正常显示
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"处理完成！文件已成功保存到: {output_path}")

    except FileNotFoundError:
        print(f"错误: 文件未找到于路径 '{input_path}'")
    except json.JSONDecodeError:
        print(f"错误: 文件 '{input_path}' 不是一个有效的JSON格式。")
    except Exception as e:
        print(f"发生了一个未知错误: {e}")


# --- 使用说明 ---
# 1. 请将此脚本与您的JSON文件放在同一个目录下，或者使用绝对路径。
# 2. 修改下面的 input_file_path 为你的原始文件路径。
# 3. 运行脚本。

# 你的原始文件路径
# 在Windows上，路径中的反斜杠'\'最好使用双反斜杠'\\'或者正斜杠'/'
input_file_path = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\MMLU-STEM.json'

# 获取输入文件的目录和文件名
input_dir, input_filename = os.path.split(input_file_path)
file_name_part, file_ext_part = os.path.splitext(input_filename)

# 构建输出文件路径，例如： MMLU-STEM_modified.json
output_file_path = os.path.join(input_dir, f"{file_name_part}_modified{file_ext_part}")


# 调用函数执行处理
process_json_file(input_file_path, output_file_path)