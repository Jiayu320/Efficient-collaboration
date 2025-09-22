# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-7-sonnet-latest
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 2
- 准确率: 6.67%
- 平均执行时间: 198.91 秒
- 平均成本: $0.0298


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.77 |
| Dependency Structure And Flow | 4.73 |
| Plan Relevance And Efficiency | 4.60 |
| Plan Soundness And Decomposition | 4.60 |
| Task Clarity And Executability | 4.73 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 2.64 |
| Correctness And Factual Accuracy | 2.31 |
| Effective Use Of Context | 2.39 |
| Instruction Following And Adherence | 2.46 |
| Relevance And Conciseness | 2.66 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.56 |
| Correctness And Factual Accuracy | 3.03 |
| Effective Use Of Context | 3.51 |
| Instruction Following And Adherence | 2.94 |
| Relevance And Conciseness | 3.33 |
## 任务规划指标

- 平均任务步骤数: 6.17
- 平均压缩比例: 75.47%
- 平均每步骤Token限制: 45.12 tokens

## 理论性能指标

- 平均理论执行时间: 9.721 秒
- 平均顺序执行时间: 25.171 秒
- 平均并行加速比: 3.41x
- 理论与实际执行时间比例: 0.05x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.953 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 183.844 秒

### 生成速度
- 小模型平均每秒生成token数: 6.56 tokens/s
- 大模型平均每秒生成token数: 9.62 tokens/s
- 路由模型平均每秒生成token数: 25.96 tokens/s
- 总平均每秒生成token数: 42.13 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 168.22 | 0.0222 | 5 | 100.00% | 36.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 205.75 | 0.0238 | 7 | 85.71% | 57.1 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 213.24 | 0.0246 | 7 | 71.43% | 31.4 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 148.49 | 0.0157 | 5 | 60.00% | 28.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 193.58 | 0.0288 | 6 | 66.67% | 31.7 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 245.83 | 0.0306 | 9 | 100.00% | 52.2 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 237.88 | 0.0516 | 8 | 25.00% | 51.2 |
| 8 | In a mathematics test number of participants is... | ✗ | 209.80 | 0.0205 | 8 | 75.00% | 46.2 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 221.79 | 0.0328 | 7 | 71.43% | 35.7 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 178.35 | 0.0221 | 6 | 100.00% | 43.3 |
| 11 | Consider the following two person game. A numbe... | ✗ | 168.01 | 0.0176 | 5 | 100.00% | 50.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 222.96 | 0.0241 | 8 | 87.50% | 70.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 196.73 | 0.0520 | 6 | 83.33% | 70.0 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 143.40 | 0.0182 | 4 | 75.00% | 35.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✗ | 160.02 | 0.1048 | 0 | 0.00% | 0.0 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 210.28 | 0.0438 | 7 | 42.86% | 55.7 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 246.33 | 0.0213 | 8 | 87.50% | 47.5 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 235.75 | 0.0240 | 8 | 87.50% | 55.0 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 181.65 | 0.0267 | 5 | 80.00% | 56.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 175.41 | 0.0201 | 6 | 83.33% | 45.0 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 224.68 | 0.0343 | 7 | 71.43% | 41.4 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 187.56 | 0.0283 | 6 | 100.00% | 73.3 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 179.86 | 0.0199 | 6 | 50.00% | 28.3 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 184.19 | 0.0186 | 6 | 100.00% | 35.0 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 165.27 | 0.0302 | 5 | 80.00% | 66.0 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 254.22 | 0.0265 | 6 | 83.33% | 51.7 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 224.55 | 0.0224 | 7 | 71.43% | 38.6 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 187.37 | 0.0334 | 5 | 60.00% | 42.0 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 232.17 | 0.0339 | 7 | 85.71% | 50.0 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 163.82 | 0.0218 | 5 | 80.00% | 30.0 |
