import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from token_patch import get_deepseek_tokenizer, count_deepseek_tokens

def test_token_calculation():
    """测试DeepSeek tokenizer计算tokens"""
    sample_text = "这是一个测试文本，用于验证DeepSeek tokenizer的token计算"
    tokens = count_deepseek_tokens(sample_text)
    print(f"测试文本: {sample_text}")
    print(f"DeepSeek tokenizer计算的tokens: {tokens}")
    print(f"简单split方法计算的tokens: {len(sample_text.split())}")
    
    # 显示实际的tokens
    tokenizer = get_deepseek_tokenizer()
    token_ids = tokenizer.encode(sample_text)
    print(f"Token IDs: {token_ids}")
    print(f"Token数量: {len(token_ids)}")

if __name__ == "__main__":
    test_token_calculation()
