import json
import os

# 1. 定义新的、通用的 system prompt
new_system_prompt = """You are an expert at breaking down complex problems into a step-by-step plan. Your task is to generate a solution plan for the given problem in XML format.

**Instructions:**
1.  The plan must be enclosed in `<Plan>` tags.
2.  The plan must contain between 2 and 10 `<Step>` tags.
3.  Each `<Step>` must have `ID`, `Task`, `Difficulty`, `Token`, and `Rely` attributes.
4.  The `Task` must be a clear, actionable question that ends with a question mark (?).
5.  The final step must provide the conclusive result or final answer.
6.  If a step depends on a previous one, use the `Rely` attribute to list the `ID`s.

### Example
**Problem**: For how many rational numbers between 0 and 1 will $20!$ be the resulting product of their numerator and denominator in lowest terms?
**Plan**:
<Plan>
<Step ID="1" Task="What are the distinct prime factors of 20! ?" Difficulty="4" Token="50" Rely=""/>
<Step ID="2" Task="Count the number of distinct prime factors found in Step 1. Let this count be k. What is the value of k?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="3" Task="The number of pairs of coprime factors (a,b) of 20! is 2^k. The number of rational numbers a/b between 0 and 1 is half of this. Using the formula N = 2^(k-1), what is the final number of such rational numbers?" Difficulty="4" Token="50" Rely="2"/>
</Plan>

Apply the entire framework described above to the problem provided below. 
**Problem**: """

# 2. 指定需要更新的 JSON 文件路径
# 使用原始字符串 (r"...") 来避免反斜杠问题
file_paths = [
    r"data_reports/dataset/s1k1_data/qwen3-235b-a22b-thinking-2507/gpt-4o/qwen2.5-3b-instruct/20250924_013352/datasetTraining_w_thinking.json",
    r"data_reports/dataset/s1k1_data/qwen3-235b-a22b-thinking-2507/gpt-4o/qwen2.5-3b-instruct/20250924_013352/datasetTraining_wo_thinking.json"
]

def update_json_files(paths, new_prompt):
    """
    读取JSON文件列表，替换每个条目中的'system'字段，然后写回原文件。
    """
    for file_path in paths:
        print(f"🔄 Processing file: {file_path}")
        if not os.path.exists(file_path):
            print(f"❌ Error: File not found at {file_path}. Skipping.\n")
            continue
        
        try:
            # 读取原始数据
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 遍历并更新每一个数据条目
            updated_count = 0
            for entry in data:
                if 'system' in entry:
                    entry['system'] = new_prompt
                    updated_count += 1
            
            # 写回更新后的数据
            with open(file_path, 'w', encoding='utf-8') as f:
                # indent=4 格式化输出，便于阅读
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print(f"✅ Successfully updated {updated_count} entries in {os.path.basename(file_path)}.\n")

        except json.JSONDecodeError:
            print(f"❌ Error: Could not decode JSON from {file_path}. The file might be corrupted. Skipping.\n")
        except Exception as e:
            print(f"❌ An unexpected error occurred with {file_path}: {e}\n")

# 运行更新函数
if __name__ == "__main__":
    update_json_files(file_paths, new_system_prompt)
    print("✨ Script finished.")