from typing import Dict, Any

def get_model_performance(model_name: str) -> Dict[str, float]:
    """
    根据模型名称返回其性能指标（延迟和吞吐量）
    
    参数:
        model_name: 模型名称（字符串或包含模型名称的字符串）
    
    返回:
        包含输入和输出性能指标的字典 {'latency': float, 'throughput': float}
    """
    # 标准化模型名称为小写以便匹配
    model_name_lower = model_name.lower()
    
    # Claude模型性能
    if "claude-3-5" in model_name_lower or "claude-3.5" in model_name_lower or "claude-3-5-sonnet" in model_name_lower:
        return {"latency": 1.06, "throughput": 57.07}
    
    # OpenAI模型性能
    elif "gpt-4o" in model_name_lower:
        return {"latency": 0.61, "throughput": 58.71}
    
    # DeepSeek系列
    elif "deepseek-r1" in model_name_lower:
        return {"latency": 1.01, "throughput": 55.17}
    elif "deepseek-chat" in model_name_lower:
        return {"latency": 0.94, "throughput": 54.79}
    elif "deepseek-reasoner" in model_name_lower:
        return {"latency": 1.01, "throughput": 55.17}

    elif "llama3-8b" in model_name_lower or "llama-3-8b" in model_name_lower:
        return {"latency": 0.44, "throughput": 3422}
    # 本地模型
    elif "local" in model_name_lower:
        return {"latency": 0.5, "throughput": 100.0}

    # 默认性能（当无法识别模型时使用）
    else:
        print(f"警告: 未识别的模型 '{model_name}'，使用默认性能")
        return {"latency": 0.5, "throughput": 100.0}