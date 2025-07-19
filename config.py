'''
包含配置相关的代码
'''
import os
import yaml
import argparse
from typing import Dict, Any

class ModelConfig:
    """模型配置类，用于管理API和模型设置"""
    
    def __init__(self, 
                 small_model="qwen/qwen3-14b:free", 
                 large_model="qwen/qwen3-235b-a22b", 
                 router_model=None,
                 threshold=2,
                 api_key_path="usage/openrouter",
                 prompt_path="prompt/generate_prompt.txt",
                 api_base="https://openrouter.ai/api/v1"):
        """
        初始化模型配置
        
        参数:
            small_model: 小模型的名称
            large_model: 大模型的名称
            router_model: 路由模型的名称，用于生成任务计划，如果为None则使用small_model
            threshold: 使用大模型的难度阈值
            api_key_path: API密钥文件路径
            prompt_path: 提示词文件路径
            api_base: API基础URL
        """
        self.small_model = small_model
        self.large_model = large_model
        self.router_model = router_model if router_model else small_model
        self.threshold = threshold
        self.api_key_path = api_key_path
        self.api_base = api_base
        
        # 加载API密钥
        self.api_key = self._get_api_key(api_key_path)
        
        # 加载提示词
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
        except Exception as e:
            print(f"无法加载提示词文件: {e}")
            self.system_prompt = ""
    
    def _get_api_key(self, file_path):
        """从文件中获取API密钥"""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read().strip()
        else:
            raise FileNotFoundError(f"API密钥文件 '{file_path}' 未找到")
    
    def get_headers(self):
        """获取API请求头"""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def get_payload(self, query, model_override=None):
        """获取API请求载荷"""
        model = model_override if model_override else self.small_model
        return {
            "model": model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": query}
            ],
            "stream": True
        }
    
    def get_client(self):
        """获取OpenAI客户端"""
        from openai import OpenAI
        return OpenAI(
            base_url=self.api_base,
            api_key=self.api_key
        )
    
    def select_model_by_difficulty(self, difficulty):
        """根据难度选择模型"""
        difficulty = int(difficulty) if difficulty.isdigit() else 0
        if difficulty < self.threshold:
            return self.small_model
        else:
            return self.large_model


def load_config(config_path="config.yaml") -> Dict[str, Any]:
    """加载YAML配置文件
    
    参数:
        config_path: 配置文件路径
        
    返回:
        配置字典
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        print(f"无法加载配置文件 {config_path}: {e}")
        # 返回默认配置
        return {
            "models": {
                "small_model": "qwen/qwen3-14b:free",
                "large_model": "qwen/qwen3-235b-a22b",
                "router_model": "qwen/qwen-2.5-7b-instruct",
                "threshold": 2
            },
            "api": {
                "key_path": "usage/openrouter",
                "base_url": "https://openrouter.ai/api/v1"
            },
            "system": {
                "prompt_path": "prompt/generate_prompt.txt",
                "workers": 4,
                "enable_judge": False,
                "gold_answer": ""
            },
            "query": "What is the result of 1+1?",
            "dataset": {
                "enabled": False,
                "path": "dataset/original_data/math200.json",
                "limit": 10
            }
        }

def parse_args():
    """解析命令行参数，可覆盖配置文件中的设置"""
    parser = argparse.ArgumentParser(description='并行任务处理系统')
    parser.add_argument('--config', type=str, default="config.yaml",
                      help='配置文件路径')
    parser.add_argument('--dataset', action='store_true',
                      help='启用数据集处理模式')
    parser.add_argument('--dataset-path', type=str,
                      help='数据集文件路径')
    parser.add_argument('--dataset-limit', type=int,
                      help='处理数据集的最大问题数量')
    return parser.parse_args()
