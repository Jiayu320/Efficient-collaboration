import os
import json
import re
import logging
from openai import OpenAI
from collections import defaultdict
from tqdm import tqdm

# --- 配置日志 ---
# 设置日志级别为 INFO，如果需要查看详细的Prompt和模型输出，请改为 logging.DEBUG
LOG_LEVEL = logging.INFO 
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- 模型和API配置 ---
DIFFICULTY_THRESHOLD = 4
MODELS_CONFIG = {
    'small': {
        'model_name': 'qwen2.5-3b-instruct',
        'api_key_path': 'usage/qwen',
        'base_url': 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    },
    'large': {
        'model_name': 'gpt-4o',
        'api_key_path': 'usage/bianxie1',
        'base_url': 'https://api.bianxie.ai/v1'
    },
    'evaluator': {
        'model_name': 'deepseek-chat',
        'api_key_path': 'usage/deepseek2',
        'base_url': 'https://api.deepseek.com'
    },
    'final_answer_summarizer': {
        'model_name': 'qwen2.5-3b-instruct',
        'api_key_path': 'usage/qwen',
        'base_url': 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    },
    'judger': {
        'model_name': 'deepseek-chat',
        'api_key_path': 'usage/deepseek',
        'base_url': 'https://api.deepseek.com'
    }
}

# --- Prompt模板 ---
PROMPT_TEMPLATE_EXECUTE = """
You are a specialized AI module acting as a precision-focused computational and reasoning engine. Your sole function is to execute a single, specific subtask from a larger problem-solving plan with absolute accuracy.
You will be provided with the following inputs:

1.  **`PROBLEM`**: The overall problem for context, but you should not attempt to solve it.
2.  **`CURRENT STEP (Task)`**: The specific, isolated instruction you must execute.
3.  **`CONTEXT (Results from prior steps)`**: Crucial information from completed steps. **You MUST use this context if the task relies on it.**

Your output must strictly adhere to the following two-part format:

1.  **`Reasoning:`**: Provide a brief, step-by-step explanation of your process for completing the task. Show your work for any calculations. This section should be concise and logical.
2.  **`Answer:`**: State the final, direct answer to the `Task`. This should be the conclusive output of your reasoning, presented as cleanly as possible (e.g., a number, a formula, a short statement).

**CRITICAL RULES:**
* **DO NOT** exceed the scope of the `Task`.
* **DO NOT** provide any information that was not explicitly requested.
* **DO NOT** add conversational filler, greetings, or sign-offs.
* Your entire response must be under **{Token}** tokens.

**PROBLEM:**
{Problem}

**CURRENT STEP:**
Task: {Task}
{Relied_Results}
"""

PROMPT_TEMPLATE_SUMMARIZE = """
Based on the results of all steps below, please provide only the final answer. No other explanations or details are needed.

PROBLEM:
{query}

SOLUTION STEPS:
{steps}
"""

PROMPT_TEMPLATE_JUDGE = """
Here is a math problem with a standard answer and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.

Problem: {question}

Standard answer: {gold_answer}

Answer: {final_answer}

If the student's answer is correct, just output True; otherwise, just output False.
No explanation is required.
"""


def get_api_key(file_path):
    if not os.path.exists(file_path):
        logger.error(f"API密钥文件 '{file_path}' 未找到")
        raise FileNotFoundError(f"API密钥文件 '{file_path}' 未找到")
    with open(file_path, 'r') as f:
        return f.read().strip()

def get_openai_client(model_type):
    config = MODELS_CONFIG[model_type]
    return OpenAI(
        api_key=get_api_key(config['api_key_path']),
        base_url=config['base_url']
    )

def call_model(client, model_name, prompt, temperature=0.0, max_tokens=2048):
    logger.debug(f"\n--- PROMPT for {model_name} ---\n{prompt}\n------------------------------")
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        response_content = response.choices[0].message.content.strip()
        logger.debug(f"\n--- RESPONSE from {model_name} ---\n{response_content}\n---------------------------------")
        return response_content
    except Exception as e:
        logger.error(f"调用模型 {model_name} 时出错: {e}")
        return None

def construct_relied_results(tasks, current_step_id):
    rely_ids_str = tasks[current_step_id].get('Rely', '')
    if not rely_ids_str:
        return ""
    
    relied_results = "\n**CONTEXT (Results from prior steps):**\n"
    rely_ids = rely_ids_str.split(',')
    
    for step_id in rely_ids:
        step_id = step_id.strip()
        if step_id in tasks and tasks[step_id].get('Result'):
            task_info = tasks[step_id]
            relied_results += f"\nTask {step_id}: {task_info.get('Task', '')} ; Result: {task_info.get('Result')}"
            
    return relied_results if len(relied_results) > len("\n**CONTEXT (Results from prior steps):**\n") else ""

def find_target_files(root_dir):
    target_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        if 'dataset_results.json' in filenames:
            target_files.append(os.path.join(dirpath, 'dataset_results.json'))
    return target_files

def update_model_solution(model_solution, task_id, new_result):
    pattern = re.compile(rf"(### 步骤 {task_id}:.*?)\n(.*?)\n\n", re.DOTALL)
    match = pattern.search(model_solution)
    if match:
        header = match.group(1)
        updated_block = f"{header}\n{new_result}\n\n"
        return model_solution.replace(match.group(0), updated_block)
    return model_solution

def reevaluate_task(problem_data, task_id, experiment_dir):
    logger.info(f"正在为问题 #{problem_data.get('problem_id', 'N/A')} 的任务 {task_id} 进行重新评估...")
    
    eval_prompt_path = os.path.join("evaluationPrompt", "ExecutorEvaluation.txt")
    if not os.path.exists(eval_prompt_path):
        logger.error(f"评估Prompt文件未找到: {eval_prompt_path}")
        return None
    with open(eval_prompt_path, 'r', encoding='utf-8') as f:
        eval_base_prompt = f.read()

    task = problem_data['tasks'][task_id]
    context = {
        "Original Question": problem_data['problem'],
        "Full Plan": json.dumps(problem_data['tasks'], indent=2),
        "Subtask to Evaluate": f"ID: {task_id}, Task: {task['Task']}",
        "Context Provided": construct_relied_results(problem_data['tasks'], task_id),
        "Executor's Response": task['Result']
    }
    
    full_eval_prompt = eval_base_prompt + "\n\n-----" + "\n## Evaluation Context\n"
    for key, value in context.items():
        full_eval_prompt += f"### {key}\n{value}\n\n"

    eval_client = get_openai_client('evaluator')
    report_str = call_model(eval_client, MODELS_CONFIG['evaluator']['model_name'], full_eval_prompt)
    
    if not report_str:
        logger.error("评估模型未能返回有效报告。")
        return None

    try:
        report_json_str = report_str[report_str.find('{'):report_str.rfind('}')+1]
        new_report = json.loads(report_json_str)
        
        eval_file_path = os.path.join(experiment_dir, "evaluation_reports", f"evaluation_problem_{problem_data['problem_id']}.json")
        if os.path.exists(eval_file_path):
            with open(eval_file_path, 'r+', encoding='utf-8') as f:
                eval_data = json.load(f)
                if 'executor_reports' not in eval_data: eval_data['executor_reports'] = {}
                if task_id not in eval_data['executor_reports']: eval_data['executor_reports'][task_id] = {}
                eval_data['executor_reports'][task_id]['report'] = new_report
                f.seek(0)
                json.dump(eval_data, f, indent=2, ensure_ascii=False)
                f.truncate()
            logger.info(f"已成功更新评估文件: {eval_file_path}")
            return new_report
        else:
            logger.warning(f"评估文件未找到，无法更新: {eval_file_path}")
            return None
    except json.JSONDecodeError as e:
        logger.error(f"解析评估报告JSON时失败: {e}\n原始报告内容: {report_str}")
        return None

def update_summary_report(experiment_dir):
    """更新 dataset_report.md 文件"""
    logger.info(f"正在同步/更新总结报告: {os.path.join(experiment_dir, 'dataset_report.md')}")
    all_planner_scores = defaultdict(list)
    all_executor_scores = defaultdict(lambda: defaultdict(list))
    total_problems = 0
    correct_count = 0

    results_file = os.path.join(experiment_dir, 'dataset_results.json')
    if os.path.exists(results_file):
        with open(results_file, 'r', encoding='utf-8') as f:
            results_data = json.load(f)
            total_problems = len(results_data)
            for item in results_data:
                if item.get('is_correct', False):
                    correct_count += 1

    eval_reports_dir = os.path.join(experiment_dir, 'evaluation_reports')
    if os.path.exists(eval_reports_dir):
        for filename in os.listdir(eval_reports_dir):
            if filename.startswith('evaluation_problem_') and filename.endswith('.json'):
                with open(os.path.join(eval_reports_dir, filename), 'r', encoding='utf-8') as f:
                    eval_data = json.load(f)
                    
                    if 'planner_report' in eval_data and 'evaluationReport' in eval_data['planner_report']:
                        for dim, values in eval_data['planner_report']['evaluationReport'].items():
                            if isinstance(values, dict) and 'score' in values:
                                try: all_planner_scores[dim].append(float(values['score']))
                                except (ValueError, TypeError): pass

                    if 'executor_reports' in eval_data:
                        for task_id, report_data in eval_data['executor_reports'].items():
                            model_used = report_data.get('model_used', 'unknown_model')
                            if 'report' in report_data and 'evaluationReport' in report_data['report']:
                                for dim, values in report_data['report']['evaluationReport'].items():
                                     if isinstance(values, dict) and 'score' in values:
                                        try: all_executor_scores[model_used][dim].append(float(values['score']))
                                        except (ValueError, TypeError): pass

    avg_planner_scores = {dim: sum(scores) / len(scores) if scores else 0 for dim, scores in all_planner_scores.items()}
    avg_executor_scores = {model: {dim: sum(scores) / len(scores) if scores else 0 for dim, scores in dims.items()} for model, dims in all_executor_scores.items()}
    accuracy = (correct_count / total_problems * 100) if total_problems > 0 else 0

    report_path = os.path.join(experiment_dir, 'dataset_report.md')
    if not os.path.exists(report_path):
        logger.error(f"报告文件 {report_path} 不存在。")
        return
        
    with open(report_path, 'r', encoding='utf-8') as f: content = f.read()

    content = re.sub(r'(正确数量: )\d+', f'\\g<1>{correct_count}', content)
    content = re.sub(r'(准确率: )\d+\.\d+%', f'\\g<1>{accuracy:.2f}%', content)

    for dim, score in avg_planner_scores.items():
        dim_title = ' '.join(re.findall('[A-Z][^A-Z]*', dim)).title()
        pattern = re.compile(f"({dim_title} \|) [\d\.]+")
        content = pattern.sub(f"\\1 {score:.2f}", content)
        
    for model, dims in avg_executor_scores.items():
        for dim, score in dims.items():
            dim_title = ' '.join(re.findall('[A-Z][^A-Z]*', dim)).title()
            pattern = re.compile(rf"(#### 模型: `{model}`.*?{dim_title} \|) [\d\.]+", re.DOTALL)
            content = pattern.sub(f"\\1 {score:.2f}", content)

    if os.path.exists(results_file):
        with open(results_file, 'r', encoding='utf-8') as f:
            results_data = json.load(f)
            for i, item in enumerate(results_data):
                problem_text_safe = re.escape(item['problem'][:40])
                is_correct_symbol = '✓' if item.get('is_correct', False) else '✗'
                pattern = re.compile(rf"(\| {i+1}\s*\|.*?{problem_text_safe}.*?\|)\s*[✓✗]\s*\|", re.DOTALL)
                content = pattern.sub(f"\\1 {is_correct_symbol} |", content)

    with open(report_path, 'w', encoding='utf-8') as f: f.write(content)
    logger.info("总结报告同步/更新完毕。")


def process_experiment_file(file_path):
    """处理单个 dataset_results.json 文件"""
    experiment_dir = os.path.dirname(file_path)
    
    # ★★★ 新增机制：运行前预检查和同步 ★★★
    logger.info(f"运行前预检查: 为保证状态一致，首先同步 '{os.path.basename(experiment_dir)}' 的总结报告...")
    update_summary_report(experiment_dir)
    logger.info("预检查同步完成，开始处理空缺结果。")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error(f"无法读取或解析JSON文件: {file_path}，跳过。")
        return

    is_file_modified = False
    
    problem_iterator = tqdm(enumerate(data), total=len(data), desc=f"Processing {os.path.basename(experiment_dir)}")
    
    for i, problem_data in problem_iterator:
        problem_id = i + 1
        problem_data['problem_id'] = problem_id
        problem_iterator.set_postfix_str(f"Problem #{problem_id}")

        tasks_to_fix = []
        if 'tasks' in problem_data and problem_data['tasks'] is not None:
            for task_id, task_details in problem_data['tasks'].items():
                if not task_details.get('Result'):
                    tasks_to_fix.append(task_id)

        if tasks_to_fix:
            is_file_modified = True
            logger.info(f"在问题 #{problem_id}/{len(data)} 中发现 {len(tasks_to_fix)} 个空任务: {tasks_to_fix}")
            
            for task_id in tasks_to_fix:
                logger.info(f"  正在修复问题 #{problem_id} 的任务 {task_id}...")
                task_details = problem_data['tasks'][task_id]
                
                difficulty = int(task_details.get('Difficulty', '0'))
                model_type = 'large' if difficulty >= DIFFICULTY_THRESHOLD else 'small'
                client = get_openai_client(model_type)
                model_name = MODELS_CONFIG[model_type]['model_name']
                
                relied_results = construct_relied_results(problem_data['tasks'], task_id)
                prompt = PROMPT_TEMPLATE_EXECUTE.format(
                    Token=task_details.get('Token', 150),
                    Problem=problem_data.get('problem', ''),
                    Task=task_details.get('Task', ''),
                    Relied_Results=relied_results
                )
                
                new_result = call_model(client, model_name, prompt)
                if new_result:
                    problem_data['tasks'][task_id]['Result'] = new_result
                    logger.info(f"    任务 {task_id} 已成功修复。")
                    problem_data['model_solution'] = update_model_solution(
                        problem_data['model_solution'], task_id, new_result
                    )
                    reevaluate_task(problem_data, task_id, experiment_dir)
                else:
                    logger.error(f"    任务 {task_id} 修复失败，模型未返回结果。")

            logger.info(f"为问题 #{problem_id} 重新生成最终答案...")
            steps_text = ""
            sorted_tasks = sorted(problem_data['tasks'].items(), key=lambda item: int(item[0]))
            for step_id, attrs in sorted_tasks:
                steps_text += f"步骤 {step_id}: {attrs.get('Task', '')}\n{attrs.get('Result', '（此步骤未完成）')}\n\n"
            
            summarizer_client = get_openai_client('final_answer_summarizer')
            summarizer_prompt = PROMPT_TEMPLATE_SUMMARIZE.format(
                query=problem_data['problem'], steps=steps_text
            )
            
            new_final_answer = call_model(summarizer_client, MODELS_CONFIG['final_answer_summarizer']['model_name'], summarizer_prompt)
            
            if new_final_answer:
                problem_data['model_solution'] = re.sub(
                    r"(## 最终答案\n)(.*)",
                    lambda m: m.group(1) + new_final_answer,
                    problem_data['model_solution'],
                    flags=re.DOTALL
                )
                
                logger.info(f"  已生成新的最终答案。正在重新判断正误...")
                judger_client = get_openai_client('judger')
                judge_prompt = PROMPT_TEMPLATE_JUDGE.format(
                    question=problem_data['problem'],
                    gold_answer=problem_data['gold_solution'],
                    final_answer=new_final_answer
                )
                
                judgement = call_model(judger_client, MODELS_CONFIG['judger']['model_name'], judge_prompt)
                
                if judgement is not None:
                    is_correct = 'true' in judgement.lower()
                    problem_data['is_correct'] = is_correct
                    problem_data['judge_result'] = str(is_correct)
                    logger.info(f"    判断结果: {is_correct}")
                else:
                    logger.error("    判断模型未能返回有效结果。")

    if is_file_modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"文件 {file_path} 已更新。")
        # 在所有修改完成后，再次更新报告以反映最新状态
        update_summary_report(experiment_dir)

def main():
    root_directory = os.path.join("data_reports", "dataset", "s1k_testPerformance")
    
    if not os.path.isdir(root_directory):
        logger.error(f"指定的目录不存在: {root_directory}")
        return
        
    target_files = find_target_files(root_directory)
    if not target_files:
        logger.warning(f"在目录 '{root_directory}' 中未找到任何 'dataset_results.json' 文件。")
        return

    file_iterator = tqdm(target_files, desc="Overall Progress")
    for file_path in file_iterator:
        process_experiment_file(file_path)

if __name__ == "__main__":
    main()