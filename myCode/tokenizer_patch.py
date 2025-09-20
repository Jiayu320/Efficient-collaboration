import transformers
import os

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

# 计算文本的token数
def count_deepseek_tokens(text):
    """使用DeepSeek tokenizer计算文本的token数"""
    tokenizer = get_deepseek_tokenizer()
    return len(tokenizer.encode(text))
