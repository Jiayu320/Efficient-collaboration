# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 正确数量: 12
- 准确率: 20.00%
- 平均执行时间: 17.64 秒
- 平均成本: $0.0003

## 任务规划指标

- 平均任务步骤数: 7.97
- 平均压缩比例: 82.48%
- 平均每步骤Token限制: 34.43 tokens

## 理论性能指标

- 平均理论执行时间: 8.563 秒
- 平均顺序执行时间: 20.333 秒
- 平均并行加速比: 2.37x
- 理论与实际执行时间比例: 0.49x


## 任务分配统计

- 总任务数: 470
- 小模型执行任务数: 325
- 大模型执行任务数: 145
- 小模型任务占比: 69.15%
- 大模型任务占比: 30.85%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.218 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 16.874 秒

### 生成速度
- 小模型平均每秒生成token数: 2.38 tokens/s
- 大模型平均每秒生成token数: 0.89 tokens/s
- 路由模型平均每秒生成token数: 28.01 tokens/s
- 总平均每秒生成token数: 31.28 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 12.63 | 0.0000 | 5 | 60.00% | 19.0 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 13.31 | 0.0000 | 7 | 71.43% | 32.9 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 16.58 | 0.0000 | 9 | 88.89% | 24.4 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✓ | 19.86 | 0.0011 | 10 | 60.00% | 29.0 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 20.10 | 0.0000 | 10 | 90.00% | 30.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 18.46 | 0.0000 | 10 | 70.00% | 31.0 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 33.53 | 0.0000 | 6 | 100.00% | 47.5 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✓ | 8.49 | 0.0000 | - | - | - |
| 9 | Alice and Bob play the following game. A stack ... | ✓ | 20.42 | 0.0022 | 5 | 100.00% | 33.0 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✗ | 18.14 | 0.0000 | 10 | 40.00% | 26.0 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 17.82 | 0.0008 | 8 | 62.50% | 38.8 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 18.06 | 0.0007 | 8 | 100.00% | 36.2 |
| 13 | Find the largest possible real part of \[(75+11... | ✓ | 16.98 | 0.0000 | 8 | 87.50% | 32.5 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 13.11 | 0.0000 | 6 | 100.00% | 40.0 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 15.91 | 0.0000 | 7 | 85.71% | 32.9 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 13.32 | 0.0010 | 5 | 80.00% | 36.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 19.35 | 0.0000 | 8 | 87.50% | 33.1 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 18.41 | 0.0000 | 7 | 71.43% | 57.9 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✓ | 17.57 | 0.0000 | 9 | 88.89% | 38.9 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 15.06 | 0.0000 | 5 | 100.00% | 61.0 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✓ | 13.94 | 0.0000 | 6 | 100.00% | 38.3 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 18.24 | 0.0000 | 10 | 50.00% | 25.5 |
| 23 | A list of positive integers has the following p... | ✗ | 19.88 | 0.0000 | 10 | 80.00% | 24.5 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 15.23 | 0.0011 | 7 | 71.43% | 42.9 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 20.66 | 0.0000 | 9 | 66.67% | 25.6 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 17.56 | 0.0009 | 7 | 85.71% | 61.4 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 14.37 | 0.0000 | 7 | 85.71% | 42.9 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 12.78 | 0.0000 | 6 | 83.33% | 25.0 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 17.99 | 0.0000 | 9 | 66.67% | 18.3 |
| 30 | There is a collection of $25$ indistinguishable... | ✓ | 22.16 | 0.0019 | 10 | 100.00% | 49.0 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✗ | 12.71 | 0.0000 | 6 | 66.67% | 18.3 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 18.62 | 0.0000 | 10 | 50.00% | 28.5 |
| 33 | The 9 members of a baseball team went to an ice... | ✗ | 11.65 | 0.0000 | 4 | 100.00% | 41.2 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 17.52 | 0.0000 | 9 | 88.89% | 32.2 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 15.46 | 0.0000 | 8 | 75.00% | 23.1 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 23.99 | 0.0021 | 9 | 77.78% | 25.6 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 15.71 | 0.0000 | 6 | 100.00% | 28.3 |
| 38 | Let $k$ be real numbers such that the system $|... | ✗ | 17.38 | 0.0000 | 7 | 85.71% | 28.6 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✓ | 22.09 | 0.0000 | 10 | 100.00% | 28.5 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 35.10 | 0.0000 | 19 | 47.37% | 26.3 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 23.36 | 0.0000 | 9 | 66.67% | 33.9 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 20.04 | 0.0014 | 8 | 87.50% | 36.2 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 16.89 | 0.0000 | 9 | 88.89% | 38.3 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 17.91 | 0.0000 | 9 | 100.00% | 43.3 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 15.95 | 0.0000 | 6 | 83.33% | 33.3 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✗ | 17.91 | 0.0000 | 9 | 77.78% | 41.1 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✗ | 19.02 | 0.0000 | 10 | 90.00% | 25.5 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 21.61 | 0.0061 | 8 | 100.00% | 78.8 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✗ | 15.80 | 0.0000 | 7 | 100.00% | 30.7 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 18.42 | 0.0000 | 10 | 70.00% | 30.0 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✓ | 15.81 | 0.0000 | 8 | 75.00% | 26.9 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✓ | 17.61 | 0.0000 | 8 | 75.00% | 37.5 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✓ | 12.04 | 0.0000 | 5 | 80.00% | 52.0 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 14.81 | 0.0000 | 6 | 100.00% | 35.0 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 14.84 | 0.0009 | 6 | 100.00% | 36.7 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 17.61 | 0.0000 | 10 | 60.00% | 23.5 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 19.91 | 0.0000 | 7 | 100.00% | 35.0 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 16.20 | 0.0000 | 8 | 87.50% | 22.5 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 15.02 | 0.0000 | 7 | 100.00% | 25.7 |
| 60 | There are exactly three positive real numbers $... | ✓ | 17.47 | 0.0007 | 8 | 100.00% | 31.2 |
