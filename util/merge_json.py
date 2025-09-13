"""
合并两个JSON文件的工具脚本。
"""

import os
import sys
import argparse
from datetime import datetime
import ujson as json

# 导入项目中的io_file工具
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.io_file import read_json, write_json


def merge_json_files(file1, file2, output_file=None, format_type='list'):
    """
    合并两个JSON文件的内容

    参数:
    file1 (str): 第一个JSON文件路径
    file2 (str): 第二个JSON文件路径
    output_file (str, optional): 输出的JSON文件路径。如果未指定，将自动生成
    format_type (str): 数据格式类型，'list'表示列表格式，'dict'表示字典格式
    """
    try:
        # 读取两个JSON文件
        print(f"正在读取第一个JSON文件: {file1}")
        data1 = read_json(file1)
        
        print(f"正在读取第二个JSON文件: {file2}")
        data2 = read_json(file2)
        
        # 如果未指定输出文件，则自动生成文件名
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_dir = os.path.dirname(file1)
            output_file = os.path.join(base_dir, f"merged_data_{timestamp}.json")
        
        # 根据数据格式合并数据
        if format_type == 'list':
            # 列表格式合并
            if isinstance(data1, list) and isinstance(data2, list):
                merged_data = data1 + data2
            elif isinstance(data1, list):
                merged_data = data1 + [data2]
            elif isinstance(data2, list):
                merged_data = [data1] + data2
            else:
                merged_data = [data1, data2]
        else:
            # 字典格式合并
            if isinstance(data1, dict) and isinstance(data2, dict):
                merged_data = {**data1, **data2}
            else:
                raise ValueError("当format_type='dict'时，两个JSON文件都必须是字典格式")
        
        # 保存合并后的数据
        print(f"正在保存合并后的数据: {output_file}")
        write_json(output_file, merged_data)
        
        # 显示数据信息
        if isinstance(merged_data, list):
            print(f"合并完成! 输出文件: {output_file}")
            print(f"合并前文件1数据数量: {len(data1) if isinstance(data1, list) else 1}")
            print(f"合并前文件2数据数量: {len(data2) if isinstance(data2, list) else 1}")
            print(f"合并后数据总数量: {len(merged_data)}")
        else:
            print(f"合并完成! 输出文件: {output_file}")
            print(f"合并前文件1字段数量: {len(data1) if isinstance(data1, dict) else 0}")
            print(f"合并前文件2字段数量: {len(data2) if isinstance(data2, dict) else 0}")
            print(f"合并后字段总数量: {len(merged_data)}")
        
        return True
        
    except Exception as e:
        print(f"合并过程中出错: {str(e)}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='合并两个JSON文件')
    parser.add_argument('--file1', 
                        default='D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration\\dataset\\original_data\\AIME24.json',
                        help='第一个JSON文件路径')
    parser.add_argument('--file2', 
                        default='D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration\\dataset\\original_data\\AIME25.json', 
                        help='第二个JSON文件路径')
    parser.add_argument('-o', 
                        '--output', 
                        default='D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration\\dataset\\original_data\\AIME24_25.json', 
                        help='输出的JSON文件路径（可选）')
    parser.add_argument('--format', 
                        choices=['list', 'dict'], 
                        default='list',
                        help='数据格式类型，list表示列表格式，dict表示字典格式（默认: list）')
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.isfile(args.file1):
        print(f"错误: 文件不存在 - {args.file1}")
        sys.exit(1)
    
    if not os.path.isfile(args.file2):
        print(f"错误: 文件不存在 - {args.file2}")
        sys.exit(1)
    
    # 合并JSON文件
    result = merge_json_files(args.file1, args.file2, args.output, args.format)
    
    if not result:
        sys.exit(1)
