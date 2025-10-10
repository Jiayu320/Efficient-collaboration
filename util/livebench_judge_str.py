import json
import re
import os

def update_markdown_report(md_filepath, processed_data, correct_count, total_count):
    """
    根据处理后的JSON数据，更新对应的Markdown报告文件。
    此版本能正确处理问题描述中包含'|'字符的情况。
    """
    if not os.path.exists(md_filepath):
        print(f"\n警告：未找到对应的Markdown报告文件：{md_filepath}")
        return

    print(f"  -> 正在更新Markdown报告: {os.path.basename(md_filepath)} ...")

    try:
        with open(md_filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 更新 "概述" 部分
        accuracy = (correct_count / total_count) * 100 if total_count > 0 else 0
        content = re.sub(r"(正确数量: )\d+", f"\\g<1>{correct_count}", content)
        content = re.sub(r"(准确率: )\d+\.\d+%", f"\\g<1>{accuracy:.2f}%", content)

        # 更新 "详细结果" 表格
        lines = content.split('\n')
        table_header_index = -1
        for i, line in enumerate(lines):
            if "## 详细结果" in line:
                for j in range(i + 1, len(lines)):
                    if lines[j].strip().startswith('| # |'):
                        table_header_index = j
                        break
                break
        
        if table_header_index != -1:
            for i in range(table_header_index + 2, len(lines)):
                line = lines[i]
                if not line.strip().startswith('|'):
                    break
                
                parts = line.rsplit('|', 7)
                if len(parts) == 8:
                    row_num_str = parts[0].split('|')[1].strip()
                    if row_num_str.isdigit():
                        item_index = int(row_num_str) - 1
                        if 0 <= item_index < len(processed_data):
                            is_correct = processed_data[item_index]['judge_str_correct']
                            correct_symbol = '✓' if is_correct else '✗'
                            parts[1] = f" {correct_symbol} "
                            lines[i] = "|".join(parts)
        content = '\n'.join(lines)

        with open(md_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("  -> Markdown报告文件更新成功！✨")

    except Exception as e:
        print(f"  -> 更新Markdown文件时发生错误: {e}")


def extract_and_judge_answers(json_filepath):
    """
    处理单个json文件及其对应的md报告的核心函数。
    (*** 此函数已按要求修改 ***)
    """
    print(f"  -> 正在处理JSON文件: {os.path.basename(json_filepath)} ...")
    
    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"  -> 读取或解析JSON文件时出错: {e}")
        return
        
    if not data:
        print("  -> JSON文件为空，已跳过。")
        return

    correct_items_count = 0
    for item in data:
        model_solution = item.get("model_solution", "")
        gold_solution = item.get("gold_solution", "")
        extracted_answer = None
        is_correct = False
        
        # 核心修改逻辑：从 "## 最终答案" 后的 <solution> 标签中提取答案
        if "## 最终答案" in model_solution:
            # 1. 切分字符串，获取 "## 最终答案" 之后的内容
            final_answer_part = model_solution.split("## 最终答案", 1)[-1]
            
            # 2. 使用正则表达式查找 <solution> 和 </solution> 之间的内容
            # re.DOTALL 标志让 '.' 可以匹配包括换行符在内的任意字符
            match = re.search(r"<solution>(.*?)</solution>", final_answer_part, re.DOTALL)
            
            if match:
                # 3. 提取匹配到的内容，并去除首尾空白
                extracted_answer = match.group(1).strip()

        # 比较提取出的答案和标准答案
        if gold_solution is not None and extracted_answer is not None:
            if extracted_answer.strip() == str(gold_solution).strip():
                is_correct = True
                
        item.update({
            'answer_choice': None,  # 根据新格式，此字段可能不再需要
            'answer_choice_value': extracted_answer, # 保存提取出的答案
            'judge_str_correct': is_correct
        })
        
        if is_correct:
            correct_items_count += 1

    directory = os.path.dirname(json_filepath)
    filename = os.path.basename(json_filepath)
    output_filename = os.path.splitext(filename)[0] + "_processed.json"
    output_filepath = os.path.join(directory, output_filename)

    try:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  -> JSON结果已保存至: {os.path.basename(output_filepath)}")
    except Exception as e:
        print(f"  -> 写入新JSON文件时出错: {e}")
        return

    total_items_count = len(data)
    if total_items_count > 0:
        accuracy = (correct_items_count / total_items_count) * 100
        print("\n     ----- 评估摘要 -----")
        print(f"     总条目数: {total_items_count}, 正确数: {correct_items_count}")
        print(f"     最终正确率: {accuracy:.2f}%")
        print("     --------------------")
    
    md_file_path = os.path.join(directory, "dataset_report.md")
    update_markdown_report(md_file_path, data, correct_items_count, total_items_count)


def process_all_folders(root_directory):
    """
    遍历指定根目录，查找并处理所有包含dataset_results.json的子文件夹。
    """
    print(f"🚀 开始在根目录中搜索: {root_directory}")
    
    # 1. 查找所有符合条件的文件夹
    target_folders = []
    for dirpath, _, filenames in os.walk(root_directory):
        if 'dataset_results.json' in filenames:
            target_folders.append(dirpath)

    if not target_folders:
        print("\n❌ 未找到任何包含 'dataset_results.json' 的子文件夹。")
        return

    # 2. 逐一处理找到的文件夹
    print(f"\n✅ 成功找到 {len(target_folders)} 个待处理的文件夹。")
    for i, folder_path in enumerate(target_folders):
        print("\n" + "="*70)
        print(f"📂 开始处理第 {i+1}/{len(target_folders)} 个文件夹: {folder_path}")
        print("="*70)
        json_path = os.path.join(folder_path, 'dataset_results.json')
        extract_and_judge_answers(json_path)

    print("\n\n🎉 全部处理完毕！")


# --- 主程序入口 ---
if __name__ == "__main__":
    # 只需要在这里设置您的顶层搜索路径
    # 脚本将自动处理此路径下的所有相关子文件夹
    root_search_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\data_reports\dataset\livebench-reasoning-10\gpt-4.1-mini\gpt-4.1-mini\gpt-4.1-mini\20251008_140252"
    
    process_all_folders(root_search_path)