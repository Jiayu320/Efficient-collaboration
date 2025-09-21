# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen2.5-3b-instruct
- 难度阈值: 1
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 10
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 183.91 秒
- 平均成本: $0.0137


## 平均评估分数

### 规划器平均分数
|维度|平均分 (满分5分)|
|---|---|
|Plansoundnessanddecomposition|2.90|
|Dependencystructureandflow|3.40|
|Taskclarityandexecutability|4.20|
|Attributeaccuracy|2.70|
|Planrelevanceandefficiency|3.30|

### 执行器平均分数
|维度|平均分 (满分5分)|
|---|---|
|Instructionfollowingandadherence|3.29|
|Correctnessandfactualaccuracy|3.31|
|Effectiveuseofcontext|3.14|
|Clarityandmachineusability|4.05|
|Relevanceandconciseness|3.98|
## 任务规划指标

- 平均任务步骤数: 4.30
- 平均压缩比例: 74.29%
- 平均每步骤Token限制: 36.04 tokens

## 理论性能指标

- 平均理论执行时间: 7.089 秒
- 平均顺序执行时间: 22.106 秒
- 平均并行加速比: 4.68x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.154 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 173.319 秒

### 生成速度
- 小模型平均每秒生成token数: 0.00 tokens/s
- 大模型平均每秒生成token数: 11.12 tokens/s
- 路由模型平均每秒生成token数: 13.26 tokens/s
- 总平均每秒生成token数: 24.38 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 175.20 | 0.0133 | 5 | 100.00% | 36.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✓ | 131.78 | 0.0010 | 0 | 0.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 190.46 | 0.0138 | 4 | 100.00% | 40.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 143.19 | 0.0076 | 3 | 100.00% | 30.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 233.92 | 0.0198 | 4 | 100.00% | 47.5 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 201.21 | 0.0183 | 5 | 100.00% | 44.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 163.32 | 0.0075 | 5 | 20.00% | 50.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 224.49 | 0.0270 | 7 | 42.86% | 42.9 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 198.88 | 0.0150 | 5 | 80.00% | 36.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 176.65 | 0.0137 | 5 | 100.00% | 34.0 |
