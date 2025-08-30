"""
自动化执行脚本，用于多次执行main.py，并在每次执行前修改config.yaml中的threshold值
"""
import os
import re
import subprocess
import time
from datetime import datetime

def modify_threshold(config_file, threshold_value):
    """
    修改配置文件中的threshold值
    
    参数:
        config_file: 配置文件路径
        threshold_value: 新的threshold值
    """
    # 读取配置文件内容
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式替换threshold值
    modified_content = re.sub(r'threshold:\s*\d+', f'threshold: {threshold_value}', content)
    
    # 写入修改后的内容
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"已将threshold修改为: {threshold_value}")

def run_main_with_threshold(threshold_value, config_file="config.yaml"):
    """
    使用指定的threshold值运行main.py
    
    参数:
        threshold_value: threshold值
        config_file: 配置文件路径
    """
    # 修改threshold值
    modify_threshold(config_file, threshold_value)
    
    # 获取当前时间作为运行标识
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    print(f"\n===== 开始运行 (threshold={threshold_value}) - {timestamp} =====")
    
    # 运行main.py
    try:
        # 使用subprocess运行main.py，并捕获输出
        process = subprocess.run(["python", "main.py"], 
                                capture_output=True, 
                                text=True, 
                                check=False)
        
        # 打印输出
        print(process.stdout)
        
        # 如果有错误，也打印出来
        if process.stderr:
            print("错误输出:")
            print(process.stderr)
        
        # 保存运行结果
        result_dir = "threshold_results"
        os.makedirs(result_dir, exist_ok=True)
        result_file = os.path.join(result_dir, f"result_threshold_{threshold_value}_{timestamp}.txt")
        
        with open(result_file, 'w', encoding='utf-8') as f:
            f.write(f"===== 运行结果 (threshold={threshold_value}) =====\n\n")
            f.write(process.stdout)
            if process.stderr:
                f.write("\n\n===== 错误输出 =====\n\n")
                f.write(process.stderr)
        
        print(f"运行结果已保存至: {result_file}")
        return True
    except Exception as e:
        print(f"运行过程中出错: {e}")
        return False

def main():
    """主函数"""
    config_file = "config.yaml"
    thresholds = [2, 3, 4]  # 要测试的threshold值列表
    
    print(f"开始使用不同的threshold值运行main.py")
    print(f"配置文件: {config_file}")
    print(f"要测试的threshold值: {thresholds}")
    
    # 备份原始配置文件
    backup_file = f"{config_file}.bak"
    try:
        with open(config_file, 'r', encoding='utf-8') as src:
            with open(backup_file, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
        print(f"已创建配置文件备份: {backup_file}")
    except Exception as e:
        print(f"备份配置文件时出错: {e}")
        return
    
    try:
        # 对每个threshold值运行一次
        for threshold in thresholds:
            run_main_with_threshold(threshold, config_file)
            
            # 在运行之间等待一小段时间，避免过快地修改配置
            if threshold != thresholds[-1]:
                print(f"等待5秒后继续下一次运行...\n")
                time.sleep(5)
        
        print("\n所有运行已完成!")
    except Exception as e:
        print(f"执行过程中出错: {e}")
    finally:
        # 恢复原始配置
        try:
            with open(backup_file, 'r', encoding='utf-8') as src:
                with open(config_file, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            print(f"已恢复原始配置文件")
        except Exception as e:
            print(f"恢复配置文件时出错: {e}")

if __name__ == "__main__":
    main()
