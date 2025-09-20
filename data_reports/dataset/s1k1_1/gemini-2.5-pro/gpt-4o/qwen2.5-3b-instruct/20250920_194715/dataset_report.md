# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 1
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 10
- 正确数量: 3
- 准确率: 30.00%
- 平均执行时间: 88.36 秒
- 平均成本: $0.0379

## 任务规划指标

- 平均任务步骤数: 6.30
- 平均压缩比例: 75.17%
- 平均每步骤Token限制: 58.83 tokens

## 理论性能指标

- 平均理论执行时间: 9.996 秒
- 平均顺序执行时间: 16.490 秒
- 平均并行加速比: 1.65x
- 理论与实际执行时间比例: 0.11x


## 任务分配统计

- 总任务数: 63
- 小模型执行任务数: 0
- 大模型执行任务数: 63
- 小模型任务占比: 0.00%
- 大模型任务占比: 100.00%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 9.780 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 22.996 秒

### 生成速度
- 小模型平均每秒生成token数: 0.00 tokens/s
- 大模型平均每秒生成token数: 10.41 tokens/s
- 路由模型平均每秒生成token数: 18.50 tokens/s
- 总平均每秒生成token数: 28.91 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 72.68 | 0.0333 | 6 | 83.33% | 56.7 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 290.71 | 0.0688 | 8 | 75.00% | 86.2 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 61.23 | 0.0255 | 6 | 83.33% | 41.7 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 44.01 | 0.0220 | 5 | 80.00% | 40.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✓ | 52.40 | 0.0358 | 6 | 83.33% | 50.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 61.01 | 0.0308 | 5 | 80.00% | 56.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 89.87 | 0.0574 | 8 | 50.00% | 62.5 |
| 8 | In a mathematics test number of participants is... | ✗ | 78.93 | 0.0350 | 8 | 50.00% | 66.2 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 60.85 | 0.0385 | 6 | 66.67% | 65.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 71.95 | 0.0321 | 5 | 100.00% | 64.0 |
