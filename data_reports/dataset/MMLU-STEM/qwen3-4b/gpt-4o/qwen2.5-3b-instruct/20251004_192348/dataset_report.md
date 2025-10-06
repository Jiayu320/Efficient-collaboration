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
- 正确数量: 18
- 准确率: 36.00%
- 平均执行时间: 45.68 秒
- 平均成本: $0.0031

## 任务规划指标

- 平均任务步骤数: 4.32
- 平均压缩比例: 76.16%
- 平均每步骤Token限制: 99.62 tokens

## 理论性能指标

- 平均理论执行时间: 5.714 秒
- 平均顺序执行时间: 8.024 秒
- 平均并行加速比: 1.45x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.717 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 37.246 秒

### 生成速度
- 小模型平均每秒生成token数: 4.87 tokens/s
- 大模型平均每秒生成token数: 11.07 tokens/s
- 路由模型平均每秒生成token数: 6.47 tokens/s
- 总平均每秒生成token数: 22.40 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 35.44 | 0.0000 | 6 | 50.00% | 106.7 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 82.51 | 0.0000 | 5 | 80.00% | 31.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 100.96 | 0.0000 | 6 | 66.67% | 16.7 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 10.56 | 0.0036 | 3 | 66.67% | 43.3 |
| 5 | Find the product of the given polynomials in th... | ✓ | 52.81 | 0.0052 | 3 | 66.67% | 133.3 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 44.23 | 0.0123 | 5 | 100.00% | 300.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 14.17 | 0.0070 | 4 | 75.00% | 212.5 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 33.62 | 0.0080 | 6 | 66.67% | 63.3 |
| 9 | Find the degree for the given field extension Q... | ✓ | 36.84 | 0.0082 | 5 | 80.00% | 154.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 59.47 | 0.0054 | 5 | 60.00% | 18.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 41.91 | 0.0082 | 4 | 75.00% | 187.5 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 79.25 | 0.0029 | 7 | 57.14% | 78.6 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 69.11 | 0.0000 | - | - | - |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 88.26 | 0.0000 | 3 | 100.00% | 20.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 26.38 | 0.0000 | 4 | 100.00% | 26.2 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 22.74 | 0.0064 | 5 | 80.00% | 200.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 38.97 | 0.0032 | 5 | 100.00% | 54.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 34.39 | 0.0000 | - | - | - |
| 19 | The set of all real numbers under the usual mul... | ✗ | 33.06 | 0.0000 | - | - | - |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 47.63 | 0.0007 | 3 | 66.67% | 40.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 28.96 | 0.0076 | 3 | 100.00% | 233.3 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 51.07 | 0.0039 | 5 | 40.00% | 26.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 35.38 | 0.0008 | 3 | 66.67% | 23.3 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 110.66 | 0.0000 | 5 | 100.00% | 30.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 77.69 | 0.0000 | - | - | - |
| 26 | Let G denoted the set of all n x n non-singular... | ✗ | 0.00 | 0.0000 | - | - | - |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 54.30 | 0.0070 | 4 | 75.00% | 237.5 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 95.42 | 0.0000 | 5 | 60.00% | 38.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 21.85 | 0.0049 | 5 | 60.00% | 24.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 52.45 | 0.0000 | 4 | 75.00% | 237.5 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 20.31 | 0.0090 | 5 | 80.00% | 24.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 85.93 | 0.0000 | 4 | 100.00% | 35.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✗ | 26.43 | 0.0013 | 3 | 66.67% | 166.7 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 35.59 | 0.0171 | 7 | 57.14% | 214.3 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 21.24 | 0.0023 | 3 | 66.67% | 166.7 |
| 36 | Find the degree for the given field extension Q... | ✓ | 14.77 | 0.0026 | 5 | 60.00% | 26.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 42.40 | 0.0000 | 3 | 100.00% | 11.7 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 82.97 | 0.0000 | 6 | 66.67% | 75.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 96.70 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 28.47 | 0.0000 | 5 | 80.00% | 22.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 49.48 | 0.0000 | 3 | 100.00% | 16.7 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 77.62 | 0.0000 | 5 | 40.00% | 44.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 10.21 | 0.0057 | 3 | 66.67% | 21.7 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 19.02 | 0.0016 | 3 | 66.67% | 126.7 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 28.06 | 0.0030 | 6 | 66.67% | 25.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 32.29 | 0.0031 | 3 | 100.00% | 40.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 54.38 | 0.0033 | 3 | 100.00% | 183.3 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 40.24 | 0.0000 | 4 | 100.00% | 250.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 11.97 | 0.0024 | 3 | 66.67% | 150.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 26.08 | 0.0064 | 3 | 100.00% | 250.0 |
