# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: openai/gpt-5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 24
- 正确数量: 9
- 准确率: 37.5%
- 平均执行时间: 275.11 秒
- 平均成本: $0.0191


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.84 |
| Dependency Structure And Flow | 4.80 |
| Plan Relevance And Efficiency | 4.84 |
| Plan Soundness And Decomposition | 5.00 |
| Task Clarity And Executability | 4.64 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.86 |
| Correctness And Factual Accuracy | 4.61 |
| Effective Use Of Context | 4.69 |
| Instruction Following And Adherence | 4.67 |
| Relevance And Conciseness | 4.83 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.86 |
| Correctness And Factual Accuracy | 4.61 |
| Effective Use Of Context | 4.69 |
| Instruction Following And Adherence | 4.67 |
| Relevance And Conciseness | 4.83 |
## 任务规划指标

- 平均任务步骤数: 3.83
- 平均压缩比例: 70.27%
- 平均每步骤Token限制: 10.00 tokens

## 理论性能指标

- 平均理论执行时间: 35.229 秒
- 平均顺序执行时间: 53.311 秒
- 平均并行加速比: 1.55x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 20.640 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 185.518 秒

### 生成速度
- 小模型平均每秒生成token数: 2.58 tokens/s
- 大模型平均每秒生成token数: 3.53 tokens/s
- 路由模型平均每秒生成token数: 5.91 tokens/s
- 总平均每秒生成token数: 12.02 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 190.78 | 0.0131 | 5 | 80.00% | 40.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 359.42 | 0.0029 | 0 | 0.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 215.01 | 0.0246 | 4 | 100.00% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 169.44 | 0.0086 | 3 | 100.00% | 35.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✓ | 291.86 | 0.0217 | 5 | 80.00% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 164.60 | 0.0000 | 0 | 0.00% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✓ | 403.94 | 0.0727 | 6 | 33.33% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 328.53 | 0.0393 | 5 | 80.00% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 365.24 | 0.0180 | 6 | 83.33% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✓ | 196.24 | 0.0307 | 4 | 25.00% | 0.0 |
| 11 | Consider the following two person game. A numbe... | ✓ | 223.83 | 0.0138 | 5 | 100.00% | 64.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 377.26 | 0.0029 | 0 | 0.00% | 0.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 259.69 | 0.0360 | 5 | 100.00% | 0.0 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 205.42 | 0.0167 | 4 | 75.00% | 25.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✓ | 292.74 | 0.0159 | 5 | 100.00% | 0.0 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 413.46 | 0.0192 | 7 | 85.71% | 0.0 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 301.81 | 0.0338 | 5 | 100.00% | 0.0 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 223.03 | 0.0182 | 3 | 100.00% | 0.0 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✓ | 214.21 | 0.0305 | 4 | 100.00% | 0.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 266.97 | 0.0100 | 4 | 100.00% | 0.0 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✓ | 253.74 | 0.0200 | 5 | 100.00% | 38.0 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 310.70 | 0.0032 | 0 | 0.00% | 0.0 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 289.01 | 0.0152 | 4 | 100.00% | 0.0 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 438.32 | 0.0284 | 5 | 100.00% | 0.0 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 119.65 | 0.0000 | 0 | 0.00% | 0.0 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 384.54 | 0.0194 | 5 | 100.00% | 58.0 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 331.34 | 0.0250 | 7 | 85.71% | 0.0 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 287.07 | 0.0131 | 5 | 80.00% | 0.0 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 129.44 | 0.0028 | 0 | 0.00% | 0.0 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 245.95 | 0.0168 | 4 | 100.00% |
| **平均表现** | **4.73** |
