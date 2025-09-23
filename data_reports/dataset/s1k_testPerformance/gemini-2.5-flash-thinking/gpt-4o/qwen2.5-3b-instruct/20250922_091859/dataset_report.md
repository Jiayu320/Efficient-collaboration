# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-flash-thinking
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 1
- 准确率: 3.33%
- 平均执行时间: 174.32 秒
- 平均成本: $0.0081


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 4.00 |
| Dependency Structure And Flow | 5.00 |
| Plan Relevance And Efficiency | 5.00 |
| Plan Soundness And Decomposition | 5.00 |
| Task Clarity And Executability | 4.96 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.71 |
| Correctness And Factual Accuracy | 4.34 |
| Effective Use Of Context | 4.57 |
| Instruction Following And Adherence | 4.51 |
| Relevance And Conciseness | 4.69 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.71 |
| Correctness And Factual Accuracy | 4.34 |
| Effective Use Of Context | 4.57 |
| Instruction Following And Adherence | 4.51 |
| Relevance And Conciseness | 4.69 |
## 任务规划指标

- 平均任务步骤数: 4.63
- 平均压缩比例: 60.54%
- 平均每步骤Token限制: 47.52 tokens

## 理论性能指标

- 平均理论执行时间: 6.551 秒
- 平均顺序执行时间: 17.468 秒
- 平均并行加速比: 2.33x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 7.775 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 140.824 秒

### 生成速度
- 小模型平均每秒生成token数: 3.97 tokens/s
- 大模型平均每秒生成token数: 5.26 tokens/s
- 路由模型平均每秒生成token数: 22.38 tokens/s
- 总平均每秒生成token数: 31.62 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 117.74 | 0.0028 | 4 | 100.00% | 45.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 367.18 | 0.0059 | 8 | 100.00% | 71.2 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 158.33 | 0.0032 | 6 | 66.67% | 38.3 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 130.28 | 0.0062 | 5 | 60.00% | 42.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 142.67 | 0.0093 | 5 | 80.00% | 52.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 158.14 | 0.0069 | 6 | 83.33% | 46.7 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 278.45 | 0.0313 | 7 | 42.86% | 77.1 |
| 8 | In a mathematics test number of participants is... | ✗ | 193.73 | 0.0282 | 6 | 50.00% | 81.7 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 272.08 | 0.0194 | 10 | 40.00% | 62.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 168.21 | 0.0084 | 6 | 66.67% | 61.7 |
| 11 | Consider the following two person game. A numbe... | ✗ | 165.97 | 0.0036 | 5 | 100.00% | 80.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 334.73 | 0.0053 | 7 | 85.71% | 74.3 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 223.56 | 0.0086 | 5 | 100.00% | 94.0 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 138.99 | 0.0024 | 4 | 75.00% | 50.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✗ | 244.34 | 0.0000 | 0 | 0.00% | 0.0 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 191.25 | 0.0104 | 5 | 100.00% | 92.0 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 263.77 | 0.0040 | 7 | 100.00% | 61.4 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 195.88 | 0.0208 | 6 | 83.33% | 58.3 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 142.07 | 0.0085 | 4 | 100.00% | 62.5 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 227.11 | 0.0067 | 9 | 77.78% | 43.3 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 186.18 | 0.0136 | 6 | 83.33% | 58.3 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 177.84 | 0.0000 | 0 | 0.00% | 0.0 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 119.40 | 0.0068 | 4 | 50.00% | 45.0 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 199.73 | 0.0121 | 7 | 71.43% | 37.1 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 293.00 | 0.0188 | 7 | 100.00% | 91.4 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 28.52 | 0.0000 | 0 | 0.00% | 0.0 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 28.19 | 0.0000 | 0 | 0.00% | 0.0 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 27.01 | 0.0000 | 0 | 0.00% | 0.0 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 28.24 | 0.0000 | 0 | 0.00% | 0.0 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 27.14 | 0.0000 | 0 | 0.00% |
| **平均表现** | **4.57** |
