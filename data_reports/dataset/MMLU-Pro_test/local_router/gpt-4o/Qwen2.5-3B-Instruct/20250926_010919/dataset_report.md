# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-Pro_test.json
- 问题总数: 5
- 正确数量: 1
- 准确率: 20.00%
- 平均执行时间: 127.18 秒
- 平均成本: $0.0074


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 1.60 |
| Dependency Structure And Flow | 2.60 |
| Plan Relevance And Efficiency | 1.80 |
| Plan Soundness And Decomposition | 1.80 |
| Task Clarity And Executability | 2.20 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.67 |
| Correctness And Factual Accuracy | 4.20 |
| Effective Use Of Context | 3.93 |
| Instruction Following And Adherence | 4.07 |
| Relevance And Conciseness | 4.60 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 5.00 |
| Correctness And Factual Accuracy | 5.00 |
| Effective Use Of Context | 5.00 |
| Instruction Following And Adherence | 5.00 |
| Relevance And Conciseness | 5.00 |
## 任务规划指标

- 平均任务步骤数: 3.20
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 58.33 tokens

## 理论性能指标

- 平均理论执行时间: 4.923 秒
- 平均顺序执行时间: 18.485 秒
- 平均并行加速比: 3.80x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.696 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 118.223 秒

### 生成速度
- 小模型平均每秒生成token数: 0.58 tokens/s
- 大模型平均每秒生成token数: 9.27 tokens/s
- 路由模型平均每秒生成token数: 41.35 tokens/s
- 总平均每秒生成token数: 51.20 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Typical advertising regulatory bodies suggest, ... | ✓ | 154.25 | 0.0100 | 4 | 100.00% | 57.5 |
| 2 | Managers are entrusted to run the company in th... | ✗ | 124.34 | 0.0085 | 3 | 100.00% | 63.3 |
| 3 | There are two main issues associated with _____... | ✗ | 140.78 | 0.0074 | 4 | 100.00% | 52.5 |
| 4 | _______ locate morality beyond the sphere of ra... | ✗ | 116.44 | 0.0062 | 3 | 100.00% | 63.3 |
| 5 |  Some of key differences between Islamic financ... | ✗ | 100.08 | 0.0049 | 2 | 100.00% | 55.0 |
