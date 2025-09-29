# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 30
- 正确数量: 2
- 准确率: 6.67%
- 平均执行时间: 249.48 秒
- 平均成本: $0.0137


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 2.80 |
| Dependency Structure And Flow | 4.30 |
| Plan Relevance And Efficiency | 3.90 |
| Plan Soundness And Decomposition | 3.73 |
| Task Clarity And Executability | 4.77 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.19 |
| Correctness And Factual Accuracy | 3.04 |
| Effective Use Of Context | 3.46 |
| Instruction Following And Adherence | 3.19 |
| Relevance And Conciseness | 4.13 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.13 |
| Correctness And Factual Accuracy | 3.13 |
| Effective Use Of Context | 3.40 |
| Instruction Following And Adherence | 3.27 |
| Relevance And Conciseness | 4.09 |
## 任务规划指标

- 平均任务步骤数: 5.37
- 平均压缩比例: 84.14%
- 平均每步骤Token限制: 56.19 tokens

## 理论性能指标

- 平均理论执行时间: 6.388 秒
- 平均顺序执行时间: 14.136 秒
- 平均并行加速比: 2.25x
- 理论与实际执行时间比例: 0.03x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.454 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 238.666 秒

### 生成速度
- 小模型平均每秒生成token数: 2.50 tokens/s
- 大模型平均每秒生成token数: 15.90 tokens/s
- 路由模型平均每秒生成token数: 30.23 tokens/s
- 总平均每秒生成token数: 48.62 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✓ | 212.54 | 0.0193 | 6 | 83.33% | 55.0 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 233.45 | 0.0185 | 6 | 83.33% | 45.0 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 272.44 | 0.0273 | 8 | 62.50% | 68.8 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 246.91 | 0.0295 | 6 | 66.67% | 78.3 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 188.24 | 0.0094 | 4 | 100.00% | 65.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 173.45 | 0.0088 | 4 | 75.00% | 52.5 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 811.55 | 0.0071 | 5 | 100.00% | 36.0 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 332.44 | 0.0216 | 10 | 80.00% | 59.0 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 160.64 | 0.0107 | 4 | 100.00% | 62.5 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 215.78 | 0.0136 | 7 | 57.14% | 42.9 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 204.80 | 0.0140 | 5 | 80.00% | 58.0 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 175.41 | 0.0067 | 5 | 80.00% | 46.0 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 201.39 | 0.0128 | 5 | 100.00% | 60.0 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 231.14 | 0.0133 | 6 | 66.67% | 60.0 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 258.24 | 0.0223 | 7 | 71.43% | 54.3 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 106.82 | 0.0069 | 2 | 100.00% | 70.0 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 145.11 | 0.0055 | 3 | 100.00% | 50.0 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 194.59 | 0.0156 | 5 | 100.00% | 72.0 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 239.19 | 0.0133 | 6 | 100.00% | 55.0 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 178.57 | 0.0097 | 4 | 75.00% | 60.0 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 204.24 | 0.0238 | 5 | 100.00% | 78.0 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 210.93 | 0.0168 | 5 | 80.00% | 54.0 |
| 23 | A list of positive integers has the following p... | ✗ | 154.70 | 0.0082 | 4 | 100.00% | 55.0 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 259.59 | 0.0130 | 7 | 71.43% | 45.7 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 310.62 | 0.0156 | 9 | 100.00% | 48.9 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 129.74 | 0.0084 | 3 | 66.67% | 70.0 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 189.62 | 0.0100 | 4 | 100.00% | 55.0 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 315.60 | 0.0082 | 8 | 50.00% | 36.2 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 176.79 | 0.0168 | 4 | 100.00% | 47.5 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 749.88 | 0.0050 | 4 | 75.00% | 45.0 |
