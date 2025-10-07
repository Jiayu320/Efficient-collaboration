# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-1.7b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 23
- 准确率: 46.00%
- 平均执行时间: 54.01 秒
- 平均成本: $0.0018

## 任务规划指标

- 平均任务步骤数: 4.34
- 平均压缩比例: 87.41%
- 平均每步骤Token限制: 38.73 tokens

## 理论性能指标

- 平均理论执行时间: 5.489 秒
- 平均顺序执行时间: 6.842 秒
- 平均并行加速比: 1.26x
- 理论与实际执行时间比例: 0.10x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.206 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 48.406 秒

### 生成速度
- 小模型平均每秒生成token数: 10.29 tokens/s
- 大模型平均每秒生成token数: 1.78 tokens/s
- 路由模型平均每秒生成token数: 4.43 tokens/s
- 总平均每秒生成token数: 16.50 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 63.73 | 0.0000 | 4 | 100.00% | 32.5 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 74.14 | 0.0052 | 5 | 100.00% | 34.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 54.78 | 0.0000 | 6 | 83.33% | 20.8 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 74.37 | 0.0072 | 4 | 75.00% | 33.8 |
| 5 | Find the product of the given polynomials in th... | ✗ | 20.77 | 0.0000 | 3 | 100.00% | 41.7 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 28.22 | 0.0000 | 4 | 100.00% | 35.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 41.35 | 0.0046 | 4 | 75.00% | 35.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 23.00 | 0.0000 | 4 | 75.00% | 32.5 |
| 9 | Find the degree for the given field extension Q... | ✓ | 78.76 | 0.0017 | 4 | 100.00% | 32.5 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 60.08 | 0.0000 | 4 | 100.00% | 37.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 77.67 | 0.0094 | 4 | 75.00% | 33.8 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✗ | 106.37 | 0.0000 | 6 | 66.67% | 25.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 33.49 | 0.0000 | 7 | 100.00% | 23.6 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 97.47 | 0.0000 | 4 | 100.00% | 72.5 |
| 15 | Find the maximum possible order for an element ... | ✓ | 33.22 | 0.0000 | 4 | 100.00% | 32.5 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 67.81 | 0.0000 | 4 | 75.00% | 42.5 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 34.33 | 0.0013 | 3 | 100.00% | 31.7 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 28.25 | 0.0018 | 3 | 100.00% | 33.3 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 55.47 | 0.0000 | 6 | 50.00% | 28.3 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 65.00 | 0.0046 | 4 | 75.00% | 35.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 59.23 | 0.0000 | 4 | 75.00% | 36.2 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 28.29 | 0.0027 | 3 | 100.00% | 50.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 39.22 | 0.0000 | 4 | 75.00% | 40.0 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 67.15 | 0.0000 | 5 | 60.00% | 28.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 35.70 | 0.0056 | 4 | 75.00% | 35.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 54.84 | 0.0026 | 7 | 100.00% | 68.6 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 128.32 | 0.0000 | 7 | 85.71% | 28.6 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 79.88 | 0.0000 | 10 | 100.00% | 38.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 26.01 | 0.0000 | 4 | 75.00% | 35.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 75.82 | 0.0000 | 4 | 75.00% | 62.5 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 47.68 | 0.0049 | 4 | 75.00% | 65.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 44.86 | 0.0000 | 4 | 100.00% | 30.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 29.05 | 0.0027 | 4 | 75.00% | 32.5 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 47.56 | 0.0000 | 5 | 100.00% | 40.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 37.59 | 0.0030 | 4 | 100.00% | 35.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 67.64 | 0.0000 | 4 | 100.00% | 32.5 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 32.32 | 0.0012 | 3 | 100.00% | 33.3 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 52.14 | 0.0000 | 5 | 100.00% | 54.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 71.30 | 0.0000 | 3 | 100.00% | 31.7 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 14.03 | 0.0000 | 4 | 100.00% | 65.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 65.31 | 0.0024 | 3 | 100.00% | 36.7 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 95.27 | 0.0051 | 3 | 100.00% | 31.7 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 33.04 | 0.0000 | 4 | 75.00% | 36.2 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 33.81 | 0.0000 | 4 | 75.00% | 35.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 45.45 | 0.0053 | 4 | 75.00% | 37.5 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 41.74 | 0.0050 | 4 | 75.00% | 32.5 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 50.72 | 0.0043 | 4 | 75.00% | 35.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 73.82 | 0.0000 | 4 | 100.00% | 32.5 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 62.75 | 0.0052 | 4 | 75.00% | 35.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 41.64 | 0.0035 | 4 | 100.00% | 90.0 |
