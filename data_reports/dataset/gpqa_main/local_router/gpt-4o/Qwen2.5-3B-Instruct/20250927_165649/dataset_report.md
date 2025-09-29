# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 5
- 正确数量: 1
- 准确率: 20.00%
- 平均执行时间: 193.62 秒
- 平均成本: $0.0135


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 2.60 |
| Dependency Structure And Flow | 4.20 |
| Plan Relevance And Efficiency | 3.40 |
| Plan Soundness And Decomposition | 3.00 |
| Task Clarity And Executability | 4.20 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.57 |
| Correctness And Factual Accuracy | 3.96 |
| Effective Use Of Context | 4.57 |
| Instruction Following And Adherence | 4.04 |
| Relevance And Conciseness | 4.48 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.33 |
| Correctness And Factual Accuracy | 3.00 |
| Effective Use Of Context | 5.00 |
| Instruction Following And Adherence | 3.67 |
| Relevance And Conciseness | 4.33 |
## 任务规划指标

- 平均任务步骤数: 5.20
- 平均压缩比例: 74.44%
- 平均每步骤Token限制: 63.02 tokens

## 理论性能指标

- 平均理论执行时间: 5.598 秒
- 平均顺序执行时间: 12.959 秒
- 平均并行加速比: 2.36x
- 理论与实际执行时间比例: 0.03x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.396 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 183.608 秒

### 生成速度
- 小模型平均每秒生成token数: 2.03 tokens/s
- 大模型平均每秒生成token数: 19.59 tokens/s
- 路由模型平均每秒生成token数: 35.16 tokens/s
- 总平均每秒生成token数: 56.78 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 146.66 | 0.0113 | 4 | 75.00% | 65.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 193.71 | 0.0116 | 5 | 100.00% | 64.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 164.54 | 0.0078 | 4 | 100.00% | 55.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 297.53 | 0.0206 | 9 | 22.22% | 61.1 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 165.68 | 0.0161 | 4 | 75.00% | 70.0 |
