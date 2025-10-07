# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Llama-3.2-1B-Instruct/full/Llama-3-2-1B_ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 正确数量: 5
- 准确率: 8.33%
- 平均执行时间: 14.32 秒
- 平均成本: $0.0229

## 任务规划指标

- 平均任务步骤数: 4.42
- 平均压缩比例: 80.44%
- 平均每步骤Token限制: 57.81 tokens

## 理论性能指标

- 平均理论执行时间: 5.546 秒
- 平均顺序执行时间: 7.758 秒
- 平均并行加速比: 1.42x
- 理论与实际执行时间比例: 0.39x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.163 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 7.340 秒

### 生成速度
- 小模型平均每秒生成token数: 57.24 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 26.80 tokens/s
- 总平均每秒生成token数: 84.04 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✓ | 20.36 | 0.0287 | 4 | 100.00% | 47.5 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 15.65 | 0.0262 | 5 | 80.00% | 42.0 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 15.53 | 0.0179 | 4 | 100.00% | 37.5 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 16.25 | 0.0273 | 4 | 100.00% | 50.0 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 12.72 | 0.0223 | 3 | 100.00% | 63.3 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 6.35 | 0.0103 | 4 | 25.00% | 97.5 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 13.75 | 0.0220 | 5 | 80.00% | 34.0 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 6.61 | 0.0095 | 4 | 25.00% | 45.0 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 6.98 | 0.0089 | 4 | 25.00% | 47.5 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 13.51 | 0.0221 | 5 | 80.00% | 34.0 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 6.35 | 0.0092 | 4 | 25.00% | 45.0 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 12.50 | 0.0182 | 4 | 100.00% | 47.5 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 13.39 | 0.0210 | 4 | 100.00% | 52.5 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 20.53 | 0.0285 | 5 | 100.00% | 64.0 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 17.32 | 0.0288 | 4 | 100.00% | 90.0 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 13.11 | 0.0187 | 3 | 100.00% | 43.3 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 18.98 | 0.0270 | 5 | 100.00% | 42.0 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 15.13 | 0.0237 | 4 | 100.00% | 112.5 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 20.38 | 0.0339 | 6 | 66.67% | 30.0 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 19.94 | 0.0284 | 5 | 100.00% | 46.0 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 14.08 | 0.0207 | 4 | 100.00% | 52.5 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 5.90 | 0.0098 | 5 | 20.00% | 56.0 |
| 23 | A list of positive integers has the following p... | ✗ | 20.93 | 0.0278 | 5 | 100.00% | 44.0 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 15.78 | 0.0254 | 4 | 100.00% | 50.0 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 24.58 | 0.0360 | 5 | 100.00% | 98.0 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 11.66 | 0.0152 | 4 | 100.00% | 45.0 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 9.79 | 0.0115 | 4 | 50.00% | 37.5 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 21.18 | 0.0350 | 5 | 100.00% | 46.0 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 14.98 | 0.0232 | 4 | 100.00% | 50.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 12.75 | 0.0186 | 4 | 100.00% | 50.0 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✗ | 15.19 | 0.0242 | 4 | 100.00% | 45.0 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 16.16 | 0.0466 | 8 | 50.00% | 68.8 |
| 33 | The 9 members of a baseball team went to an ice... | ✗ | 18.51 | 0.0290 | 5 | 100.00% | 110.0 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 10.35 | 0.0151 | 3 | 100.00% | 46.7 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 17.16 | 0.0232 | 4 | 100.00% | 45.0 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 15.13 | 0.0216 | 4 | 100.00% | 40.0 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 6.32 | 0.0093 | 4 | 25.00% | 55.0 |
| 38 | Let $k$ be real numbers such that the system $|... | ✗ | 23.10 | 0.0448 | 5 | 100.00% | 56.0 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✓ | 13.64 | 0.0267 | 4 | 75.00% | 40.0 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 12.75 | 0.0347 | 10 | 40.00% | 59.0 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 14.85 | 0.0245 | 5 | 100.00% | 120.0 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 19.34 | 0.0269 | 4 | 100.00% | 105.0 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 9.00 | 0.0129 | 4 | 50.00% | 42.5 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 16.87 | 0.0283 | 4 | 100.00% | 105.0 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 16.35 | 0.0254 | 4 | 100.00% | 100.0 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✓ | 13.05 | 0.0215 | 3 | 100.00% | 43.3 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✓ | 14.76 | 0.0207 | 4 | 100.00% | 50.0 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 5.72 | 0.0086 | 4 | 25.00% | 27.5 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✗ | 12.40 | 0.0215 | 4 | 100.00% | 97.5 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 23.76 | 0.0403 | 5 | 100.00% | 58.0 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✗ | 18.06 | 0.0280 | 5 | 100.00% | 82.0 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 22.04 | 0.0335 | 5 | 100.00% | 36.0 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✗ | 5.81 | 0.0106 | 4 | 25.00% | 45.0 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 16.67 | 0.0268 | 4 | 100.00% | 55.0 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 5.53 | 0.0089 | 4 | 25.00% | 27.5 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 5.62 | 0.0083 | 4 | 25.00% | 85.0 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 15.03 | 0.0372 | 5 | 60.00% | 76.0 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 13.39 | 0.0216 | 4 | 100.00% | 52.5 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 14.83 | 0.0215 | 4 | 100.00% | 45.0 |
| 60 | There are exactly three positive real numbers $... | ✗ | 10.98 | 0.0174 | 4 | 50.00% | 50.0 |
