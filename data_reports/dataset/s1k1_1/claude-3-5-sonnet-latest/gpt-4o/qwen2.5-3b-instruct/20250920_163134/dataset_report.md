# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_1.json
- 问题总数: 50
- 正确数量: 1
- 准确率: 2.00%
- 平均执行时间: 53.03 秒
- 平均成本: $0.0150

## 任务规划指标

- 平均任务步骤数: 7.72
- 平均压缩比例: 79.12%
- 平均每步骤Token限制: 48.22 tokens

## 理论性能指标

- 平均理论执行时间: 11.134 秒
- 平均顺序执行时间: 25.751 秒
- 平均并行加速比: 2.31x
- 理论与实际执行时间比例: 0.21x


## 任务分配统计

- 总任务数: 386
- 小模型执行任务数: 208
- 大模型执行任务数: 178
- 小模型任务占比: 53.89%
- 大模型任务占比: 46.11%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.707 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 31.991 秒

### 生成速度
- 小模型平均每秒生成token数: 4.14 tokens/s
- 大模型平均每秒生成token数: 4.66 tokens/s
- 路由模型平均每秒生成token数: 9.23 tokens/s
- 总平均每秒生成token数: 18.02 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 43.34 | 0.0113 | 7 | 85.71% | 50.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 46.51 | 0.0181 | 8 | 87.50% | 47.5 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✗ | 42.17 | 0.0151 | 8 | 100.00% | 43.8 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 29.89 | 0.0072 | 6 | 50.00% | 26.7 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 41.31 | 0.0172 | 10 | 40.00% | 44.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 50.89 | 0.0152 | 9 | 77.78% | 48.9 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 44.34 | 0.0275 | 9 | 33.33% | 56.7 |
| 8 | In a mathematics test number of participants is... | ✗ | 39.43 | 0.0202 | 9 | 88.89% | 57.8 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 45.78 | 0.0100 | 7 | 85.71% | 41.4 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 41.77 | 0.0106 | 7 | 42.86% | 38.6 |
| 11 | Consider the following two person game. A numbe... | ✗ | 50.04 | 0.0121 | 8 | 87.50% | 36.2 |
| 12 | Suppose  $a,\,b,$  and  $c$  are three complex ... | ✗ | 65.84 | 0.0252 | 8 | 100.00% | 55.0 |
| 13 | Prove that the function \[ f(\nu)= \int_1^{\fra... | ✗ | 41.41 | 0.0154 | 7 | 71.43% | 57.1 |
| 14 | Joanie takes a $\$6,\!000$ loan to pay for her ... | ✗ | 41.99 | 0.0074 | 5 | 60.00% | 38.0 |
| 15 | A function  $f:[0,\infty)\to[0,\infty)$  is int... | ✗ | 57.37 | 0.0232 | 8 | 100.00% | 58.1 |
| 16 | Let  $n\geq1$  be a positive integer.  $n$  lam... | ✗ | 51.92 | 0.0144 | 9 | 66.67% | 48.9 |
| 17 | For her zeroth project at Magic School, Emilia ... | ✗ | 45.80 | 0.0156 | 9 | 88.89% | 53.3 |
| 18 | In quantum mechanics, when calculating the inte... | ✗ | 68.16 | 0.0195 | 8 | 100.00% | 53.8 |
| 19 | Consider the additive group  $\mathbb{Z}^{2}$ .... | ✗ | 45.70 | 0.0216 | 9 | 77.78% | 53.3 |
| 20 | Find the sum of all positive integers $n$ such ... | ✗ | 51.06 | 0.0141 | 8 | 87.50% | 51.2 |
| 21 | For any positive integer $a,$ $\sigma(a)$ denot... | ✗ | 66.34 | 0.0140 | 9 | 77.78% | 48.9 |
| 22 | Carl chooses a *functional expression**  $E$  w... | ✗ | 43.70 | 0.0124 | 9 | 100.00% | 56.7 |
| 23 | Compute the mean molecular speed v in the light... | ✗ | 30.79 | 0.0072 | 5 | 40.00% | 28.0 |
| 24 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 90.73 | 0.0132 | 7 | 57.14% | 45.7 |
| 25 | Consider any rectangular table having finitely ... | ✗ | 49.04 | 0.0243 | 9 | 66.67% | 66.7 |
| 26 | The path of an asteroid that comes close to the... | ✗ | 76.60 | 0.0160 | 8 | 75.00% | 43.8 |
| 27 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 87.58 | 0.0109 | 8 | 87.50% | 33.8 |
| 28 | B.4 If $\Delta E_{r m s}=5.54 \times 10^{-17} \... | ✗ | 48.11 | 0.0102 | 7 | 57.14% | 42.9 |
| 29 |  $(BEL 5)$  Let  $G$  be the centroid of the tr... | ✗ | 55.50 | 0.0172 | 8 | 75.00% | 55.0 |
| 30 | 10) The handle of a gallon of milk is plugged b... | ✗ | 36.46 | 0.0133 | 7 | 71.43% | 45.7 |
| 31 | The sequences of real numbers $\left\{a_{i}\rig... | ✗ | 87.26 | 0.0150 | 7 | 100.00% | 64.3 |
| 32 | Given are real numbers $x, y$. For any pair of ... | ✗ | 56.10 | 0.0150 | 8 | 75.00% | 42.5 |
| 33 | Let $\omega$ be a nonreal root of $x^3 = 1,$ an... | ✗ | 53.19 | 0.0138 | 8 | 100.00% | 43.1 |
| 34 | Find the number of permutations of $1, 2, 3, 4,... | ✗ | 48.16 | 0.0167 | 9 | 88.89% | 53.9 |
| 35 | Find continuous functions  $x(t),\ y(t)$  such ... | ✗ | 52.36 | 0.0157 | 8 | 87.50% | 51.2 |
| 36 | Let $P(x)$ be a polynomial with integer coeffic... | ✗ | 67.54 | 0.0134 | 9 | 88.89% | 36.1 |
| 37 | Segments $\overline{AB}, \overline{AC},$ and $\... | ✗ | 85.08 | 0.0119 | 5 | 100.00% | 54.0 |
| 38 | Let  $(a_i)_{1\le i\le2015}$  be a sequence con... | ✗ | 40.89 | 0.0149 | 8 | 100.00% | 50.0 |
| 39 | Ana, Bob, and Cao bike at constant rates of $8.... | ✗ | 67.62 | 0.0182 | 9 | 100.00% | 50.0 |
| 40 | Consider the integer \[N = 9 + 99 + 999 + 9999 ... | ✗ | 50.36 | 0.0099 | 5 | 100.00% | 50.0 |
| 41 | A particle is located on the coordinate plane a... | ✗ | 57.51 | 0.0165 | 9 | 88.89% | 38.9 |
| 42 | How many positive integers less than 10,000 hav... | ✗ | 40.67 | 0.0150 | 8 | 50.00% | 47.5 |
| 43 | Identify the final product produced when cyclob... | ✗ | 38.74 | 0.0110 | 5 | 100.00% | 54.0 |
| 44 | There is a C-NOT gate where the condition is th... | ✗ | 58.31 | 0.0108 | 6 | 83.33% | 41.7 |
| 45 | An ideal gas is expanded from $\left(\mathrm{p}... | ✗ | 40.42 | 0.0185 | 10 | 30.00% | 45.0 |
| 46 | Let  $ f: Z \to Z$  be such that  $ f(1) \equal... | ✗ | 67.48 | 0.0214 | 9 | 77.78% | 55.6 |
| 47 | (d) Express $\frac{d^{2} x}{d t^{2}}$ and $\fra... | ✗ | 64.32 | 0.0110 | 7 | 85.71% | 44.3 |
| 48 | A train with cross-sectional area $S_{t}$ is mo... | ✓ | 34.56 | 0.0145 | 5 | 100.00% | 60.0 |
| 49 | An IPv4 packet contains the following data (in ... | ✗ | 70.96 | 0.0111 | 7 | 85.71% | 42.9 |
| 50 | Prove that if every subspace of a Hausdorff spa... | ✗ | 40.30 | 0.0143 | 8 | 75.00% | 58.8 |
