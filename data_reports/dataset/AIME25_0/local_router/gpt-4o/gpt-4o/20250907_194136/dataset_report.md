# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/AIME25_0.json
- 问题总数: 15
- 正确数量: 5
- 准确率: 33.33%
- 平均执行时间: 16.25 秒
- 平均成本: $0.0042

## 任务规划指标

- 平均任务步骤数: 7.87
- 平均压缩比例: 77.83%
- 平均每步骤Token限制: 31.28 tokens

## 理论性能指标

- 平均理论执行时间: 7.503 秒
- 平均顺序执行时间: 19.040 秒
- 平均并行加速比: 2.57x
- 理论与实际执行时间比例: 0.46x


## 任务分配统计

- 总任务数: 118
- 小模型执行任务数: 3
- 大模型执行任务数: 115
- 小模型任务占比: 2.54%
- 大模型任务占比: 97.46%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.968 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.447 秒

### 生成速度
- 小模型平均每秒生成token数: 6.85 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 28.82 tokens/s
- 总平均每秒生成token数: 35.67 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 19.64 | 0.0049 | 8 | 100.00% | 40.0 |
| 2 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 15.07 | 0.0073 | 9 | 55.56% | 28.3 |
| 3 | The 9 members of a baseball team went to an ice... | ✓ | 12.36 | 0.0030 | 6 | 83.33% | 35.0 |
| 4 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 17.06 | 0.0035 | 8 | 75.00% | 28.1 |
| 5 | There are $8!=40320$ eight-digit positive integ... | ✗ | 17.16 | 0.0033 | 7 | 85.71% | 20.7 |
| 6 | An isosceles trapezoid has an inscribed circle ... | ✗ | 12.48 | 0.0018 | 6 | 66.67% | 27.5 |
| 7 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✓ | 16.24 | 0.0051 | 7 | 85.71% | 34.3 |
| 8 | Let $k$ be real numbers such that the system $|... | ✓ | 15.99 | 0.0041 | 8 | 87.50% | 27.5 |
| 9 | The parabola with equation $y=x^{2}-4$ is rotat... | ✓ | 19.02 | 0.0055 | 9 | 77.78% | 32.8 |
| 10 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 16.72 | 0.0061 | 8 | 75.00% | 35.0 |
| 11 | A piecewise linear periodic function is defined... | ✗ | 16.48 | 0.0044 | 9 | 77.78% | 34.4 |
| 12 | The set of points in 3-dimensional coordinate s... | ✗ | 17.91 | 0.0040 | 9 | 100.00% | 24.4 |
| 13 | Alex divides a disk into four quadrants with tw... | ✗ | 13.37 | 0.0031 | 7 | 57.14% | 28.6 |
| 14 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 17.40 | 0.0048 | 9 | 77.78% | 39.4 |
| 15 | Let $N$ denote the number of ordered triples of... | ✗ | 16.81 | 0.0024 | 8 | 62.50% | 33.1 |
