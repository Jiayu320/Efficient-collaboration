# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: deepseek-chat
- 路由模型: gemini-2.5-flash-thinking
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 241.25 秒
- 平均成本: $0.0017

## 任务规划指标

- 平均任务步骤数: 13.22
- 平均压缩比例: 48.23%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 132.959 秒
- 平均顺序执行时间: 305.409 秒
- 平均并行加速比: 2.30x
- 理论与实际执行时间比例: 0.55x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 3.005 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 196.406 秒

### 生成速度
- 小模型平均每秒生成token数: 11.69 tokens/s
- 大模型平均每秒生成token数: 6.26 tokens/s
- 路由模型平均每秒生成token数: 0.00 tokens/s
- 总平均每秒生成token数: 17.95 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 106.66 | 0.0013 | 10 | 50.00% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 256.18 | 0.0022 | 10 | 60.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 133.85 | 0.0001 | 9 | 55.56% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 68.56 | 0.0004 | 7 | 57.14% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 406.26 | 0.0013 | 13 | 38.46% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 0.00 | 0.0000 | - | - | - |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 143.73 | 0.0078 | 18 | 27.78% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 868.59 | 0.0007 | 16 | 56.25% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 200.52 | 0.0009 | 18 | 33.33% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 228.15 | 0.0026 | 18 | 55.56% | 0.0 |
