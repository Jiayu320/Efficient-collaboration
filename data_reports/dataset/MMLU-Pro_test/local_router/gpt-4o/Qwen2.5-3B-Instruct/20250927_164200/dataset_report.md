# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-Pro_test.json
- 问题总数: 5
- 正确数量: 1
- 准确率: 20.00%
- 平均执行时间: 151.17 秒
- 平均成本: $0.0066


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.20 |
| Dependency Structure And Flow | 4.60 |
| Plan Relevance And Efficiency | 4.40 |
| Plan Soundness And Decomposition | 4.20 |
| Task Clarity And Executability | 4.60 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.00 |
| Correctness And Factual Accuracy | 3.86 |
| Effective Use Of Context | 3.86 |
| Instruction Following And Adherence | 3.57 |
| Relevance And Conciseness | 4.00 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.00 |
| Correctness And Factual Accuracy | 2.00 |
| Effective Use Of Context | 4.00 |
| Instruction Following And Adherence | 2.00 |
| Relevance And Conciseness | 2.75 |
## 任务规划指标

- 平均任务步骤数: 3.80
- 平均压缩比例: 73.00%
- 平均每步骤Token限制: 55.53 tokens

## 理论性能指标

- 平均理论执行时间: 4.229 秒
- 平均顺序执行时间: 10.154 秒
- 平均并行加速比: 2.44x
- 理论与实际执行时间比例: 0.03x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.394 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 143.029 秒

### 生成速度
- 小模型平均每秒生成token数: 1.77 tokens/s
- 大模型平均每秒生成token数: 8.56 tokens/s
- 路由模型平均每秒生成token数: 40.20 tokens/s
- 总平均每秒生成token数: 50.53 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Typical advertising regulatory bodies suggest, ... | ✗ | 197.72 | 0.0069 | 5 | 40.00% | 46.0 |
| 2 | Managers are entrusted to run the company in th... | ✓ | 127.20 | 0.0048 | 3 | 100.00% | 56.7 |
| 3 | There are two main issues associated with _____... | ✗ | 157.93 | 0.0080 | 4 | 75.00% | 50.0 |
| 4 | _______ locate morality beyond the sphere of ra... | ✗ | 114.90 | 0.0063 | 3 | 100.00% | 70.0 |
| 5 |  Some of key differences between Islamic financ... | ✗ | 158.09 | 0.0072 | 4 | 50.00% | 55.0 |
