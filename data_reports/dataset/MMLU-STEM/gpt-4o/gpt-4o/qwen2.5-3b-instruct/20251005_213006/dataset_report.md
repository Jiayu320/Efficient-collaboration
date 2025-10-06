# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 19
- 准确率: 38.00%
- 平均执行时间: 43.99 秒
- 平均成本: $0.0091

## 任务规划指标

- 平均任务步骤数: 5.71
- 平均压缩比例: 67.35%
- 平均每步骤Token限制: 39.30 tokens

## 理论性能指标

- 平均理论执行时间: 5.309 秒
- 平均顺序执行时间: 8.541 秒
- 平均并行加速比: 1.63x
- 理论与实际执行时间比例: 0.12x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.439 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 34.442 秒

### 生成速度
- 小模型平均每秒生成token数: 10.13 tokens/s
- 大模型平均每秒生成token数: 13.89 tokens/s
- 路由模型平均每秒生成token数: 6.72 tokens/s
- 总平均每秒生成token数: 30.74 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 131.38 | 0.0127 | 6 | 66.67% | 26.7 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✓ | 61.78 | 0.0069 | 6 | 66.67% | 20.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 97.37 | 0.0075 | 9 | 44.44% | 12.2 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 64.96 | 0.0166 | 6 | 66.67% | 48.3 |
| 5 | Find the product of the given polynomials in th... | ✗ | 94.31 | 0.0056 | 4 | 75.00% | 30.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 53.16 | 0.0203 | 8 | 62.50% | 31.2 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 51.90 | 0.0090 | 6 | 66.67% | 41.7 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 58.12 | 0.0142 | 8 | 50.00% | 18.8 |
| 9 | Find the degree for the given field extension Q... | ✓ | 22.79 | 0.0100 | 5 | 100.00% | 74.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 83.19 | 0.0062 | 6 | 83.33% | 25.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 28.06 | 0.0114 | 5 | 60.00% | 82.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 93.78 | 0.0092 | 7 | 42.86% | 16.4 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 69.30 | 0.0042 | 5 | 60.00% | 12.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 40.28 | 0.0106 | 5 | 100.00% | 40.0 |
| 15 | Find the maximum possible order for an element ... | ✓ | 16.34 | 0.0080 | 4 | 100.00% | 82.5 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 18.72 | 0.0112 | 6 | 66.67% | 40.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 18.49 | 0.0000 | - | - | - |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 12.98 | 0.0000 | - | - | - |
| 19 | The set of all real numbers under the usual mul... | ✗ | 24.84 | 0.0000 | - | - | - |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 8.26 | 0.0084 | 3 | 66.67% | 40.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 20.12 | 0.0084 | 5 | 60.00% | 26.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 42.10 | 0.0000 | - | - | - |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 9.69 | 0.0121 | 5 | 40.00% | 48.0 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 39.66 | 0.0000 | - | - | - |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 27.40 | 0.0133 | 7 | 57.14% | 27.1 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 18.61 | 0.0115 | 5 | 100.00% | 42.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 32.75 | 0.0112 | 5 | 60.00% | 58.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 47.61 | 0.0063 | 6 | 50.00% | 22.5 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 12.68 | 0.0140 | 6 | 66.67% | 35.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 53.52 | 0.0000 | - | - | - |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 13.15 | 0.0137 | 5 | 60.00% | 58.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 25.51 | 0.0095 | 5 | 60.00% | 30.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✗ | 34.86 | 0.0074 | 5 | 80.00% | 38.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 41.58 | 0.0131 | 6 | 50.00% | 83.3 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 55.38 | 0.0119 | 6 | 66.67% | 41.7 |
| 36 | Find the degree for the given field extension Q... | ✓ | 74.08 | 0.0123 | 6 | 66.67% | 38.3 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 23.05 | 0.0000 | - | - | - |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✓ | 15.18 | 0.0143 | 5 | 60.00% | 30.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 61.53 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 15.45 | 0.0093 | 5 | 60.00% | 46.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 17.82 | 0.0070 | 4 | 100.00% | 32.5 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 89.98 | 0.0095 | 6 | 83.33% | 26.7 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 71.69 | 0.0096 | 8 | 62.50% | 37.5 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 23.00 | 0.0089 | 6 | 66.67% | 41.7 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 23.76 | 0.0115 | 5 | 60.00% | 36.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 63.49 | 0.0079 | 5 | 80.00% | 30.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 14.67 | 0.0125 | 5 | 80.00% | 92.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 107.05 | 0.0189 | 7 | 57.14% | 30.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 40.38 | 0.0129 | 7 | 57.14% | 34.3 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 33.92 | 0.0142 | 6 | 66.67% | 25.0 |
