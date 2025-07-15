#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
将处理好的数据转换为LLaMA-Factory格式的脚本
"""

import os
import sys
import argparse

# 将父目录添加到搜索路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.llama_factory import convert_to_llama_factory_format

def main():
    # 参数解析
    parser = argparse.ArgumentParser(description="将处理好的数据转换为LLaMA-Factory格式")
    parser.add_argument("--input_dir", type=str, default="../dataset/processed/limo", 
                        help="输入目录路径，包含处理好的JSON文件")
    parser.add_argument("--output_file", type=str, default="../dataset/dataset/limo_factory/llama_factory_data.json", 
                        help="输出文件路径")
    parser.add_argument("--format", type=str, choices=["llama", "alpaca"], default="llama", 
                        help="输出格式类型")
    
    args = parser.parse_args()
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    
    # 执行转换
    convert_to_llama_factory_format(args.input_dir, args.output_file, args.format)

if __name__ == "__main__":
    main()
