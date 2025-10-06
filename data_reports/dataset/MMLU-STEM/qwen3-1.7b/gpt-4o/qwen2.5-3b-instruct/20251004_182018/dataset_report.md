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
- 正确数量: 14
- 准确率: 28.00%
- 平均执行时间: 37.36 秒
- 平均成本: $0.0026

## 任务规划指标

- 平均任务步骤数: 4.57
- 平均压缩比例: 91.74%
- 平均每步骤Token限制: 46.57 tokens

## 理论性能指标

- 平均理论执行时间: 5.160 秒
- 平均顺序执行时间: 6.377 秒
- 平均并行加速比: 1.25x
- 理论与实际执行时间比例: 0.14x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.095 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 28.662 秒

### 生成速度
- 小模型平均每秒生成token数: 3.62 tokens/s
- 大模型平均每秒生成token数: 10.93 tokens/s
- 路由模型平均每秒生成token数: 9.16 tokens/s
- 总平均每秒生成token数: 23.71 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 30.41 | 0.0048 | 4 | 100.00% | 100.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 83.97 | 0.0000 | 2 | 100.00% | 150.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 11.79 | 0.0000 | 8 | 100.00% | 21.2 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 19.93 | 0.0045 | 2 | 100.00% | 100.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 37.99 | 0.0065 | 3 | 100.00% | 103.3 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 19.55 | 0.0008 | 8 | 100.00% | 10.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 41.68 | 0.0020 | 5 | 100.00% | 10.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 75.63 | 0.0087 | 4 | 100.00% | 100.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 37.54 | 0.0000 | 1 | 100.00% | 100.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 16.82 | 0.0000 | 2 | 100.00% | 55.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 39.79 | 0.0014 | 3 | 100.00% | 100.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✗ | 56.53 | 0.0000 | - | - | - |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 9.33 | 0.0036 | 3 | 100.00% | 10.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 171.74 | 0.0042 | 4 | 100.00% | 32.5 |
| 15 | Find the maximum possible order for an element ... | ✓ | 64.22 | 0.0000 | 2 | 100.00% | 55.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 18.46 | 0.0022 | 6 | 66.67% | 15.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 34.74 | 0.0000 | - | - | - |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 24.89 | 0.0000 | - | - | - |
| 19 | The set of all real numbers under the usual mul... | ✗ | 24.06 | 0.0019 | 5 | 100.00% | 82.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✗ | 30.37 | 0.0026 | 5 | 100.00% | 10.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 21.52 | 0.0019 | 5 | 80.00% | 10.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 32.96 | 0.0000 | - | - | - |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 26.20 | 0.0048 | 3 | 100.00% | 10.0 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 23.92 | 0.0005 | 5 | 100.00% | 20.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 74.84 | 0.0035 | 5 | 100.00% | 46.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 96.96 | 0.0034 | 6 | 100.00% | 70.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 21.56 | 0.0000 | 6 | 66.67% | 70.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 47.98 | 0.0021 | 5 | 100.00% | 30.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 18.93 | 0.0012 | 11 | 100.00% | 100.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 25.91 | 0.0033 | 4 | 50.00% | 100.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 17.78 | 0.0007 | 2 | 100.00% | 10.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 25.65 | 0.0032 | 7 | 100.00% | 10.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 24.42 | 0.0045 | 5 | 60.00% | 100.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 22.33 | 0.0009 | 4 | 100.00% | 20.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 18.71 | 0.0079 | 5 | 60.00% | 24.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 15.18 | 0.0046 | 1 | 100.00% | 100.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 47.10 | 0.0010 | 3 | 100.00% | 10.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 29.40 | 0.0000 | 7 | 100.00% | 12.9 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 50.23 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 39.35 | 0.0034 | 5 | 80.00% | 20.0 |
| 41 | The set of integers Z with the binary operation... | ✗ | 52.41 | 0.0012 | 4 | 100.00% | 10.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 45.98 | 0.0000 | - | - | - |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 63.62 | 0.0092 | 5 | 60.00% | 64.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 12.82 | 0.0010 | 6 | 100.00% | 10.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 42.48 | 0.0000 | 5 | 80.00% | 10.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 35.70 | 0.0064 | 5 | 100.00% | 10.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 24.10 | 0.0011 | 6 | 100.00% | 10.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 14.86 | 0.0073 | 2 | 100.00% | 25.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 15.62 | 0.0000 | 6 | 100.00% | 55.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 30.24 | 0.0112 | 6 | 33.33% | 38.3 |
