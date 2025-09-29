# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/natural.json
- 问题总数: 5
- 正确数量: 1
- 准确率: 20.00%
- 平均执行时间: 185.49 秒
- 平均成本: $0.0154


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 2.60 |
| Dependency Structure And Flow | 3.80 |
| Plan Relevance And Efficiency | 3.60 |
| Plan Soundness And Decomposition | 3.20 |
| Task Clarity And Executability | 4.20 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.36 |
| Correctness And Factual Accuracy | 4.20 |
| Effective Use Of Context | 3.80 |
| Instruction Following And Adherence | 3.88 |
| Relevance And Conciseness | 4.36 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.25 |
| Correctness And Factual Accuracy | 3.50 |
| Effective Use Of Context | 5.00 |
| Instruction Following And Adherence | 2.50 |
| Relevance And Conciseness | 3.00 |
## 任务规划指标

- 平均任务步骤数: 5.80
- 平均压缩比例: 93.81%
- 平均每步骤Token限制: 52.95 tokens

## 理论性能指标

- 平均理论执行时间: 7.429 秒
- 平均顺序执行时间: 14.033 秒
- 平均并行加速比: 1.88x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.493 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 173.998 秒

### 生成速度
- 小模型平均每秒生成token数: 4.20 tokens/s
- 大模型平均每秒生成token数: 22.05 tokens/s
- 路由模型平均每秒生成token数: 15.72 tokens/s
- 总平均每秒生成token数: 41.98 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the total work done on an object when i... | ✓ | 115.87 | 0.0048 | 3 | 100.00% | 43.3 |
| 2 | Propose a system of 'Practical Numbers' that de... | ✗ | 239.04 | 0.0208 | 8 | 100.00% | 57.5 |
| 3 | Solve the differential equation (1/F)(dF/dx) = ... | ✗ | 213.32 | 0.0148 | 7 | 85.71% | 48.6 |
| 4 | Two equal masses, each with a mass similar to t... | ✗ | 178.67 | 0.0238 | 6 | 83.33% | 63.3 |
| 5 | Prove that for a vector space V = F^n, where n ... | ✗ | 180.56 | 0.0129 | 5 | 100.00% | 52.0 |
