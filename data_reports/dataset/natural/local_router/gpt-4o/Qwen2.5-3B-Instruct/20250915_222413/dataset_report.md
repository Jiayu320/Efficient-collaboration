# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/natural.json
- 问题总数: 50
- 正确数量: 15
- 准确率: 30.00%
- 平均执行时间: 34.87 秒
- 平均成本: $0.0029

## 任务规划指标

- 平均任务步骤数: 9.16
- 平均压缩比例: 78.26%
- 平均每步骤Token限制: 33.18 tokens

## 理论性能指标

- 平均理论执行时间: 8.515 秒
- 平均顺序执行时间: 22.232 秒
- 平均并行加速比: 2.66x
- 理论与实际执行时间比例: 0.24x


## 任务分配统计

- 总任务数: 458
- 小模型执行任务数: 8
- 大模型执行任务数: 450
- 小模型任务占比: 1.75%
- 大模型任务占比: 98.25%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.212 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 28.867 秒

### 生成速度
- 小模型平均每秒生成token数: 0.00 tokens/s
- 大模型平均每秒生成token数: 3.04 tokens/s
- 路由模型平均每秒生成token数: 16.85 tokens/s
- 总平均每秒生成token数: 19.89 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the total work done on an object when i... | ✓ | 33.54 | 0.0017 | 10 | 80.00% | 21.0 |
| 2 | Propose a system of 'Practical Numbers' that de... | ✗ | 33.08 | 0.0025 | 10 | 70.00% | 56.0 |
| 3 | Solve the differential equation (1/F)(dF/dx) = ... | ✗ | 33.38 | 0.0033 | 10 | 100.00% | 22.5 |
| 4 | Two equal masses, each with a mass similar to t... | ✗ | 40.25 | 0.0052 | 10 | 100.00% | 49.0 |
| 5 | Prove that for a vector space V = F^n, where n ... | ✓ | 31.04 | 0.0023 | 7 | 100.00% | 57.1 |
| 6 | Discuss the feasibility of solving the particle... | ✗ | 55.77 | 0.0049 | 10 | 100.00% | 65.0 |
| 7 | Given the area of a parallelogram is 420 square... | ✓ | 60.40 | 0.0029 | 10 | 100.00% | 18.0 |
| 8 | What is the minimum number of red squares requi... | ✗ | 37.23 | 0.0027 | 6 | 100.00% | 40.8 |
| 9 | Two 3.0g bullets are fired with speeds of 40.0 ... | ✓ | 39.73 | 0.0025 | 7 | 42.86% | 19.3 |
| 10 | Consider a partial differential equation (PDE) ... | ✓ | 53.15 | 0.0064 | 9 | 100.00% | 30.6 |
| 11 | A plywood fish tank is 16' long x 4' wide x 3.5... | ✗ | 29.69 | 0.0016 | 9 | 66.67% | 19.4 |
| 12 | Given the context of a student seeking to remed... | ✗ | 31.96 | 0.0030 | 9 | 88.89% | 32.8 |
| 13 | A vector is rotated by Euler angles $\alpha$, $... | ✓ | 29.10 | 0.0008 | 10 | 40.00% | 24.0 |
| 14 | Consider a Brownian motion $B_t$ conditioned on... | ✗ | 32.11 | 0.0023 | 10 | 70.00% | 58.0 |
| 15 | Consider a scenario where space mining is condu... | ✓ | 35.32 | 0.0034 | 10 | 100.00% | 41.5 |
| 16 | Given a function $f:[a,b]\to \mathbb{R}$ that i... | ✓ | 30.34 | 0.0028 | 8 | 75.00% | 28.1 |
| 17 | Given the discussion on the Younger Dryas event... | ✗ | 34.73 | 0.0026 | 10 | 80.00% | 28.0 |
| 18 | Consider a point charge q at rest. Using the Li... | ✓ | 30.36 | 0.0016 | 10 | 60.00% | 24.0 |
| 19 | A projectile is launched with an initial veloci... | ✗ | 30.37 | 0.0017 | 7 | 85.71% | 20.0 |
| 20 | What steps would you take to diagnose and repai... | ✗ | 30.22 | 0.0010 | 10 | 70.00% | 27.0 |
| 21 | Given the molecular structure of oil and its pr... | ✗ | 28.23 | 0.0005 | 8 | 50.00% | 30.0 |
| 22 | Explain the importance of factor groups in abst... | ✓ | 31.69 | 0.0029 | 9 | 88.89% | 39.4 |
| 23 | Consider Young's double slit experiment, where ... | ✗ | 34.19 | 0.0034 | 10 | 100.00% | 34.0 |
| 24 | Suppose we want to approximate $\tan(1)$ to a p... | ✗ | 35.22 | 0.0051 | 10 | 90.00% | 28.5 |
| 25 | A sample of carbon dioxide with a mass of 2.45g... | ✗ | 39.02 | 0.0012 | 7 | 42.86% | 21.4 |
| 26 | Consider a stationary electron in a universe wi... | ✓ | 28.90 | 0.0011 | 8 | 75.00% | 29.4 |
| 27 | Given the weekly scrap rate data for 13 weeks a... | ✗ | 35.75 | 0.0030 | 10 | 80.00% | 33.5 |
| 28 | Solve the fractional differential equation $$a\... | ✗ | 44.86 | 0.0037 | 10 | 80.00% | 45.5 |
| 29 | Given 10.00 mL of a strong acid solution mixed ... | ✓ | 44.06 | 0.0036 | 10 | 70.00% | 21.5 |
| 30 | Design a constant heat source for the calibrati... | ✗ | 31.46 | 0.0020 | 10 | 80.00% | 34.5 |
| 31 | Consider a spaceship traveling in interstellar ... | ✓ | 31.96 | 0.0021 | 10 | 80.00% | 32.5 |
| 32 | Describe the conventional choice for the refere... | ✗ | 34.42 | 0.0041 | 10 | 90.00% | 33.5 |
| 33 | Consider an accelerating reference frame with r... | ✗ | 36.66 | 0.0071 | 9 | 100.00% | 46.1 |
| 34 | Define a continuous product for a function f(x)... | ✗ | 29.20 | 0.0007 | 10 | 50.00% | 30.5 |
| 35 | Analyze the case study of Sears, Roebuck and Co... | ✗ | 30.25 | 0.0016 | 10 | 60.00% | 32.5 |
| 36 | If a bowling ball at absolute zero suddenly app... | ✗ | 28.23 | 0.0036 | 7 | 71.43% | 36.4 |
| 37 | In the context of supersymmetric (SUSY) theorie... | ✗ | 34.09 | 0.0050 | 10 | 80.00% | 57.0 |
| 38 | What are the odds of winning at Minesweeper wit... | ✗ | 29.71 | 0.0012 | 9 | 55.56% | 34.4 |
| 39 | A spacecraft is accelerating at 1 g to reach 10... | ✗ | 42.43 | 0.0059 | 10 | 60.00% | 22.0 |
| 40 | What is the current radius of the cosmological ... | ✗ | 41.69 | 0.0026 | 10 | 60.00% | 19.0 |
| 41 | Find the partial sum of the polynomial $4x^2+7x... | ✓ | 32.96 | 0.0023 | 10 | 80.00% | 23.5 |
| 42 | Consider the formation of sulfur hexafluoride (... | ✗ | 29.01 | 0.0008 | 9 | 55.56% | 27.2 |
| 43 | What are the key factors to consider when evalu... | ✗ | 36.14 | 0.0034 | 10 | 90.00% | 38.5 |
| 44 | Given a sequence $a_n$ defined by the recurrenc... | ✗ | 33.31 | 0.0065 | 10 | 70.00% | 34.5 |
| 45 | Suppose we have a binary random event X with pr... | ✗ | 29.13 | 0.0026 | 7 | 100.00% | 25.0 |
| 46 | Consider the logistic curve given by the differ... | ✗ | 36.68 | 0.0049 | 10 | 100.00% | 44.0 |
| 47 | Prove that for an independent family of subsets... | ✗ | 29.80 | 0.0016 | 9 | 44.44% | 48.9 |
| 48 | Prove by mathematical induction that $\sum\limi... | ✗ | 29.82 | 0.0030 | 6 | 100.00% | 25.0 |
| 49 | What is the maximum angle of an inclined plane,... | ✓ | 31.10 | 0.0020 | 10 | 80.00% | 28.0 |
| 50 | Computerplus company already paid a $6 dividend... | ✗ | 31.97 | 0.0034 | 8 | 100.00% | 20.6 |
