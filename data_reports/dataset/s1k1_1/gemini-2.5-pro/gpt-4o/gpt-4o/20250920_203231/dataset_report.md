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
- 正确数量: 5
- 准确率: 50.00%
- 平均执行时间: 122.65 秒
- 平均成本: $0.0392

## 任务规划指标

- 平均任务步骤数: 5.70
- 平均压缩比例: 71.94%
- 平均每步骤Token限制: 80.04 tokens

## 理论性能指标

- 平均理论执行时间: 10.005 秒
- 平均顺序执行时间: 16.094 秒
- 平均并行加速比: 1.62x
- 理论与实际执行时间比例: 0.08x


## 任务分配统计

- 总任务数: 57
- 小模型执行任务数: 0
- 大模型执行任务数: 57
- 小模型任务占比: 0.00%
- 大模型任务占比: 100.00%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 14.848 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 37.072 秒

### 生成速度
- 小模型平均每秒生成token数: 6.36 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 13.77 tokens/s
- 总平均每秒生成token数: 20.13 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 66.92 | 0.0164 | 3 | 100.00% | 33.3 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✓ | 280.71 | 0.0727 | 6 | 100.00% | 193.3 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 71.30 | 0.0257 | 5 | 60.00% | 46.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 68.86 | 0.0199 | 5 | 60.00% | 42.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 107.01 | 0.0326 | 6 | 66.67% | 95.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✓ | 111.58 | 0.0259 | 4 | 100.00% | 77.5 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 136.27 | 0.0689 | 7 | 28.57% | 154.3 |
| 8 | In a mathematics test number of participants is... | ✗ | 119.64 | 0.0550 | 8 | 37.50% | 63.8 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✓ | 115.06 | 0.0314 | 6 | 66.67% | 46.7 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 149.13 | 0.0433 | 7 | 100.00% | 48.6 |
