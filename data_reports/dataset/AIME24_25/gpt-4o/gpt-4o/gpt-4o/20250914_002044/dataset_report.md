# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 3
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 正确数量: 1
- 准确率: 1.67%
- 平均执行时间: 16.87 秒
- 平均成本: $0.0177

## 任务规划指标

- 平均任务步骤数: 6.80
- 平均压缩比例: 93.97%
- 平均每步骤Token限制: 36.20 tokens

## 理论性能指标

- 平均理论执行时间: 7.301 秒
- 平均顺序执行时间: 12.139 秒
- 平均并行加速比: 1.67x
- 理论与实际执行时间比例: 0.43x


## 任务分配统计

- 总任务数: 408
- 小模型执行任务数: 63
- 大模型执行任务数: 345
- 小模型任务占比: 15.44%
- 大模型任务占比: 84.56%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.390 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 6.834 秒

### 生成速度
- 小模型平均每秒生成token数: 14.97 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 17.49 tokens/s
- 总平均每秒生成token数: 32.47 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 16.27 | 0.0150 | 7 | 71.43% | 27.1 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 17.07 | 0.0174 | 7 | 100.00% | 35.0 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 15.73 | 0.0169 | 8 | 75.00% | 25.6 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 17.75 | 0.0188 | 7 | 100.00% | 44.3 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 16.71 | 0.0164 | 7 | 100.00% | 35.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 17.89 | 0.0191 | 8 | 100.00% | 43.8 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 18.01 | 0.0174 | 7 | 100.00% | 32.9 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✓ | 17.73 | 0.0174 | 6 | 100.00% | 43.3 |
| 9 | Alice and Bob play the following game. A stack ... | ✓ | 33.43 | 0.0477 | 6 | 100.00% | 30.8 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✗ | 14.97 | 0.0166 | 8 | 75.00% | 31.9 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 17.05 | 0.0149 | 6 | 100.00% | 35.0 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 16.07 | 0.0163 | 7 | 100.00% | 33.6 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 15.83 | 0.0156 | 6 | 100.00% | 35.0 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 18.05 | 0.0176 | 8 | 87.50% | 38.8 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✓ | 18.40 | 0.0194 | 8 | 100.00% | 35.6 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 13.66 | 0.0145 | 5 | 100.00% | 37.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✓ | 16.73 | 0.0155 | 6 | 100.00% | 40.0 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 17.49 | 0.0184 | 7 | 100.00% | 40.7 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✓ | 18.00 | 0.0190 | 8 | 100.00% | 31.2 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 19.00 | 0.0183 | 8 | 100.00% | 43.1 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 18.28 | 0.0170 | 6 | 100.00% | 35.8 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 21.45 | 0.0161 | 6 | 100.00% | 35.0 |
| 23 | A list of positive integers has the following p... | ✗ | 15.76 | 0.0143 | 5 | 100.00% | 39.0 |
| 24 | Find the number of ways to place a digit in eac... | ✓ | 15.03 | 0.0163 | 6 | 83.33% | 34.2 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✓ | 16.38 | 0.0168 | 6 | 100.00% | 33.3 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 14.89 | 0.0150 | 6 | 100.00% | 45.0 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 14.80 | 0.0149 | 5 | 100.00% | 37.0 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✓ | 17.37 | 0.0165 | 8 | 100.00% | 31.2 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 15.73 | 0.0257 | 7 | 85.71% | 40.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✓ | 15.14 | 0.0160 | 7 | 100.00% | 26.4 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 13.49 | 0.0145 | 5 | 100.00% | 40.0 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 12.41 | 0.0151 | 7 | 42.86% | 37.1 |
| 33 | The 9 members of a baseball team went to an ice... | ✗ | 16.95 | 0.0190 | 7 | 100.00% | 42.9 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 15.19 | 0.0141 | 6 | 83.33% | 30.0 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 17.60 | 0.0157 | 7 | 85.71% | 34.3 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 15.65 | 0.0170 | 6 | 100.00% | 35.8 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 16.93 | 0.0164 | 8 | 87.50% | 32.5 |
| 38 | Let $k$ be real numbers such that the system $|... | ✓ | 16.04 | 0.0155 | 7 | 85.71% | 35.7 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✓ | 20.59 | 0.0209 | 9 | 88.89% | 37.8 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 15.03 | 0.0193 | 7 | 100.00% | 35.7 |
| 41 | A piecewise linear periodic function is defined... | ✓ | 16.05 | 0.0199 | 7 | 85.71% | 38.6 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 16.18 | 0.0181 | 7 | 100.00% | 42.9 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 13.46 | 0.0145 | 6 | 83.33% | 39.2 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 17.56 | 0.0188 | 8 | 87.50% | 37.5 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 19.04 | 0.0182 | 7 | 100.00% | 33.6 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✓ | 14.26 | 0.0153 | 5 | 80.00% | 30.0 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✗ | 14.46 | 0.0138 | 5 | 100.00% | 34.0 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✓ | 16.70 | 0.0143 | 7 | 85.71% | 36.4 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✗ | 19.27 | 0.0185 | 7 | 100.00% | 35.0 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 14.74 | 0.0185 | 6 | 100.00% | 36.7 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✗ | 17.01 | 0.0194 | 8 | 87.50% | 40.0 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 19.11 | 0.0184 | 9 | 88.89% | 32.2 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✓ | 15.25 | 0.0190 | 6 | 100.00% | 36.7 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✓ | 17.84 | 0.0204 | 8 | 87.50% | 34.4 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✓ | 16.69 | 0.0159 | 7 | 100.00% | 34.3 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✓ | 14.96 | 0.0142 | 6 | 100.00% | 35.8 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 17.96 | 0.0205 | 7 | 100.00% | 41.4 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 19.01 | 0.0191 | 8 | 100.00% | 31.2 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 15.73 | 0.0169 | 7 | 100.00% | 37.1 |
| 60 | There are exactly three positive real numbers $... | ✗ | 16.24 | 0.0169 | 6 | 100.00% | 46.7 |
