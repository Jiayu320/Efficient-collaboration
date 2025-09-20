import json
import os

def process_and_merge_json(input_files, output_file, keys_to_keep):
    """
    读取多个JSON文件，筛选每个对象的键，然后将结果合并到一个输出文件中。

    参数:
    input_files (list): 输入的JSON文件路径列表。
    output_file (str): 合并和处理后的输出JSON文件路径。
    keys_to_keep (list): 需要保留的键名列表。
    """
    merged_data = []

    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建目录: {output_dir}")

    # 遍历所有输入文件
    for file_path in input_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"成功读取文件: {file_path}")

                # 遍历文件中的每个JSON对象
                for item in data:
                    # 创建一个新字典，只包含需要保留的键
                    filtered_item = {key: item[key] for key in keys_to_keep if key in item}
                    merged_data.append(filtered_item)
        
        except FileNotFoundError:
            print(f"错误: 文件未找到 {file_path}")
        except json.JSONDecodeError:
            print(f"错误: 文件格式不正确 {file_path}")
        except Exception as e:
            print(f"处理文件 {file_path} 时发生未知错误: {e}")

    # 将合并后的数据写入新文件
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # 使用 indent=4 参数使输出的JSON文件格式美观
            json.dump(merged_data, f, ensure_ascii=False, indent=4)
        print(f"处理完成！合并后的数据已保存到: {output_file}")
        print(f"总共合并了 {len(merged_data)} 条记录。")
    except Exception as e:
        print(f"写入输出文件 {output_file} 时发生错误: {e}")


if __name__ == "__main__":
    # --- 配置 ---
    # 需要处理的JSON文件列表
    input_json_files = [
        'dataset/generated_data/limo_training.json',
        'dataset/generated_data/s1k1_1_training.json'
    ]

    # 合并后输出的文件路径
    output_json_file = 'dataset/generated_data/training_data.json'

    # 需要保留的键
    keys = [
        "question",
        "answer",
        "solution",
        "plan",
        "difficulty",
        "correct"
    ]
    # --- 运行 ---
    process_and_merge_json(input_json_files, output_json_file, keys)
