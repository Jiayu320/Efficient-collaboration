import pandas as pd
import os
import sys
import argparse

def convert_parquet_to_json(input_file, output_file=None, orient='records', lines=False):
    """
    将parquet文件转换为JSON格式
    
    参数:
    input_file (str): 输入的parquet文件路径
    output_file (str, optional): 输出的JSON文件路径。如果未指定，将使用与输入文件相同的名称，但扩展名为.json
    orient (str, optional): pandas to_json的orient参数。默认为'records'
    lines (bool, optional): 是否使用换行符分隔的JSON格式。默认为False
    """
    # 如果未指定输出文件，则根据输入文件名生成
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.json"
    
    try:
        # 读取parquet文件
        print(f"正在读取文件: {input_file}")
        df = pd.read_parquet(input_file)
        
        # 将数据转换为JSON并保存
        print(f"正在将数据保存为JSON: {output_file}")
        df.to_json(output_file, orient=orient, force_ascii=False, lines=lines)
        
        print(f"转换完成! 输出文件: {output_file}")
        print(f"数据行数: {len(df)}")
        
    except Exception as e:
        print(f"转换过程中出错: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将parquet文件转换为JSON格式')
    parser.add_argument('input_file', nargs='?', default="D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration\\dataset\\original_data\\livebench-reasoning\\test-00000-of-00001.parquet", help='输入的parquet文件路径')
    parser.add_argument('-o', '--output', default="D:\\JIAYU\\Documents\\GitHub\\Efficient-collaboration\\dataset\\original_data\\livebench-reasoning.json", help='输出的JSON文件路径（可选）')
    parser.add_argument('--orient', default='records',
                        help='JSON格式方向，可选值: split, records, index, columns, values（默认: records）')
    parser.add_argument('--lines', action='store_true', 
                        help='是否使用换行符分隔的JSON格式（适用于大文件）')
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input_file):
        print(f"错误: 找不到输入文件 '{args.input_file}'")
        sys.exit(1)
    
    # 执行转换
    success = convert_parquet_to_json(args.input_file, args.output, args.orient, args.lines)
    sys.exit(0 if success else 1)
