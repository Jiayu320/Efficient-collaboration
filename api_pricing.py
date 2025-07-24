'''
管理不同API模型的价格费率
该文件提供集中化的API价格管理，方便价格调整
'''
from typing import Dict, Any

def get_model_pricing(model_name: str) -> Dict[str, float]:
    """
    根据模型名称返回其价格费率（美元/百万tokens）
    
    参数:
        model_name: 模型名称（字符串或包含模型名称的字符串）
    
    返回:
        包含输入和输出价格的字典 {'prompt': float, 'completion': float}
    """
    # 标准化模型名称为小写以便匹配
    model_name_lower = model_name.lower()
    
    # Claude模型价格
    if "claude-3-5" in model_name_lower or "claude-3.5" in model_name_lower or "claude-3-5-sonnet" in model_name_lower:
        return {"prompt": 3.0, "completion": 15.0}
    elif "claude-3" in model_name_lower or "claude3" in model_name_lower:
        return {"prompt": 3.0, "completion": 15.0}
    elif "claude-2" in model_name_lower or "claude2" in model_name_lower:
        return {"prompt": 8.0, "completion": 24.0}
    
    # OpenAI模型价格
    elif "gpt-4o" in model_name_lower:
        return {"prompt": 2.5, "completion": 10.0}
    elif "gpt-4" in model_name_lower:
        return {"prompt": 30.0, "completion": 60.0}
    elif "gpt-3.5" in model_name_lower:
        return {"prompt": 0.5, "completion": 1.5}
    
    # 通义千问系列
    elif "qwen-2.5-7b" in model_name_lower or "qwen2.5-7b" in model_name_lower or "qwen3-1.7b" in model_name_lower:
        return {"prompt": 0.04, "completion": 0.10}
    elif "qwen3-7b" in model_name_lower:
        return {"prompt": 0.15, "completion": 0.15}
    elif "qwen3-14b" in model_name_lower or "qwen-3-14b" in model_name_lower:
        return {"prompt": 0.30, "completion": 0.30}
    elif "qwen3-72b" in model_name_lower:
        return {"prompt": 0.9, "completion": 0.9}
    elif "qwen3-235b" in model_name_lower or "qwen-3-235b" in model_name_lower:
        return {"prompt": 3.0, "completion": 3.0}
    
    # DeepSeek系列
    elif "deepseek-r1" in model_name_lower:
        return {"prompt": 0.272, "completion": 0.272}
    elif "deepseek-coder" in model_name_lower:
        return {"prompt": 0.2, "completion": 0.2}
    

    elif "llama3-8b" in model_name_lower or "llama-3-8b" in model_name_lower:
        return {"prompt": 0.03, "completion": 0.06}
    # 本地模型
    elif "local" in model_name_lower:
        return {"prompt": 0.0, "completion": 0.0}
    
    # 默认价格（当无法识别模型时使用）
    else:
        print(f"警告: 未识别的模型 '{model_name}'，使用默认价格")
        return {"prompt": 0.5, "completion": 1.0}
