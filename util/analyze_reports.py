import os
import json
import datetime
import numpy as np # 引入 numpy 库用于统计计算

def parse_markdown_report(file_path):
    """
    解析 Markdown 报告文件，从'详细结果'表格中提取压缩比例。
    (此函数与上一版本相同)
    """
    compression_stats = {'correct': [], 'incorrect': []}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return compression_stats

    in_results_table = False
    header_found = False
    correct_col_idx = -1
    ratio_col_idx = -1

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        if "## 详细结果" in line_stripped:
            in_results_table = True
            continue
        if in_results_table and not header_found and line_stripped.startswith('| # |'):
            headers = [h.strip() for h in line_stripped.split('|') if h.strip()]
            try:
                correct_col_idx = headers.index('正确?')
                ratio_col_idx = headers.index('压缩比例')
                header_found = True
            except ValueError:
                break
            continue
        if in_results_table and header_found and line_stripped.startswith('|') and not line_stripped.startswith('| ---'):
            parts = [p.strip() for p in line_stripped.split('|')]
            if len(parts) > max(correct_col_idx + 1, ratio_col_idx + 1):
                is_correct_str = parts[correct_col_idx + 1]
                ratio_str = parts[ratio_col_idx + 1]
                if '%' in ratio_str:
                    try:
                        ratio_value = float(ratio_str.replace('%', '').strip())
                        if '✓' in is_correct_str:
                            compression_stats['correct'].append(ratio_value)
                        elif '✗' in is_correct_str:
                            compression_stats['incorrect'].append(ratio_value)
                    except (ValueError, IndexError):
                        continue
    return compression_stats

def calculate_detailed_statistics(data_list):
    """
    使用 numpy 计算数据集的详细统计信息。
    """
    if not data_list:
        return {
            "count": 0, "mean": "N/A", "std": "N/A", "min": "N/A",
            "p25": "N/A", "median": "N/A", "p75": "N/A", "max": "N/A"
        }
    
    # 将列表转换为 numpy 数组
    np_array = np.array(data_list)
    
    return {
        "count": len(np_array),
        "mean": f"{np.mean(np_array):.2f}",
        "std": f"{np.std(np_array):.2f}",
        "min": f"{np.min(np_array):.2f}",
        "p25": f"{np.percentile(np_array, 25):.2f}", # 25% 分位数
        "median": f"{np.median(np_array):.2f}",      # 中位数 (50%)
        "p75": f"{np.percentile(np_array, 75):.2f}", # 75% 分位数
        "max": f"{np.max(np_array):.2f}"
    }

def analyze_data_and_reports_detailed(root_directory):
    """
    分析数据并生成包含详细统计指标的最终报告。
    """
    # 初始化列表以收集所有数据点
    correct_steps_list = []
    incorrect_steps_list = []
    correct_ratios_list = []
    incorrect_ratios_list = []

    processed_json_count = 0
    processed_md_count = 0

    for subdir, _, files in os.walk(root_directory):
        if 'dataset_results.json' in files:
            processed_json_count += 1
            json_path = os.path.join(subdir, 'dataset_results.json')
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data:
                        is_correct = item.get('is_correct')
                        total_tasks = item.get('total_tasks_num')
                        if total_tasks is not None:
                            if is_correct is True:
                                correct_steps_list.append(total_tasks)
                            elif is_correct is False:
                                incorrect_steps_list.append(total_tasks)
            except Exception as e:
                print(f"处理文件 '{json_path}' 时出错：{e}")

            md_path = os.path.join(subdir, 'dataset_report.md')
            if os.path.exists(md_path):
                processed_md_count += 1
                md_stats = parse_markdown_report(md_path)
                correct_ratios_list.extend(md_stats['correct'])
                incorrect_ratios_list.extend(md_stats['incorrect'])

    # --- 计算所有收集到数据的详细统计信息 ---
    stats_correct_steps = calculate_detailed_statistics(correct_steps_list)
    stats_incorrect_steps = calculate_detailed_statistics(incorrect_steps_list)
    stats_correct_ratios = calculate_detailed_statistics(correct_ratios_list)
    stats_incorrect_ratios = calculate_detailed_statistics(incorrect_ratios_list)

    # --- 辅助函数：生成报告的统计部分 ---
    def format_stats_block(stats, unit=""):
        if stats["count"] == 0:
            return "  - 总数: 0\n  - *无可用数据进行统计*"
        return (
            f"  - **总数:** {stats['count']}\n"
            f"  - **平均值:** {stats['mean']}{unit}\n"
            f"  - **标准差:** {stats['std']}{unit}\n"
            f"  - **最小值:** {stats['min']}{unit}\n"
            f"  - **分布情况:**\n"
            f"    - *25%分位数:* {stats['p25']}{unit}\n"
            f"    - *中位数 (50%):* {stats['median']}{unit}\n"
            f"    - *75%分位数:* {stats['p75']}{unit}\n"
            f"  - **最大值:** {stats['max']}{unit}"
        )

    # --- 生成最终的 Markdown 报告 ---
    report_content = f"""# 综合分析报告 (详细版)

**报告生成时间:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 概述

- **扫描目录:** `{root_directory}`
- **已处理 JSON 文件数量:** `{processed_json_count}`
- **已处理 Markdown 报告数量:** `{processed_md_count}`

---

## 统计结果

### 1. 任务步骤数分析 (来自 `dataset_results.json`)

#### ✅ 回答正确的情况
{format_stats_block(stats_correct_steps)}

#### ❌ 回答错误的情况
{format_stats_block(stats_incorrect_steps)}

---

### 2. 任务压缩比例分析 (来自 `dataset_report.md`)

#### ✅ 回答正确的情况
{format_stats_block(stats_correct_ratios, unit="%")}

#### ❌ 回答错误的情况
{format_stats_block(stats_incorrect_ratios, unit="%")}
"""

    report_file_path = os.path.join(root_directory, 'analysis_report_detailed.md')
    try:
        with open(report_file_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        print(f"\n详细报告生成成功！已保存至: {report_file_path}")
    except Exception as e:
        print(f"写入详细报告文件时出错：{e}")

# --- 使用说明 ---
if __name__ == '__main__':
    # 确保已安装 numpy: pip install numpy
    # 请在这里设置您的目标文件夹路径
    target_directory = r'D:\JIAYU\Documents\GitHub\Efficient-collaboration\data_reports\dataset\MMLU-STEM\qwen3-0.6b'
    
    if os.path.isdir(target_directory):
        analyze_data_and_reports_detailed(target_directory)
    else:
        print(f"错误：提供的路径 '{target_directory}' 不是一个有效的目录。")