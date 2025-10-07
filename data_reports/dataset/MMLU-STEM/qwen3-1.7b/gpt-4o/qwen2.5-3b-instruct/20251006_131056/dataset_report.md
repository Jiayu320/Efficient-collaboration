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
- 正确数量: 22
- 准确率: 44.00%
- 平均执行时间: 55.34 秒
- 平均成本: $0.0020

## 任务规划指标

- 平均任务步骤数: 4.22
- 平均压缩比例: 85.63%
- 平均每步骤Token限制: 35.94 tokens

## 理论性能指标

- 平均理论执行时间: 5.186 秒
- 平均顺序执行时间: 6.602 秒
- 平均并行加速比: 1.29x
- 理论与实际执行时间比例: 0.09x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.191 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 49.638 秒

### 生成速度
- 小模型平均每秒生成token数: 9.04 tokens/s
- 大模型平均每秒生成token数: 2.01 tokens/s
- 路由模型平均每秒生成token数: 4.27 tokens/s
- 总平均每秒生成token数: 15.32 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 76.12 | 0.0019 | 4 | 100.00% | 32.5 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 74.36 | 0.0000 | 5 | 100.00% | 28.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 56.66 | 0.0000 | 6 | 66.67% | 32.5 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 60.31 | 0.0044 | 4 | 75.00% | 35.0 |
| 5 | Find the product of the given polynomials in th... | ✗ | 37.32 | 0.0058 | 3 | 100.00% | 43.3 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 73.38 | 0.0000 | 5 | 100.00% | 29.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 32.62 | 0.0039 | 4 | 75.00% | 32.5 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 70.85 | 0.0000 | 4 | 75.00% | 37.5 |
| 9 | Find the degree for the given field extension Q... | ✓ | 69.77 | 0.0000 | 4 | 100.00% | 32.5 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 47.33 | 0.0000 | 4 | 100.00% | 32.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 33.46 | 0.0048 | 4 | 75.00% | 65.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✗ | 68.38 | 0.0024 | 5 | 60.00% | 30.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 45.60 | 0.0000 | 5 | 80.00% | 27.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 65.32 | 0.0068 | 6 | 100.00% | 50.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 23.45 | 0.0000 | 4 | 100.00% | 28.8 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 51.44 | 0.0000 | 4 | 75.00% | 35.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 29.74 | 0.0000 | 3 | 100.00% | 31.7 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 36.01 | 0.0000 | 5 | 100.00% | 28.0 |
| 19 | The set of all real numbers under the usual mul... | ✗ | 38.17 | 0.0000 | 6 | 50.00% | 28.3 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 99.15 | 0.0053 | 4 | 75.00% | 35.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 56.99 | 0.0059 | 4 | 75.00% | 33.8 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 14.19 | 0.0000 | 4 | 100.00% | 32.5 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 61.88 | 0.0043 | 4 | 75.00% | 35.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 69.42 | 0.0000 | 5 | 100.00% | 26.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 28.60 | 0.0043 | 4 | 75.00% | 35.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 52.75 | 0.0063 | 6 | 50.00% | 35.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 35.75 | 0.0035 | 4 | 75.00% | 37.5 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 29.62 | 0.0000 | 5 | 100.00% | 72.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 71.28 | 0.0000 | 4 | 75.00% | 35.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 78.40 | 0.0050 | 4 | 75.00% | 32.5 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 32.83 | 0.0000 | 4 | 75.00% | 32.5 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✗ | 31.89 | 0.0000 | 4 | 100.00% | 32.5 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 47.50 | 0.0044 | 4 | 75.00% | 40.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 132.37 | 0.0020 | 4 | 100.00% | 32.5 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 56.25 | 0.0000 | 4 | 100.00% | 42.5 |
| 36 | Find the degree for the given field extension Q... | ✓ | 39.15 | 0.0000 | 4 | 100.00% | 32.5 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 23.86 | 0.0000 | 3 | 100.00% | 31.7 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 42.07 | 0.0000 | 5 | 100.00% | 68.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 54.80 | 0.0000 | 3 | 100.00% | 40.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 50.16 | 0.0029 | 4 | 75.00% | 40.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 66.55 | 0.0024 | 4 | 100.00% | 30.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 56.63 | 0.0020 | 3 | 100.00% | 31.7 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 59.40 | 0.0000 | 4 | 75.00% | 35.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 47.09 | 0.0058 | 4 | 75.00% | 35.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 96.09 | 0.0000 | 4 | 75.00% | 35.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✓ | 33.61 | 0.0000 | 4 | 75.00% | 32.5 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 102.69 | 0.0026 | 4 | 75.00% | 30.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 80.41 | 0.0048 | 4 | 100.00% | 40.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 65.62 | 0.0048 | 4 | 75.00% | 35.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 59.59 | 0.0060 | 4 | 100.00% | 32.5 |
