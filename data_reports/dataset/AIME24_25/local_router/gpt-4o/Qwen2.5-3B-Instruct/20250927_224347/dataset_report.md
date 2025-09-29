# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep3
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 30
- 正确数量: 1
- 准确率: 3.33%
- 平均执行时间: 70.62 秒
- 平均成本: $0.0112


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 2.70 |
| Dependency Structure And Flow | 4.27 |
| Plan Relevance And Efficiency | 3.80 |
| Plan Soundness And Decomposition | 3.53 |
| Task Clarity And Executability | 4.93 |
## 任务规划指标

- 平均任务步骤数: 4.80
- 平均压缩比例: 82.60%
- 平均每步骤Token限制: 52.22 tokens

## 理论性能指标

- 平均理论执行时间: 5.658 秒
- 平均顺序执行时间: 12.912 秒
- 平均并行加速比: 2.31x
- 理论与实际执行时间比例: 0.08x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.421 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 60.795 秒

### 生成速度
- 小模型平均每秒生成token数: 2.08 tokens/s
- 大模型平均每秒生成token数: 14.91 tokens/s
- 路由模型平均每秒生成token数: 33.00 tokens/s
- 总平均每秒生成token数: 49.99 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 70.34 | 0.0108 | 6 | 83.33% | 53.3 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 63.51 | 0.0122 | 4 | 100.00% | 57.5 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 57.78 | 0.0098 | 4 | 75.00% | 57.5 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 76.65 | 0.0237 | 6 | 66.67% | 70.0 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 75.56 | 0.0204 | 5 | 80.00% | 70.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 73.06 | 0.0228 | 5 | 80.00% | 66.0 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 70.41 | 0.0139 | 5 | 80.00% | 52.0 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 66.80 | 0.0138 | 6 | 83.33% | 60.0 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 59.23 | 0.0129 | 4 | 100.00% | 55.0 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 60.02 | 0.0109 | 5 | 40.00% | 44.0 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 77.49 | 0.0129 | 6 | 100.00% | 48.3 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 74.16 | 0.0115 | 5 | 80.00% | 54.0 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 70.95 | 0.0114 | 5 | 100.00% | 60.0 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 67.24 | 0.0099 | 5 | 60.00% | 50.0 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 61.35 | 0.0186 | 5 | 80.00% | 70.0 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 67.65 | 0.0003 | 2 | 100.00% | 30.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 64.29 | 0.0095 | 4 | 100.00% | 62.5 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 58.32 | 0.0141 | 4 | 100.00% | 70.0 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 83.51 | 0.0069 | 5 | 100.00% | 42.0 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 76.54 | 0.0065 | 4 | 100.00% | 45.0 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 77.93 | 0.0138 | 4 | 100.00% | 60.0 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 91.05 | 0.0190 | 7 | 42.86% | 57.1 |
| 23 | A list of positive integers has the following p... | ✗ | 66.56 | 0.0087 | 4 | 75.00% | 55.0 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 61.21 | 0.0074 | 4 | 75.00% | 45.0 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 92.28 | 0.0102 | 5 | 80.00% | 46.0 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 50.30 | 0.0022 | 2 | 100.00% | 35.0 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 85.33 | 0.0053 | 5 | 80.00% | 36.0 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 74.63 | 0.0033 | 8 | 50.00% | 33.8 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 74.22 | 0.0051 | 6 | 66.67% | 26.7 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 70.36 | 0.0084 | 4 | 100.00% | 55.0 |
