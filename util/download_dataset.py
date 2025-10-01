import os
from datasets import load_dataset
from huggingface_hub import HfFolder

# --- 配置 ---

# 1. Hugging Face Hub 上的数据集名称
dataset_name = "simplescaling/data_ablation_full59K"

# 2. 您想要保存数据集的本地路径
#    在 Windows 上使用原始字符串 (r"...") 是一个好习惯，可以避免反斜杠问题
save_path = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\data_ablation_full59K"

# --- 脚本 ---

# 确保您已通过 huggingface-cli 登录
# 如果您的 token 未保存，您可能需要手动提供
# from huggingface_hub import login
# login("YOUR_HF_TOKEN") # 替换为您的 Hugging Face 令牌

print(f"准备下载数据集: '{dataset_name}'")
print(f"将要保存到本地路径: '{save_path}'")

# 创建目标保存目录（如果它不存在）
os.makedirs(save_path, exist_ok=True)
print(f"已确保目录存在: '{save_path}'")

# 加载数据集
# cache_dir 参数是可选的，它可以让您指定一个不同的临时缓存位置
print("开始从 Hugging Face Hub 加载数据集...")
ds = load_dataset(dataset_name)
print("数据集加载完成。")

# 将数据集保存到本地磁盘
print(f"正在将数据集保存到 '{save_path}'...")
ds.save_to_disk(save_path)

print("\n脚本执行完毕！")
print(f"数据集 '{dataset_name}' 已成功下载并保存到 '{save_path}'。")


# --- 如何从本地加载 ---
# 您之后可以使用以下代码直接从本地磁盘加载数据，无需重新下载：
#
# from datasets import load_from_disk
#
# print("\n演示如何从本地加载:")
# reloaded_ds = load_from_disk(save_path)
# print(reloaded_ds)