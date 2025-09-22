# Efficient LLM Collaboration Inference

Efficient LLM Collaboration Inference is an advanced system designed to optimize the collaborative reasoning process of multiple Large Language Models (LLMs). By leveraging automated task decomposition, dynamic model allocation, and parallel processing, the system efficiently solves complex problems that would be challenging for a single model.

## Core Features

  - **Automated Task Decomposition**: Utilizes a sophisticated "Planner" model to break down complex problems into a directed acyclic graph (DAG) of smaller, manageable sub-tasks.
  - **Dynamic Model Allocation**: Intelligently assigns the most suitable model (e.g., a smaller, faster model or a larger, more powerful one) to each sub-task based on its estimated difficulty.
  - **Parallel Task Execution**: Employs a multi-threaded scheduler to execute independent sub-tasks in parallel, significantly reducing overall processing time.
  - **Comprehensive Performance Monitoring**: Tracks and reports detailed performance metrics, including execution time, Time To First Token (TTFT), token usage, and estimated costs, providing deep insights into the system's efficiency.
  - **Batch Processing and Evaluation**: Supports batch processing of datasets for systematic evaluation and reporting, enabling robust model and system performance analysis.

## Demonstration

The following video demonstrates the complete workflow of the system, from receiving a complex problem to generating a final, consolidated solution.

<video src="demo/demonstration.mp4" controls title="System Workflow Demonstration" width="800"></video>

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

<image src="img/comparsion.jpg" title="Comparison" width="800"></image>

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

    <!-- end list -->

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

## Evaluation Framework

To ensure the quality and reliability of our system, we employ a rigorous, two-part evaluation framework that assesses both the **Planner** and the **Executor** models using a powerful LLM as a judge.

### Planner Evaluation

The Planner is evaluated on its ability to generate a high-quality, machine-executable plan. The evaluation focuses on five key dimensions:

| Dimension                         | Description                                                                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Plan Soundness & Decomposition** | Assesses if the plan correctly and logically breaks down the problem. A flawed decomposition invalidates the entire solution strategy.   |
| **Dependency Structure & Flow** | Evaluates the correctness of the task dependency graph (`Rely` attributes), which is crucial for maximizing parallelism and ensuring correct context. |
| **Task Clarity & Executability** | Measures whether each task is an unambiguous, operational instruction suitable for an AI executor. Vague tasks lead to poor results.      |
| **Attribute Accuracy** | Judges the planner's estimation of `Difficulty` and `Token` attributes, which are vital for efficient dynamic model allocation.          |
| **Plan Relevance & Efficiency** | Checks for redundant or irrelevant steps. A good plan is lean, purposeful, and free of wasted computations.                             |

### Executor Evaluation

The Executor models are evaluated on their ability to accurately and efficiently execute the individual sub-tasks assigned by the Planner.

| Dimension                          | Description                                                                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instruction Following & Adherence** | Assesses how well the model adheres to the specific constraints and instructions of the assigned task.                                     |
| **Effective Use of Context** | Evaluates whether the model correctly utilizes the provided results from prior steps to inform its own execution.                          |
| **Correctness & Factual Accuracy** | Measures the factual and logical accuracy of the model's response. This is the primary measure of successful task completion.                 |
| **Clarity & Machine Usability** | Judges whether the output is clear, well-structured, and easily parsable for subsequent steps.                                             |
| **Relevance & Conciseness** | Assesses if the model's response is concise and strictly relevant to the task, avoiding conversational filler or extraneous information. |

## Performance Benchmarks

We conducted extensive testing by using different state-of-the-art models as the Planner while keeping the Executor models (`qwen2.5-3b-instruct` and `gpt-4o`) constant. The results below are averaged scores (out of 5) across a standardized test dataset.

### Planner Performance Comparison

This table shows how well different models perform at decomposing problems into logical plans.

| Planner Model              | Plan Soundness | Dependency Structure | Task Clarity | Attribute Accuracy | Plan Relevance | **Overall Average** |
| -------------------------- | :------------: | :------------------: | :----------: | :----------------: | :------------: | :-----------------: |
| **gemini-2.5-flash-thinking** |      5.00      |         5.00         |     4.96     |        4.00        |      5.00      |      **4.79** |
| **deepseek-reasoner** |      5.00      |         4.97         |     4.97     |        3.93        |      5.00      |      **4.77** |
| **claude-3-5-sonnet-latest** |      4.60      |         4.80         |     4.90     |        3.77        |      4.60      |      **4.53** |
| **claude-3-7-sonnet-latest** |      4.60      |         4.73         |     4.73     |        3.77        |      4.60      |      **4.49** |
| **deepseek-chat** |      4.45      |         4.38         |     4.41     |        3.45        |      4.55      |      **4.25** |

### Executor Performance based on Planner Quality

This table shows the performance of the Executor models, demonstrating how the quality of the plan generated by the Planner impacts their ability to solve sub-tasks correctly.

| Planner Model              | Executor Model           | Instruction Following | Context Use | Correctness | Clarity | Conciseness | **Overall Average** |
| -------------------------- | ------------------------ | :-------------------: | :---------: | :---------: | :-----: | :---------: | :-----------------: |
| **deepseek-reasoner** | `gpt-4o`                 |         3.78          |    3.99     |    3.78     |  4.30   |    4.20     |      **4.01** |
| **deepseek-chat** | `gpt-4o`                 |         3.86          |    3.83     |    3.73     |  4.14   |    4.04     |      **3.92** |
|                            | `qwen2.5-3b-instruct`    |         3.22          |    3.68     |    3.62     |  3.88   |    3.65     |      **3.61** |
| **deepseek-reasoner** | `qwen2.5-3b-instruct`    |         3.09          |    3.52     |    3.38     |  3.64   |    3.42     |      **3.41** |
| **claude-3-7-sonnet-latest** | `qwen2.5-3b-instruct`    |         2.94          |    3.51     |    3.03     |  3.56   |    3.33     |      **3.27** |
| **claude-3-5-sonnet-latest** | `qwen2.5-3b-instruct`    |         2.76          |    3.24     |    2.80     |  3.49   |    3.26     |      **3.11** |
| **gemini-2.5-flash-thinking**| `qwen2.5-3b-instruct`    |         2.70          |    2.91     |    2.61     |  3.22   |    3.15     |      **2.92** |
| **claude-3-5-sonnet-latest** | `gpt-4o`                 |         2.71          |    2.93     |    2.64     |  3.10   |    3.06     |      **2.89** |
| **gemini-2.5-flash-thinking**| `gpt-4o`                 |         2.51          |    2.66     |    2.50     |  2.69   |    2.67     |      **2.61** |
| **claude-3-7-sonnet-latest** | `gpt-4o`                 |         2.46          |    2.39     |    2.31     |  2.64   |    2.66     |      **2.49** |

## Model Training

The Planner model can be a general-purpose SOTA model or a fine-tuned smaller model. For our experiments, we fine-tuned a `Qwen3-1.7B-Instruct` model to act as a highly efficient Planner. The fine-tuning was performed using the **LLaMA-Factory** framework on a curated dataset of high-quality problem-plan pairs.

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.