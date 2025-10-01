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
- 平均执行时间: 225.68 秒
- 平均成本: $0.0271

## 任务规划指标

- 平均任务步骤数: 13.70
- 平均压缩比例: 49.72%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 98.341 秒
- 平均顺序执行时间: 198.047 秒
- 平均并行加速比: 2.04x
- 理论与实际执行时间比例: 0.44x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 3.147 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 178.143 秒

### 生成速度
- 小模型平均每秒生成token数: 15.24 tokens/s
- 大模型平均每秒生成token数: 4.80 tokens/s
- 路由模型平均每秒生成token数: 3.40 tokens/s
- 总平均每秒生成token数: 23.44 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 104.07 | 0.0209 | 7 | 42.86% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 154.19 | 0.0243 | 9 | 66.67% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 192.81 | 0.0128 | 10 | 60.00% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 145.91 | 0.0081 | 9 | 55.56% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 208.92 | 0.0196 | 14 | 50.00% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 392.96 | 0.0136 | 12 | 58.33% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 222.15 | 0.0931 | 21 | 23.81% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 356.46 | 0.0491 | 20 | 55.00% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 192.74 | 0.0109 | 15 | 40.00% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 286.62 | 0.0182 | 20 | 45.00% | 0.0 |
