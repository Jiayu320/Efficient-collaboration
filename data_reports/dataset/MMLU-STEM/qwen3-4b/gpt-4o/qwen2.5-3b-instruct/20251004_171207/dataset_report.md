# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-4b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 20
- 准确率: 40.00%
- 平均执行时间: 52.59 秒
- 平均成本: $0.0045

## 任务规划指标

- 平均任务步骤数: 4.39
- 平均压缩比例: 72.20%
- 平均每步骤Token限制: 101.28 tokens

## 理论性能指标

- 平均理论执行时间: 5.532 秒
- 平均顺序执行时间: 8.092 秒
- 平均并行加速比: 1.51x
- 理论与实际执行时间比例: 0.11x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.244 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 40.145 秒

### 生成速度
- 小模型平均每秒生成token数: 5.68 tokens/s
- 大模型平均每秒生成token数: 11.15 tokens/s
- 路由模型平均每秒生成token数: 4.83 tokens/s
- 总平均每秒生成token数: 21.67 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 56.45 | 0.0113 | 4 | 75.00% | 225.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 23.93 | 0.0053 | 2 | 100.00% | 250.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 92.39 | 0.0058 | 5 | 60.00% | 18.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 28.23 | 0.0032 | 3 | 66.67% | 46.7 |
| 5 | Find the product of the given polynomials in th... | ✗ | 57.34 | 0.0000 | - | - | - |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 37.95 | 0.0118 | 5 | 100.00% | 300.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 58.68 | 0.0051 | 4 | 75.00% | 175.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 16.56 | 0.0106 | 6 | 66.67% | 266.7 |
| 9 | Find the degree for the given field extension Q... | ✓ | 55.99 | 0.0071 | 5 | 40.00% | 162.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 99.53 | 0.0025 | 6 | 100.00% | 19.2 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 24.85 | 0.0100 | 4 | 75.00% | 237.5 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 104.39 | 0.0154 | 7 | 57.14% | 78.6 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 56.29 | 0.0000 | - | - | - |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 149.19 | 0.0000 | 3 | 100.00% | 21.7 |
| 15 | Find the maximum possible order for an element ... | ✗ | 40.53 | 0.0000 | - | - | - |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 31.84 | 0.0064 | 3 | 100.00% | 233.3 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 32.34 | 0.0065 | 5 | 80.00% | 38.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 25.55 | 0.0000 | - | - | - |
| 19 | The set of all real numbers under the usual mul... | ✗ | 60.77 | 0.0024 | 6 | 33.33% | 73.3 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 25.95 | 0.0022 | 3 | 66.67% | 43.3 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 13.68 | 0.0044 | 3 | 66.67% | 200.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 58.90 | 0.0000 | - | - | - |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 40.40 | 0.0009 | 3 | 66.67% | 18.3 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 142.08 | 0.0024 | 5 | 100.00% | 30.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 29.22 | 0.0023 | 3 | 66.67% | 200.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✗ | 80.56 | 0.0068 | 7 | 28.57% | 25.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 39.91 | 0.0106 | 6 | 66.67% | 55.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 80.96 | 0.0017 | 5 | 60.00% | 140.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 32.10 | 0.0093 | 4 | 75.00% | 25.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 18.45 | 0.0039 | 3 | 66.67% | 166.7 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 0.00 | 0.0000 | - | - | - |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 80.63 | 0.0037 | 6 | 83.33% | 31.7 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✗ | 37.08 | 0.0013 | 3 | 66.67% | 18.3 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 28.29 | 0.0146 | 7 | 57.14% | 21.4 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 34.93 | 0.0040 | 3 | 66.67% | 166.7 |
| 36 | Find the degree for the given field extension Q... | ✓ | 76.17 | 0.0058 | 5 | 60.00% | 26.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 33.85 | 0.0000 | - | - | - |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✓ | 89.97 | 0.0020 | 5 | 60.00% | 130.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 88.05 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 25.06 | 0.0025 | 3 | 66.67% | 23.3 |
| 41 | The set of integers Z with the binary operation... | ✓ | 47.34 | 0.0007 | 3 | 100.00% | 23.3 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 53.61 | 0.0000 | - | - | - |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 61.67 | 0.0041 | 6 | 66.67% | 26.7 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 30.74 | 0.0019 | 3 | 66.67% | 150.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 81.00 | 0.0097 | 6 | 83.33% | 40.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 48.53 | 0.0014 | 3 | 66.67% | 18.3 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 33.80 | 0.0041 | 3 | 100.00% | 216.7 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 97.59 | 0.0137 | 7 | 57.14% | 20.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 24.40 | 0.0025 | 3 | 66.67% | 16.7 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 41.54 | 0.0060 | 4 | 100.00% | 175.0 |
