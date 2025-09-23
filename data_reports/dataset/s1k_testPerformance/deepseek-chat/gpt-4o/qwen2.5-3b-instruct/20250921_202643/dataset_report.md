# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: deepseek-chat
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 4
- 准确率: 13.33%
- 平均执行时间: 245.64 秒
- 平均成本: $0.0126


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.45 |
| Dependency Structure And Flow | 4.38 |
| Plan Relevance And Efficiency | 4.55 |
| Plan Soundness And Decomposition | 4.45 |
| Task Clarity And Executability | 4.41 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.49 |
| Correctness And Factual Accuracy | 4.07 |
| Effective Use Of Context | 4.14 |
| Instruction Following And Adherence | 4.21 |
| Relevance And Conciseness | 4.41 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.49 |
| Correctness And Factual Accuracy | 4.07 |
| Effective Use Of Context | 4.14 |
| Instruction Following And Adherence | 4.21 |
| Relevance And Conciseness | 4.41 |
## 任务规划指标

- 平均任务步骤数: 5.03
- 平均压缩比例: 72.09%
- 平均每步骤Token限制: 46.21 tokens

## 理论性能指标

- 平均理论执行时间: 15.504 秒
- 平均顺序执行时间: 72.421 秒
- 平均并行加速比: 11.25x
- 理论与实际执行时间比例: 0.06x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.597 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 235.322 秒

### 生成速度
- 小模型平均每秒生成token数: 2.51 tokens/s
- 大模型平均每秒生成token数: 5.16 tokens/s
- 路由模型平均每秒生成token数: 16.73 tokens/s
- 总平均每秒生成token数: 24.40 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 149.58 | 0.0016 | 3 | 100.00% | 33.3 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 261.49 | 0.0041 | 0 | 0.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 180.78 | 0.0036 | 5 | 80.00% | 34.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 2.56 | 0.0000 | - | - | - |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 270.04 | 0.0281 | 8 | 75.00% | 53.8 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 237.39 | 0.0206 | 7 | 71.43% | 50.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✓ | 308.94 | 0.0293 | 4 | 50.00% | 105.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 401.98 | 0.0325 | 9 | 66.67% | 54.4 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✓ | 246.79 | 0.0185 | 5 | 80.00% | 50.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 239.65 | 0.0109 | 6 | 66.67% | 55.0 |
| 11 | Consider the following two person game. A numbe... | ✗ | 332.09 | 0.0158 | 5 | 100.00% | 62.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 249.27 | 0.0118 | 2 | 100.00% | 75.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✓ | 203.30 | 0.0263 | 5 | 80.00% | 70.0 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 165.80 | 0.0011 | 4 | 75.00% | 30.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✗ | 257.55 | 0.0041 | 0 | 0.00% | 0.0 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 233.90 | 0.0117 | 6 | 66.67% | 46.7 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 322.96 | 0.0055 | 7 | 100.00% | 40.0 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 303.23 | 0.0185 | 7 | 71.43% | 54.3 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 225.06 | 0.0094 | 4 | 100.00% | 45.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 251.95 | 0.0075 | 8 | 100.00% | 34.4 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 272.42 | 0.0134 | 5 | 100.00% | 62.0 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 283.18 | 0.0041 | 0 | 0.00% | 0.0 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 208.38 | 0.0012 | 6 | 66.67% | 33.3 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 190.08 | 0.0013 | 6 | 83.33% | 38.3 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 377.72 | 0.0420 | 9 | 44.44% | 84.4 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 239.46 | 0.0130 | 5 | 100.00% | 52.0 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 304.24 | 0.0083 | 5 | 80.00% | 36.0 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 196.33 | 0.0091 | 4 | 50.00% | 42.5 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 230.27 | 0.0233 | 6 | 83.33% | 66.7 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 222.94 | 0.0017 | 5 | 100.00% |
| **平均表现** | **4.26** |
