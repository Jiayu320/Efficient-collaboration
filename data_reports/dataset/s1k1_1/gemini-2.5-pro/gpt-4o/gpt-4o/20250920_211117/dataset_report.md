# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 1
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 10
- 正确数量: 4
- 准确率: 40.00%
- 平均执行时间: 105.16 秒
- 平均成本: $0.0285

## 任务规划指标

- 平均任务步骤数: 4.89
- 平均压缩比例: 73.15%
- 平均每步骤Token限制: 62.84 tokens

## 理论性能指标

- 平均理论执行时间: 8.543 秒
- 平均顺序执行时间: 13.548 秒
- 平均并行加速比: 1.56x
- 理论与实际执行时间比例: 0.08x


## 任务分配统计

- 总任务数: 44
- 小模型执行任务数: 0
- 大模型执行任务数: 44
- 小模型任务占比: 0.00%
- 大模型任务占比: 100.00%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 12.181 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 43.685 秒

### 生成速度
- 小模型平均每秒生成token数: 4.29 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 14.04 tokens/s
- 总平均每秒生成token数: 18.33 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 63.40 | 0.0173 | 3 | 100.00% | 43.3 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✓ | 166.22 | 0.0415 | 5 | 100.00% | 92.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 60.92 | 0.0240 | 5 | 80.00% | 40.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 88.94 | 0.0197 | 4 | 75.00% | 47.5 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 87.77 | 0.0310 | 5 | 80.00% | 54.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 19.55 | 0.0000 | - | - | - |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 150.39 | 0.0697 | 9 | 33.33% | 82.2 |
| 8 | In a mathematics test number of participants is... | ✗ | 238.59 | 0.0255 | 5 | 40.00% | 84.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 94.29 | 0.0251 | 4 | 50.00% | 65.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✓ | 81.57 | 0.0310 | 4 | 100.00% | 57.5 |
