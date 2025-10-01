# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 正确数量: 2
- 准确率: 20.00%
- 平均执行时间: 51.74 秒
- 平均成本: $0.0401

## 任务规划指标

- 平均任务步骤数: 6.50
- 平均压缩比例: 69.48%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 36.864 秒
- 平均顺序执行时间: 56.678 秒
- 平均并行加速比: 1.64x
- 理论与实际执行时间比例: 0.71x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 5.008 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 8.935 秒

### 生成速度
- 小模型平均每秒生成token数: 34.67 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 7.97 tokens/s
- 总平均每秒生成token数: 42.64 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 67.40 | 0.0267 | 6 | 83.33% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 46.25 | 0.0345 | 5 | 100.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 43.80 | 0.0340 | 5 | 100.00% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 31.12 | 0.0144 | 6 | 50.00% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 52.42 | 0.0383 | 7 | 57.14% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 48.91 | 0.0388 | 6 | 66.67% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 40.45 | 0.0796 | 8 | 25.00% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 69.70 | 0.0464 | 7 | 57.14% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 61.97 | 0.0476 | 9 | 55.56% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 55.40 | 0.0404 | 6 | 100.00% | 0.0 |
