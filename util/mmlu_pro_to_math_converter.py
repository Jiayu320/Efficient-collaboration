import os
import json
import sys
import pandas as pd

def convert_mmlu_to_math_format(input_file, output_file):
    """
    将MMLU-Pro数据转换为math200.json的格式
    
    Args:
        input_file: MMLU-Pro数据文件路径
        output_file: 输出文件路径
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"输入文件不存在: {input_file}")
        return

    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取输入文件
    try:
        # 判断文件类型
        if input_file.endswith('.json'):
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        elif input_file.endswith('.parquet'):
            # 读取parquet文件
            df = pd.read_parquet(input_file)
            data = df.to_dict('records')
        else:
            print(f"不支持的文件类型: {input_file}")
            return
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return
    
    # 转换数据格式
    converted_data = []
    for item in data:
        # 从问题中提取出 problem
        problem = item.get("question", "")
        
        # 提取选项
        options = item.get("options", [])
        
        # 将选项添加到问题中，作为原始问题的一部分，并带有A、B、C等标号
        if options:
            option_text = "\n\n" + "\n".join([f"{chr(65+i)}. {option}" for i, option in enumerate(options)])
            problem += option_text
        
        # 提取答案
        answer_index = item.get("answer_index")
        answer = item.get("answer", "")
        
        # 构建解答
        solution = item.get("cot_content", "")
        if not solution:
            solution = f"The answer is {answer}."
        
        # 构建新的数据项
        new_item = {
            "problem": problem,
            "solution": solution,
        }
        
        # 添加其他属性
        for key, value in item.items():
            if key not in ["question", "solution", "cot_content"]:
                new_item[key] = value
        
        converted_data.append(new_item)
    
    # 保存转换后的数据
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(converted_data, f, ensure_ascii=False, indent=2)
        print(f"已成功转换并保存到: {output_file}")
    except Exception as e:
        print(f"保存文件时出错: {e}")

def main():
    # 项目根目录
    base_dir = "D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration"
    
    # 检查输入文件路径 - 优先使用JSON文件，如果不存在则使用parquet文件
    test_json = os.path.join(base_dir, "dataset", "original_data", "MMLU-Pro_test.json")
    validation_json = os.path.join(base_dir, "dataset", "original_data", "MMLU-Pro_validation.json")
    
    test_parquet = os.path.join(base_dir, "dataset", "original_data", "MMLU-Pro", "test-00000-of-00001.parquet")
    validation_parquet = os.path.join(base_dir, "dataset", "original_data", "MMLU-Pro", "validation-00000-of-00001.parquet")
    
    # 选择实际存在的文件
    test_file = test_json if os.path.exists(test_json) and os.path.getsize(test_json) > 0 else test_parquet
    validation_file = validation_json if os.path.exists(validation_json) and os.path.getsize(validation_json) > 0 else validation_parquet
    
    # 输出文件路径
    test_output = os.path.join(base_dir, "dataset", "TestData", "MMLU-Pro_test.json")
    validation_output = os.path.join(base_dir, "dataset", "TestData", "MMLU-Pro_validation.json")
    
    # 转换测试集
    print(f"正在转换测试集... 使用文件: {test_file}")
    convert_mmlu_to_math_format(test_file, test_output)
    
    # 转换验证集
    print(f"正在转换验证集... 使用文件: {validation_file}")
    convert_mmlu_to_math_format(validation_file, validation_output)
    
    print("转换完成!")

if __name__ == "__main__":
    main()