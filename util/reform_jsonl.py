import json

def convert_json_format(input_file, output_file):
    """
    将input_file中的JSONL数据转换为math200格式的JSON，只保留指定字段。
    
    Args:
        input_file (str): 输入文件路径（.jsonl格式）
        output_file (str): 输出文件路径（.json格式）
    """
    try:
        # 读取输入文件（JSONL格式）
        data = []
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():  # 跳过空行
                    data.append(json.loads(line))
        
        # 转换为新格式，只保留solution字段
        new_data = []
        for item in data:
            # new_item = {"id": item['id'], "problem": item['problem'], "solution": item['solution'], "answer": item['answer']}
            new_item = {
                "question": item['question'],  # 确保有question字段
                "answer": item.get('answer', ''),  # 确保有answer字段
                "solution": item.get('solution', '')  # 确保有solution字段
            }
            new_data.append(new_item)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)
        
        print(f"转换完成！已将 {len(new_data)} 个问题的解答保存到 {output_file}")
    
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    input_file = "D:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/original_data/limo_v2.jsonl"
    output_file = "d:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/limo_v2.json"
    convert_json_format(input_file, output_file)