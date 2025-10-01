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
- 平均执行时间: 142.37 秒
- 平均成本: $0.0215

## 任务规划指标

- 平均任务步骤数: 6.60
- 平均压缩比例: 66.04%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 58.210 秒
- 平均顺序执行时间: 88.971 秒
- 平均并行加速比: 1.62x
- 理论与实际执行时间比例: 0.41x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 4.705 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 104.525 秒

### 生成速度
- 小模型平均每秒生成token数: 10.33 tokens/s
- 大模型平均每秒生成token数: 7.32 tokens/s
- 路由模型平均每秒生成token数: 3.30 tokens/s
- 总平均每秒生成token数: 20.94 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 113.99 | 0.0233 | 6 | 83.33% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 269.85 | 0.0209 | 5 | 100.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 108.85 | 0.0100 | 7 | 57.14% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 60.17 | 0.0075 | 6 | 50.00% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 133.07 | 0.0168 | 6 | 66.67% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 156.55 | 0.0145 | 5 | 80.00% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 109.83 | 0.0502 | 8 | 25.00% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 155.12 | 0.0414 | 8 | 50.00% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 225.83 | 0.0199 | 8 | 62.50% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 90.40 | 0.0106 | 7 | 85.71% | 0.0 |
