import json
import random
import os
from collections import Counter

def load_json_data(filepath):
    """安全地加载JSON文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：文件未找到 -> {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"错误：无法解析JSON文件 -> {filepath}")
        return None

def save_json_data(data, filepath):
    """将数据保存为格式化的JSON文件"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"\n数据已成功保存到 -> {filepath}")
    except Exception as e:
        print(f"错误：保存文件时出错 -> {e}")

def sample_data(data, level, count, source_name):
    """从数据集中根据难度等级随机抽样"""
    # 筛选出符合难度等级的数据
    filtered_data = [item for item in data if item.get("difficulty_level") == level]
    
    # 检查是否有足够的数据进行抽样
    if len(filtered_data) < count:
        print(f"警告：在 {source_name} 中，难度 {level} 的数据不足。")
        print(f"需要 {count} 个，但只有 {len(filtered_data)} 个。将使用所有可用的数据。")
        count = len(filtered_data)
        
    # 随机抽样
    sampled_items = random.sample(filtered_data, count)
    
    # 为抽样出的每条数据添加来源信息
    for item in sampled_items:
        item['data_source'] = source_name
        
    return sampled_items

def main():
    # --- 1. 定义文件路径 ---
    base_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData"
    
    initial_data_path = os.path.join(base_path, "s1k1_data.json")
    mmlu_path = os.path.join(base_path, "MMLU-STEM.json")
    math_path = os.path.join(base_path, "MATH.json")
    gpqa_path = os.path.join(base_path, "gpqa.json")
    gsm8k_path = os.path.join(base_path, "GSM8K_train.json")
    output_path = os.path.join(base_path, "training_data_all.json")

    # --- 2. 加载你现有的数据 ---
    print("开始处理数据...")
    combined_data = []
    initial_data = load_json_data(initial_data_path)
    if initial_data:
        # 为初始数据的每一项添加来源信息
        for item in initial_data:
            item['data_source'] = "s1k1_data.json"
        combined_data.extend(initial_data)
        print(f"已加载初始数据: {len(initial_data)} 条")

    # --- 3. 定义抽样计划 ---
    # 格式: (文件路径, 文件名, [(难度等级1, 数量1), (难度等级2, 数量2), ...])
    sampling_plan = [
        (mmlu_path, "MMLU-STEM.json", [(1, 100), (3, 100), (5, 300), (7, 100)]),
        (math_path, "MATH.json", [(3, 50), (5, 300)]),
        (gpqa_path, "gpqa.json", [(5, 50)]),
        # 注意: 你的要求是两次100个难度为5的，这里合并为一次性提取200个
        (gsm8k_path, "GSM8K_train.json", [(5, 200)]) 
    ]

    # --- 4. 执行抽样 ---
    for path, name, samples in sampling_plan:
        print(f"\n正在处理文件: {name}")
        source_data = load_json_data(path)
        if source_data:
            for level, count in samples:
                print(f" -> 正在从 {name} 中抽样 {count} 条难度为 {level} 的数据...")
                new_samples = sample_data(source_data, level, count, name)
                combined_data.extend(new_samples)
                print(f"    成功抽样 {len(new_samples)} 条。")

    # --- 5. 保存合并后的数据 ---
    save_json_data(combined_data, output_path)

    # --- 6. 生成并输出最终的难度分布报告 ---
    if not combined_data:
        print("没有数据可以分析。")
        return

    difficulty_levels = [item.get("difficulty_level", "未知") for item in combined_data]
    distribution = Counter(difficulty_levels)
    
    print("\n--- 最终数据集难度分布报告 ---")
    print(f"总问题数: {len(combined_data)}")
    
    # 按难度等级排序并打印
    for level in sorted(distribution.keys()):
        count = distribution[level]
        print(f"难度等级 {level}: {count:>5} 个问题")
    print("--- 报告结束 ---")


if __name__ == "__main__":
    main()
