import os
import json

# llama_factory 目录路径
dir_path = os.path.join(os.path.dirname(__file__), '../dataset/llama_factory')
output_path = os.path.join(dir_path, 'training_data_all.json')

all_data = []

for filename in os.listdir(dir_path):
    if filename.endswith('.json') and filename != 'training_data_all.json':
        file_path = os.path.join(dir_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    all_data.extend(data)
                else:
                    all_data.append(data)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"合并完成，共 {len(all_data)} 条数据，已保存到 {output_path}")
