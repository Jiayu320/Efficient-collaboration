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
- 正确数量: 18
- 准确率: 30.00%
- 平均执行时间: 15.79 秒
- 平均成本: $0.0030

## 任务规划指标

- 平均任务步骤数: 7.90
- 平均压缩比例: 87.49%
- 平均每步骤Token限制: 32.83 tokens

## 理论性能指标

- 平均理论执行时间: 7.999 秒
- 平均顺序执行时间: 19.198 秒
- 平均并行加速比: 2.40x
- 理论与实际执行时间比例: 0.51x


## 任务分配统计

- 总任务数: 458
- 小模型执行任务数: 18
- 大模型执行任务数: 440
- 小模型任务占比: 3.93%
- 大模型任务占比: 96.07%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.828 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 10.874 秒

### 生成速度
- 小模型平均每秒生成token数: 0.23 tokens/s
- 大模型平均每秒生成token数: 6.86 tokens/s
- 路由模型平均每秒生成token数: 31.16 tokens/s
- 总平均每秒生成token数: 38.24 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 11.21 | 0.0011 | 6 | 50.00% | 25.8 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✓ | 13.33 | 0.0013 | 9 | 66.67% | 23.9 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 14.28 | 0.0022 | 8 | 87.50% | 22.5 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✓ | 16.09 | 0.0020 | 10 | 70.00% | 25.0 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 22.76 | 0.0044 | 10 | 90.00% | 39.5 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 16.15 | 0.0035 | 9 | 77.78% | 29.4 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✓ | 15.16 | 0.0031 | 7 | 100.00% | 27.1 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 17.05 | 0.0031 | 10 | 80.00% | 20.0 |
| 9 | Alice and Bob play the following game. A stack ... | ✓ | 17.81 | 0.0068 | 4 | 100.00% | 57.5 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✗ | 10.39 | 0.0010 | 6 | 83.33% | 20.0 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✓ | 15.08 | 0.0030 | 7 | 100.00% | 35.0 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 19.18 | 0.0032 | 10 | 100.00% | 25.5 |
| 13 | Find the largest possible real part of \[(75+11... | ✓ | 15.71 | 0.0025 | 7 | 85.71% | 33.6 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 12.81 | 0.0015 | 6 | 100.00% | 26.7 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 18.17 | 0.0047 | 7 | 100.00% | 42.9 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 12.03 | 0.0024 | 5 | 100.00% | 46.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 20.81 | 0.0034 | 9 | 88.89% | 35.6 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 22.55 | 0.0052 | 8 | 100.00% | 52.5 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✓ | 18.35 | 0.0044 | 8 | 87.50% | 30.6 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 15.47 | 0.0021 | 5 | 100.00% | 40.0 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✓ | 14.74 | 0.0030 | 6 | 100.00% | 51.7 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 15.34 | 0.0029 | 9 | 77.78% | 50.0 |
| 23 | A list of positive integers has the following p... | ✗ | 14.67 | 0.0020 | 8 | 87.50% | 31.2 |
| 24 | Find the number of ways to place a digit in eac... | ✓ | 17.79 | 0.0048 | 9 | 66.67% | 42.2 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✓ | 19.23 | 0.0045 | 10 | 80.00% | 21.0 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 15.11 | 0.0028 | 7 | 100.00% | 28.6 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 14.93 | 0.0026 | 6 | 100.00% | 36.7 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 12.84 | 0.0008 | 7 | 85.71% | 38.6 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 17.02 | 0.0052 | 8 | 87.50% | 35.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 13.62 | 0.0013 | 9 | 66.67% | 30.0 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✗ | 13.47 | 0.0024 | 7 | 85.71% | 24.3 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 15.89 | 0.0034 | 9 | 77.78% | 30.6 |
| 33 | The 9 members of a baseball team went to an ice... | ✓ | 13.20 | 0.0032 | 5 | 100.00% | 30.0 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 20.80 | 0.0047 | 10 | 80.00% | 38.5 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 11.50 | 0.0012 | 6 | 83.33% | 20.8 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 14.77 | 0.0015 | 9 | 66.67% | 26.7 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✓ | 14.63 | 0.0027 | 8 | 100.00% | 33.1 |
| 38 | Let $k$ be real numbers such that the system $|... | ✗ | 8.31 | 0.0000 | - | - | - |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 8.25 | 0.0000 | - | - | - |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 17.35 | 0.0041 | 9 | 88.89% | 38.3 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 19.40 | 0.0062 | 10 | 90.00% | 25.5 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 20.33 | 0.0045 | 10 | 90.00% | 37.5 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 15.09 | 0.0014 | 9 | 55.56% | 28.3 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✓ | 16.71 | 0.0024 | 10 | 80.00% | 24.0 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 18.58 | 0.0048 | 9 | 77.78% | 48.9 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✗ | 12.79 | 0.0017 | 8 | 75.00% | 18.8 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✗ | 13.05 | 0.0007 | 7 | 85.71% | 25.0 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 18.83 | 0.0030 | 10 | 100.00% | 30.5 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✓ | 17.24 | 0.0036 | 8 | 87.50% | 30.0 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✓ | 16.75 | 0.0050 | 9 | 77.78% | 25.6 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✓ | 18.78 | 0.0063 | 9 | 100.00% | 32.8 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 17.03 | 0.0029 | 9 | 88.89% | 30.6 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✓ | 12.34 | 0.0035 | 5 | 100.00% | 40.0 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 12.50 | 0.0000 | 6 | 100.00% | 33.3 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 10.24 | 0.0014 | 4 | 100.00% | 35.0 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 16.35 | 0.0024 | 8 | 100.00% | 33.1 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 21.28 | 0.0085 | 8 | 100.00% | 46.2 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✓ | 17.35 | 0.0038 | 9 | 88.89% | 25.6 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 13.95 | 0.0033 | 7 | 85.71% | 29.3 |
| 60 | There are exactly three positive real numbers $... | ✗ | 20.98 | 0.0038 | 10 | 90.00% | 38.0 |
