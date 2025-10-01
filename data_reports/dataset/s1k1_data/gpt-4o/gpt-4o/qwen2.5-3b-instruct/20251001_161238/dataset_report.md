# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 121.30 秒
- 平均成本: $0.0251

## 任务规划指标

- 平均任务步骤数: 7.10
- 平均压缩比例: 68.15%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 58.401 秒
- 平均顺序执行时间: 86.520 秒
- 平均并行加速比: 1.56x
- 理论与实际执行时间比例: 0.48x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.731 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 107.124 秒

### 生成速度
- 小模型平均每秒生成token数: 13.55 tokens/s
- 大模型平均每秒生成token数: 9.98 tokens/s
- 路由模型平均每秒生成token数: 3.34 tokens/s
- 总平均每秒生成token数: 26.87 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 100.23 | 0.0193 | 6 | 83.33% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 230.34 | 0.0457 | 8 | 75.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 67.43 | 0.0230 | 7 | 71.43% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 95.92 | 0.0163 | 7 | 57.14% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 199.67 | 0.0289 | 7 | 57.14% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 76.37 | 0.0095 | 7 | 85.71% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 67.10 | 0.0556 | 8 | 37.50% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 136.10 | 0.0083 | 7 | 85.71% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 88.55 | 0.0223 | 7 | 57.14% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 151.30 | 0.0216 | 7 | 71.43% | 0.0 |
