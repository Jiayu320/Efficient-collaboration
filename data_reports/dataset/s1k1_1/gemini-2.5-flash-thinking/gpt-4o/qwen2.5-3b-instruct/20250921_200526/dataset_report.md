# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-flash-thinking
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 1
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 122.91 秒
- 平均成本: $0.0031


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
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 37.50 tokens

## 理论性能指标

- 平均理论执行时间: 6.217 秒
- 平均顺序执行时间: 15.367 秒
- 平均并行加速比: 2.47x
- 理论与实际执行时间比例: 0.05x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 3.602 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 108.504 秒

### 生成速度
- 小模型平均每秒生成token数: 2.80 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 44.72 tokens/s
- 总平均每秒生成token数: 47.52 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 122.91 | 0.0031 | 4 | 100.00% | 37.5 |
