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
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 66.75 秒
- 平均成本: $0.0179

## 任务规划指标

- 平均任务步骤数: 7.90
- 平均压缩比例: 67.22%
- 平均每步骤Token限制: 43.27 tokens

## 理论性能指标

- 平均理论执行时间: 11.086 秒
- 平均顺序执行时间: 26.008 秒
- 平均并行加速比: 2.34x
- 理论与实际执行时间比例: 0.17x


## 任务分配统计

- 总任务数: 79
- 小模型执行任务数: 42
- 大模型执行任务数: 37
- 小模型任务占比: 53.16%
- 大模型任务占比: 46.84%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 3.187 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 42.150 秒

### 生成速度
- 小模型平均每秒生成token数: 5.68 tokens/s
- 大模型平均每秒生成token数: 2.54 tokens/s
- 路由模型平均每秒生成token数: 7.71 tokens/s
- 总平均每秒生成token数: 15.94 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 41.44 | 0.0130 | 5 | 100.00% | 42.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 62.09 | 0.0226 | 9 | 66.67% | 45.6 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 61.15 | 0.0167 | 7 | 100.00% | 52.9 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 45.73 | 0.0087 | 5 | 40.00% | 27.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 40.75 | 0.0108 | 6 | 66.67% | 38.3 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 89.69 | 0.0229 | 9 | 77.78% | 42.2 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 53.44 | 0.0304 | 9 | 33.33% | 54.4 |
| 8 | In a mathematics test number of participants is... | ✗ | 112.09 | 0.0255 | 10 | 60.00% | 49.5 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 64.20 | 0.0148 | 10 | 50.00% | 43.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 96.89 | 0.0138 | 9 | 77.78% | 37.8 |
