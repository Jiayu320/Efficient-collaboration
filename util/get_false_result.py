import json

def extract_false_results(input_file, output_file):
    """
    从input_file中提取"correct": false的题目，保存到output_file中。
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径
    """
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 提取correct为false的题目
        false_data = []
        for item in data:
            if item.get('correct') == True:
            # if item.get('correct') == False:  # 只提取correct为false的题目
                new_item = {
                    "dataset_source": 's1k1_1',  # 添加数据集标识
                    "question": item.get('question', ''),  # 确保有question字段
                    "answer": item.get('answer', ''),  # 确保有answer字段
                }
                false_data.append(new_item)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(false_data, f, ensure_ascii=False, indent=2)
        
        print(f"提取完成！已将 {len(false_data)} 个错误答案的题目保存到 {output_file}")
    
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    input_file = "d:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/generated_data/s1k1_1_training.json"
    # output_file = "d:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/generated_data/s1k1_1_false_results.json"
    output_file = "d:/JIAYU/Documents/GitHub/Efficient-collaboration/dataset/generated_data/s1k1_1_true_results.json"
    extract_false_results(input_file, output_file)
