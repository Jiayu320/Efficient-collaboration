import pandas as pd

df = pd.read_json("hf://datasets/HuggingFaceH4/MATH-500/test.jsonl", encoding="ISO-8859-1", lines=True)

# 预览数据集
print(df.head())

# 保存到本地为jsonl格式
df.to_json("math500_test.jsonl", orient='records', lines=True, force_ascii=False)
