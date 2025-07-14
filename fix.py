"""
修复数据处理中可能出现的缺失值问题

这个脚本用于检测process_data.py生成的结果中是否有缺失的字段，如果有则调用相应函数重新处理。
主要修复以下问题：
1. difficulties 为空
2. summaries 为空
3. relations 为空
4. 字段中包含API错误信息(如令牌额度已用尽、错误代码等)
5. 组编号不连续(例如缺少某些group编号)
"""

import json
import os
import time
import concurrent.futures
import traceback
from tqdm import tqdm
from util.io_file import read_json, write_json
from process_data import generate_cot_summary, rate_cot_difficulty, analyzing_step_dependencies, convert_group_results_to_dict, analyze_group_results

def check_and_fix_file(file_path, api_key=None, analysis_model="gpt-4"):
    """
    检查并修复单个文件中的缺失数据
    
    参数:
        file_path: JSON文件路径
        api_key: API密钥（可选）
        analysis_model: 模型的版本号（可选）
    
    返回:
        修复状态和消息的元组
    """
    try:
        print(f"正在检查文件: {file_path}")
        data = read_json(file_path)
        
        # 确保是列表格式
        if isinstance(data, dict):
            data = [data]
            
        item = data[0]  # 假设每个文件只包含一个问题
        
        if "analysis" not in item:
            return False, f"文件 {file_path} 缺少 analysis 字段，无法修复"
        
        analysis = item["analysis"]
        question = item.get("question", "")
        sentence_groups = analysis.get("sentence_groups", {})
        
        if not sentence_groups:
            return False, f"文件 {file_path} 缺少 sentence_groups 数据，无法修复"
            
        fixes_applied = []
        needs_saving = False
        
        # 检查是否有带有错误信息的字段需要修复
        found_error = False
        discontinuity_found = False
        
        # 检查 difficulties 字段是否有错误信息
        if "difficulties" in analysis and isinstance(analysis["difficulties"], dict):
            for key, value in list(analysis["difficulties"].items()):
                if isinstance(value, str) and ("出错" in value.lower() or "额度已用尽" in value):
                    print(f"发现错误信息在difficulties字段: {value}")
                    analysis["difficulties"] = {}  # 清空错误数据
                    found_error = True
                    break
        
        # 检查 summaries 字段是否有错误信息
        if "summaries" in analysis and isinstance(analysis["summaries"], dict):
            for key, value in list(analysis["summaries"].items()):
                if isinstance(value, str) and ("出错" in value.lower() or "额度已用尽" in value):
                    print(f"发现错误信息在summaries字段: {value}")
                    analysis["summaries"] = {}  # 清空错误数据
                    found_error = True
                    break
        
        # 检查 relations 字段是否有错误信息
        if "relations" in analysis and isinstance(analysis["relations"], dict):
            for key, value in list(analysis["relations"].items()):
                if isinstance(value, str) and ("出错" in value.lower() or "额度已用尽" in value):
                    print(f"发现错误信息在relations字段: {value}")
                    analysis["relations"] = {}  # 清空错误数据
                    found_error = True
                    break
            # 特别检查grouperror类型的键
            if "grouperror" in analysis["relations"]:
                print(f"发现grouperror在relations字段: {analysis['relations']['grouperror']}")
                analysis["relations"] = {}
                found_error = True

        # 检查组编号是否连续
        if "summaries" in analysis and isinstance(analysis["summaries"], dict) and len(analysis["summaries"]) > 1:
            group_nums = []
            for key in analysis["summaries"].keys():
                if key.startswith("group") and key[5:].isdigit():
                    group_nums.append(int(key[5:]))
            
            if group_nums:
                group_nums.sort()
                expected_groups = list(range(1, max(group_nums) + 1))
                missing_groups = [num for num in expected_groups if num not in group_nums]
                
                if missing_groups:
                    print(f"发现summaries字段组编号不连续，缺少组: {missing_groups}")
                    discontinuity_found = True
                    analysis["summaries"] = {}  # 清空以便重新生成
        
        # 同样检查difficulties字段的组编号连续性
        if "difficulties" in analysis and isinstance(analysis["difficulties"], dict) and len(analysis["difficulties"]) > 1:
            group_nums = []
            for key in analysis["difficulties"].keys():
                if key.startswith("group") and key[5:].isdigit():
                    group_nums.append(int(key[5:]))
            
            if group_nums:
                group_nums.sort()
                expected_groups = list(range(1, max(group_nums) + 1))
                missing_groups = [num for num in expected_groups if num not in group_nums]
                
                if missing_groups:
                    print(f"发现difficulties字段组编号不连续，缺少组: {missing_groups}")
                    discontinuity_found = True
                    analysis["difficulties"] = {}  # 清空以便重新生成
        
        # 同样检查relations字段的组编号连续性
        if "relations" in analysis and isinstance(analysis["relations"], dict) and len(analysis["relations"]) > 1:
            group_nums = []
            for key in analysis["relations"].keys():
                if key.startswith("group") and key[5:].isdigit():
                    group_nums.append(int(key[5:]))
            
            if group_nums:
                group_nums.sort()
                expected_groups = list(range(1, max(group_nums) + 1))
                missing_groups = [num for num in expected_groups if num not in group_nums]
                
                if missing_groups:
                    print(f"发现relations字段组编号不连续，缺少组: {missing_groups}")
                    discontinuity_found = True
                    analysis["relations"] = {}  # 清空以便重新生成
        
        # 如果找到错误信息或不连续性，将相应字段置空，以便后续重新处理
        if found_error:
            needs_saving = True
            fixes_applied.append("错误信息")
            
        if discontinuity_found:
            needs_saving = True
            fixes_applied.append("不连续编号")

        # 检查并修复 difficulties 字段
        if "difficulties" not in analysis or not analysis["difficulties"]:
            print(f"正在修复 {file_path} 的 difficulties 字段")
            try:
                group_difficulty = rate_cot_difficulty(question, sentence_groups, api_key, analysis_model)
                if group_difficulty:
                    # 先进行解析
                    group_summary = analysis.get("summaries", {})
                    # 将 summaries 转换回格式化的字符串以供 analyze_group_results 使用
                    summary_str = "\n".join([f"* Group {k.replace('group', '')}: {v}" for k, v in group_summary.items()])
                    group_results = analyze_group_results(summary_str, group_difficulty)
                    
                    # 获取当前的 relations
                    current_relations = analysis.get("relations", {})
                    
                    # 只更新 difficulties 部分
                    formatted_results = convert_group_results_to_dict(group_results, current_relations)
                    analysis["difficulties"] = formatted_results["difficulties"]
                    needs_saving = True
                    fixes_applied.append("difficulties")
                    time.sleep(1)
            except Exception as e:
                print(f"修复 difficulties 失败: {str(e)}")
        
        # 检查并修复 summaries 字段
        if "summaries" not in analysis or not analysis["summaries"]:
            print(f"正在修复 {file_path} 的 summaries 字段")
            try:
                group_summary = generate_cot_summary(question, sentence_groups, api_key, analysis_model)
                if group_summary:
                    # 如果有 difficulties，使用它来生成完整的结果
                    group_difficulty = ""
                    if "difficulties" in analysis and analysis["difficulties"]:
                        difficulties_dict = analysis["difficulties"]
                        group_difficulty = "\n".join([f"Group {k.replace('group', '')}: {v}" for k, v in difficulties_dict.items()])
                    
                    group_results = analyze_group_results(group_summary, group_difficulty)
                    
                    # 获取当前的 relations
                    current_relations = analysis.get("relations", {})
                    
                    # 只更新 summaries 部分
                    formatted_results = convert_group_results_to_dict(group_results, current_relations)
                    analysis["summaries"] = formatted_results["summaries"]
                    needs_saving = True
                    fixes_applied.append("summaries")
                    time.sleep(1)
            except Exception as e:
                print(f"修复 summaries 失败: {str(e)}")
        
        # 检查并修复 relations 字段
        if "relations" not in analysis or not analysis["relations"]:
            print(f"正在修复 {file_path} 的 relations 字段")
            try:
                group_relations = analyzing_step_dependencies(question, sentence_groups, api_key, analysis_model)
                if group_relations:
                    analysis["relations"] = group_relations
                    needs_saving = True
                    fixes_applied.append("relations")
                    time.sleep(1)
            except Exception as e:
                print(f"修复 relations 失败: {str(e)}")
        
        # 如果有修复，保存回原文件
        if needs_saving:
            write_json(file_path, data)
            return True, f"已修复字段: {', '.join(fixes_applied)}"
        else:
            return True, "文件无需修复"
            
    except Exception as e:
        error_msg = f"处理文件 {file_path} 时出错: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return False, error_msg

def process_directory(input_dir, api_key=None, max_workers=4, analysis_model="deepseek-ai/DeepSeek-R1"):
    """
    处理目录中的所有JSON文件，检查并修复缺失数据
    
    参数:
        input_dir: 输入目录路径
        api_key: API密钥（可选）
        max_workers: 最大并行处理线程数
        analysis_model: 模型的版本号（可选）
    
    返回:
        修复成功和失败的文件列表
    """
    # 获取所有JSON文件
    json_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) 
                 if os.path.isfile(os.path.join(input_dir, f)) and f.endswith('.json')]
    
    print(f"找到 {len(json_files)} 个文件待检查")
    
    successful_files = []
    failed_files = []
    
    # 使用线程池并行处理文件
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 创建一个字典，将每个未来的结果与其文件路径关联起来
        future_to_file = {executor.submit(check_and_fix_file, file_path, api_key, analysis_model): file_path for file_path in json_files}
        
        # 使用tqdm显示进度
        for future in tqdm(concurrent.futures.as_completed(future_to_file), total=len(json_files), desc="修复进度"):
            file_path = future_to_file[future]
            try:
                success, message = future.result()
                if success:
                    successful_files.append((file_path, message))
                else:
                    failed_files.append((file_path, message))
            except Exception as e:
                failed_files.append((file_path, str(e)))
    
    # 打印处理结果
    print(f"\n成功处理 {len(successful_files)} 个文件, 失败 {len(failed_files)} 个文件")
    
    if failed_files:
        print("\n失败的文件:")
        for file_path, message in failed_files:
            print(f"- {file_path}: {message}")
    
    return successful_files, failed_files

def get_api_key(file_path="together_ai"):
    """
    从文件获取API密钥
    """
    try:
        with open(file_path, "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"无法读取API密钥: {str(e)}")
        return None

def fix_failed_files(stats_file_path, api_key=None, max_workers=4, analysis_model="deepseek-reasoner"):
    """
    针对processing_stats.json中的失败文件列表进行重新处理
    
    参数:
        stats_file_path: processing_stats.json文件路径
        api_key: API密钥（可选）
        max_workers: 最大并行处理线程数
        analysis_model: 模型的版本号（可选）
    
    返回:
        修复成功和失败的文件列表
    """
    try:
        # 读取processing_stats.json文件
        with open(stats_file_path, "r", encoding="utf-8") as f:
            stats_data = json.load(f)
        
        failed_files = stats_data.get("failed_file_paths", [])
        
        if not failed_files:
            print("未找到失败的文件记录")
            return [], []
        
        print(f"从{stats_file_path}中找到{len(failed_files)}个失败文件待修复")
        
        # 规范化文件路径
        normalized_files = []
        for file_path in failed_files:
            # 将路径中的正斜杠替换为反斜杠(如果在Windows系统上)
            normalized_path = file_path.replace("/", os.sep).replace("\\\\", os.sep)
            normalized_files.append(normalized_path)
        
        successful_files = []
        still_failed_files = []
        
        # 使用线程池并行处理文件
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 创建一个字典，将每个未来的结果与其文件路径关联起来
            future_to_file = {executor.submit(check_and_fix_file, file_path, api_key, analysis_model): file_path for file_path in normalized_files}
            
            # 使用tqdm显示进度
            for future in tqdm(concurrent.futures.as_completed(future_to_file), total=len(normalized_files), desc="修复失败文件"):
                file_path = future_to_file[future]
                try:
                    success, message = future.result()
                    if success:
                        successful_files.append((file_path, message))
                    else:
                        still_failed_files.append((file_path, message))
                except Exception as e:
                    still_failed_files.append((file_path, str(e)))
        
        # 打印处理结果
        print(f"\n成功修复 {len(successful_files)} 个文件, 仍然失败 {len(still_failed_files)} 个文件")
        
        if still_failed_files:
            print("\n仍然失败的文件:")
            for file_path, message in still_failed_files:
                print(f"- {file_path}: {message}")
        
        # 更新stats文件中的失败文件列表
        if successful_files:
            repaired_paths = [path for path, _ in successful_files]
            stats_data["failed_file_paths"] = [path for path in stats_data["failed_file_paths"] 
                                               if path.replace("/", os.sep).replace("\\\\", os.sep) not in repaired_paths]
            stats_data["successful_files"] = stats_data.get("successful_files", 0) + len(successful_files)
            stats_data["failed_files"] = stats_data.get("failed_files", 0) - len(successful_files)
            
            # 写回stats文件
            with open(stats_file_path, "w", encoding="utf-8") as f:
                json.dump(stats_data, f, indent=4, ensure_ascii=False)
            
            print(f"\n已更新{stats_file_path}文件中的统计信息")
        
        return successful_files, still_failed_files
    except Exception as e:
        error_msg = f"处理失败文件列表时出错: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return [], [(stats_file_path, error_msg)]

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="检查并修复处理数据中的缺失值")
    parser.add_argument("--input_dir", type=str, default="data\\structure\\limo_out", help="输入目录，包含需要检查的JSON文件")
    parser.add_argument("--api_key_file", type=str, default="deepseek", help="API密钥文件")
    parser.add_argument("--max_workers", type=int, default=4, help="最大并行处理线程数")
    parser.add_argument("--model", type=str, default="deepseek-reasoner", help="分析模型名称")
    parser.add_argument("--fix_failed", default="data\\training\\processing_stats.json", type=str, help="修复processing_stats.json中记录的失败文件")

    args = parser.parse_args()
    
    # 获取API密钥
    api_key = get_api_key(args.api_key_file)
    
    if args.fix_failed:
        # 修复失败文件列表
        fix_failed_files(args.fix_failed, api_key, args.max_workers, args.model)
    else:
        # 处理目录
        process_directory(args.input_dir, api_key, args.max_workers, args.model)
