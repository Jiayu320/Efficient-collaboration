# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 5
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 206.54 秒
- 平均成本: $0.0157


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 2.00 |
| Dependency Structure And Flow | 3.40 |
| Plan Relevance And Efficiency | 2.00 |
| Plan Soundness And Decomposition | 2.20 |
| Task Clarity And Executability | 4.80 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.09 |
| Correctness And Factual Accuracy | 2.45 |
| Effective Use Of Context | 2.91 |
| Instruction Following And Adherence | 2.55 |
| Relevance And Conciseness | 3.91 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.86 |
| Correctness And Factual Accuracy | 2.43 |
| Effective Use Of Context | 3.86 |
| Instruction Following And Adherence | 2.71 |
| Relevance And Conciseness | 4.14 |
## 任务规划指标

- 平均任务步骤数: 5.80
- 平均压缩比例: 84.50%
- 平均每步骤Token限制: 50.15 tokens

## 理论性能指标

- 平均理论执行时间: 7.269 秒
- 平均顺序执行时间: 23.649 秒
- 平均并行加速比: 3.27x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.469 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 194.840 秒

### 生成速度
- 小模型平均每秒生成token数: 3.01 tokens/s
- 大模型平均每秒生成token数: 22.42 tokens/s
- 路由模型平均每秒生成token数: 31.13 tokens/s
- 总平均每秒生成token数: 56.57 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 224.20 | 0.0186 | 6 | 100.00% | 45.0 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 170.39 | 0.0165 | 5 | 80.00% | 54.0 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 252.22 | 0.0211 | 8 | 62.50% | 53.8 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 200.99 | 0.0109 | 5 | 100.00% | 44.0 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 184.89 | 0.0113 | 5 | 80.00% | 54.0 |
