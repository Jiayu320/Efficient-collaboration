# 单模型数据集处理报告

## 模型信息

- 模型: qwen/qwen3-4b:free
- 延迟 (TTFT): 0.690 秒
- 吞吐量: 184.10 tokens/s

## 概述

- 数据集: dataset/original_data/AIME25_0.json
- 问题总数: 15
- 正确数量: 13
- 准确率: 86.67%
- 平均执行时间: 86.71 秒
- 平均理论时间: 3.30 秒
- 实际/理论时间比率: 26.27x
- 平均成本: $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 2.168 秒
- 平均每秒生成token数: 10.44 tokens/s
- 理论每秒生成token数: 184.10 tokens/s
- 实际/理论吞吐量比率: 0.06x

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 23.29 | 3.24 | 0.0000 |
| 2 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✓ | 64.94 | 6.39 | 0.0000 |
| 3 | The 9 members of a baseball team went to an ice... | ✓ | 55.46 | 5.40 | 0.0000 |
| 4 | Find the number of ordered pairs $(x,y)$, where... | ✓ | 46.05 | 5.60 | 0.0000 |
| 5 | There are $8!=40320$ eight-digit positive integ... | ✓ | 61.42 | 8.14 | 0.0000 |
| 6 | An isosceles trapezoid has an inscribed circle ... | ✓ | 35.51 | 4.91 | 0.0000 |
| 7 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✓ | 152.19 | 0.70 | 0.0000 |
| 8 | Let $k$ be real numbers such that the system $|... | ✓ | 35.42 | 7.92 | 0.0000 |
| 9 | The parabola with equation $y=x^{2}-4$ is rotat... | ✓ | 116.82 | 0.70 | 0.0000 |
| 10 | The 27 cells of a $3\times9$ grid are filled in... | ✓ | 105.34 | 0.70 | 0.0000 |
| 11 | A piecewise linear periodic function is defined... | ✓ | 127.80 | 0.70 | 0.0000 |
| 12 | The set of points in 3-dimensional coordinate s... | ✗ | 99.55 | 0.69 | 0.0000 |
| 13 | Alex divides a disk into four quadrants with tw... | ✗ | 135.92 | 3.05 | 0.0000 |
| 14 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✓ | 116.16 | 0.70 | 0.0000 |
| 15 | Let $N$ denote the number of ordered triples of... | ✓ | 124.78 | 0.70 | 0.0000 |
