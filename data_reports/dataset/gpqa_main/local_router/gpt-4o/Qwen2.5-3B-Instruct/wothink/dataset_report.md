# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 5
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 161.03 秒
- 平均成本: $0.0124


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 1.60 |
| Dependency Structure And Flow | 3.00 |
| Plan Relevance And Efficiency | 1.40 |
| Plan Soundness And Decomposition | 1.40 |
| Task Clarity And Executability | 4.00 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.33 |
| Correctness And Factual Accuracy | 3.48 |
| Effective Use Of Context | 4.81 |
| Instruction Following And Adherence | 4.14 |
| Relevance And Conciseness | 4.24 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.50 |
| Correctness And Factual Accuracy | 3.00 |
| Effective Use Of Context | 3.00 |
| Instruction Following And Adherence | 2.00 |
| Relevance And Conciseness | 3.00 |
## 任务规划指标

- 平均任务步骤数: 4.60
- 平均压缩比例: 63.33%
- 平均每步骤Token限制: 56.08 tokens

## 理论性能指标

- 平均理论执行时间: 6.074 秒
- 平均顺序执行时间: 11.763 秒
- 平均并行加速比: 1.92x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.792 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 149.084 秒

### 生成速度
- 小模型平均每秒生成token数: 1.67 tokens/s
- 大模型平均每秒生成token数: 30.67 tokens/s
- 路由模型平均每秒生成token数: 22.76 tokens/s
- 总平均每秒生成token数: 55.09 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 155.00 | 0.0105 | 4 | 100.00% | 62.5 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 122.94 | 0.0088 | 3 | 66.67% | 56.7 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 135.94 | 0.0070 | 4 | 50.00% | 50.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 241.43 | 0.0194 | 8 | 25.00% | 53.8 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 149.82 | 0.0162 | 4 | 75.00% | 57.5 |
