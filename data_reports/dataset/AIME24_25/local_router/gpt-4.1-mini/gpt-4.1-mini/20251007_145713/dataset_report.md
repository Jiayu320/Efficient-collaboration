# 数据集处理报告

## 模型配置

- 小模型: gpt-4.1-mini
- 大模型: gpt-4.1-mini
- 路由模型: saves/Llama-3.2-1B-Instruct/full/Llama-3-2-1B_ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 正确数量: 24
- 准确率: 40.00%
- 平均执行时间: 33.88 秒
- 平均成本: $0.0123

## 任务规划指标

- 平均任务步骤数: 4.28
- 平均压缩比例: 95.65%
- 平均每步骤Token限制: 51.87 tokens

## 理论性能指标

- 平均理论执行时间: 6.947 秒
- 平均顺序执行时间: 8.858 秒
- 平均并行加速比: 1.28x
- 理论与实际执行时间比例: 0.21x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.690 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 23.295 秒

### 生成速度
- 小模型平均每秒生成token数: 48.66 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 11.55 tokens/s
- 总平均每秒生成token数: 60.21 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✓ | 31.77 | 0.0099 | 4 | 100.00% | 50.0 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 62.86 | 0.0150 | 4 | 100.00% | 40.0 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 19.07 | 0.0087 | 3 | 100.00% | 43.3 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 21.58 | 0.0095 | 4 | 100.00% | 55.0 |
| 5 | Let $p$ be the least prime number for which the... | ✓ | 49.26 | 0.0130 | 3 | 100.00% | 43.3 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✓ | 106.06 | 0.0271 | 5 | 100.00% | 70.0 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✓ | 42.08 | 0.0175 | 7 | 85.71% | 32.9 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✓ | 18.57 | 0.0084 | 4 | 100.00% | 57.5 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 26.47 | 0.0104 | 4 | 100.00% | 50.0 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 26.56 | 0.0112 | 5 | 60.00% | 34.0 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 35.83 | 0.0117 | 4 | 100.00% | 42.5 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 29.92 | 0.0110 | 4 | 100.00% | 42.5 |
| 13 | Find the largest possible real part of \[(75+11... | ✓ | 24.50 | 0.0101 | 4 | 75.00% | 40.0 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 35.86 | 0.0109 | 4 | 100.00% | 55.0 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✓ | 44.67 | 0.0148 | 4 | 100.00% | 112.5 |
| 16 | Among the 900 residents of Aimeville, there are... | ✓ | 22.89 | 0.0096 | 3 | 100.00% | 46.7 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 27.29 | 0.0117 | 5 | 80.00% | 48.0 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 23.65 | 0.0090 | 4 | 100.00% | 35.0 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 35.31 | 0.0116 | 4 | 100.00% | 50.0 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✓ | 35.61 | 0.0129 | 3 | 100.00% | 50.0 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 25.14 | 0.0112 | 4 | 100.00% | 47.5 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 23.45 | 0.0094 | 4 | 100.00% | 42.5 |
| 23 | A list of positive integers has the following p... | ✓ | 32.01 | 0.0129 | 4 | 100.00% | 42.5 |
| 24 | Find the number of ways to place a digit in eac... | ✓ | 27.70 | 0.0115 | 4 | 100.00% | 47.5 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✓ | 41.96 | 0.0139 | 5 | 100.00% | 98.0 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 18.23 | 0.0094 | 4 | 100.00% | 37.5 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✓ | 28.42 | 0.0104 | 4 | 100.00% | 50.0 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 16.34 | 0.0082 | 4 | 100.00% | 45.0 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 22.27 | 0.0118 | 4 | 100.00% | 50.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 24.87 | 0.0112 | 3 | 100.00% | 43.3 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✗ | 19.37 | 0.0084 | 4 | 100.00% | 42.5 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✓ | 99.54 | 0.0229 | 6 | 100.00% | 65.0 |
| 33 | The 9 members of a baseball team went to an ice... | ✓ | 29.38 | 0.0157 | 4 | 100.00% | 52.5 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✓ | 25.26 | 0.0112 | 4 | 100.00% | 55.0 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✓ | 52.79 | 0.0189 | 4 | 100.00% | 50.0 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✓ | 31.37 | 0.0109 | 4 | 100.00% | 42.5 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 48.95 | 0.0135 | 4 | 100.00% | 50.0 |
| 38 | Let $k$ be real numbers such that the system $|... | ✓ | 31.19 | 0.0115 | 4 | 100.00% | 42.5 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 24.34 | 0.0109 | 5 | 100.00% | 58.0 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 17.29 | 0.0105 | 6 | 50.00% | 28.3 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 23.67 | 0.0147 | 8 | 50.00% | 47.5 |
| 42 | The set of points in 3-dimensional coordinate s... | ✓ | 43.94 | 0.0148 | 4 | 100.00% | 85.0 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 7.86 | 0.0070 | 4 | 75.00% | 52.5 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 22.79 | 0.0089 | 3 | 100.00% | 100.0 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 26.64 | 0.0118 | 5 | 100.00% | 72.0 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✓ | 38.67 | 0.0114 | 4 | 100.00% | 42.5 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✓ | 23.60 | 0.0094 | 4 | 100.00% | 40.0 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 16.71 | 0.0090 | 4 | 100.00% | 22.5 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✓ | 30.66 | 0.0123 | 4 | 100.00% | 75.0 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 25.72 | 0.0119 | 5 | 100.00% | 40.0 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✗ | 31.83 | 0.0134 | 5 | 80.00% | 92.0 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 34.10 | 0.0117 | 6 | 83.33% | 33.3 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✗ | 23.76 | 0.0106 | 4 | 100.00% | 55.0 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 58.56 | 0.0158 | 5 | 100.00% | 46.0 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 27.02 | 0.0104 | 4 | 100.00% | 50.0 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 32.94 | 0.0116 | 4 | 100.00% | 40.0 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 50.15 | 0.0152 | 4 | 100.00% | 70.0 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 102.06 | 0.0282 | 5 | 100.00% | 58.0 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 25.17 | 0.0107 | 4 | 100.00% | 57.5 |
| 60 | There are exactly three positive real numbers $... | ✗ | 27.08 | 0.0111 | 4 | 100.00% | 45.0 |
