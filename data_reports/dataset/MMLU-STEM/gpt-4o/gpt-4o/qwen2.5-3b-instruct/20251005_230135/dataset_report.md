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
- 正确数量: 17
- 准确率: 34.00%
- 平均执行时间: 34.61 秒
- 平均成本: $0.0073

## 任务规划指标

- 平均任务步骤数: 4.73
- 平均压缩比例: 65.80%
- 平均每步骤Token限制: 31.42 tokens

## 理论性能指标

- 平均理论执行时间: 4.288 秒
- 平均顺序执行时间: 6.909 秒
- 平均并行加速比: 1.64x
- 理论与实际执行时间比例: 0.12x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.396 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 26.206 秒

### 生成速度
- 小模型平均每秒生成token数: 9.14 tokens/s
- 大模型平均每秒生成token数: 14.63 tokens/s
- 路由模型平均每秒生成token数: 7.18 tokens/s
- 总平均每秒生成token数: 30.96 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 64.14 | 0.0096 | 3 | 66.67% | 20.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✓ | 70.33 | 0.0104 | 5 | 100.00% | 19.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 83.19 | 0.0071 | 6 | 33.33% | 10.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 7.04 | 0.0056 | 3 | 66.67% | 23.3 |
| 5 | Find the product of the given polynomials in th... | ✗ | 48.81 | 0.0000 | - | - | - |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 0.00 | 0.0000 | - | - | - |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 8.94 | 0.0095 | 5 | 40.00% | 34.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 24.94 | 0.0101 | 6 | 66.67% | 48.3 |
| 9 | Find the degree for the given field extension Q... | ✓ | 13.58 | 0.0071 | 3 | 100.00% | 63.3 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 30.96 | 0.0086 | 6 | 50.00% | 18.3 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 75.00 | 0.0095 | 5 | 80.00% | 21.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✗ | 66.04 | 0.0083 | 7 | 42.86% | 14.3 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 130.73 | 0.0087 | 5 | 80.00% | 15.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 76.62 | 0.0076 | 4 | 100.00% | 22.5 |
| 15 | Find the maximum possible order for an element ... | ✗ | 46.35 | 0.0088 | 5 | 80.00% | 19.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✓ | 19.93 | 0.0065 | 4 | 75.00% | 30.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 22.39 | 0.0000 | - | - | - |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 39.82 | 0.0000 | - | - | - |
| 19 | The set of all real numbers under the usual mul... | ✗ | 28.73 | 0.0065 | 5 | 40.00% | 16.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✗ | 13.95 | 0.0059 | 3 | 66.67% | 36.7 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 14.81 | 0.0105 | 5 | 60.00% | 34.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 44.23 | 0.0000 | - | - | - |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 50.62 | 0.0048 | 5 | 40.00% | 26.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 52.28 | 0.0115 | 6 | 33.33% | 33.3 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 14.98 | 0.0103 | 5 | 60.00% | 34.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 29.18 | 0.0091 | 4 | 50.00% | 40.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 15.79 | 0.0171 | 6 | 66.67% | 40.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 41.75 | 0.0092 | 5 | 60.00% | 70.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 27.42 | 0.0093 | 4 | 75.00% | 30.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 14.04 | 0.0077 | 5 | 60.00% | 36.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 0.00 | 0.0000 | - | - | - |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 19.30 | 0.0078 | 4 | 100.00% | 35.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✗ | 30.21 | 0.0000 | - | - | - |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 37.25 | 0.0089 | 6 | 50.00% | 35.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 17.09 | 0.0094 | 5 | 60.00% | 34.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 21.45 | 0.0094 | 4 | 75.00% | 30.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 22.51 | 0.0000 | - | - | - |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 13.79 | 0.0157 | 5 | 40.00% | 21.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 33.10 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 40.95 | 0.0057 | 5 | 60.00% | 28.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 15.60 | 0.0084 | 4 | 100.00% | 40.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 64.60 | 0.0042 | 5 | 60.00% | 18.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 10.41 | 0.0112 | 4 | 75.00% | 42.5 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 9.88 | 0.0112 | 5 | 40.00% | 42.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 22.93 | 0.0099 | 4 | 75.00% | 30.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✓ | 8.20 | 0.0061 | 4 | 75.00% | 20.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 24.38 | 0.0072 | 4 | 75.00% | 32.5 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 32.94 | 0.0128 | 5 | 80.00% | 60.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 21.51 | 0.0099 | 5 | 60.00% | 28.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 107.59 | 0.0066 | 5 | 80.00% | 38.0 |
