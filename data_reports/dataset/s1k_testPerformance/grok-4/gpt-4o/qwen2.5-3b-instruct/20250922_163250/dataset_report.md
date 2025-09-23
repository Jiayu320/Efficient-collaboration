# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: grok-4
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k_testPerformance.json
- 问题总数: 30
- 正确数量: 3
- 准确率: 10.00%
- 平均执行时间: 488.23 秒
- 平均成本: $0.0257


## 平均评估分数

### 规划器平均分数
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Attribute Accuracy | 3.64 |
| Dependency Structure And Flow | 4.82 |
| Plan Relevance And Efficiency | 4.79 |
| Plan Soundness And Decomposition | 4.71 |
| Task Clarity And Executability | 4.86 |

### 执行器平均分数

#### 模型: `gpt-4o`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.66 |
| Correctness And Factual Accuracy | 3.93 |
| Effective Use Of Context | 4.22 |
| Instruction Following And Adherence | 4.11 |
| Relevance And Conciseness | 4.62 |

#### 模型: `qwen2.5-3b-instruct`
| 维度 | 平均分 (满分5分) |
| --- | --- |
| Clarity And Machine Usability | 4.23 |
| Correctness And Factual Accuracy | 3.21 |
| Effective Use Of Context | 4.15 |
| Instruction Following And Adherence | 3.24 |
| Relevance And Conciseness | 4.03 |
## 任务规划指标

- 平均任务步骤数: 4.67
- 平均压缩比例: 74.35%
- 平均每步骤Token限制: 36.12 tokens

## 理论性能指标

- 平均理论执行时间: 22.689 秒
- 平均顺序执行时间: 39.541 秒
- 平均并行加速比: 1.71x
- 理论与实际执行时间比例: 0.05x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 72.705 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 233.964 秒

### 生成速度
- 小模型平均每秒生成token数: 1.22 tokens/s
- 大模型平均每秒生成token数: 2.33 tokens/s
- 路由模型平均每秒生成token数: 4.68 tokens/s
- 总平均每秒生成token数: 8.23 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 163.30 | 0.0195 | 3 | 100.00% | 40.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 679.64 | 0.0410 | 8 | 100.00% | 53.8 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 242.66 | 0.0193 | 4 | 75.00% | 27.5 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 225.10 | 0.0203 | 3 | 66.67% | 33.3 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 257.37 | 0.0238 | 6 | 66.67% | 28.3 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 254.38 | 0.0347 | 4 | 100.00% | 55.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 242.93 | 0.0603 | 6 | 33.33% | 63.3 |
| 8 | In a mathematics test number of participants is... | ✗ | 382.64 | 0.0477 | 6 | 83.33% | 46.7 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 251.56 | 0.0301 | 3 | 100.00% | 50.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 291.04 | 0.0199 | 3 | 100.00% | 46.7 |
| 11 | Consider the following two person game. A numbe... | ✗ | 700.52 | 0.0355 | 10 | 100.00% | 47.0 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 1008.36 | 0.0210 | 6 | 100.00% | 50.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✓ | 715.67 | 0.0391 | 6 | 83.33% | 50.0 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 270.25 | 0.0236 | 8 | 87.50% | 31.2 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✓ | 1441.50 | 0.0469 | 6 | 83.33% | 45.0 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 381.47 | 0.0209 | 8 | 100.00% | 41.2 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 292.26 | 0.0264 | 6 | 50.00% | 38.3 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 509.51 | 0.0219 | 3 | 66.67% | 40.0 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 383.91 | 0.0259 | 6 | 83.33% | 31.7 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 234.81 | 0.0198 | 4 | 100.00% | 35.0 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 261.83 | 0.0182 | 5 | 100.00% | 28.0 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 1868.50 | 0.0079 | 0 | 0.00% | 0.0 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 139.04 | 0.0184 | 3 | 100.00% | 33.3 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 304.07 | 0.0125 | 0 | 0.00% | 0.0 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 465.68 | 0.0000 | 0 | 0.00% | 0.0 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 452.47 | 0.0228 | 7 | 85.71% | 31.4 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 416.41 | 0.0277 | 5 | 80.00% | 36.0 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 696.00 | 0.0000 | 0 | 0.00% | 0.0 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 582.04 | 0.0437 | 7 | 85.71% | 55.7 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 531.94 | 0.0209 | 4 | 100.00% |
| **平均表现** | **3.77** |
