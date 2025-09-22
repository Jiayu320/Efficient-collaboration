# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: meta-llama/llama-3-8b-instruct
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 186.78 秒
- 平均成本: $0.0071


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 2.57 |
| Dependency Structure And Flow | 3.60 |
| Plan Relevance And Efficiency | 2.53 |
| Plan Soundness And Decomposition | 2.37 |
| Task Clarity And Executability | 3.73 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.39 |
| Correctness And Factual Accuracy | 2.48 |
| Effective Use Of Context | 2.88 |
| Instruction Following And Adherence | 2.67 |
| Relevance And Conciseness | 3.24 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.21 |
| Correctness And Factual Accuracy | 2.83 |
| Effective Use Of Context | 2.92 |
| Instruction Following And Adherence | 2.69 |
| Relevance And Conciseness | 2.90 |
## 任务规划指标

- 平均任务步骤数: 4.37
- 平均压缩比例: 86.36%
- 平均每步骤Token限制: 42.04 tokens

## 理论性能指标

- 平均理论执行时间: 5.530 秒
- 平均顺序执行时间: 13.742 秒
- 平均并行加速比: 2.97x
- 理论与实际执行时间比例: 0.03x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 3.047 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 169.534 秒

### 生成速度
- 小模型平均每秒生成token数: 6.06 tokens/s
- 大模型平均每秒生成token数: 11.92 tokens/s
- 路由模型平均每秒生成token数: 27.35 tokens/s
- 总平均每秒生成token数: 45.34 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 158.70 | 0.0090 | 5 | 100.00% | 46.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 149.24 | 0.0056 | 5 | 100.00% | 46.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 787.81 | 0.0103 | 7 | 85.71% | 31.4 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 150.31 | 0.0078 | 4 | 100.00% | 42.5 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 150.10 | 0.0096 | 3 | 100.00% | 53.3 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 192.61 | 0.0206 | 6 | 100.00% | 56.7 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 115.40 | 0.0002 | 0 | 0.00% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 158.15 | 0.0001 | 6 | 83.33% | 43.3 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 157.58 | 0.0099 | 5 | 80.00% | 52.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 173.62 | 0.0079 | 6 | 50.00% | 31.7 |
| 11 | Consider the following two person game. A numbe... | ✗ | 148.17 | 0.0032 | 4 | 100.00% | 25.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 179.51 | 0.0190 | 7 | 100.00% | 80.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 98.32 | 0.0025 | 3 | 100.00% | 43.3 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 121.81 | 0.0001 | 4 | 100.00% | 20.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✗ | 142.87 | 0.0044 | 3 | 100.00% | 50.0 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 180.86 | 0.0028 | 5 | 100.00% | 38.0 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 374.15 | 0.0053 | 5 | 60.00% | 34.0 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 122.23 | 0.0093 | 4 | 75.00% | 40.0 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 432.77 | 0.0131 | 5 | 60.00% | 52.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 136.10 | 0.0020 | 4 | 100.00% | 45.0 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 136.97 | 0.0032 | 4 | 100.00% | 52.5 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 158.39 | 0.0128 | 4 | 100.00% | 35.0 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 113.06 | 0.0001 | 3 | 66.67% | 40.0 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 325.78 | 0.0143 | 5 | 80.00% | 46.0 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 146.39 | 0.0001 | 6 | 100.00% | 16.7 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 133.35 | 0.0129 | 4 | 75.00% | 52.5 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 135.89 | 0.0130 | 4 | 100.00% | 47.5 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 120.49 | 0.0088 | 4 | 75.00% | 57.5 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 99.88 | 0.0028 | 3 | 100.00% | 50.0 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 102.89 | 0.0024 | 3 | 100.00% | 33.3 |
