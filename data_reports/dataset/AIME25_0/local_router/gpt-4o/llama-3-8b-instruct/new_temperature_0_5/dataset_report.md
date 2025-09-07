# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft (New)
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/AIME25_0.json
- 问题总数: 15
- 正确数量: 8
- 准确率: 53.33%
- 平均执行时间: 17.69 秒
- 平均成本: $0.0033

## 任务规划指标

- 平均任务步骤数: 7.87
- 平均压缩比例: 81.39%
- 平均每步骤Token限制: 34.94 tokens

## 理论性能指标

- 平均理论执行时间: 7.675 秒
- 平均顺序执行时间: 19.139 秒
- 平均并行加速比: 2.52x
- 理论与实际执行时间比例: 0.43x


## 任务分配统计

- 总任务数: 118
- 小模型执行任务数: 5
- 大模型执行任务数: 113
- 小模型任务占比: 4.24%
- 大模型任务占比: 95.76%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.120 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.809 秒

### 生成速度
- 小模型平均每秒生成token数: 1.11 tokens/s
- 大模型平均每秒生成token数: 6.80 tokens/s
- 路由模型平均每秒生成token数: 26.19 tokens/s
- 总平均每秒生成token数: 34.09 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 22.74 | 0.0041 | 8 | 87.50% | 41.2 |
| 2 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 16.32 | 0.0046 | 9 | 55.56% | 40.0 |
| 3 | The 9 members of a baseball team went to an ice... | ✓ | 16.64 | 0.0033 | 7 | 85.71% | 40.0 |
| 4 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 15.10 | 0.0014 | 8 | 75.00% | 36.9 |
| 5 | There are $8!=40320$ eight-digit positive integ... | ✗ | 16.69 | 0.0018 | 7 | 85.71% | 25.0 |
| 6 | An isosceles trapezoid has an inscribed circle ... | ✗ | 14.93 | 0.0019 | 8 | 75.00% | 25.6 |
| 7 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 15.36 | 0.0008 | 6 | 66.67% | 26.7 |
| 8 | Let $k$ be real numbers such that the system $|... | ✓ | 22.08 | 0.0032 | 10 | 90.00% | 31.5 |
| 9 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 19.51 | 0.0041 | 8 | 100.00% | 26.9 |
| 10 | The 27 cells of a $3\times9$ grid are filled in... | ✓ | 12.77 | 0.0030 | 6 | 83.33% | 37.5 |
| 11 | A piecewise linear periodic function is defined... | ✓ | 19.79 | 0.0051 | 10 | 70.00% | 31.0 |
| 12 | The set of points in 3-dimensional coordinate s... | ✗ | 19.77 | 0.0044 | 9 | 100.00% | 36.1 |
| 13 | Alex divides a disk into four quadrants with tw... | ✓ | 14.76 | 0.0014 | 7 | 71.43% | 32.1 |
| 14 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✓ | 16.45 | 0.0028 | 8 | 75.00% | 35.0 |
| 15 | Let $N$ denote the number of ordered triples of... | ✓ | 22.41 | 0.0069 | 7 | 100.00% | 58.6 |
