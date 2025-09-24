# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-235b-a22b-thinking-2507
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 30
- 正确数量: 12
- 准确率: 40.00%
- 平均执行时间: 237.95 秒
- 平均成本: $0.0128

## 任务规划指标

- 平均任务步骤数: 5.47
- 平均压缩比例: 83.04%
- 平均每步骤Token限制: 45.17 tokens

## 理论性能指标

- 平均理论执行时间: 7.367 秒
- 平均顺序执行时间: 19.971 秒
- 平均并行加速比: 2.73x
- 理论与实际执行时间比例: 0.03x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 28.296 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 35.477 秒

### 生成速度
- 小模型平均每秒生成token数: 1.01 tokens/s
- 大模型平均每秒生成token数: 3.53 tokens/s
- 路由模型平均每秒生成token数: 5.20 tokens/s
- 总平均每秒生成token数: 9.73 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 78.30 | 0.0124 | 4 | 75.00% | 47.5 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 253.29 | 0.0198 | 7 | 71.43% | 44.3 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 610.96 | 0.0103 | 5 | 80.00% | 43.0 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 420.10 | 0.0152 | 5 | 80.00% | 64.0 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 226.29 | 0.0155 | 4 | 100.00% | 65.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 100.71 | 0.0151 | 5 | 80.00% | 44.0 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 296.44 | 0.0072 | 9 | 77.78% | 28.9 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 144.59 | 0.0034 | 5 | 80.00% | 30.0 |
| 9 | Alice and Bob play the following game. A stack ... | ✓ | 131.47 | 0.0114 | 5 | 80.00% | 46.0 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✗ | 99.55 | 0.0031 | 5 | 60.00% | 28.0 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✓ | 247.00 | 0.0151 | 6 | 83.33% | 55.0 |
| 12 | Consider the paths of length $16$ that follow t... | ✓ | 132.51 | 0.0077 | 7 | 57.14% | 37.1 |
| 13 | Find the largest possible real part of \[(75+11... | ✓ | 81.52 | 0.0084 | 5 | 80.00% | 40.0 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 704.29 | 0.0100 | 4 | 75.00% | 42.5 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✓ | 220.90 | 0.0247 | 8 | 75.00% | 42.5 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 94.71 | 0.0087 | 4 | 75.00% | 47.5 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 134.57 | 0.0229 | 6 | 100.00% | 50.0 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 186.99 | 0.0144 | 5 | 100.00% | 50.0 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 227.58 | 0.0205 | 6 | 83.33% | 51.7 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✓ | 148.35 | 0.0182 | 7 | 100.00% | 45.7 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✓ | 365.72 | 0.0187 | 6 | 100.00% | 65.0 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 251.89 | 0.0061 | 3 | 100.00% | 40.0 |
| 23 | A list of positive integers has the following p... | ✓ | 286.97 | 0.0104 | 5 | 100.00% | 46.0 |
| 24 | Find the number of ways to place a digit in eac... | ✓ | 145.76 | 0.0110 | 5 | 80.00% | 40.0 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 111.03 | 0.0192 | 7 | 71.43% | 50.0 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 294.77 | 0.0058 | 4 | 100.00% | 40.0 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 121.16 | 0.0029 | 5 | 100.00% | 30.0 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✓ | 356.13 | 0.0198 | 6 | 100.00% | 51.7 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✓ | 314.75 | 0.0121 | 5 | 60.00% | 38.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✓ | 350.32 | 0.0145 | 6 | 66.67% | 51.7 |
