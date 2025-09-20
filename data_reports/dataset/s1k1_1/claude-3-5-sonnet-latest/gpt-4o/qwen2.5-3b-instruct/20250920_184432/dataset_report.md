# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 1
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 10
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 37.66 秒
- 平均成本: $0.0369

## 任务规划指标

- 平均任务步骤数: 7.70
- 平均压缩比例: 71.09%
- 平均每步骤Token限制: 41.40 tokens

## 理论性能指标

- 平均理论执行时间: 10.457 秒
- 平均顺序执行时间: 24.225 秒
- 平均并行加速比: 2.31x
- 理论与实际执行时间比例: 0.28x


## 任务分配统计

- 总任务数: 77
- 小模型执行任务数: 0
- 大模型执行任务数: 77
- 小模型任务占比: 0.00%
- 大模型任务占比: 100.00%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 3.018 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 16.902 秒

### 生成速度
- 小模型平均每秒生成token数: 0.00 tokens/s
- 大模型平均每秒生成token数: 24.43 tokens/s
- 路由模型平均每秒生成token数: 12.27 tokens/s
- 总平均每秒生成token数: 36.70 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 38.55 | 0.0274 | 6 | 100.00% | 41.7 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 43.28 | 0.0486 | 9 | 66.67% | 43.3 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 31.40 | 0.0261 | 6 | 83.33% | 33.3 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 24.85 | 0.0161 | 5 | 40.00% | 26.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 38.55 | 0.0375 | 7 | 71.43% | 37.9 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 43.15 | 0.0434 | 9 | 66.67% | 41.1 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 36.74 | 0.0472 | 8 | 37.50% | 47.5 |
| 8 | In a mathematics test number of participants is... | ✗ | 44.75 | 0.0595 | 10 | 80.00% | 56.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 34.31 | 0.0208 | 8 | 87.50% | 45.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 41.03 | 0.0421 | 9 | 77.78% | 42.2 |
