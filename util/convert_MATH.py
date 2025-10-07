import os
import json
import re

def convert_math_dataset(source_dir, output_file):
    """
    遍历源数据目录，将所有JSON文件合并并转换为目标格式。

    Args:
        source_dir (str): 包含原始JSON文件的根目录路径。
        output_file (str): 转换后输出的JSON文件路径。
    """
    consolidated_data = []
    current_id = 0  # 您可以修改ID的起始值，例如改为 60

    print(f"🚀 开始处理目录: {source_dir}")

    # os.walk 会遍历指定目录下的所有子目录和文件
    for root, _, files in os.walk(source_dir):
        # 按文件名排序，确保每次运行结果的顺序一致
        for filename in sorted(files):
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_data = json.load(f)

                    # 提取 problem 和 solution 字段
                    problem_text = original_data.get("problem", "")
                    solution_text = original_data.get("solution", "")
                    
                    if not problem_text or not solution_text:
                        print(f"⚠️  警告: 文件 {file_path} 缺少 'problem' 或 'solution' 字段，已跳过。")
                        continue

                    # --- 核心：从 solution 文本中提取 answer ---
                    # 查找所有 \boxed{...} 中的内容
                    matches = re.findall(r'\\boxed\{([^}]+)\}', solution_text)
                    
                    final_answer = ""
                    if matches:
                        # 通常最后一个是最终答案
                        last_match = matches[-1]
                        # 尝试从匹配项中提取核心数值 (整数、小数或分数)
                        # 这个正则表达式可以处理类似 \textbf{113} 的情况
                        core_value = re.search(r'[-+]?[\d.,/]+', last_match)
                        if core_value:
                            final_answer = core_value.group(0)
                        else:
                            # 如果找不到数字，则使用原始匹配内容并去除首尾空格
                            final_answer = last_match.strip()
                    else:
                        print(f"🤔 警告: 在文件 {file_path} 中未找到 \\boxed{{...}} 格式的答案。")
                        
                    # 构建新的数据条目
                    # 注意：根据您的要求，这里保留了 "solution" 字段。
                    # 如果您确认不需要 "solution" 字段，可以删除下面字典中的 "solution": solution_text 这一行。
                    new_entry = {
                        "id": current_id,
                        "problem": problem_text,
                        "solution": solution_text,
                        "answer": final_answer
                    }

                    consolidated_data.append(new_entry)
                    current_id += 1

                except json.JSONDecodeError:
                    print(f"❌ 错误: 无法解析文件 {file_path} 的JSON内容。")
                except Exception as e:
                    print(f"❌ 发生意外错误，文件 {file_path}: {e}")

    # --- 写入最终的JSON文件 ---
    try:
        # 确保输出文件的目录存在
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"已创建输出目录: {output_dir}")
            
        with open(output_file, 'w', encoding='utf-8') as f:
            # indent=4 使JSON文件格式化，方便查看
            json.dump(consolidated_data, f, ensure_ascii=False, indent=4)
        
        print(f"\n✅ 处理完成！共转换 {len(consolidated_data)} 个文件。")
        print(f"数据已保存至: {output_file}")

    except Exception as e:
        print(f"❌ 写入输出文件 {output_file} 时出错: {e}")


if __name__ == '__main__':
    # --- 请在这里配置您的路径 ---
    # 原始数据集的根目录
    source_directory = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\MATH\all_MATH\test"
    
    # 目标文件的完整路径
    output_json_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\MATH.json"
    
    # 运行转换函数
    convert_math_dataset(source_directory, output_json_path)