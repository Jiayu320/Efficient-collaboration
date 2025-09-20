# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 10
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 87.33 秒
- 平均成本: $0.0231

## 任务规划指标

- 平均任务步骤数: 7.50
- 平均压缩比例: 70.67%
- 平均每步骤Token限制: 42.61 tokens

## 理论性能指标

- 平均理论执行时间: 10.664 秒
- 平均顺序执行时间: 24.804 秒
- 平均并行加速比: 2.33x
- 理论与实际执行时间比例: 0.12x


## 任务分配统计

- 总任务数: 75
- 小模型执行任务数: 43
- 大模型执行任务数: 32
- 小模型任务占比: 57.33%
- 大模型任务占比: 42.67%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 5.256 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 48.719 秒

### 生成速度
- 小模型平均每秒生成token数: 3.85 tokens/s
- 大模型平均每秒生成token数: 5.23 tokens/s
- 路由模型平均每秒生成token数: 5.33 tokens/s
- 总平均每秒生成token数: 14.40 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 51.89 | 0.0183 | 6 | 100.00% | 41.7 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 120.48 | 0.0298 | 9 | 66.67% | 47.8 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 64.63 | 0.0159 | 6 | 66.67% | 35.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 29.86 | 0.0099 | 5 | 40.00% | 26.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 76.50 | 0.0310 | 9 | 55.56% | 38.9 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 176.76 | 0.0242 | 9 | 100.00% | 42.2 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 101.27 | 0.0306 | 7 | 28.57% | 47.1 |
| 8 | In a mathematics test number of participants is... | ✗ | 96.86 | 0.0383 | 9 | 77.78% | 62.2 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 80.44 | 0.0141 | 7 | 71.43% | 41.4 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 74.61 | 0.0193 | 8 | 100.00% | 43.8 |
