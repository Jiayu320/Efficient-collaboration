import json
import os
import networkx as nx
import concurrent.futures
import traceback
import time
from collections import defaultdict, deque
import transformers
from util.io_file import read_json, write_json

import tqdm as tqdm

def count_tokens_in_group(group_sentences, tokenizer):
    """
    计算一个组中所有句子的token数量
    
    Args:
        group_sentences: 组中的句子列表
        tokenizer: 用于分词的tokenizer
        
    Returns:
        int: 该组的估计token数量
    """
    tokenizer = transformers.AutoTokenizer.from_pretrained(tokenizer)
    total_tokens = 0
    for sentence in group_sentences:
        if not sentence:
            continue
        tokens = tokenizer(sentence).input_ids
        total_tokens += len(tokens)
    return total_tokens

def create_dag_from_relations(relations):
    """
    从依赖关系字典创建有向无环图(DAG)，并进行传递约简
    
    Args:
        relations: 依赖关系字典
    
    Returns:
        networkx DiGraph对象
    """
    G = nx.DiGraph()
    
    # 收集所有节点并构建边
    for node, dependencies in relations.items():
        if not G.has_node(node):
            G.add_node(node)
        for dep in dependencies:
            G.add_edge(dep, node)  # 依赖指向节点
    
    # 执行传递约简，去除冗余边
    try:
        reduced_G = nx.transitive_reduction(G)
        return reduced_G
    except:
        # 如果图中有环，传递约简可能会失败
        return G

def calculate_depth(relations):
    """
    计算每个组的深度和获得最终结果所需的总步数
    
    Args:
        relations: 依赖关系字典
    
    Returns:
        depths: 每个组的深度字典
        total_steps: 到达最后一组所需的总步数
    """
    # 创建DAG并进行传递约简
    G = create_dag_from_relations(relations)
    
    # 提取边列表
    edges = list(G.edges())
    
    # 初始化入度字典和邻接表
    in_degree = defaultdict(int)
    adjacency_list = defaultdict(list)
    
    nodes = set(G.nodes())
    
    # 填充邻接表和计算入度
    for u, v in edges:
        adjacency_list[u].append(v)
        in_degree[v] += 1
    
    # 找出所有入度为0的节点（根节点）
    queue = deque([node for node in nodes if in_degree[node] == 0])
    depths = {node: 0 for node in queue}  # 根节点深度为0
    
    # 广度优先搜索计算深度
    while queue:
        node = queue.popleft()
        current_depth = depths[node]
        
        for neighbor in adjacency_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                # 更新为最大深度
                depths[neighbor] = current_depth + 1
    
    # 为所有没有被赋值深度的节点设置默认值
    for node in nodes:
        if node not in depths:
            # 可能存在的环或者孤立节点
            depths[node] = 0
    
    # 找出最大深度，即总步数（+1 因为最小深度为0）
    total_steps = max(depths.values()) + 1 if depths else 0
    
    return depths, total_steps

def analyze_json_file(file_path, tokenizer):
    """
    分析单个JSON文件并更新其中的深度和token信息

    Args:
        file_path: JSON文件路径
        tokenizer: 分词器名称
    """
    try:
        # 读取JSON文件
        data = read_json(file_path)
        
        # 确保必要的字段存在
        if 'analysis' not in data or 'relations' not in data['analysis'] or 'sentence_groups' not in data['analysis']:
            print(f"文件 {file_path} 缺少必要的字段")
            return False
        
        # 计算每个组的深度和总步数
        depths, total_steps = calculate_depth(data['analysis']['relations'])
        
        # 将深度转换为整数
        depths = {k: int(v) for k, v in depths.items()}
        # 将深度和总步数添加到分析中
        sorted_depths = {k: v for k, v in sorted(depths.items(), 
                             key=lambda item: int(item[0].replace('group', ''))
                             if item[0].startswith('group') and item[0][5:].isdigit()
                             else float('inf'))}
        data['analysis']['depth'] = sorted_depths
        data['analysis']['total_steps'] = total_steps
        total_groups = len(data['analysis']['sentence_groups'])
        data['analysis']['compression_ratio'] = total_steps / total_groups if total_groups > 0 else 0

        # 计算每个组的token数量
        groups_token = {}
        for group_id, sentences in data['analysis']['sentence_groups'].items():
            groups_token[group_id] = count_tokens_in_group(sentences, tokenizer)
        
        # 将token数量添加到分析中
        data['analysis']['groups_token'] = groups_token
        
        # 保存更新后的JSON文件
        write_json(file_path, data)
        return True, data['analysis']['compression_ratio']
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {str(e)}")
        traceback.print_exc()
        return False, 0

def process_directory(args):
    """
    处理目录中的所有JSON文件
    
    Args:
        directory_path: 目录路径
    """
    # 获取目录中所有JSON文件
    directory_path = args.dir
    json_files = []
    error_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json') and file[:-5].isdigit():
                json_files.append(os.path.join(root, file))
    
    print(f"找到 {len(json_files)} 个JSON文件")
    
    avg_compression_ratio = 0
    # 使用线程池并行处理文件
    success_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(analyze_json_file, file_path, args.tokenizer): file_path for file_path in json_files}
        
        # 使用tqdm显示进度条
        for future in tqdm.tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="处理文件"):
            file_path = futures[future]
            try:
                success, compression_ratio = future.result()
                if success:
                    success_count += 1
                    avg_compression_ratio += compression_ratio
            except Exception as e:
                print(f"处理文件 {file_path} 时出错: {str(e)}")
                error_files.append(file_path)
                traceback.print_exc()
    stats = {
        'total_files': len(json_files),
        'success_count': success_count,
        'error_files': error_files,
        'avg_compression_ratio': avg_compression_ratio / success_count if success_count > 0 else 0
    }
    write_json(os.path.join(directory_path, 'analysis_stats.json'), stats)
    print(f"成功处理 {success_count}/{len(json_files)} 个文件")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='分析JSON文件中的依赖关系')
    parser.add_argument('--dir', type=str, default='data/structure/claude_out', help='要处理的目录路径')
    parser.add_argument('--file', type=str, default=None, help='要处理的单个文件路径')
    parser.add_argument('--tokenizer',  type=str, default='Qwen/Qwen2.5-Math-1.5B', help='分词器名称')
    args = parser.parse_args()
    start_time = time.time()
    
    if args.file:
        # 处理单个文件
        print(f"处理文件: {args.file}")
        success, _ = analyze_json_file(args.file, args.tokenizer)
        print(f"处理{'成功' if success else '失败'}")
    else:
        # 处理整个目录
        print(f"处理目录: {args.dir}")
        process_directory(args)
    
    end_time = time.time()
    print(f"总耗时: {end_time - start_time:.2f} 秒")

if __name__ == "__main__":
    main()

