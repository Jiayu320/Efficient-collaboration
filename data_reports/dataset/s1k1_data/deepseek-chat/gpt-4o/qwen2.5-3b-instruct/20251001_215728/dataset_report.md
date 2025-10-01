# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: deepseek-chat
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 正确数量: 2
- 准确率: 20.00%
- 平均执行时间: 234.33 秒
- 平均成本: $0.0254

## 任务规划指标

- 平均任务步骤数: 13.10
- 平均压缩比例: 51.16%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 93.081 秒
- 平均顺序执行时间: 194.956 秒
- 平均并行加速比: 2.15x
- 理论与实际执行时间比例: 0.40x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.609 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 209.869 秒

### 生成速度
- 小模型平均每秒生成token数: 18.10 tokens/s
- 大模型平均每秒生成token数: 7.01 tokens/s
- 路由模型平均每秒生成token数: 2.89 tokens/s
- 总平均每秒生成token数: 28.00 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 112.43 | 0.0239 | 8 | 62.50% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 271.62 | 0.0435 | 11 | 72.73% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 145.48 | 0.0077 | 14 | 50.00% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 188.89 | 0.0044 | 11 | 54.55% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 192.77 | 0.0084 | 13 | 38.46% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✓ | 459.95 | 0.0409 | 14 | 57.14% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 171.22 | 0.0798 | 17 | 35.29% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 189.05 | 0.0368 | 14 | 50.00% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 140.18 | 0.0011 | 15 | 26.67% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 471.74 | 0.0074 | 14 | 64.29% | 0.0 |
