# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 1
- 准确率: 3.33%
- 平均执行时间: 205.72 秒
- 平均成本: $0.0314


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.77 |
| Dependency Structure And Flow | 4.80 |
| Plan Relevance And Efficiency | 4.60 |
| Plan Soundness And Decomposition | 4.60 |
| Task Clarity And Executability | 4.90 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.43 |
| Correctness And Factual Accuracy | 3.79 |
| Effective Use Of Context | 4.09 |
| Instruction Following And Adherence | 3.88 |
| Relevance And Conciseness | 4.39 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.22 |
| Correctness And Factual Accuracy | 3.50 |
| Effective Use Of Context | 4.03 |
| Instruction Following And Adherence | 3.43 |
| Relevance And Conciseness | 3.95 |
## 任务规划指标

- 平均任务步骤数: 6.57
- 平均压缩比例: 74.94%
- 平均每步骤Token限制: 47.04 tokens

## 理论性能指标

- 平均理论执行时间: 9.616 秒
- 平均顺序执行时间: 27.026 秒
- 平均并行加速比: 2.85x
- 理论与实际执行时间比例: 0.05x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.462 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 190.289 秒

### 生成速度
- 小模型平均每秒生成token数: 6.45 tokens/s
- 大模型平均每秒生成token数: 13.49 tokens/s
- 路由模型平均每秒生成token数: 26.08 tokens/s
- 总平均每秒生成token数: 46.02 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 174.41 | 0.0209 | 5 | 100.00% | 34.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 238.01 | 0.0407 | 7 | 85.71% | 65.7 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 236.27 | 0.0194 | 9 | 55.56% | 25.6 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 149.23 | 0.0168 | 5 | 40.00% | 36.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 236.18 | 0.0407 | 8 | 50.00% | 40.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 249.74 | 0.0208 | 8 | 100.00% | 43.8 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 248.77 | 0.0633 | 8 | 25.00% | 62.5 |
| 8 | In a mathematics test number of participants is... | ✗ | 251.40 | 0.0459 | 8 | 50.00% | 52.5 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 232.68 | 0.0271 | 8 | 62.50% | 32.5 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 194.77 | 0.0188 | 7 | 100.00% | 44.3 |
| 11 | Consider the following two person game. A numbe... | ✗ | 176.37 | 0.0343 | 5 | 100.00% | 58.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 216.22 | 0.0258 | 7 | 71.43% | 50.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 212.71 | 0.0338 | 6 | 83.33% | 56.7 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 129.73 | 0.0154 | 4 | 75.00% | 27.5 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✓ | 209.85 | 0.0474 | 7 | 71.43% | 57.1 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 192.29 | 0.0338 | 6 | 50.00% | 63.3 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 237.12 | 0.0271 | 7 | 100.00% | 45.7 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 223.46 | 0.0477 | 7 | 85.71% | 55.7 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 222.87 | 0.0360 | 6 | 83.33% | 80.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 163.95 | 0.0194 | 6 | 100.00% | 46.7 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 239.54 | 0.0365 | 9 | 55.56% | 43.3 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 216.72 | 0.0235 | 8 | 87.50% | 58.8 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 156.62 | 0.0204 | 5 | 40.00% | 26.0 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 193.84 | 0.0220 | 6 | 100.00% | 33.3 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 184.61 | 0.0291 | 7 | 71.43% | 62.9 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 260.94 | 0.0641 | 6 | 66.67% | 40.0 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 205.27 | 0.0222 | 7 | 71.43% | 32.9 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 152.53 | 0.0273 | 4 | 100.00% | 37.5 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 197.53 | 0.0409 | 6 | 66.67% | 65.0 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 167.96 | 0.0202 | 5 | 100.00% | 34.0 |
