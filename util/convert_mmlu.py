import json
import os

def convert_mmlu_dataset(input_path, output_path):
    """
    该函数读取 MMLU-Pro 格式的 .json 文件，
    并将其转换为仅包含 "problem", "answer", 和 "answer_id" 的新格式。

    Args:
        input_path (str): 原始 .json 文件的路径。
        output_path (str): 目标 .json 文件的路径。
    """
    try:
        # 读取整个 JSON 文件（因为它是一个列表，而不是 .jsonl）
        with open(input_path, 'r', encoding='utf-8') as infile:
            original_data = json.load(infile)

        # 用于存储所有转换后记录的列表
        converted_data = []

        # 遍历原始数据列表中的每一个记录
        for i, original_record in enumerate(original_data):
            try:
                # 1. 提取必要的原始字段
                problem = original_record['problem']
                options = original_record['options']
                answer_index = original_record['answer_index']

                # 2. 根据 'answer_index' 从 'options' 列表中获取正确答案的文本
                correct_answer_text = options[answer_index]

                # 3. 构建符合目标格式的新字典
                new_record = {
                    'problem': problem,           # 'problem' 内容直接复制
                    'answer': correct_answer_text, # 'answer' 是正确选项的文本
                    'answer_id': original_record['answer']     # 'answer_id' 是正确选项的索引
                }
                
                converted_data.append(new_record)

            except (KeyError, TypeError) as e:
                # 如果记录缺少必要的键（如 'options' 或 'answer_index'），则打印警告并跳过
                print(f"⚠️ 警告：正在跳过第 {i+1} 条记录，缺少关键字段或类型错误: {e}")
                continue
            except IndexError:
                # 如果 'answer_index' 超出 'options' 列表的范围，也跳过该记录
                print(f"⚠️ 警告：正在跳过第 {i+1} 条记录，因为答案索引 "
                      f"'{original_record.get('answer_index')}' 无效。")
                continue

        # 确保输出文件的目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
        # 将转换后的数据列表写入到目标 .json 文件
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(converted_data, outfile, ensure_ascii=False, indent=4)
            
        print(f"✅ 转换成功！处理了 {len(original_data)} 条记录，生成了 {len(converted_data)} 条新记录。")
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
    input_file_path = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\MMLU-Pro_validation.json'
    
    # 转换后的目标文件路径
    output_file_path = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\MMLU-Pro_validation_0.json'
    
    # 调用转换函数
    convert_mmlu_dataset(input_file_path, output_file_path)