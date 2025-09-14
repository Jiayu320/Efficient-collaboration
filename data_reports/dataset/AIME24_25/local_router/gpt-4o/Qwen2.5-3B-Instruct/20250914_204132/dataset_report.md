# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 正确数量: 17
- 准确率: 28.33%
- 平均执行时间: 15.77 秒
- 平均成本: $0.0034

## 任务规划指标

- 平均任务步骤数: 7.72
- 平均压缩比例: 80.36%
- 平均每步骤Token限制: 36.39 tokens

## 理论性能指标

- 平均理论执行时间: 7.539 秒
- 平均顺序执行时间: 19.003 秒
- 平均并行加速比: 2.53x
- 理论与实际执行时间比例: 0.48x


## 任务分配统计

- 总任务数: 463
- 小模型执行任务数: 32
- 大模型执行任务数: 431
- 小模型任务占比: 6.91%
- 大模型任务占比: 93.09%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.841 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.089 秒

### 生成速度
- 小模型平均每秒生成token数: 1.52 tokens/s
- 大模型平均每秒生成token数: 8.88 tokens/s
- 路由模型平均每秒生成token数: 30.58 tokens/s
- 总平均每秒生成token数: 40.98 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 15.84 | 0.0039 | 8 | 75.00% | 30.6 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 18.58 | 0.0045 | 10 | 90.00% | 35.0 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 12.60 | 0.0017 | 8 | 75.00% | 29.4 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 15.13 | 0.0049 | 7 | 85.71% | 41.4 |
| 5 | Let $p$ be the least prime number for which the... | ✓ | 16.33 | 0.0044 | 5 | 100.00% | 55.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 19.81 | 0.0083 | 9 | 77.78% | 32.8 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✓ | 14.47 | 0.0033 | 8 | 87.50% | 33.8 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 16.95 | 0.0037 | 8 | 62.50% | 31.2 |
| 9 | Alice and Bob play the following game. A stack ... | ✓ | 18.13 | 0.0069 | 4 | 100.00% | 55.0 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✗ | 12.68 | 0.0011 | 8 | 75.00% | 40.6 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 11.64 | 0.0008 | 8 | 50.00% | 28.1 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 16.74 | 0.0021 | 8 | 62.50% | 36.2 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 14.84 | 0.0034 | 8 | 75.00% | 46.2 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 17.80 | 0.0060 | 9 | 77.78% | 40.0 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 15.23 | 0.0042 | 8 | 75.00% | 50.0 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 9.86 | 0.0008 | 5 | 80.00% | 40.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✓ | 16.87 | 0.0045 | 8 | 87.50% | 44.4 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 18.94 | 0.0049 | 9 | 88.89% | 51.1 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 18.80 | 0.0088 | 8 | 87.50% | 41.2 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✓ | 14.87 | 0.0022 | 8 | 75.00% | 33.1 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 15.66 | 0.0032 | 7 | 85.71% | 32.9 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 9.15 | 0.0011 | 5 | 80.00% | 40.0 |
| 23 | A list of positive integers has the following p... | ✗ | 14.66 | 0.0033 | 9 | 77.78% | 27.8 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 16.33 | 0.0041 | 9 | 88.89% | 25.6 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 32.09 | 0.0011 | 8 | 75.00% | 32.5 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✓ | 13.01 | 0.0034 | 6 | 100.00% | 43.3 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 13.56 | 0.0033 | 6 | 100.00% | 34.2 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 12.88 | 0.0022 | 8 | 75.00% | 31.2 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 12.12 | 0.0034 | 7 | 85.71% | 25.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✓ | 11.63 | 0.0009 | 8 | 37.50% | 29.4 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 15.20 | 0.0025 | 7 | 85.71% | 38.6 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✓ | 14.22 | 0.0021 | 10 | 60.00% | 24.5 |
| 33 | The 9 members of a baseball team went to an ice... | ✓ | 12.57 | 0.0030 | 5 | 100.00% | 24.0 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 13.38 | 0.0014 | 9 | 77.78% | 24.4 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 12.32 | 0.0020 | 7 | 85.71% | 23.6 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 13.76 | 0.0030 | 9 | 66.67% | 23.9 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 12.92 | 0.0028 | 7 | 71.43% | 38.6 |
| 38 | Let $k$ be real numbers such that the system $|... | ✓ | 14.51 | 0.0029 | 8 | 87.50% | 38.8 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 18.48 | 0.0059 | 8 | 100.00% | 37.5 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 15.03 | 0.0054 | 8 | 100.00% | 43.8 |
| 41 | A piecewise linear periodic function is defined... | ✓ | 16.18 | 0.0039 | 10 | 50.00% | 51.0 |
| 42 | The set of points in 3-dimensional coordinate s... | ✓ | 16.26 | 0.0037 | 9 | 88.89% | 35.0 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 11.89 | 0.0021 | 6 | 66.67% | 28.3 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 15.85 | 0.0044 | 9 | 88.89% | 40.6 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 13.57 | 0.0020 | 8 | 62.50% | 48.8 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✓ | 24.70 | 0.0041 | 8 | 87.50% | 35.0 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✗ | 13.59 | 0.0014 | 7 | 71.43% | 24.3 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 14.87 | 0.0022 | 9 | 66.67% | 27.8 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✗ | 14.55 | 0.0031 | 9 | 88.89% | 26.1 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 22.60 | 0.0098 | 9 | 100.00% | 45.6 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✗ | 15.25 | 0.0034 | 9 | 88.89% | 27.2 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 12.35 | 0.0008 | 8 | 75.00% | 31.2 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✓ | 11.28 | 0.0032 | 6 | 66.67% | 58.3 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 11.18 | 0.0000 | 7 | 71.43% | 40.7 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 11.55 | 0.0012 | 6 | 83.33% | 33.3 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✓ | 14.16 | 0.0023 | 8 | 87.50% | 36.9 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✓ | 16.47 | 0.0048 | 7 | 85.71% | 37.9 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 32.60 | 0.0038 | 7 | 100.00% | 27.9 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 24.25 | 0.0050 | 9 | 77.78% | 35.6 |
| 60 | There are exactly three positive real numbers $... | ✗ | 23.19 | 0.0034 | 7 | 85.71% | 57.1 |
