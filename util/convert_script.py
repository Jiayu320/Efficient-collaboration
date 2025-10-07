import json
import os

def convert_dataset(input_path, output_path):
    """
    该函数读取一个 .jsonl 格式的数据集文件，
    根据特定规则进行转换，并将其保存为 .json 格式的文件。

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

                # 1. 根据要求，将 'prompt', 'problem', 'testcases' 拼接成新的 'problem' 字段
                #    使用换行符分隔，以提高可读性
                # --- 主要改动在这里 ---
                # 在 test case 内容前添加了 "test case:" 标签
                new_problem_content = (
                    f"{original_record.get('prompt', '')}\n\n"
                    f"{original_record.get('problem', '')}\n\n"
                    f"Test case:\n{original_record.get('testcases', '')}"
                )
                # --- 改动结束 ---

                # 2. 构建符合目标格式的新字典
                new_record = {
                    # 保留原始数据中的一些字段
                    '_id': original_record.get('_id'),
                    'setup_code': original_record.get('setup_code'),
                    'classification': original_record.get('classification'),
                    
                    # 使用新拼接的 'problem' 字段
                    'problem': new_problem_content,
                    
                    # 3. 将 'reference_solution' 映射到 'answer'
                    'answer': original_record.get('reference_solution'),
                    
                    # 4. 按照要求，单独保留 'testcases' 字段
                    'testcases': original_record.get('testcases')
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
    input_file_path = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\ncb_python_en.jsonl'
    
    # 转换后的目标文件路径
    output_file_path = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\ncb_python_en.json'
    
    # 调用转换函数
    convert_dataset(input_file_path, output_file_path)