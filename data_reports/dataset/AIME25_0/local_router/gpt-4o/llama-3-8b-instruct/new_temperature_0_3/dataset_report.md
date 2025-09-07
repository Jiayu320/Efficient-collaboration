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
- 正确数量: 3
- 准确率: 20.00%
- 平均执行时间: 17.73 秒
- 平均成本: $0.0027

## 任务规划指标

- 平均任务步骤数: 8.20
- 平均压缩比例: 77.45%
- 平均每步骤Token限制: 31.30 tokens

## 理论性能指标

- 平均理论执行时间: 7.604 秒
- 平均顺序执行时间: 19.727 秒
- 平均并行加速比: 2.63x
- 理论与实际执行时间比例: 0.43x


## 任务分配统计

- 总任务数: 123
- 小模型执行任务数: 6
- 大模型执行任务数: 117
- 小模型任务占比: 4.88%
- 大模型任务占比: 95.12%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.175 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.793 秒

### 生成速度
- 小模型平均每秒生成token数: 0.38 tokens/s
- 大模型平均每秒生成token数: 5.50 tokens/s
- 路由模型平均每秒生成token数: 26.60 tokens/s
- 总平均每秒生成token数: 32.48 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 21.59 | 0.0045 | 8 | 100.00% | 41.2 |
| 2 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 14.10 | 0.0000 | 10 | 50.00% | 31.5 |
| 3 | The 9 members of a baseball team went to an ice... | ✓ | 13.39 | 0.0026 | 5 | 100.00% | 34.0 |
| 4 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 18.55 | 0.0021 | 7 | 85.71% | 23.6 |
| 5 | There are $8!=40320$ eight-digit positive integ... | ✗ | 13.83 | 0.0012 | 7 | 85.71% | 18.6 |
| 6 | An isosceles trapezoid has an inscribed circle ... | ✗ | 14.57 | 0.0016 | 8 | 50.00% | 27.5 |
| 7 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✓ | 15.74 | 0.0014 | 8 | 62.50% | 35.0 |
| 8 | Let $k$ be real numbers such that the system $|... | ✗ | 19.53 | 0.0029 | 8 | 87.50% | 30.6 |
| 9 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 23.69 | 0.0062 | 9 | 100.00% | 37.2 |
| 10 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 21.12 | 0.0038 | 10 | 80.00% | 34.5 |
| 11 | A piecewise linear periodic function is defined... | ✗ | 19.42 | 0.0035 | 10 | 70.00% | 32.0 |
| 12 | The set of points in 3-dimensional coordinate s... | ✗ | 17.60 | 0.0033 | 9 | 77.78% | 24.4 |
| 13 | Alex divides a disk into four quadrants with tw... | ✗ | 20.03 | 0.0030 | 8 | 75.00% | 32.5 |
| 14 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 16.69 | 0.0038 | 8 | 87.50% | 35.6 |
| 15 | Let $N$ denote the number of ordered triples of... | ✗ | 16.16 | 0.0006 | 8 | 50.00% | 31.2 |
