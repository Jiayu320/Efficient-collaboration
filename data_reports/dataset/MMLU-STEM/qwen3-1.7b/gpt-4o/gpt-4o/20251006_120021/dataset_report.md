# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: qwen3-1.7b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 36
- 准确率: 72.00%
- 平均执行时间: 13.34 秒
- 平均成本: $0.0103

## 任务规划指标

- 平均任务步骤数: 4.31
- 平均压缩比例: 88.27%
- 平均每步骤Token限制: 37.12 tokens

## 理论性能指标

- 平均理论执行时间: 4.755 秒
- 平均顺序执行时间: 6.023 秒
- 平均并行加速比: 1.28x
- 理论与实际执行时间比例: 0.36x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.454 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 4.179 秒

### 生成速度
- 小模型平均每秒生成token数: 42.23 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 14.66 tokens/s
- 总平均每秒生成token数: 56.89 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 22.84 | 0.0106 | 4 | 100.00% | 32.5 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✓ | 21.03 | 0.0148 | 5 | 100.00% | 29.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 23.32 | 0.0168 | 7 | 100.00% | 18.6 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 14.21 | 0.0089 | 4 | 75.00% | 32.5 |
| 5 | Find the product of the given polynomials in th... | ✓ | 9.80 | 0.0085 | 3 | 100.00% | 43.3 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 18.39 | 0.0163 | 5 | 100.00% | 32.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 7.95 | 0.0051 | 4 | 75.00% | 35.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 11.55 | 0.0087 | 4 | 75.00% | 37.5 |
| 9 | Find the degree for the given field extension Q... | ✓ | 12.87 | 0.0099 | 4 | 100.00% | 32.5 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 12.57 | 0.0107 | 4 | 100.00% | 40.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 13.58 | 0.0157 | 6 | 66.67% | 38.3 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 11.67 | 0.0109 | 6 | 66.67% | 25.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 19.00 | 0.0180 | 6 | 100.00% | 41.7 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 18.57 | 0.0245 | 5 | 100.00% | 72.0 |
| 15 | Find the maximum possible order for an element ... | ✓ | 14.79 | 0.0096 | 4 | 100.00% | 65.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✓ | 10.53 | 0.0100 | 4 | 75.00% | 32.5 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 11.03 | 0.0067 | 4 | 100.00% | 28.8 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 13.25 | 0.0092 | 5 | 100.00% | 28.0 |
| 19 | The set of all real numbers under the usual mul... | ✗ | 0.00 | 0.0000 | - | - | - |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 10.45 | 0.0079 | 4 | 75.00% | 35.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 17.03 | 0.0117 | 4 | 75.00% | 32.5 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 18.28 | 0.0082 | 3 | 100.00% | 43.3 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 20.72 | 0.0076 | 4 | 75.00% | 32.5 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 15.82 | 0.0114 | 6 | 100.00% | 17.5 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 9.95 | 0.0097 | 4 | 75.00% | 35.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 17.93 | 0.0121 | 7 | 100.00% | 38.6 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 11.63 | 0.0111 | 4 | 75.00% | 32.5 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 13.36 | 0.0101 | 4 | 100.00% | 57.5 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 10.58 | 0.0087 | 4 | 75.00% | 35.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 9.19 | 0.0058 | 4 | 75.00% | 32.5 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 12.83 | 0.0120 | 6 | 66.67% | 35.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 11.47 | 0.0067 | 4 | 100.00% | 35.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 10.09 | 0.0073 | 4 | 75.00% | 35.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 13.97 | 0.0105 | 4 | 100.00% | 30.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 14.82 | 0.0155 | 4 | 100.00% | 32.5 |
| 36 | Find the degree for the given field extension Q... | ✗ | 13.71 | 0.0102 | 4 | 100.00% | 32.5 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 10.75 | 0.0057 | 3 | 100.00% | 30.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 16.14 | 0.0142 | 5 | 100.00% | 64.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 13.30 | 0.0141 | 3 | 100.00% | 31.7 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 10.22 | 0.0052 | 4 | 75.00% | 35.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 9.05 | 0.0047 | 3 | 100.00% | 33.3 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 10.39 | 0.0072 | 3 | 100.00% | 35.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 13.32 | 0.0130 | 4 | 75.00% | 36.2 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 11.71 | 0.0062 | 4 | 75.00% | 32.5 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 11.04 | 0.0102 | 4 | 75.00% | 32.5 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 11.05 | 0.0074 | 4 | 75.00% | 42.5 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 10.90 | 0.0072 | 4 | 75.00% | 30.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 13.79 | 0.0148 | 4 | 100.00% | 57.5 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 11.68 | 0.0105 | 4 | 75.00% | 32.5 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 14.78 | 0.0153 | 4 | 100.00% | 70.0 |
