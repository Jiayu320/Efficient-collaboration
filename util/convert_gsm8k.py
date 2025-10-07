import json
import os
import re

def convert_gsm8k_dataset(input_path, output_path):
    """
    该函数读取 GSM8K 数据集的 .jsonl 文件，
    将其转换为包含 "problem", "solution", 和 "answer" 的 .json 格式。

    Args:
        input_path (str): 原始 .jsonl 文件的路径。
        output_path (str): 目标 .json 文件的路径。
    """
    # 用于存储所有转换后记录的列表
    converted_data = []

    try:
        # 逐行读取原始 .jsonl 文件
        with open(input_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                # 将每一行解析为 JSON 对象 (Python 字典)
                original_record = json.loads(line)

                # 原始记录包含 "question" 和 "answer"
                question = original_record.get('question', '')
                full_answer_text = original_record.get('answer', '')

                # 1. 提取最终答案
                # 最终答案在 "####" 标记之后
                final_answer = ""
                if "####" in full_answer_text:
                    # 分割字符串并获取标记后的部分，去除多余的空格
                    final_answer = full_answer_text.split('####')[-1].strip()
                
                # 2. 提取解题过程 (solution)
                # 解题过程是 "####" 标记之前的所有内容
                solution = full_answer_text.split('####')[0].strip()

                # 3. 构建符合目标格式的新字典
                # 根据你的描述，"problem" 对应 "question"，"solution" 对应解题过程，"answer" 对应最终答案
                new_record = {
                    'problem': question,
                    'solution': solution,
                    'answer': final_answer
                }
                
                # 将转换后的记录添加到列表中
                converted_data.append(new_record)

        # 确保输出文件的目录存在，如果不存在则创建
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
        # 将转换后的数据列表写入到目标 .json 文件中
        with open(output_path, 'w', encoding='utf-8') as outfile:
            # 使用 indent=4 参数可以使输出的 JSON 文件格式化，更易于阅读
            json.dump(converted_data, outfile, ensure_ascii=False, indent=4)
            
        print(f"✅ 转换成功！总共处理了 {len(converted_data)} 条记录。")
        print(f"   原始文件: {input_path}")
        print(f"   输出文件: {output_path}")

    except FileNotFoundError:
        print(f"❌ 错误：找不到输入文件 {input_path}")
    except json.JSONDecodeError as e:
        print(f"❌ 错误：解析 JSON 文件失败。详情: {e}")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")

# --- 主程序入口 ---
if __name__ == "__main__":
    # --- 请在这里修改你的文件路径 ---
    # 原始数据文件路径
    input_file_path = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\GSM8K_train.jsonl'
    
    # 转换后的目标文件路径
    output_file_path = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\GSM8K_train.json'
    
    # 调用转换函数
    convert_gsm8k_dataset(input_file_path, output_file_path)