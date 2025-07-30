import json
import os
import time
from tqdm import tqdm
import sys
from config import ModelConfig, load_config
import openai
# 导入执行模块但不直接导入judge_correct函数
import execution

def get_api_key(file_path):
    """从文件中获取API密钥"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read().strip()
    else:
        raise FileNotFoundError(f"API密钥文件 '{file_path}' 未找到")

def load_data(json_path):
    """加载JSON数据
    
    参数:
        json_path: JSON文件路径
        
    返回:
        加载的数据列表
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def save_data(data, json_path):
    """保存数据到JSON文件
    
    参数:
        data: 要保存的数据
        json_path: JSON文件路径
    """
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"数据已保存至 {json_path}")

def rejudge_results(data_path, config_file="config.yaml"):
    """重新判断结果正确性
    
    参数:
        data_path: 数据文件路径
        config_file: 配置文件路径
        
    返回:
        更新后的数据
    """
    print(f"开始处理文件: {data_path}")
    
    # 加载配置
    yaml_config = load_config(config_file)
    
    # 构建模型配置
    model_config = ModelConfig(
        large_model=yaml_config["models"]["large_model"],
        large_key_path=yaml_config["api"]["large_key_path"],
        large_api_base=yaml_config["api"].get("large_api_base_url", yaml_config["api"]["base_url"])
    )
    
    # 设置API密钥
    large_key = get_api_key(model_config.large_key_path)
    
    # 初始化OpenAI客户端
    global large_model_client
    large_model_client = openai.OpenAI(
        api_key=large_key,
        base_url=model_config.large_api_base
    )
    
    # 确保执行模块可以访问到large_model_client
    print("初始化API客户端...")
    execution.large_model_client = large_model_client
    
    # 测试API客户端是否正常工作
    try:
        print("测试API客户端连接...")
        test_response = large_model_client.chat.completions.create(
            model=model_config.large_model,
            messages=[
                {"role": "user", "content": "Say 'API connection successful'"}
            ],
            stream=False
        )
        print(f"API测试结果: {test_response.choices[0].message.content}")
    except Exception as e:
        print(f"API客户端测试失败: {str(e)}")
        print("尝试重新初始化客户端...")
        
        # 重新初始化客户端
        large_model_client = openai.OpenAI(
            api_key=large_key,
            base_url=model_config.large_api_base
        )
        execution.large_model_client = large_model_client
    
    # 加载数据
    data = load_data(data_path)
    print(f"加载了 {len(data)} 条数据")
    
    # 记录更新统计
    total_items = len(data)
    updated_items = 0
    true_to_false = 0
    false_to_true = 0
    
    # 处理每条数据
    for i in tqdm(range(total_items), desc="重新判断"):
        item = data[i]
        
        # 确保数据有必要的字段
        if "question" in item and "answer" in item and "solution" in item:
            question = item["question"]
            gold_answer = item["answer"]
            
            # 提取最终答案
            solution = item["solution"]
            final_answer = ""
            
            # 尝试从solution提取最终答案
            if "最终答案" in solution:
                try:
                    final_answer = solution.split("最终答案")[-1].strip()
                except Exception as e:
                    print(f"从solution提取最终答案时出错: {e}")
            
            # 如果无法提取或最终答案为空，尝试从solution最后一行提取
            if not final_answer:
                try:
                    # 获取最后一行非空内容
                    lines = [line for line in solution.split('\n') if line.strip()]
                    if lines:
                        final_answer = lines[-1].strip()
                except Exception as e:
                    print(f"从solution最后一行提取答案时出错: {e}")
            
            # 如果仍然无法提取，使用整个solution作为答案
            if not final_answer:
                final_answer = solution
            
            # 记录原始correct值
            original_correct = item.get("correct", None)
            
            # 调用judge_correct判断正确性
            if gold_answer and final_answer:
                try:
                    # 确保execution模块可以访问到large_model_client
                    if execution.large_model_client is None:
                        print(f"警告: large_model_client 未设置，重新设置...")
                        execution.large_model_client = large_model_client
                    
                    # 检查客户端是否有效
                    if not hasattr(execution.large_model_client, 'chat'):
                        print(f"错误: large_model_client 没有 chat 属性，重新初始化...")
                        execution.large_model_client = openai.OpenAI(
                            api_key=large_key,
                            base_url=model_config.large_api_base
                        )
                    
                    print(f"处理条目 {i+1}/{total_items}: 问题={question[:30]}..., 标准答案={gold_answer}")
                    is_correct, result_text = execution.judge_correct(question, gold_answer, final_answer, model_config)
                    print(f"判断结果: {is_correct}, 原始状态: {original_correct}")
                    
                    # 更新correct字段
                    item["correct"] = is_correct
                    
                    # 统计状态变化
                    if original_correct is not None:
                        if original_correct != is_correct:
                            updated_items += 1
                            if original_correct and not is_correct:
                                true_to_false += 1
                            elif not original_correct and is_correct:
                                false_to_true += 1
                    
                    # 防止API限制，添加短暂延迟
                    time.sleep(1.0)
                    
                except Exception as e:
                    print(f"条目 {i+1} 判断出错: {str(e)}")
                    import traceback
                    traceback.print_exc()
        else:
            print(f"条目 {i+1} 缺少必要字段，跳过")
    
    # 打印统计信息
    print(f"\n判断完成! 总计 {total_items} 条数据")
    print(f"更新了 {updated_items} 条数据")
    print(f"从True改为False: {true_to_false} 条")
    print(f"从False改为True: {false_to_true} 条")
    
    return data

def main():
    """主函数"""
    # 使用正确的文件路径 - limo_training.json 或者 training_data.json
    data_path = "dataset/generated_data/limo_training.json"
    backup_path = "dataset/generated_data/limo_training_backup.json"
    
    # 备份原始数据
    data = load_data(data_path)
    save_data(data, backup_path)
    print(f"原始数据已备份至 {backup_path}")
    
    # 重新判断
    updated_data = rejudge_results(data_path)
    
    # 保存更新后的数据
    save_data(updated_data, data_path)
    
    print("处理完成!")

if __name__ == "__main__":
    main()
