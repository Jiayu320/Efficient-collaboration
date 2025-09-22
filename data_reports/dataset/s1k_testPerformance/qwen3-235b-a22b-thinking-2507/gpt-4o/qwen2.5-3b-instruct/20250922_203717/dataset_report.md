# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-235b-a22b-thinking-2507
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 2
- 准确率: 6.67%
- 平均执行时间: 321.63 秒
- 平均成本: $0.0053


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.66 |
| Dependency Structure And Flow | 4.86 |
| Plan Relevance And Efficiency | 4.86 |
| Plan Soundness And Decomposition | 4.86 |
| Task Clarity And Executability | 4.86 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 2.20 |
| Correctness And Factual Accuracy | 2.20 |
| Effective Use Of Context | 2.20 |
| Instruction Following And Adherence | 2.09 |
| Relevance And Conciseness | 2.23 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 3.33 |
| Correctness And Factual Accuracy | 3.04 |
| Effective Use Of Context | 3.38 |
| Instruction Following And Adherence | 3.08 |
| Relevance And Conciseness | 3.15 |
## 任务规划指标

- 平均任务步骤数: 5.00
- 平均压缩比例: 82.37%
- 平均每步骤Token限制: 45.83 tokens

## 理论性能指标

- 平均理论执行时间: 7.211 秒
- 平均顺序执行时间: 18.934 秒
- 平均并行加速比: 2.59x
- 理论与实际执行时间比例: 0.02x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 27.816 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 204.552 秒

### 生成速度
- 小模型平均每秒生成token数: 1.29 tokens/s
- 大模型平均每秒生成token数: 1.83 tokens/s
- 路由模型平均每秒生成token数: 7.72 tokens/s
- 总平均每秒生成token数: 10.85 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 126.25 | 0.0005 | 3 | 100.00% | 33.3 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 270.73 | 0.0045 | 6 | 100.00% | 65.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 243.12 | 0.0045 | 6 | 50.00% | 31.7 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 207.80 | 0.0041 | 3 | 66.67% | 30.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✓ | 328.57 | 0.0115 | 4 | 75.00% | 47.5 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 200.02 | 0.0006 | 5 | 100.00% | 42.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 38.55 | 0.0000 | 0 | 0.00% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 434.32 | 0.0048 | 8 | 75.00% | 55.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 207.33 | 0.0007 | 7 | 71.43% | 45.7 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 248.70 | 0.0057 | 6 | 100.00% | 35.0 |
| 11 | Consider the following two person game. A numbe... | ✗ | 219.63 | 0.0005 | 5 | 100.00% | 60.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 1102.19 | 0.0091 | 2 | 100.00% | 65.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 308.18 | 0.0061 | 5 | 100.00% | 56.0 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 172.37 | 0.0040 | 4 | 75.00% | 35.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✗ | 281.55 | 0.0048 | 5 | 80.00% | 50.0 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 356.37 | 0.0085 | 7 | 85.71% | 74.3 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 325.80 | 0.0100 | 6 | 100.00% | 58.3 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 241.81 | 0.0059 | 4 | 75.00% | 50.0 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 247.27 | 0.0049 | 5 | 100.00% | 50.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 350.04 | 0.0041 | 6 | 83.33% | 53.3 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 335.28 | 0.0169 | 6 | 83.33% | 46.7 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 536.11 | 0.0118 | 5 | 60.00% | 52.0 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 179.93 | 0.0047 | 3 | 66.67% | 40.0 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 331.53 | 0.0029 | 7 | 71.43% | 22.9 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 402.85 | 0.0036 | 5 | 100.00% | 68.0 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 364.45 | 0.0067 | 6 | 83.33% | 38.3 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 877.65 | 0.0119 | 6 | 83.33% | 38.3 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 171.53 | 0.0006 | 3 | 100.00% | 26.7 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 278.42 | 0.0008 | 7 | 85.71% | 52.9 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 260.57 | 0.0031 | 5 | 100.00% | 52.0 |
