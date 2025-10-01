# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 204.12 秒
- 平均成本: $0.0223

## 任务规划指标

- 平均任务步骤数: 7.40
- 平均压缩比例: 51.63%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 58.319 秒
- 平均顺序执行时间: 108.852 秒
- 平均并行加速比: 1.91x
- 理论与实际执行时间比例: 0.29x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 6.710 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 140.871 秒

### 生成速度
- 小模型平均每秒生成token数: 12.27 tokens/s
- 大模型平均每秒生成token数: 4.92 tokens/s
- 路由模型平均每秒生成token数: 2.67 tokens/s
- 总平均每秒生成token数: 19.86 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 179.37 | 0.0138 | 6 | 50.00% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 252.15 | 0.0235 | 7 | 57.14% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 117.01 | 0.0110 | 6 | 66.67% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 133.83 | 0.0165 | 7 | 42.86% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 249.13 | 0.0193 | 8 | 62.50% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 216.03 | 0.0219 | 5 | 60.00% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 200.66 | 0.0510 | 10 | 30.00% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 238.97 | 0.0298 | 8 | 50.00% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 125.76 | 0.0222 | 10 | 40.00% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 328.27 | 0.0142 | 7 | 57.14% | 0.0 |
