import os
import json
import re
import requests
import time
import argparse
import random
import glob
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# API配置
API_BASE_URL = "https://api.deepseek.com"
TIMEOUT = 60

# 指定使用的模型
MODEL_NAME = "deepseek-chat"

class ApiKeyManager:
    """API密钥管理器，用于在多个API密钥之间轮换"""
    def __init__(self, key_dir="usage"):
        self.key_dir = key_dir
        self.api_keys = []
        self.current_index = 0
        self.load_all_keys()
        
    def load_all_keys(self):
        """加载所有API密钥"""
        # 查找key_dir目录下的所有deepseek*文件
        key_files = glob.glob(os.path.join(self.key_dir, "deepseek*"))
        self.api_keys = []
        
        for key_file in key_files:
            try:
                with open(key_file, 'r') as f:
                    key = f.read().strip()
                    if key:
                        self.api_keys.append(key)
            except Exception as e:
                print(f"加载API密钥 {key_file} 时出错: {e}")
                
        print(f"加载了 {len(self.api_keys)} 个DeepSeek API密钥")
        if not self.api_keys:
            raise ValueError("没有找到DeepSeek API密钥，请确保usage目录下有deepseek*文件")
            
    def get_next_key(self):
        """获取下一个API密钥"""
        if not self.api_keys:
            raise ValueError("没有可用的API密钥")
            
        key = self.api_keys[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.api_keys)
        return key
        
    def get_random_key(self):
        """随机获取一个API密钥"""
        if not self.api_keys:
            raise ValueError("没有可用的API密钥")
            
        return random.choice(self.api_keys)

def load_api_key(key_path):
    """从指定文件中加载API密钥"""
    try:
        with open(key_path, 'r') as f:
            return f.read().strip()
    except Exception as e:
        print(f"加载API密钥时出错: {e}")
        return None

def extract_final_answer(solution_text):
    """从模型输出文本中提取最终答案"""
    
    return solution_text

def verify_answer(gold_solution, model_answer, api_key):
    """调用DeepSeek API验证模型答案是否与标准答案一致"""
    prompt = f"""
Here is a standard answer and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.

Standard answer: {gold_solution}

Answer: {model_answer}

If the student's answer is correct, just output True; otherwise, just output False.
No explanation is required.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.post(
                API_BASE_URL + "/v1/chat/completions", 
                headers=headers,
                json=data,
                timeout=TIMEOUT
            )
            response.raise_for_status()
            result = response.json()
            
            # 提取API响应中的判断结果
            judge_text = result["choices"][0]["message"]["content"].strip()
            
            # 提取True/False判断
            is_correct = "True" in judge_text[:10]  # 假设判断结果在开头
            
            return {
                "is_correct": is_correct,
                "judge_result": judge_text,
                "model_used": MODEL_NAME
            }
        except Exception as e:
            # 如果不是最后一次尝试，则等待并重试
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 3  # 指数退避，更长的等待时间
                print(f"API调用出错: {e}，{wait_time}秒后重试...")
                time.sleep(wait_time)
            else:
                print(f"API调用失败，已达到最大重试次数: {e}")
                return {"is_correct": False, "judge_result": f"API错误: {str(e)}", "model_used": MODEL_NAME}

def process_result_file(file_path, key_manager):
    """处理单个结果文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = False
        correct_to_wrong = 0
        wrong_to_correct = 0
        api_call_count = 0  # 记录API调用次数
        
        for item in data:
            gold_solution = item.get("gold_solution")
            model_solution = item.get("model_solution")
            
            if not gold_solution or not model_solution:
                continue
                
            # 从模型输出中提取最终答案
            model_answer = extract_final_answer(model_solution)
            if not model_answer:
                continue
            
            # 获取一个API密钥
            api_key = key_manager.get_random_key()
                
            # 调用API验证答案
            result = verify_answer(gold_solution, model_answer, api_key)
            api_call_count += 1
            
            # 更新结果并跟踪变化情况
            if item.get("is_correct") != result["is_correct"] or item.get("judge_result") != result["judge_result"]:
                # 记录从正确变为错误或从错误变为正确的情况
                if item.get("is_correct") == True and result["is_correct"] == False:
                    correct_to_wrong += 1
                elif item.get("is_correct") == False and result["is_correct"] == True:
                    wrong_to_correct += 1
                
                item["is_correct"] = result["is_correct"]
                item["judge_result"] = result["judge_result"]
                item["verification_model"] = MODEL_NAME  # 记录用于验证的模型
                updated = True
                
            # 适当延迟，避免API请求过快
            time.sleep(1)
        
        # 如果有更新，保存文件
        if updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            # 更新报告文件
            report_path = os.path.join(os.path.dirname(file_path), "dataset_report.md")
            if os.path.exists(report_path):
                update_report(report_path, data)
            
            # 打印API调用次数
            print(f"文件 {os.path.basename(file_path)} 的API调用次数: {api_call_count}次")
                
        return updated, correct_to_wrong, wrong_to_correct
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False, 0, 0

def update_report(report_path, data):
    """更新报告文件中的准确率等统计信息"""
    try:
        # 读取原报告内容
        with open(report_path, 'r', encoding='utf-8') as f:
            report_content = f.read()
            
        # 计算新的统计数据
        total = len(data)
        correct = sum(1 for item in data if item.get("is_correct", False))
        accuracy = (correct / total) * 100 if total > 0 else 0
        
        # 更新报告中的统计信息
        report_content = re.sub(
            r"- 问题总数: \d+\n- 正确数量: \d+\n- 准确率: \d+\.\d+%", 
            f"- 问题总数: {total}\n- 正确数量: {correct}\n- 准确率: {accuracy:.2f}%", 
            report_content
        )
        
        # 保存更新后的报告
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
    except Exception as e:
        print(f"更新报告 {report_path} 时出错: {e}")

def find_all_result_files(base_dir):
    """查找所有的dataset_results.json文件"""
    result_files = []
    for root, dirs, files in os.walk(base_dir):
        if "dataset_results.json" in files:
            result_files.append(os.path.join(root, "dataset_results.json"))
    return result_files

def main():
    parser = argparse.ArgumentParser(description="验证模型判断结果")
    parser.add_argument("--key_dir", type=str, default="usage", 
                       help="API密钥目录路径，默认为usage")
    parser.add_argument("--data_dir", type=str, default="data_reports/dataset", 
                       help="数据目录路径，默认为data_reports/dataset")
    parser.add_argument("--workers", type=int, default=10,
                       help="并行处理的线程数，默认为3")
    parser.add_argument("--limit", type=int, default=None,
                       help="限制处理的文件数量，默认不限制")
    args = parser.parse_args()
    
    try:
        # 初始化API密钥管理器
        key_manager = ApiKeyManager(key_dir=args.key_dir)
        
        # 查找所有结果文件
        all_result_files = find_all_result_files(args.data_dir)
        
        # 如果设置了限制，则只处理指定数量的文件
        if args.limit and args.limit > 0:
            result_files = all_result_files[:args.limit]
            print(f"找到 {len(all_result_files)} 个结果文件，将处理其中的 {len(result_files)} 个")
        else:
            result_files = all_result_files
            print(f"找到 {len(result_files)} 个结果文件")
        
        # 并行处理文件
        updated_count = 0
        total_correct_to_wrong = 0
        total_wrong_to_correct = 0
        
        # 使用tqdm显示进度
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = [executor.submit(process_result_file, file, key_manager) for file in result_files]
            
            for future in tqdm(futures, total=len(result_files), desc="处理文件"):
                try:
                    updated, correct_to_wrong, wrong_to_correct = future.result()
                    if updated:
                        updated_count += 1
                        total_correct_to_wrong += correct_to_wrong
                        total_wrong_to_correct += wrong_to_correct
                except Exception as e:
                    print(f"处理文件时发生错误: {str(e)}")
    except Exception as e:
        print(f"程序运行出错: {e}")
        return
        
    # 显示总结信息
    print("\n" + "="*50)
    print(f"处理完成，更新了 {updated_count} 个文件")
    print(f"从正确修改为错误的判断数量: {total_correct_to_wrong}")
    print(f"从错误修改为正确的判断数量: {total_wrong_to_correct}")
    print(f"净变化: {total_wrong_to_correct - total_correct_to_wrong}")
    print(f"总准确率变化方向: {'提高' if total_wrong_to_correct > total_correct_to_wrong else '下降' if total_wrong_to_correct < total_correct_to_wrong else '不变'}")
    print("="*50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序运行出错: {str(e)}")
        import traceback
        traceback.print_exc()