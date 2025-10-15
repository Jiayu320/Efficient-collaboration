# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: meta-llama/llama-3-8b-instruct
- 路由模型: gpt-4.1-mini
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24.json
- 问题总数: 30
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 73.55 秒
- 平均成本: $0.0017

## 任务规划指标

- 平均任务步骤数: 5.77
- 平均压缩比例: 93.07%
- 平均每步骤Token限制: 49.00 tokens

## 理论性能指标

- 平均理论执行时间: 9.586 秒
- 平均顺序执行时间: 14.511 秒
- 平均并行加速比: 1.52x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.005 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 57.763 秒

### 生成速度
- 小模型平均每秒生成token数: 34.41 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 7.40 tokens/s
- 总平均每秒生成token数: 41.81 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 36.42 | 0.0012 | 4 | 75.00% | 47.5 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 49.79 | 0.0014 | 7 | 100.00% | 38.6 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 71.87 | 0.0018 | 8 | 100.00% | 55.6 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 82.63 | 0.0018 | 8 | 100.00% | 58.8 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 151.16 | 0.0021 | 5 | 100.00% | 60.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 12.13 | 0.0000 | 1 | 100.00% | 0.0 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 54.25 | 0.0019 | 6 | 83.33% | 61.7 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 31.74 | 0.0011 | 6 | 83.33% | 43.3 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 35.22 | 0.0013 | 5 | 100.00% | 60.0 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✗ | 34.99 | 0.0014 | 6 | 66.67% | 35.0 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 64.85 | 0.0015 | 5 | 100.00% | 58.0 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 71.61 | 0.0018 | 7 | 100.00% | 32.9 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 48.65 | 0.0016 | 6 | 100.00% | 48.3 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 64.76 | 0.0013 | 5 | 100.00% | 66.0 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 171.41 | 0.0027 | 7 | 100.00% | 54.3 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 46.96 | 0.0012 | 4 | 100.00% | 45.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 188.15 | 0.0029 | 7 | 71.43% | 44.3 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 157.37 | 0.0024 | 6 | 100.00% | 58.3 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 55.46 | 0.0018 | 7 | 85.71% | 44.3 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 31.26 | 0.0015 | 4 | 100.00% | 52.5 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 39.95 | 0.0015 | 6 | 100.00% | 45.0 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 32.65 | 0.0014 | 5 | 80.00% | 52.0 |
| 23 | A list of positive integers has the following p... | ✗ | 151.48 | 0.0019 | 4 | 100.00% | 55.0 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 26.97 | 0.0017 | 6 | 66.67% | 36.7 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 88.37 | 0.0021 | 5 | 80.00% | 62.0 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 82.22 | 0.0017 | 5 | 100.00% | 60.0 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 55.25 | 0.0016 | 7 | 100.00% | 51.4 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 120.37 | 0.0017 | 7 | 100.00% | 45.7 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 68.09 | 0.0018 | 7 | 100.00% | 35.0 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 80.43 | 0.0019 | 7 | 100.00% | 62.9 |
