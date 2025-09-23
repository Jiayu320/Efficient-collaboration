# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: deepseek-reasoner
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 5
- 准确率: 16.67%
- 平均执行时间: 602.53 秒
- 平均成本: $0.0110


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.93 |
| Dependency Structure And Flow | 4.97 |
| Plan Relevance And Efficiency | 5.00 |
| Plan Soundness And Decomposition | 5.00 |
| Task Clarity And Executability | 4.97 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.53 |
| Correctness And Factual Accuracy | 3.91 |
| Effective Use Of Context | 4.11 |
| Instruction Following And Adherence | 3.96 |
| Relevance And Conciseness | 4.43 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.10 |
| Correctness And Factual Accuracy | 3.76 |
| Effective Use Of Context | 3.92 |
| Instruction Following And Adherence | 3.47 |
| Relevance And Conciseness | 3.85 |
## 任务规划指标

- 平均任务步骤数: 5.63
- 平均压缩比例: 79.42%
- 平均每步骤Token限制: 39.08 tokens

## 理论性能指标

- 平均理论执行时间: 10.577 秒
- 平均顺序执行时间: 26.917 秒
- 平均并行加速比: 2.52x
- 理论与实际执行时间比例: 0.02x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 47.452 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 271.427 秒

### 生成速度
- 小模型平均每秒生成token数: 0.65 tokens/s
- 大模型平均每秒生成token数: 1.45 tokens/s
- 路由模型平均每秒生成token数: 2.95 tokens/s
- 总平均每秒生成token数: 5.05 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 171.75 | 0.0026 | 3 | 100.00% | 33.3 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✓ | 854.66 | 0.0175 | 5 | 100.00% | 56.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 331.60 | 0.0026 | 6 | 83.33% | 18.3 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 212.61 | 0.0040 | 5 | 60.00% | 31.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 395.25 | 0.0100 | 6 | 83.33% | 38.3 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 416.33 | 0.0079 | 6 | 100.00% | 28.3 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 782.64 | 0.0312 | 9 | 22.22% | 54.4 |
| 8 | In a mathematics test number of participants is... | ✗ | 578.26 | 0.0332 | 9 | 66.67% | 51.1 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 1196.20 | 0.0036 | 10 | 40.00% | 29.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✓ | 451.62 | 0.0182 | 7 | 100.00% | 50.0 |
| 11 | Consider the following two person game. A numbe... | ✗ | 519.18 | 0.0098 | 6 | 83.33% | 46.7 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 1030.66 | 0.0093 | 5 | 80.00% | 42.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 885.26 | 0.0210 | 7 | 100.00% | 54.3 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 226.97 | 0.0035 | 4 | 75.00% | 35.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✓ | 647.32 | 0.0130 | 8 | 75.00% | 47.5 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 608.36 | 0.0103 | 5 | 100.00% | 40.0 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 537.61 | 0.0197 | 5 | 100.00% | 54.0 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 561.48 | 0.0144 | 5 | 60.00% | 38.0 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 448.30 | 0.0137 | 5 | 100.00% | 42.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✓ | 639.69 | 0.0140 | 7 | 71.43% | 42.9 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 471.65 | 0.0080 | 5 | 100.00% | 34.0 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 1605.40 | 0.0007 | 0 | 0.00% | 0.0 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 219.20 | 0.0032 | 4 | 50.00% | 20.0 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 771.34 | 0.0046 | 6 | 83.33% | 33.3 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 643.38 | 0.0147 | 4 | 100.00% | 55.0 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 772.88 | 0.0053 | 6 | 100.00% | 45.0 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 380.60 | 0.0079 | 6 | 83.33% | 33.3 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 511.82 | 0.0033 | 5 | 80.00% | 32.0 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 757.09 | 0.0231 | 7 | 85.71% | 54.3 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 446.82 | 0.0008 | 3 | 100.00% |
| **平均表现** | **3.82** |
