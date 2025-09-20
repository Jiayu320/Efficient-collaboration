# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-7-sonnet-latest
- 难度阈值: 1
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 10
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 56.65 秒
- 平均成本: $0.0392

## 任务规划指标

- 平均任务步骤数: 7.10
- 平均压缩比例: 76.75%
- 平均每步骤Token限制: 44.56 tokens

## 理论性能指标

- 平均理论执行时间: 9.909 秒
- 平均顺序执行时间: 20.545 秒
- 平均并行加速比: 2.07x
- 理论与实际执行时间比例: 0.17x


## 任务分配统计

- 总任务数: 71
- 小模型执行任务数: 0
- 大模型执行任务数: 71
- 小模型任务占比: 0.00%
- 大模型任务占比: 100.00%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 4.992 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 19.655 秒

### 生成速度
- 小模型平均每秒生成token数: 0.00 tokens/s
- 大模型平均每秒生成token数: 17.19 tokens/s
- 路由模型平均每秒生成token数: 14.05 tokens/s
- 总平均每秒生成token数: 31.24 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 38.78 | 0.0295 | 6 | 83.33% | 55.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 114.66 | 0.0445 | 6 | 100.00% | 51.7 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 44.51 | 0.0348 | 8 | 75.00% | 38.8 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 41.66 | 0.0248 | 6 | 66.67% | 29.2 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 44.58 | 0.0507 | 6 | 83.33% | 46.7 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 46.07 | 0.0374 | 8 | 87.50% | 39.4 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 47.02 | 0.0495 | 7 | 42.86% | 67.1 |
| 8 | In a mathematics test number of participants is... | ✗ | 112.81 | 0.0518 | 9 | 55.56% | 44.4 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 37.01 | 0.0333 | 7 | 85.71% | 32.1 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 39.44 | 0.0352 | 8 | 87.50% | 41.2 |
