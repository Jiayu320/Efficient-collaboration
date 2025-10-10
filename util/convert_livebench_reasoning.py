import json
import os

def convert_json_format(source_path, target_path):
    """
    将原始JSON数据转换为指定的新格式。

    - 'id' 从1开始递增
    - 'problem' 字段取自 'turns' 列表的第一个元素
    - 'answer' 字段取自 'ground_truth'
    - 保留所有其他原始字段

    Args:
        source_path (str): 原始JSON文件的路径。
        target_path (str): 转换后新JSON文件的保存路径。
    """
    try:
        # 读取原始JSON文件
        with open(source_path, 'r', encoding='utf-8') as f_in:
            original_data = json.load(f_in)

        transformed_data = []
        # ID 从 1 开始计数
        item_id = 1

        # 遍历原始数据中的每一项
        for original_item in original_data:
            # 复制原始项目以保留所有其他字段
            new_item = original_item.copy()

            # 1. 添加新的 'id' 字段
            new_item['id'] = item_id

            # 2. 将 'turns' 的第一个元素赋值给 'problem'
            if 'turns' in original_item and len(original_item['turns']) > 0:
                new_item['problem'] = original_item['turns'][0]
            else:
                new_item['problem'] = ""  # 如果turns为空或不存在，则设为空字符串

            # 3. 将 'ground_truth' 赋值给 'answer'
            if 'ground_truth' in original_item:
                new_item['answer'] = original_item['ground_truth']
            
            # 移除不再需要的旧字段
            new_item.pop('question_id', None)
            new_item.pop('turns', None)
            new_item.pop('ground_truth', None)

            # (可选) 调整字段顺序，使 id, problem, answer 在前面，更美观
            ordered_item = {
                'id': new_item.pop('id'),
                'problem': new_item.pop('problem'),
                'answer': new_item.pop('answer'),
                **new_item  # 将剩余的字段追加到后面
            }
            
            transformed_data.append(ordered_item)
            item_id += 1
        
        # 确保目标文件夹存在
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        # 将转换后的数据写入目标文件
        with open(target_path, 'w', encoding='utf-8') as f_out:
            json.dump(transformed_data, f_out, indent=4, ensure_ascii=False)

        print(f"✅ 数据转换成功！\n- 原始文件: {source_path}\n- 新文件: {target_path}")

    except FileNotFoundError:
        print(f"❌ 错误：找不到源文件 '{source_path}'，请检查路径是否正确。")
    except Exception as e:
        print(f"❌ 处理过程中发生未知错误: {e}")


# --- 使用方法 ---
# 1. 将下面的路径替换为你的实际文件路径
source_file = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\livebench-reasoning.json'
target_file = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\livebench-reasoning.json'

# 2. 运行脚本
convert_json_format(source_file, target_file)