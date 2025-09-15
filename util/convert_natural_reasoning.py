import json
import os

def convert_natural_reasoning():
    input_file = os.path.join('dataset', 'original_data', 'natural_reasoning.jsonl')
    output_file = os.path.join('dataset', 'TestData', 'natural_reasoning_skip_empty.json')
    
    data_list = []
    counter = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 跳过空行
                data = json.loads(line.strip())
                if data["reference_answer"] is None:
                    continue
                new_data = {
                    "problem": data["question"],
                    "answer": data["reference_answer"]
                }
                # 添加其他属性
                counter += 1
                for key, value in data.items():
                    if key not in ["question", "reference_answer"]:
                        new_data[key] = value
                data_list.append(new_data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    
    print(f"转换完成，结果保存到 {output_file}, 共 {counter} 条数据。")

if __name__ == "__main__":
    convert_natural_reasoning()