# 单模型数据集处理报告

## 模型信息

- 模型: gpt-4.1-mini
- 延迟 (TTFT): 0.700 秒
- 吞吐量: 69.59 tokens/s

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 超时问题数: 0 (0.00%)
- 有效问题数: 60
- 正确数量: 34
- 准确率(有效问题): 56.67%
- 平均执行时间(有效问题): 52.02 秒
- 平均理论时间(有效问题): 55.72 秒
- 实际/理论时间比率: 0.93x
- 平均成本(有效问题): $0.0062

## 性能指标

- 平均首个令牌响应时间 (TTFT): 3.381 秒
- 平均每秒生成token数: 74.52 tokens/s
- 理论每秒生成token数: 69.59 tokens/s
- 实际/理论吞吐量比率: 1.07x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✓ | 20.56 | 15.64 | 0.0017 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✓ | 139.94 | 128.85 | 0.0143 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 63.63 | 85.58 | 0.0095 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 40.35 | 64.43 | 0.0071 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 44.00 | 50.15 | 0.0055 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 65.31 | 92.68 | 0.0103 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✓ | 23.85 | 31.87 | 0.0035 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✓ | 17.43 | 22.05 | 0.0024 |
| 9 | Alice and Bob play the following game. A stack ... | ✓ | 25.78 | 34.73 | 0.0038 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 11.81 | 15.20 | 0.0017 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✓ | 40.26 | 35.32 | 0.0039 |
| 12 | Consider the paths of length $16$ that follow t... | ✓ | 11.56 | 15.26 | 0.0016 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 18.72 | 25.65 | 0.0028 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 63.03 | 82.90 | 0.0092 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✓ | 57.15 | 45.10 | 0.0050 |
| 16 | Among the 900 residents of Aimeville, there are... | ✓ | 12.73 | 13.03 | 0.0014 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 75.72 | 103.27 | 0.0114 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 32.65 | 48.80 | 0.0054 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✓ | 51.45 | 56.81 | 0.0063 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✓ | 39.49 | 44.83 | 0.0049 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✓ | 115.55 | 123.07 | 0.0137 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 28.92 | 42.46 | 0.0047 |
| 23 | A list of positive integers has the following p... | ✓ | 13.89 | 21.78 | 0.0024 |
| 24 | Find the number of ways to place a digit in eac... | ✓ | 18.73 | 20.06 | 0.0022 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✓ | 20.08 | 23.66 | 0.0026 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 40.51 | 38.71 | 0.0043 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✓ | 25.70 | 24.58 | 0.0027 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✓ | 104.88 | 157.71 | 0.0175 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 65.88 | 69.19 | 0.0078 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 42.47 | 33.98 | 0.0037 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✓ | 22.16 | 22.33 | 0.0024 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✓ | 28.82 | 33.64 | 0.0037 |
| 33 | The 9 members of a baseball team went to an ice... | ✓ | 16.29 | 15.20 | 0.0017 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✓ | 20.34 | 21.97 | 0.0024 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✓ | 46.02 | 47.88 | 0.0053 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✓ | 17.01 | 14.97 | 0.0016 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 50.95 | 46.51 | 0.0051 |
| 38 | Let $k$ be real numbers such that the system $|... | ✓ | 35.00 | 50.05 | 0.0055 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 238.16 | 224.81 | 0.0250 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 45.18 | 37.99 | 0.0042 |
| 41 | A piecewise linear periodic function is defined... | ✓ | 68.80 | 59.83 | 0.0067 |
| 42 | The set of points in 3-dimensional coordinate s... | ✓ | 62.41 | 60.78 | 0.0067 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 52.42 | 58.09 | 0.0064 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 78.00 | 82.19 | 0.0091 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 31.23 | 28.56 | 0.0031 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✓ | 21.55 | 20.16 | 0.0022 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✓ | 18.28 | 16.46 | 0.0018 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 75.88 | 73.68 | 0.0082 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✓ | 27.08 | 24.37 | 0.0027 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✓ | 78.50 | 80.08 | 0.0089 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✓ | 53.51 | 50.35 | 0.0056 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 28.16 | 27.49 | 0.0030 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✗ | 87.41 | 91.12 | 0.0102 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 33.24 | 29.31 | 0.0032 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✓ | 42.25 | 32.49 | 0.0036 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 54.15 | 41.61 | 0.0046 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✓ | 118.52 | 96.50 | 0.0107 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 163.80 | 150.97 | 0.0168 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 84.41 | 107.32 | 0.0119 |
| 60 | There are exactly three positive real numbers $... | ✗ | 89.72 | 129.15 | 0.0143 |
