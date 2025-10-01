import json
import os

# 定义文件路径
input_file_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\data_reports\dataset\s1k1_data\gemini-2.5-pro\gpt-4o\qwen2.5-3b-instruct\20251001_142732\dataset_results.json"
output_file_path = os.path.join(os.path.dirname(input_file_path), "analysis_results.json")

# 读取原始JSON文件
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取所需字段
extracted_data = []
for item in data:
    extracted_item = {
        "problem": item.get("problem"),
        "gold_solution": item.get("gold_solution"),
        "model_solution": item.get("model_solution"),
        "difficulty": item.get("difficulty"),
        "is_correct": item.get("is_correct")
    }
    extracted_data.append(extracted_item)

# 保存到新JSON文件
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(extracted_data, f, indent=4, ensure_ascii=False)

print(f"提取完成，结果已保存到 {output_file_path}")