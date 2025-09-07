# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft (New)
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/AIME24_0.json
- 问题总数: 30
- 正确数量: 10
- 准确率: 33.33%
- 平均执行时间: 17.49 秒
- 平均成本: $0.0035

## 任务规划指标

- 平均任务步骤数: 7.90
- 平均压缩比例: 72.74%
- 平均每步骤Token限制: 33.31 tokens

## 理论性能指标

- 平均理论执行时间: 7.168 秒
- 平均顺序执行时间: 19.175 秒
- 平均并行加速比: 2.68x
- 理论与实际执行时间比例: 0.41x


## 任务分配统计

- 总任务数: 237
- 小模型执行任务数: 4
- 大模型执行任务数: 233
- 小模型任务占比: 1.69%
- 大模型任务占比: 98.31%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.160 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 12.010 秒

### 生成速度
- 小模型平均每秒生成token数: 0.26 tokens/s
- 大模型平均每秒生成token数: 8.50 tokens/s
- 路由模型平均每秒生成token数: 26.84 tokens/s
- 总平均每秒生成token数: 35.61 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 26.66 | 0.0044 | 10 | 80.00% | 33.0 |
| 2 | Let $O(0,0), A(\tfrac{1}{2}, 0),$ and $B(0, \tf... | ✓ | 18.69 | 0.0043 | 9 | 77.78% | 40.0 |
| 3 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 17.82 | 0.0029 | 9 | 77.78% | 41.7 |
| 4 | Alice and Bob play the following game. A stack ... | ✗ | 28.45 | 0.0211 | 6 | 83.33% | 50.0 |
| 5 | Eight circles of radius $34$ are sequentially t... | ✗ | 15.48 | 0.0018 | 6 | 100.00% | 35.0 |
| 6 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✓ | 18.12 | 0.0033 | 9 | 55.56% | 25.6 |
| 7 | Each vertex of a regular octagon is independent... | ✓ | 16.22 | 0.0024 | 8 | 75.00% | 36.9 |
| 8 | Find the number of triples of nonnegative integ... | ✗ | 20.04 | 0.0015 | 8 | 62.50% | 29.4 |
| 9 | There exist real numbers $x$ and $y$, both grea... | ✗ | 15.62 | 0.0023 | 8 | 62.50% | 31.2 |
| 10 | Alice chooses a set $A$ of positive integers. T... | ✗ | 15.40 | 0.0015 | 8 | 62.50% | 24.4 |
| 11 | Find the largest possible real part of \[(75+11... | ✓ | 17.88 | 0.0019 | 8 | 75.00% | 36.2 |
| 12 | Find the number of ways to place a digit in eac... | ✗ | 19.72 | 0.0057 | 10 | 70.00% | 40.5 |
| 13 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 18.42 | 0.0038 | 9 | 66.67% | 30.0 |
| 14 | Let $N$ be the greatest four-digit positive int... | ✗ | 15.93 | 0.0019 | 6 | 83.33% | 24.2 |
| 15 | Consider the paths of length $16$ that follow t... | ✗ | 16.61 | 0.0020 | 9 | 88.89% | 26.7 |
| 16 | Let $p$ be the least prime number for which the... | ✓ | 17.85 | 0.0107 | 4 | 100.00% | 40.0 |
| 17 | Let $\mathcal{B}$ be the set of rectangular box... | ✓ | 15.80 | 0.0034 | 7 | 100.00% | 24.3 |
| 18 | Find the number of rectangles that can be forme... | ✗ | 18.83 | 0.0037 | 9 | 66.67% | 40.6 |
| 19 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✓ | 16.52 | 0.0016 | 8 | 62.50% | 31.2 |
| 20 | There is a collection of $25$ indistinguishable... | ✗ | 13.28 | 0.0006 | 10 | 40.00% | 35.0 |
| 21 | Let $b \geq 2$ be an integer. Call a positive i... | ✗ | 16.69 | 0.0025 | 10 | 50.00% | 40.5 |
| 22 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 14.35 | 0.0016 | 5 | 100.00% | 35.0 |
| 23 | Let $A$, $B$, $C$, and $D$ be points on the hyp... | ✓ | 15.49 | 0.0033 | 7 | 71.43% | 33.6 |
| 24 | A list of positive integers has the following p... | ✗ | 15.72 | 0.0029 | 7 | 71.43% | 29.3 |
| 25 | Among the 900 residents of Aimeville, there are... | ✗ | 10.45 | 0.0008 | 4 | 50.00% | 28.8 |
| 26 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 16.49 | 0.0041 | 9 | 66.67% | 27.8 |
| 27 | Torus $T$ is the surface produced by revolving ... | ✗ | 17.70 | 0.0034 | 9 | 77.78% | 22.8 |
| 28 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 22.14 | 0.0007 | 12 | 33.33% | 26.7 |
| 29 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 14.46 | 0.0016 | 7 | 71.43% | 29.3 |
| 30 | Let $\omega \neq 1$ be a 13th root of unity. Fi... | ✓ | 17.75 | 0.0034 | 6 | 100.00% | 50.0 |
