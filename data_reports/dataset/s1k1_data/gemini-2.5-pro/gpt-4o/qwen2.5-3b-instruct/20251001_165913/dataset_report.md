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
- 平均执行时间: 204.05 秒
- 平均成本: $0.0240

## 任务规划指标

- 平均任务步骤数: 11.60
- 平均压缩比例: 52.29%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 87.342 秒
- 平均顺序执行时间: 167.493 秒
- 平均并行加速比: 1.88x
- 理论与实际执行时间比例: 0.43x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 3.678 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 156.110 秒

### 生成速度
- 小模型平均每秒生成token数: 12.82 tokens/s
- 大模型平均每秒生成token数: 4.80 tokens/s
- 路由模型平均每秒生成token数: 3.36 tokens/s
- 总平均每秒生成token数: 20.97 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 74.10 | 0.0164 | 6 | 50.00% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 217.22 | 0.0240 | 7 | 71.43% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 238.34 | 0.0156 | 12 | 50.00% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 131.31 | 0.0086 | 7 | 57.14% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 196.20 | 0.0190 | 10 | 50.00% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 228.74 | 0.0188 | 10 | 70.00% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 224.18 | 0.0790 | 17 | 35.29% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 307.66 | 0.0341 | 14 | 42.86% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 175.40 | 0.0106 | 13 | 46.15% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 247.37 | 0.0141 | 20 | 50.00% | 0.0 |
