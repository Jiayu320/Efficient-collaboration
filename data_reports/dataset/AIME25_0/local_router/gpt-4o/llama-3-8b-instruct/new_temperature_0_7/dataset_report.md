# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/AIME25_0.json
- 问题总数: 15
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 17.91 秒
- 平均成本: $0.0027

## 任务规划指标

- 平均任务步骤数: 7.73
- 平均压缩比例: 79.07%
- 平均每步骤Token限制: 29.92 tokens

## 理论性能指标

- 平均理论执行时间: 7.195 秒
- 平均顺序执行时间: 18.559 秒
- 平均并行加速比: 2.59x
- 理论与实际执行时间比例: 0.40x


## 任务分配统计

- 总任务数: 116
- 小模型执行任务数: 5
- 大模型执行任务数: 111
- 小模型任务占比: 4.31%
- 大模型任务占比: 95.69%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.121 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 12.643 秒

### 生成速度
- 小模型平均每秒生成token数: 1.61 tokens/s
- 大模型平均每秒生成token数: 6.03 tokens/s
- 路由模型平均每秒生成token数: 26.00 tokens/s
- 总平均每秒生成token数: 33.64 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 17.44 | 0.0025 | 8 | 75.00% | 33.1 |
| 2 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 17.47 | 0.0029 | 8 | 62.50% | 29.4 |
| 3 | The 9 members of a baseball team went to an ice... | ✗ | 12.31 | 0.0016 | 6 | 83.33% | 25.0 |
| 4 | Find the number of ordered pairs $(x,y)$, where... | ✓ | 15.95 | 0.0035 | 6 | 100.00% | 40.8 |
| 5 | There are $8!=40320$ eight-digit positive integ... | ✓ | 16.58 | 0.0025 | 7 | 85.71% | 27.9 |
| 6 | An isosceles trapezoid has an inscribed circle ... | ✗ | 15.78 | 0.0012 | 7 | 71.43% | 28.3 |
| 7 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 18.74 | 0.0008 | 6 | 83.33% | 22.5 |
| 8 | Let $k$ be real numbers such that the system $|... | ✗ | 23.91 | 0.0015 | 8 | 87.50% | 27.5 |
| 9 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 20.22 | 0.0034 | 9 | 88.89% | 31.1 |
| 10 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 16.22 | 0.0040 | 8 | 75.00% | 21.2 |
| 11 | A piecewise linear periodic function is defined... | ✓ | 21.18 | 0.0068 | 10 | 90.00% | 30.5 |
| 12 | The set of points in 3-dimensional coordinate s... | ✓ | 23.09 | 0.0048 | 9 | 88.89% | 30.6 |
| 13 | Alex divides a disk into four quadrants with tw... | ✗ | 15.28 | 0.0014 | 6 | 83.33% | 35.8 |
| 14 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 17.85 | 0.0022 | 9 | 66.67% | 29.4 |
| 15 | Let $N$ denote the number of ordered triples of... | ✗ | 16.64 | 0.0012 | 9 | 44.44% | 35.6 |
