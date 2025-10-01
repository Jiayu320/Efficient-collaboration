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
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 172.00 秒
- 平均成本: $0.0128

## 任务规划指标

- 平均任务步骤数: 6.50
- 平均压缩比例: 59.18%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 56.718 秒
- 平均顺序执行时间: 94.262 秒
- 平均并行加速比: 1.70x
- 理论与实际执行时间比例: 0.33x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 5.967 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 121.493 秒

### 生成速度
- 小模型平均每秒生成token数: 10.85 tokens/s
- 大模型平均每秒生成token数: 4.64 tokens/s
- 路由模型平均每秒生成token数: 0.80 tokens/s
- 总平均每秒生成token数: 16.30 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 80.11 | 0.0152 | 5 | 60.00% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 262.73 | 0.0130 | 7 | 71.43% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 164.05 | 0.0081 | 7 | 57.14% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 75.64 | 0.0019 | 6 | 50.00% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 133.32 | 0.0073 | 7 | 57.14% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 258.98 | 0.0019 | 7 | 71.43% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 211.22 | 0.0324 | 8 | 37.50% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 206.11 | 0.0313 | 7 | 57.14% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 179.76 | 0.0055 | 6 | 50.00% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 148.13 | 0.0111 | 5 | 80.00% | 0.0 |
