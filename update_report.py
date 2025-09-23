import os
import json
import re
from collections import defaultdict
import logging
import time
from tqdm import tqdm
import numpy as np

def setup_logging():
    """配置日志，同时输出到控制台和文件"""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"sync_report_{timestamp}.log")

    # 获取根logger并设置级别
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG) # 保证能捕获所有级别的日志

    # 避免重复添加handler
    if logger.hasHandlers():
        logger.handlers.clear()

    # 控制台处理器
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO) # 控制台只显示INFO及以上级别的重要信息
    ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(ch_formatter)

    # 文件处理器
    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setLevel(logging.DEBUG) # 文件日志记录所有DEBUG及以上级别的详细信息
    fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
    fh.setFormatter(fh_formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logging.getLogger(__name__)

logger = setup_logging()


def find_reports_to_update(root_dir):
    """查找所有符合条件的 dataset_report.md 文件。"""
    report_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'dataset_report.md' in filenames and 'dataset_results.json' in filenames and 'evaluation_reports' in dirnames:
            report_files.append(os.path.join(dirpath, 'dataset_report.md'))
    return report_files

def update_score_table(content, table_header_regex, avg_scores):
    """
    健壮地更新分数表：先移除旧的平均行，再更新维度分数，最后添加新的平均行。
    """
    table_match = re.search(table_header_regex, content, re.DOTALL)
    if not table_match:
        return content

    original_table_block = table_match.group(1)
    table_block = original_table_block

    # 1. 更新每个维度的分数
    for dim, score in avg_scores.items():
        dim_title = ' '.join(re.findall('[a-zA-Z][^A-Z]*', dim)).title()
        pattern = re.compile(rf"(\s*\|\s*{re.escape(dim_title)}\s*\|\s*)[\d\.]+")
        table_block = pattern.sub(f"\\g<1>{score:.2f}", table_block)

    # 2. (关键修复) 先移除所有旧的"平均表现"行，防止重复
    table_block = re.sub(r"\n?\s*\| \*\*平均表现\*\*.*\|", "", table_block)

    # 3. 计算并添加新的"平均表现"行
    overall_avg = np.mean(list(avg_scores.values()))
    avg_row_str = f"| **平均表现** | **{overall_avg:.2f}** |"
    
    # 将新行添加到表格末尾
    updated_table_block = table_block.strip() + f"\n{avg_row_str}"

    return content.replace(original_table_block, updated_table_block)


def update_report_file(report_path):
    """处理单个 report 文件，包含详细的日志和进度。"""
    logger.info(f"开始同步报告: {report_path}")
    base_dir = os.path.dirname(report_path)
    results_path = os.path.join(base_dir, 'dataset_results.json')
    eval_dir = os.path.join(base_dir, 'evaluation_reports')

    with open(results_path, 'r', encoding='utf-8') as f:
        results_data = json.load(f)
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 分数聚合，并带有详细进度 ---
    planner_scores = defaultdict(list)
    executor_scores = defaultdict(lambda: defaultdict(list))
    
    if os.path.exists(eval_dir):
        eval_files = [f for f in os.listdir(eval_dir) if f.startswith('evaluation_problem_') and f.endswith('.json')]
        logger.info(f"发现 {len(eval_files)} 个评估文件，开始聚合分数...")
        
        for filename in tqdm(eval_files, desc="聚合评估分数", leave=False):
            logger.debug(f"正在读取分数文件: {filename}")
            filepath = os.path.join(eval_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                eval_data = json.load(f)
                
                if eval_data.get('planner_report', {}).get('evaluationReport'):
                    for dim, values in eval_data['planner_report']['evaluationReport'].items():
                        if isinstance(values, dict) and 'score' in values:
                            try: planner_scores[dim].append(float(values['score']))
                            except (ValueError, TypeError): pass
                
                if eval_data.get('executor_reports'):
                    for report_data in eval_data['executor_reports'].values():
                        model_used = report_data.get('model_used')
                        if model_used and report_data.get('report', {}).get('evaluationReport'):
                            for dim, values in report_data['report']['evaluationReport'].items():
                                if isinstance(values, dict) and 'score' in values:
                                    try: executor_scores[model_used][dim].append(float(values['score']))
                                    except (ValueError, TypeError): pass
        logger.info("分数聚合完成。")
    else:
        logger.warning(f"评估目录未找到，跳过分数更新: {eval_dir}")

    # --- 1. 更新概述部分 ---
    total_problems = len(results_data)
    correct_count = sum(1 for item in results_data if item.get('is_correct'))
    accuracy = (correct_count / total_problems * 100) if total_problems > 0 else 0
    
    content = re.sub(r'(问题总数: )\d+', f'\\g<1>{total_problems}', content)
    content = re.sub(r'(正确数量: )\d+', f'\\g<1>{correct_count}', content)
    content = re.sub(r'(准确率: )[\d\.]+%?', f'\\g<1>{accuracy:.2f}%', content)

    # --- 2. 更新分数表格 ---
    if planner_scores:
        avg_planner_scores = {dim: np.mean(scores) for dim, scores in planner_scores.items()}
        logger.info(f"计算出的规划器平均分: {json.dumps(avg_planner_scores, indent=2)}")
        planner_header_regex = r"((?:### 规划器平均分数)[\s\S]*?\| --- \| --- \|(?:[\s\S]*?\|[\s\S]*?\|)*)"
        content = update_score_table(content, planner_header_regex, avg_planner_scores)

    for model, dims in executor_scores.items():
        if dims:
            avg_executor_scores = {dim: np.mean(scores) for dim, scores in dims.items()}
            logger.info(f"计算出的模型 '{model}' 平均分: {json.dumps(avg_executor_scores, indent=2)}")
            executor_header_regex = rf"((?:#### 模型: `{re.escape(model)}`)[\s\S]*?\| --- \| --- \|(?:[\s\S]*?\|[\s\S]*?\|)*)"
            content = update_score_table(content, executor_header_regex, avg_executor_scores)
            
    # --- 3. 更新详细结果表格 ---
    for i, item in enumerate(results_data):
        problem_num = i + 1
        is_correct_symbol = '✓' if item.get('is_correct') else '✗'
        pattern = re.compile(rf"(\| {problem_num}\s*\|.*?\|)\s*[✓✗]\s*\|")
        content = pattern.sub(f"\\g<1> {is_correct_symbol} |", content)

    # --- 保存更新后的内容 ---
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    logger.info(f"报告同步成功: {report_path}")

def main():
    """主函数，查找并更新所有相关报告。"""
    root_directory_to_process = os.path.join("data_reports", "dataset", "s1k_testPerformance")
    
    if not os.path.isdir(root_directory_to_process):
        logger.error(f"指定目录不存在: {root_directory_to_process}")
        return

    report_files = find_reports_to_update(root_directory_to_process)
    
    if not report_files:
        logger.warning(f"在 '{root_directory_to_process}' 中未找到需要更新的报告文件。")
        return

    for report_path in tqdm(report_files, desc="同步所有报告"):
        try:
            update_report_file(report_path)
        except Exception as e:
            logger.error(f"处理 {report_path} 时发生未知错误: {e}", exc_info=True)

if __name__ == "__main__":
    main()