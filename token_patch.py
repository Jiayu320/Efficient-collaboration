import transformers
import os

# 保存完整输出的全局变量
collected_output = ""

# 初始化DeepSeek tokenizer
_deepseek_tokenizer = None

def get_deepseek_tokenizer():
    """获取DeepSeek tokenizer实例（单例模式）"""
    global _deepseek_tokenizer
    if _deepseek_tokenizer is None:
        chat_tokenizer_dir = os.path.join(os.path.dirname(__file__), 'deepseek_v3_tokenizer')
        _deepseek_tokenizer = transformers.AutoTokenizer.from_pretrained(
            chat_tokenizer_dir,
            trust_remote_code=True
        )
    return _deepseek_tokenizer

def count_deepseek_tokens(text):
    """使用DeepSeek tokenizer计算文本的token数"""
    tokenizer = get_deepseek_tokenizer()
    return len(tokenizer.encode(text))

def append_output(content):
    """追加输出内容到全局变量"""
    global collected_output
    collected_output += content
    return content

def get_collected_tokens():
    """获取已收集的所有输出的token数量"""
    global collected_output
    if not collected_output:
        return 0
    return count_deepseek_tokens(collected_output)

def reset_collected_output():
    """重置收集的输出内容"""
    global collected_output
    collected_output = ""
