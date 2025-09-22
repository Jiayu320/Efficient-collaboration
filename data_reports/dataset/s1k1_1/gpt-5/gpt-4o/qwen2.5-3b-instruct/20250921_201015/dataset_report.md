# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: openai/gpt-5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 1
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 149.37 秒
- 平均成本: $0.0112


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 4.00 |
| Dependency Structure And Flow | 5.00 |
| Plan Relevance And Efficiency | 5.00 |
| Plan Soundness And Decomposition | 5.00 |
| Task Clarity And Executability | 5.00 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 1.00 |
| Correctness And Factual Accuracy | 1.00 |
| Effective Use Of Context | 1.00 |
| Instruction Following And Adherence | 1.00 |
| Relevance And Conciseness | 1.00 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.00 |
| Correctness And Factual Accuracy | 3.00 |
| Effective Use Of Context | 3.00 |
| Instruction Following And Adherence | 3.00 |
| Relevance And Conciseness | 3.00 |
## 任务规划指标

- 平均任务步骤数: 4.00
- 平均压缩比例: 75.00%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 47.365 秒
- 平均顺序执行时间: 70.740 秒
- 平均并行加速比: 1.49x
- 理论与实际执行时间比例: 0.32x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 11.014 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 116.334 秒

### 生成速度
- 小模型平均每秒生成token数: 2.19 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 16.50 tokens/s
- 总平均每秒生成token数: 18.70 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 149.37 | 0.0112 | 4 | 75.00% | 0.0 |
