# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-Pro_test.json
- 问题总数: 5
- 正确数量: 1
- 准确率: 20.00%
- 平均执行时间: 127.00 秒
- 平均成本: $0.0077


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 2.40 |
| Dependency Structure And Flow | 3.80 |
| Plan Relevance And Efficiency | 2.60 |
| Plan Soundness And Decomposition | 2.60 |
| Task Clarity And Executability | 4.60 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.75 |
| Correctness And Factual Accuracy | 4.38 |
| Effective Use Of Context | 4.38 |
| Instruction Following And Adherence | 3.50 |
| Relevance And Conciseness | 3.81 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.00 |
| Correctness And Factual Accuracy | 3.67 |
| Effective Use Of Context | 5.00 |
| Instruction Following And Adherence | 3.00 |
| Relevance And Conciseness | 3.00 |
## 任务规划指标

- 平均任务步骤数: 3.80
- 平均压缩比例: 92.00%
- 平均每步骤Token限制: 50.93 tokens

## 理论性能指标

- 平均理论执行时间: 5.097 秒
- 平均顺序执行时间: 8.769 秒
- 平均并行加速比: 1.70x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.783 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 116.168 秒

### 生成速度
- 小模型平均每秒生成token数: 1.60 tokens/s
- 大模型平均每秒生成token数: 13.36 tokens/s
- 路由模型平均每秒生成token数: 15.74 tokens/s
- 总平均每秒生成token数: 30.70 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Typical advertising regulatory bodies suggest, ... | ✗ | 175.32 | 0.0106 | 5 | 60.00% | 54.0 |
| 2 | Managers are entrusted to run the company in th... | ✓ | 101.76 | 0.0049 | 3 | 100.00% | 46.7 |
| 3 | There are two main issues associated with _____... | ✗ | 151.73 | 0.0104 | 5 | 100.00% | 44.0 |
| 4 | _______ locate morality beyond the sphere of ra... | ✗ | 103.93 | 0.0059 | 3 | 100.00% | 56.7 |
| 5 |  Some of key differences between Islamic financ... | ✗ | 102.29 | 0.0066 | 3 | 100.00% | 53.3 |
