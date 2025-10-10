import json

# 您要格式化的JSON文件路径
file_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\livebench-reasoning.json"

try:
    # 1. 以读取模式打开并加载JSON数据
    # 使用 'r' 模式和 utf-8 编码
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. 以写入模式重新打开同一个文件并写入格式化后的数据
    # 'w' 模式会覆盖文件的全部内容
    # indent=4 参数用于设置缩进为空格数
    # ensure_ascii=False 确保中文字符能正常显示
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"成功！文件 '{file_path}' 已经被格式化并覆盖保存。✅")

except FileNotFoundError:
    print(f"错误：找不到文件 '{file_path}'。请检查路径是否正确。")
except json.JSONDecodeError:
    print(f"错误：文件 '{file_path}' 的内容不是有效的JSON格式。")
except Exception as e:
    print(f"发生了一个未知错误: {e}")