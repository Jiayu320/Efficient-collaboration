import yaml
import subprocess
import os
import shutil
import time
from log_config import setup_logger, get_logger
from tqdm import tqdm # <-- NEW: Import tqdm

# --- 1. 配置区域 ---
ROUTER_MODELS_TO_TEST = [
    {
        'name': 'qwen3-1.7b',
        'router_model': 'qwen3-1.7b',
        'router_key_path': 'usage/qwen',
        'router_api_base_url': 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    },
    {
        'name': 'qwen3-0.6b',
        'router_model': 'qwen3-0.6b',
        'router_key_path': 'usage/qwen',
        'router_api_base_url': 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    },
    {
        'name': 'qwen3-4b',
        'router_model': 'qwen3-4b',
        'router_key_path': 'usage/qwen',
        'router_api_base_url': 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    }
]

# --- 2. 脚本设置 ---
CONFIG_FILE = 'config.yaml'
BACKUP_FILE = 'config.yaml.bak'
MAIN_SCRIPT = 'main.py'
LOG_DIR = 'logs'

def modify_config(model_config: dict, logger):
    """
    读取、修改并写回 config.yaml 文件。
    """
    logger.info(f"--- Modifying config for model: {model_config['name']} ---")
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)

        config_data['models']['router_model'] = model_config['router_model']
        config_data['api']['router_key_path'] = model_config['router_key_path']
        config_data['api']['router_api_base_url'] = model_config['router_api_base_url']

        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(config_data, f, allow_unicode=True, sort_keys=False)
        
        logger.info(f"'{CONFIG_FILE}' updated successfully.")
        return True
    except Exception as e:
        logger.error(f"Error modifying config file '{CONFIG_FILE}': {e}", exc_info=True)
        return False

def run_main_script(logger):
    """
    执行 main.py 脚本并捕获其输出，然后记录结果。
    """
    logger.info(f"--- Running {MAIN_SCRIPT} ... ---")
    try:
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        result = subprocess.run(
            ['python', MAIN_SCRIPT],
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            env=env
        )
        logger.info(f"--- {MAIN_SCRIPT} executed successfully ---")
        
        logger.info(f"--- STDOUT for {MAIN_SCRIPT} ---")
        for line in result.stdout.strip().splitlines():
            logger.info(line)
        logger.info(f"--- End of STDOUT ---")
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"--- ERROR: {MAIN_SCRIPT} failed with return code {e.returncode} ---")
        logger.error(f"--- STDOUT from failed run ---")
        for line in e.stdout.strip().splitlines():
            logger.error(line)
        logger.error(f"--- STDERR from failed run ---")
        for line in e.stderr.strip().splitlines():
            logger.error(line)
        logger.error(f"--- End of error logs ---")
        return False
    except Exception as e:
        logger.error(f"An unexpected error occurred while running the script: {e}", exc_info=True)
        return False

def main():
    """
    自动化测试的主函数。
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_filename = f"experiment_run_{timestamp}.log"
    setup_logger(LOG_DIR, log_filename)
    logger = get_logger()
    
    logger.info("="*80)
    logger.info("Starting new experiment run...")
    logger.info(f"Log file for this run: {os.path.join(LOG_DIR, log_filename)}")
    logger.info("="*80)

    if not os.path.exists(CONFIG_FILE):
        logger.error(f"Configuration file '{CONFIG_FILE}' not found. Aborting.")
        return

    logger.info(f"Backing up original config to '{BACKUP_FILE}'...")
    shutil.copy(CONFIG_FILE, BACKUP_FILE)
    logger.info("Backup complete.")

    try:
        # <-- MODIFIED: Wrap the loop with tqdm for a progress bar -->
        print("Starting model experiments...")
        model_iterator = tqdm(ROUTER_MODELS_TO_TEST, desc="Overall Progress", unit="model")
        
        for model_config in model_iterator:
            model_iterator.set_postfix_str(f"Testing: {model_config['name']}") # <-- NEW: Update tqdm description
            
            logger.info("\n" + "="*80 + "\n")
            logger.info(f"Starting test for: {model_config['name']}")
            
            if not modify_config(model_config, logger):
                logger.error("Skipping execution due to config modification failure.")
                continue
            
            time.sleep(1)

            run_main_script(logger)
            
            logger.info(f"Finished test for: {model_config['name']}")

    finally:
        logger.info("\n" + "="*80 + "\n")
        logger.info(f"All tests finished. Restoring original config from '{BACKUP_FILE}'...")
        if os.path.exists(BACKUP_FILE):
            shutil.move(BACKUP_FILE, CONFIG_FILE)
            logger.info("Original configuration restored.")
        logger.info("="*80)

if __name__ == '__main__':
    main()