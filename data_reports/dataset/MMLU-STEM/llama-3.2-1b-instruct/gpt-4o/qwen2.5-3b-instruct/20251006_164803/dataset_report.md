# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: meta-llama/llama-3.2-1b-instruct
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 14
- 准确率: 28.00%
- 平均执行时间: 39.69 秒
- 平均成本: $0.0004

## 任务规划指标

- 平均任务步骤数: 3.49
- 平均压缩比例: 55.11%
- 平均每步骤Token限制: 20.28 tokens

## 理论性能指标

- 平均理论执行时间: 4.303 秒
- 平均顺序执行时间: 7.326 秒
- 平均并行加速比: 2.28x
- 理论与实际执行时间比例: 0.11x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.493 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 34.412 秒

### 生成速度
- 小模型平均每秒生成token数: 6.50 tokens/s
- 大模型平均每秒生成token数: 0.93 tokens/s
- 路由模型平均每秒生成token数: 22.59 tokens/s
- 总平均每秒生成token数: 30.02 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 62.34 | 0.0000 | 4 | 100.00% | 32.5 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 38.40 | 0.0000 | 4 | 100.00% | 27.5 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 7.97 | 0.0012 | 5 | 100.00% | 30.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 67.56 | 0.0030 | 6 | 66.67% | 36.7 |
| 5 | Find the product of the given polynomials in th... | ✗ | 50.23 | 0.0000 | 8 | 75.00% | 28.1 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 89.91 | 0.0000 | 5 | 80.00% | 44.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 30.01 | 0.0000 | 4 | 75.00% | 35.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 29.45 | 0.0000 | 5 | 80.00% | 28.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 90.13 | 0.0000 | 4 | 100.00% | 32.5 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 23.67 | 0.0000 | 6 | 100.00% | 31.7 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 8.28 | 0.0000 | 0 | 0.00% | 0.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 124.19 | 0.0000 | 9 | 66.67% | 20.3 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 18.10 | 0.0000 | 0 | 0.00% | 0.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 33.49 | 0.0066 | 5 | 100.00% | 50.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 13.79 | 0.0000 | 0 | 0.00% | 0.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 24.87 | 0.0000 | 6 | 83.33% | 30.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 7.53 | 0.0000 | 0 | 0.00% | 0.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 25.94 | 0.0000 | 5 | 80.00% | 20.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 29.69 | 0.0000 | 5 | 40.00% | 30.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✗ | 79.00 | 0.0000 | 4 | 75.00% | 32.5 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 63.03 | 0.0000 | 4 | 100.00% | 22.5 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 9.60 | 0.0000 | 0 | 0.00% | 0.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 7.15 | 0.0000 | 0 | 0.00% | 0.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 79.96 | 0.0000 | 7 | 57.14% | 33.6 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 10.14 | 0.0000 | 0 | 0.00% | 0.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✗ | 96.05 | 0.0000 | 7 | 100.00% | 27.1 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 52.43 | 0.0000 | 9 | 77.78% | 23.9 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 8.00 | 0.0000 | 0 | 0.00% | 0.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 5.42 | 0.0000 | 0 | 0.00% | 0.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 28.89 | 0.0000 | 4 | 75.00% | 25.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 48.09 | 0.0024 | 4 | 75.00% | 35.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 8.20 | 0.0000 | 0 | 0.00% | 0.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✗ | 5.41 | 0.0000 | 0 | 0.00% | 0.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 5.32 | 0.0000 | 0 | 0.00% | 0.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 9.83 | 0.0000 | 0 | 0.00% | 0.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 46.57 | 0.0000 | 5 | 100.00% | 25.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 39.10 | 0.0000 | 7 | 85.71% | 5.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 126.12 | 0.0000 | 6 | 100.00% | 30.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 0.00 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 24.78 | 0.0000 | 4 | 100.00% | 48.8 |
| 41 | The set of integers Z with the binary operation... | ✓ | 48.78 | 0.0000 | 6 | 83.33% | 29.2 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 6.13 | 0.0000 | 0 | 0.00% | 0.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 71.15 | 0.0045 | 4 | 75.00% | 52.5 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 56.36 | 0.0000 | 4 | 75.00% | 25.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 89.74 | 0.0000 | 6 | 100.00% | 40.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 7.14 | 0.0000 | 0 | 0.00% | 0.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 55.26 | 0.0000 | 4 | 75.00% | 22.5 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 13.04 | 0.0000 | 0 | 0.00% | 0.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 5.88 | 0.0000 | 0 | 0.00% | 0.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 102.26 | 0.0000 | 5 | 100.00% | 40.0 |
