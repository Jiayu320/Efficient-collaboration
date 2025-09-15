# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 正确数量: 3
- 准确率: 5.00%
- 平均执行时间: 16.27 秒
- 平均成本: $0.0018

## 任务规划指标

- 平均任务步骤数: 7.87
- 平均压缩比例: 85.01%
- 平均每步骤Token限制: 33.03 tokens

## 理论性能指标

- 平均理论执行时间: 8.284 秒
- 平均顺序执行时间: 19.657 秒
- 平均并行加速比: 2.39x
- 理论与实际执行时间比例: 0.51x


## 任务分配统计

- 总任务数: 472
- 小模型执行任务数: 223
- 大模型执行任务数: 249
- 小模型任务占比: 47.25%
- 大模型任务占比: 52.75%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.598 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 13.012 秒

### 生成速度
- 小模型平均每秒生成token数: 3.41 tokens/s
- 大模型平均每秒生成token数: 4.65 tokens/s
- 路由模型平均每秒生成token数: 33.30 tokens/s
- 总平均每秒生成token数: 41.35 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 16.17 | 0.0000 | 9 | 88.89% | 28.3 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 17.87 | 0.0033 | 9 | 100.00% | 36.1 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 10.40 | 0.0000 | 7 | 71.43% | 22.1 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✓ | 17.63 | 0.0024 | 8 | 62.50% | 23.8 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 16.41 | 0.0000 | 10 | 100.00% | 30.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 13.84 | 0.0000 | 9 | 77.78% | 27.8 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 13.51 | 0.0000 | 8 | 87.50% | 26.9 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 14.17 | 0.0000 | 8 | 75.00% | 20.0 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 32.35 | 0.0237 | 6 | 100.00% | 40.0 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✗ | 12.27 | 0.0000 | 10 | 60.00% | 19.5 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✓ | 11.93 | 0.0010 | 6 | 50.00% | 29.2 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 16.14 | 0.0014 | 10 | 100.00% | 33.0 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 16.72 | 0.0007 | 9 | 88.89% | 29.4 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 14.03 | 0.0021 | 7 | 85.71% | 42.1 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 14.08 | 0.0015 | 6 | 100.00% | 38.3 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 7.52 | 0.0008 | 2 | 100.00% | 35.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✓ | 31.51 | 0.0027 | 10 | 100.00% | 32.0 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 15.37 | 0.0008 | 8 | 100.00% | 32.5 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✓ | 15.18 | 0.0014 | 9 | 77.78% | 35.0 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 14.89 | 0.0030 | 6 | 100.00% | 50.0 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 13.69 | 0.0011 | 8 | 87.50% | 30.0 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 12.46 | 0.0009 | 8 | 87.50% | 30.6 |
| 23 | A list of positive integers has the following p... | ✓ | 12.33 | 0.0007 | 8 | 75.00% | 28.8 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 17.13 | 0.0015 | 9 | 77.78% | 28.9 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 13.51 | 0.0013 | 6 | 100.00% | 21.7 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 13.08 | 0.0014 | 7 | 100.00% | 26.4 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✓ | 13.44 | 0.0022 | 5 | 100.00% | 54.0 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 10.30 | 0.0000 | 7 | 85.71% | 22.1 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✓ | 14.23 | 0.0018 | 8 | 87.50% | 35.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 9.29 | 0.0000 | 6 | 66.67% | 23.3 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 14.93 | 0.0015 | 8 | 100.00% | 25.0 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 12.73 | 0.0000 | 10 | 40.00% | 22.5 |
| 33 | The 9 members of a baseball team went to an ice... | ✓ | 10.02 | 0.0008 | 5 | 100.00% | 26.0 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 17.34 | 0.0007 | 9 | 77.78% | 27.2 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 9.81 | 0.0000 | 6 | 83.33% | 27.5 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 13.82 | 0.0021 | 7 | 100.00% | 28.6 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 11.96 | 0.0010 | 7 | 100.00% | 30.0 |
| 38 | Let $k$ be real numbers such that the system $|... | ✓ | 11.93 | 0.0000 | 8 | 87.50% | 31.9 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 32.11 | 0.0022 | 8 | 100.00% | 24.4 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 25.61 | 0.0036 | 9 | 88.89% | 34.4 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 22.70 | 0.0025 | 9 | 66.67% | 29.4 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 30.54 | 0.0035 | 9 | 88.89% | 34.4 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 21.81 | 0.0021 | 7 | 57.14% | 35.7 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 34.81 | 0.0027 | 9 | 88.89% | 37.2 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 15.64 | 0.0010 | 9 | 77.78% | 33.3 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✗ | 10.46 | 0.0000 | 9 | 44.44% | 28.9 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✓ | 18.67 | 0.0028 | 9 | 77.78% | 53.3 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 11.06 | 0.0000 | 8 | 75.00% | 23.8 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✓ | 17.99 | 0.0025 | 9 | 88.89% | 28.9 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 12.92 | 0.0000 | 11 | 54.55% | 22.7 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✓ | 18.07 | 0.0011 | 9 | 100.00% | 30.0 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 10.84 | 0.0000 | 8 | 75.00% | 29.4 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✗ | 12.20 | 0.0017 | 7 | 71.43% | 57.1 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 12.29 | 0.0000 | 7 | 100.00% | 27.1 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 15.98 | 0.0026 | 6 | 100.00% | 48.3 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 16.04 | 0.0015 | 8 | 100.00% | 40.0 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 19.67 | 0.0026 | 10 | 80.00% | 33.5 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 14.65 | 0.0000 | 9 | 100.00% | 23.9 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✓ | 21.63 | 0.0000 | 6 | 83.33% | 48.3 |
| 60 | There are exactly three positive real numbers $... | ✓ | 26.41 | 0.0136 | 7 | 100.00% | 107.1 |
