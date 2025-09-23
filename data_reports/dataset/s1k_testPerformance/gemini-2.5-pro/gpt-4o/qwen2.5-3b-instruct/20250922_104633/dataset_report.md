# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 3
- 准确率: 10.00%
- 平均执行时间: 243.56 秒
- 平均成本: $0.0264


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.90 |
| Dependency Structure And Flow | 4.93 |
| Plan Relevance And Efficiency | 4.87 |
| Plan Soundness And Decomposition | 4.87 |
| Task Clarity And Executability | 5.00 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.58 |
| Correctness And Factual Accuracy | 4.05 |
| Effective Use Of Context | 4.38 |
| Instruction Following And Adherence | 4.22 |
| Relevance And Conciseness | 4.67 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.58 |
| Correctness And Factual Accuracy | 4.05 |
| Effective Use Of Context | 4.38 |
| Instruction Following And Adherence | 4.22 |
| Relevance And Conciseness | 4.67 |
## 任务规划指标

- 平均任务步骤数: 5.47
- 平均压缩比例: 83.35%
- 平均每步骤Token限制: 75.77 tokens

## 理论性能指标

- 平均理论执行时间: 10.087 秒
- 平均顺序执行时间: 26.055 秒
- 平均并行加速比: 2.57x
- 理论与实际执行时间比例: 0.04x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 16.263 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 168.500 秒

### 生成速度
- 小模型平均每秒生成token数: 3.15 tokens/s
- 大模型平均每秒生成token数: 4.50 tokens/s
- 路由模型平均每秒生成token数: 19.34 tokens/s
- 总平均每秒生成token数: 26.98 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 119.00 | 0.0127 | 3 | 100.00% | 46.7 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 416.90 | 0.0434 | 6 | 100.00% | 113.3 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 166.11 | 0.0192 | 5 | 80.00% | 36.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 139.14 | 0.0179 | 4 | 75.00% | 45.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 203.90 | 0.0226 | 6 | 83.33% | 53.3 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✓ | 140.11 | 0.0236 | 3 | 100.00% | 100.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 314.48 | 0.0642 | 8 | 37.50% | 85.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 275.22 | 0.0320 | 6 | 50.00% | 63.3 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 257.16 | 0.0220 | 6 | 66.67% | 58.3 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 188.29 | 0.0166 | 5 | 100.00% | 58.0 |
| 11 | Consider the following two person game. A numbe... | ✗ | 259.25 | 0.0202 | 6 | 83.33% | 75.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 520.49 | 0.0314 | 9 | 77.78% | 72.2 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 225.78 | 0.0274 | 5 | 100.00% | 70.0 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 173.87 | 0.0150 | 4 | 75.00% | 42.5 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✓ | 305.41 | 0.0191 | 7 | 85.71% | 71.4 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 237.33 | 0.0166 | 5 | 100.00% | 160.0 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 317.80 | 0.0273 | 5 | 100.00% | 106.0 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 204.79 | 0.0265 | 6 | 83.33% | 58.3 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 207.78 | 0.0159 | 5 | 100.00% | 50.0 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 217.92 | 0.0225 | 8 | 87.50% | 38.8 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 239.85 | 0.0209 | 6 | 83.33% | 56.7 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 436.85 | 0.0720 | 8 | 87.50% | 83.8 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 123.21 | 0.0107 | 3 | 66.67% | 46.7 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 168.22 | 0.0142 | 4 | 100.00% | 47.5 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 343.40 | 0.0405 | 5 | 60.00% | 240.0 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 209.35 | 0.0374 | 4 | 100.00% | 107.5 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 218.95 | 0.0239 | 7 | 85.71% | 47.1 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 148.68 | 0.0153 | 4 | 100.00% | 70.0 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 385.77 | 0.0504 | 7 | 57.14% | 125.7 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 141.82 | 0.0116 | 4 | 75.00% |
| **平均表现** | **4.38** |
