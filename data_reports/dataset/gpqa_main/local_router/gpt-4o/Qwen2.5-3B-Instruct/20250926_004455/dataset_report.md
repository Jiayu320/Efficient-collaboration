# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 5
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 185.54 秒
- 平均成本: $0.0114


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 1.80 |
| Dependency Structure And Flow | 2.60 |
| Plan Relevance And Efficiency | 2.60 |
| Plan Soundness And Decomposition | 1.80 |
| Task Clarity And Executability | 3.20 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.33 |
| Correctness And Factual Accuracy | 3.62 |
| Effective Use Of Context | 4.62 |
| Instruction Following And Adherence | 3.95 |
| Relevance And Conciseness | 4.33 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 5.00 |
| Correctness And Factual Accuracy | 3.40 |
| Effective Use Of Context | 4.20 |
| Instruction Following And Adherence | 4.20 |
| Relevance And Conciseness | 5.00 |
## 任务规划指标

- 平均任务步骤数: 5.20
- 平均压缩比例: 62.44%
- 平均每步骤Token限制: 53.26 tokens

## 理论性能指标

- 平均理论执行时间: 6.222 秒
- 平均顺序执行时间: 23.795 秒
- 平均并行加速比: 3.86x
- 理论与实际执行时间比例: 0.03x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.559 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 174.451 秒

### 生成速度
- 小模型平均每秒生成token数: 1.67 tokens/s
- 大模型平均每秒生成token数: 14.29 tokens/s
- 路由模型平均每秒生成token数: 37.03 tokens/s
- 总平均每秒生成token数: 53.00 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 112.61 | 0.0080 | 3 | 100.00% | 63.3 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 179.64 | 0.0126 | 5 | 60.00% | 60.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 166.39 | 0.0048 | 5 | 80.00% | 36.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 291.28 | 0.0223 | 9 | 22.22% | 54.4 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 177.76 | 0.0094 | 4 | 50.00% | 52.5 |
