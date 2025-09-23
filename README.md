# Efficient LLM Collaboration Inference

Efficient LLM Collaboration Inference is an advanced system designed to optimize the collaborative reasoning process of multiple Large Language Models (LLMs). By leveraging automated task decomposition, dynamic model allocation, and parallel processing, the system efficiently solves complex problems that would be challenging for a single model.

-----

## Core Features

  - **Automated Task Decomposition**: Utilizes a sophisticated "Planner" model to break down complex problems into a directed acyclic graph (DAG) of smaller, manageable sub-tasks.
  - **Dynamic Model Allocation**: Intelligently assigns the most suitable model (e.g., a smaller, faster model or a larger, more powerful one) to each sub-task based on its estimated difficulty.
  - **Parallel Task Execution**: Employs a multi-threaded scheduler to execute independent sub-tasks in parallel, significantly reducing overall processing time.
  - **Comprehensive Performance Monitoring**: Tracks and reports detailed performance metrics, including execution time, Time To First Token (TTFT), token usage, and estimated costs, providing deep insights into the system's efficiency.
  - **Batch Processing and Evaluation**: Supports batch processing of datasets for systematic evaluation and reporting, enabling robust model and system performance analysis.

-----

## Demonstration

The following video demonstrates the complete workflow of the system, from receiving a complex problem to generating a final, consolidated solution.

<video src="demo/demonstration.mp4" controls title="System Workflow Demonstration" width="800"></video>

-----

## How It Works

The system operates through a structured, multi-stage pipeline:

1.  **Planning (Decomposition)**: A user's query is first sent to a **Planner Model** (also referred to as the Router). This model analyzes the problem and generates a detailed execution plan in XML format. The plan outlines a series of steps, each with a specific task, estimated difficulty, token budget, and its dependencies on other steps.
2.  **Scheduling (Dispatch)**: The system parses the XML plan to build a task dependency graph (DAG). A scheduler then identifies all tasks whose dependencies have been met and dispatches them for execution.
3.  **Execution (Solving Sub-tasks)**: Each dispatched task is sent to an **Executor Model**. The system dynamically selects either a small, efficient model (e.g., `qwen2.5-3b-instruct`) for simpler tasks or a large, powerful model (e.g., `gpt-4o`) for more complex ones, based on the `Difficulty` attribute in the plan.
4.  **Parallel Processing**: The scheduler uses a thread pool to execute multiple independent tasks concurrently. As tasks are completed, the scheduler checks for newly unblocked tasks and adds them to the execution queue.
5.  **Aggregation (Final Answer)**: Once all tasks in the plan are completed, the system gathers the results from each step and performs a final aggregation to produce the definitive answer to the original query.
6.  **Reporting**: After the process concludes, a detailed report is generated, including performance metrics, cost analysis, task dependency graphs, and quantitative evaluation scores.

### Comparison with Other Methods

Our collaborative inference approach demonstrates significant improvements in both efficiency and solution quality compared to direct, single-model methods.

-----

## Installation and Setup

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Jiayu320/Efficient-collaboration.git
    cd Efficient-collaboration
    ```

2.  **Install Dependencies**

    It is recommended to create a virtual environment first.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

    Install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: If a `requirements.txt` is not provided, you can infer dependencies from the import statements in the Python files, such as `openai`, `pyyaml`, `tqdm`, and `transformers`.)*

3.  **Configure API Keys and Models**

      - Copy the example configuration file:
        ```bash
        cp config.example.yaml config.yaml
        ```
      - Edit `config.yaml` to set up your models and API credentials.
      - Place your API keys in the files specified by the `*_key_path` variables (e.g., in a folder named `usage/`).
        ```yaml
        models:
          small_model: qwen2.5-3b-instruct
          large_model: gpt-4o
          router_model: gemini-2.5-pro # The Planner model
          threshold: 4 # Tasks with difficulty < 4 use the small model

        api:
          small_key_path: usage/qwen_key
          large_key_path: usage/openai_key
          router_key_path: usage/google_key
          small_api_base_url: https://dashscope.aliyuncs.com/compatible-mode/v1
          large_api_base_url: https://api.openai.com/v1
          router_api_base_url: https://api.generativeai.google.com/v1
        ```

-----

## Usage

The system can be run in two modes: single-query processing or batch dataset evaluation.

### Single Query Mode

To solve a single problem, define the `query` in `config.yaml` and run the main script.

```bash
python main.py --config config.yaml
```

The detailed results, including performance reports and logs, will be saved in the `data_reports/single/` directory, organized by model configuration and timestamp.

### Dataset Evaluation Mode

To evaluate the system's performance on a dataset, enable the `dataset` section in `config.yaml`, specify the file path, and run the script.

```yaml
# In config.yaml
dataset:
  enabled: true
  path: dataset/TestData/s1k_testPerformance.json
  limit: 30 # Optional: Limit the number of problems to process
```

Then, execute the main script:

```bash
python main.py
```

Dataset reports will be saved in `data_reports/dataset/`.

-----

## Evaluation Framework

To ensure the quality and reliability of our system, we employ a rigorous, two-part evaluation framework that assesses both the **Planner** and the **Executor** models using a powerful LLM as a judge.

### Planner Evaluation

The Planner is evaluated on its ability to generate a high-quality, machine-executable plan. The evaluation focuses on five key dimensions:

| Dimension                        | Description                                                                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Plan Soundness & Decomposition** | Assesses if the plan correctly and logically breaks down the problem. A flawed decomposition invalidates the entire solution strategy.    |
| **Dependency Structure & Flow** | Evaluates the correctness of the task dependency graph (`Rely` attributes), which is crucial for maximizing parallelism and ensuring correct context. |
| **Task Clarity & Executability** | Measures whether each task is an unambiguous, operational instruction suitable for an AI executor. Vague tasks lead to poor results.       |
| **Attribute Accuracy** | Judges the planner's estimation of `Difficulty` and `Token` attributes, which are vital for efficient dynamic model allocation.           |
| **Plan Relevance & Efficiency** | Checks for redundant or irrelevant steps. A good plan is lean, purposeful, and free of wasted computations.                              |

### Executor Evaluation

The Executor models are evaluated on their ability to accurately and efficiently execute the individual sub-tasks assigned by the Planner.

| Dimension                         | Description                                                                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instruction Following & Adherence** | Assesses how well the model adheres to the specific constraints and instructions of the assigned task.                                    |
| **Effective Use of Context** | Evaluates whether the model correctly utilizes the provided results from prior steps to inform its own execution.                         |
| **Correctness & Factual Accuracy** | Measures the factual and logical accuracy of the model's response. This is the primary measure of successful task completion.                 |
| **Clarity & Machine Usability** | Judges whether the output is clear, well-structured, and easily parsable for subsequent steps.                                            |
| **Relevance & Conciseness** | Assesses if the model's response is concise and strictly relevant to the task, avoiding conversational filler or extraneous information. |

-----

## Performance Benchmarks

We conducted extensive testing by using different state-of-the-art models as the **Planner**. The final **Accuracy** was evaluated on a standardized test dataset, alongside **Planner Performance Scores** (out of 5) and key **Task Planning Metrics**. The Executor models were held constant (`gpt-4o` and `qwen2.5-3b-instruct`).

### Planner Performance and Task Metrics Comparison

This table provides a comprehensive overview of how each Planner model performs in terms of final accuracy, the quality of its generated plans, and the structural characteristics of those plans.

| Planner Model | Accuracy | Planner Score (Avg) | Avg. Task Steps | Avg. Compression Ratio | Avg. Tokens per Step |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **gpt-5** | **30.00%** | 4.62 | **3.83** | 70.27% | **10.00** |
| **qwen3-235b-a22b-thinking** | 26.67% | 4.82 | 5.00 | 82.37% | 45.83 |
| **deepseek-reasoner** | 16.67% | 4.77 | 5.63 | 79.42% | 39.08 |
| **deepseek-chat** | 13.33% | 4.25 | 5.03 | 72.09% | 46.21 |
| **gemini-2.5-pro** | 10.00% | 4.71 | 5.47 | 83.35% | 75.77 |
| **grok-4** | 10.00% | 4.76 | 4.67 | 74.35% | 36.12 |
| **claude-3-7-sonnet-latest** | 6.67% | 4.49 | 6.17 | 75.47% | 45.12 |
| **claude-3-5-sonnet-latest** | 3.33% | 4.53 | 6.57 | 74.94% | 47.04 |
| **gemini-2.5-flash-thinking** | 3.33% | **4.79** | 4.63 | **60.54%** | 47.52 |
| **llama-3-8b-instruct** | 3.33% | 2.96 | 4.37 | 86.36% | 42.04 |

### Executor Performance based on Planner Quality

This table shows the performance of the Executor models, demonstrating how the quality of the plan generated by the Planner impacts their ability to solve sub-tasks correctly. Scores are averaged across all datasets.

| Planner Model | Executor Model | Instruction Following | Context Use | Correctness | Clarity | Conciseness | **Overall Average** |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **gpt-5** | `gpt-4o` / `qwen2.5-3b` | 4.67 | 4.69 | **4.61** | **4.86** | **4.83** | **4.73** |
| **qwen3-235b-a22b-thinking** | `gpt-4o` / `qwen2.5-3b` | 4.53 | 4.51 | 4.37 | 4.72 | 4.69 | 4.56 |
| **gemini-2.5-flash-thinking** | `gpt-4o` / `qwen2.5-3b` | 4.51 | 4.57 | 4.34 | 4.71 | 4.69 | 4.56 |
| **claude-3-7-sonnet-latest** | `gpt-4o` / `qwen2.5-3b` | 4.38 | 4.15 | 3.85 | 4.64 | 4.67 | 4.34 |
| **gemini-2.5-pro** | `gpt-4o` / `qwen2.5-3b` | 4.22 | 4.38 | 4.05 | 4.58 | 4.67 | 4.38 |
| **deepseek-chat** | `gpt-4o` / `qwen2.5-3b` | 4.21 | 4.14 | 4.07 | 4.49 | 4.41 | 4.26 |
| **claude-3-5-sonnet-latest** | `gpt-4o` / `qwen2.5-3b` | 3.88 | 4.09 | 3.79 | 4.43 | 4.39 | 4.12 |
| **grok-4** | `gpt-4o` | 4.11 | 4.22 | 3.93 | 4.66 | 4.62 | 4.31 |
| **deepseek-reasoner** | `gpt-4o` | 3.96 | 4.11 | 3.91 | 4.53 | 4.43 | 4.19 |
| **grok-4** | `qwen2.5-3b-instruct` | 3.24 | 4.15 | 3.21 | 4.23 | 4.03 | 3.77 |
| **llama-3-8b-instruct** | `gpt-4o` | 3.48 | 3.50 | 3.00 | 4.25 | 4.10 | 3.67 |
| **deepseek-reasoner** | `qwen2.5-3b-instruct` | 3.47 | 3.92 | 3.76 | 4.10 | 3.85 | 3.82 |
| **llama-3-8b-instruct** | `qwen2.5-3b-instruct` | 3.23 | 3.29 | 3.21 | 3.92 | 3.48 | 3.43 |

-----

## Model Training

The Planner model can be a general-purpose SOTA model or a fine-tuned smaller model. For our experiments, we fine-tuned a `Qwen3-1.7B-Instruct` model to act as a highly efficient Planner. The fine-tuning was performed using the **LLaMA-Factory** framework on a curated dataset of high-quality problem-plan pairs.

-----

## Codebase Structure

A brief overview of the key files in this repository:

| File                    | Description                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| `main.py`               | The main entry point for the application. Handles argument parsing and orchestrates the overall workflow. |
| `config.yaml`           | The central configuration file for models, API keys, system settings, and dataset paths.                 |
| `execution.py`          | Contains the core logic for parallel task execution, API calls, and the Planner's streaming response processing. |
| `dataset_runner.py`     | Manages batch processing of datasets, generates results, and saves comprehensive reports.                  |
| `evaluation.py`         | Implements the evaluation framework for scoring Planner and Executor performance.                          |
| `performance.py`        | The `PerformanceTracker` class for monitoring metrics like token usage, cost, and execution time.       |
| `output_performance.py` | Calculates theoretical performance benchmarks based on model-specific latency and throughput data.     |
| `config.py`             | Defines the `ModelConfig` class for managing model configurations and API clients.                      |
| `api_pricing.py`        | A utility module that provides up-to-date pricing information for various LLM APIs.                     |
| `analyze_model_tasks.py`| A script to analyze and report on the allocation of tasks between small and large models.                 |

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.