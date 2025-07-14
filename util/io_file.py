"""读写 json/jsonl 文件的工具函数。
"""

import ujson as json


def read_json(file_path):
    """
    读取 json 文件。
    参数：
        file_path (str): 文件路径。
    返回：
        data (dict): 读取到的 json 数据。
    """
    # print("reading")
    with open(file_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def write_json(file_path, data):
    """
    写入 json 文件。
    参数：
        file_path (str): 文件路径。
        data (dict): 需要写入的 json 数据。
    """
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def read_jsonl(file_path):
    """
    读取 jsonl 文件。
    参数：
        file_path (str): 文件路径。
    返回：
        data (list): 读取到的 jsonl 数据，每行为一个 dict。
    """
    data = []
    with open(file_path, "r", encoding="UTF-8") as f:
        for line in f:
            # print(line)
            data.append(json.loads(line))

    return data


def write_jsonl(file_path, data):
    """
    写入 jsonl 文件。
    参数：
        file_path (str): 文件路径。
        data (list): 需要写入的 jsonl 数据，每个元素为一行 dict。
    """
    with open(file_path, "w", encoding="UTF-8") as f:
        for line in data:
            json.dump(line, f)
            f.write("\n")

if __name__=="__main__":
    pass