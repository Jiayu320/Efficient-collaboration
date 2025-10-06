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
- 正确数量: 26
- 准确率: 52.00%
- 平均执行时间: 39.09 秒
- 平均成本: $0.0041

## 任务规划指标

- 平均任务步骤数: 3.24
- 平均压缩比例: 72.20%
- 平均每步骤Token限制: 22.01 tokens

## 理论性能指标

- 平均理论执行时间: 3.047 秒
- 平均顺序执行时间: 4.474 秒
- 平均并行加速比: 1.45x
- 理论与实际执行时间比例: 0.08x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.229 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 32.508 秒

### 生成速度
- 小模型平均每秒生成token数: 11.79 tokens/s
- 大模型平均每秒生成token数: 11.67 tokens/s
- 路由模型平均每秒生成token数: 4.23 tokens/s
- 总平均每秒生成token数: 27.70 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 65.14 | 0.0058 | 3 | 66.67% | 20.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 7.42 | 0.0030 | 2 | 100.00% | 25.0 |
| 3 | Find all zeros in the indicated finite field of... | ✗ | 24.64 | 0.0061 | 2 | 100.00% | 17.5 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 58.12 | 0.0020 | 3 | 100.00% | 21.7 |
| 5 | Find the product of the given polynomials in th... | ✗ | 11.01 | 0.0037 | 1 | 100.00% | 30.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 32.77 | 0.0054 | 3 | 66.67% | 25.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 43.79 | 0.0048 | 4 | 75.00% | 22.5 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 35.42 | 0.0020 | 3 | 66.67% | 20.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 54.09 | 0.0000 | 1 | 100.00% | 20.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 15.27 | 0.0057 | 2 | 100.00% | 22.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 57.94 | 0.0067 | 5 | 60.00% | 26.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 38.78 | 0.0027 | 5 | 40.00% | 17.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 73.51 | 0.0037 | 3 | 100.00% | 15.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 13.24 | 0.0079 | 1 | 100.00% | 25.0 |
| 15 | Find the maximum possible order for an element ... | ✓ | 7.22 | 0.0037 | 1 | 100.00% | 25.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 39.62 | 0.0009 | 2 | 50.00% | 22.5 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 32.31 | 0.0000 | 1 | 100.00% | 20.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 52.22 | 0.0023 | 3 | 100.00% | 25.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 35.55 | 0.0036 | 5 | 40.00% | 16.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✗ | 14.99 | 0.0029 | 4 | 50.00% | 22.5 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 33.79 | 0.0070 | 4 | 50.00% | 22.5 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 67.44 | 0.0048 | 3 | 100.00% | 13.3 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 40.08 | 0.0000 | 4 | 50.00% | 20.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 33.57 | 0.0025 | 5 | 40.00% | 22.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 40.04 | 0.0042 | 4 | 75.00% | 22.5 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 89.79 | 0.0055 | 5 | 80.00% | 21.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 57.14 | 0.0143 | 5 | 40.00% | 26.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 59.17 | 0.0087 | 5 | 40.00% | 17.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 45.61 | 0.0047 | 3 | 100.00% | 23.3 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 42.97 | 0.0017 | 3 | 33.33% | 23.3 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 39.27 | 0.0070 | 6 | 50.00% | 28.3 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 49.89 | 0.0060 | 3 | 66.67% | 25.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 26.17 | 0.0013 | 3 | 66.67% | 21.7 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 57.28 | 0.0040 | 2 | 100.00% | 22.5 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 41.97 | 0.0041 | 4 | 50.00% | 22.5 |
| 36 | Find the degree for the given field extension Q... | ✓ | 82.99 | 0.0000 | 1 | 100.00% | 20.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 15.74 | 0.0000 | 1 | 100.00% | 20.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✓ | 64.64 | 0.0048 | 5 | 100.00% | 18.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 63.41 | 0.0108 | 5 | 40.00% | 24.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 25.51 | 0.0000 | 3 | 33.33% | 23.3 |
| 41 | The set of integers Z with the binary operation... | ✓ | 27.51 | 0.0000 | 1 | 100.00% | 20.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 37.29 | 0.0035 | 4 | 50.00% | 17.5 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 37.54 | 0.0040 | 4 | 50.00% | 20.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 34.96 | 0.0055 | 5 | 40.00% | 24.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 13.48 | 0.0045 | 4 | 50.00% | 22.5 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 31.95 | 0.0040 | 5 | 40.00% | 22.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✓ | 33.17 | 0.0052 | 4 | 50.00% | 25.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 8.31 | 0.0057 | 2 | 100.00% | 22.5 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 32.41 | 0.0020 | 3 | 100.00% | 25.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 8.56 | 0.0062 | 2 | 100.00% | 27.5 |
