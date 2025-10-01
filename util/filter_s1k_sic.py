import json

def filter_json_data(input_path, output_path):
    """
    从输入的JSON文件中读取数据，筛选出"cot_type"不为"math"的条目，
    并将结果保存到输出JSON文件中。

    参数:
    input_path (str): 输入JSON文件的路径。
    output_path (str): 输出JSON文件的路径。
    """
    try:
        # 以读模式打开并加载原始JSON文件，指定UTF-8编码
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 使用列表推导式筛选出 "cot_type" 不等于 "math" 的条目
        filtered_data = [item for item in data if item.get("cot_type") != "math"]

        # 以写模式打开目标文件，并将筛选后的数据写入
        # indent=4 使输出的JSON文件格式更美观，易于阅读
        # ensure_ascii=False 确保中文字符能被正确写入
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=4, ensure_ascii=False)

        print(f"筛选完成！数据已成功保存到: {output_path}")
        print(f"原始数据条目数: {len(data)}")
        print(f"筛选后数据条目数: {len(filtered_data)}")

    except FileNotFoundError:
        print(f"错误：找不到输入文件: {input_path}")
    except json.JSONDecodeError:
        print(f"错误：输入文件 '{input_path}' 不是有效的JSON格式。")
    except Exception as e:
        print(f"处理过程中发生未知错误: {e}")

if __name__ == '__main__':
    # 定义输入和输出文件的路径
    # 请确保在Windows系统中使用双反斜杠'\\'或正斜杠'/'来表示路径
    input_file = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\s1k1_data.json"
    output_file = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\s1k1_data_sci.json"

    # 调用函数执行筛选和保存操作
    filter_json_data(input_file, output_file)
