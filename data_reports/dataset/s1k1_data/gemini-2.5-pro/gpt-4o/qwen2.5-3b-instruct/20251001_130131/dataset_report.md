# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 正确数量: 2
- 准确率: 20.00%
- 平均执行时间: 146.37 秒
- 平均成本: $0.0244

## 任务规划指标

- 平均任务步骤数: 6.30
- 平均压缩比例: 58.20%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 52.701 秒
- 平均顺序执行时间: 88.593 秒
- 平均并行加速比: 1.82x
- 理论与实际执行时间比例: 0.36x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 5.413 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 102.381 秒

### 生成速度
- 小模型平均每秒生成token数: 9.92 tokens/s
- 大模型平均每秒生成token数: 10.23 tokens/s
- 路由模型平均每秒生成token数: 1.73 tokens/s
- 总平均每秒生成token数: 21.88 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 107.14 | 0.0162 | 5 | 40.00% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 120.14 | 0.0447 | 6 | 66.67% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 146.44 | 0.0193 | 7 | 57.14% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 83.35 | 0.0137 | 6 | 50.00% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 130.89 | 0.0204 | 7 | 71.43% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 379.92 | 0.0120 | 7 | 71.43% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 196.65 | 0.0429 | 5 | 60.00% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 75.26 | 0.0461 | 7 | 42.86% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 148.08 | 0.0141 | 8 | 62.50% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 75.87 | 0.0142 | 5 | 60.00% | 0.0 |
