# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gemini-2.5-flash-thinking
- 难度阈值: 1
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 10
- 正确数量: 5
- 准确率: 50.00%
- 平均执行时间: 93.01 秒
- 平均成本: $0.0263

## 任务规划指标

- 平均任务步骤数: 5.60
- 平均压缩比例: 76.07%
- 平均每步骤Token限制: 61.73 tokens

## 理论性能指标

- 平均理论执行时间: 7.311 秒
- 平均顺序执行时间: 12.758 秒
- 平均并行加速比: 1.75x
- 理论与实际执行时间比例: 0.08x


## 任务分配统计

- 总任务数: 56
- 小模型执行任务数: 0
- 大模型执行任务数: 56
- 小模型任务占比: 0.00%
- 大模型任务占比: 100.00%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 9.976 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 37.063 秒

### 生成速度
- 小模型平均每秒生成token数: 9.16 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 21.36 tokens/s
- 总平均每秒生成token数: 30.51 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 48.77 | 0.0085 | 3 | 100.00% | 43.3 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✓ | 167.54 | 0.0332 | 5 | 100.00% | 80.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 62.62 | 0.0228 | 6 | 83.33% | 43.3 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 48.97 | 0.0120 | 4 | 75.00% | 40.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 84.70 | 0.0199 | 6 | 66.67% | 46.7 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✓ | 59.41 | 0.0211 | 5 | 100.00% | 48.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 136.23 | 0.0351 | 6 | 33.33% | 101.7 |
| 8 | In a mathematics test number of participants is... | ✗ | 99.53 | 0.0468 | 8 | 50.00% | 90.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 79.58 | 0.0184 | 6 | 66.67% | 50.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✓ | 142.77 | 0.0451 | 7 | 85.71% | 74.3 |
