import json
import sys

# 输入输出文件路径
limo_path = r'dataset/generated_data/limo_training.json'
llama_path = r'dataset/llama_factory/s1k1_1_training_llama.json'
output_path = r'dataset/llama_factory/limo_training_llama.json'

def main():
    # 读取llama格式，获取system字段
    with open(llama_path, 'r', encoding='utf-8') as f:
        llama_data = json.load(f)
    if not llama_data or 'system' not in llama_data[0]:
        print('llama json格式异常或缺少system字段')
        sys.exit(1)
    system_str = llama_data[0]['system']

    # 读取limo格式
    with open(limo_path, 'r', encoding='utf-8') as f:
        limo_data = json.load(f)

    # 转换
    new_data = []
    for item in limo_data:
        new_item = {
            'instruction': item.get('question', ''),
            'input': '',
            'output': item.get('plan', ''),
            'system': system_str
        }
        new_data.append(new_item)

    # 写入新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    print(f'转换完成，输出文件: {output_path}')

if __name__ == '__main__':
    main()
