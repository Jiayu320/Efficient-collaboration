# 数据集处理报告

## 模型配置

- 小模型: gpt-4.1-mini
- 大模型: gpt-4.1-mini
- 路由模型: saves/Llama-3.2-1B-Instruct/full/Llama-3-2-1B_ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 36
- 准确率: 72.00%
- 平均执行时间: 11.47 秒
- 平均成本: $0.0079

## 任务规划指标

- 平均任务步骤数: 3.88
- 平均压缩比例: 87.20%
- 平均每步骤Token限制: 39.37 tokens

## 理论性能指标

- 平均理论执行时间: 5.323 秒
- 平均顺序执行时间: 7.347 秒
- 平均并行加速比: 1.39x
- 理论与实际执行时间比例: 0.46x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.342 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 5.099 秒

### 生成速度
- 小模型平均每秒生成token数: 26.61 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 28.15 tokens/s
- 总平均每秒生成token数: 54.76 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 8.62 | 0.0066 | 3 | 100.00% | 33.3 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 6.68 | 0.0075 | 4 | 100.00% | 40.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 21.04 | 0.0111 | 5 | 80.00% | 44.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 11.20 | 0.0084 | 4 | 75.00% | 30.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 20.08 | 0.0099 | 4 | 100.00% | 47.5 |
| 6 | Statement 1 | If a group has an element of orde... | ✓ | 17.02 | 0.0088 | 4 | 75.00% | 45.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✓ | 14.16 | 0.0086 | 4 | 75.00% | 40.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 10.35 | 0.0079 | 4 | 75.00% | 35.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 35.81 | 0.0103 | 4 | 100.00% | 42.5 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 7.23 | 0.0070 | 4 | 75.00% | 37.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✓ | 13.24 | 0.0091 | 4 | 75.00% | 42.5 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 5.97 | 0.0051 | 1 | 100.00% | 40.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 7.84 | 0.0072 | 4 | 75.00% | 40.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 24.55 | 0.0094 | 4 | 100.00% | 45.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 5.66 | 0.0069 | 4 | 100.00% | 45.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✓ | 11.14 | 0.0079 | 4 | 75.00% | 35.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 6.71 | 0.0069 | 4 | 100.00% | 27.5 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 10.53 | 0.0077 | 4 | 100.00% | 35.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 11.11 | 0.0074 | 3 | 100.00% | 33.3 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 12.01 | 0.0087 | 4 | 75.00% | 50.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 15.87 | 0.0090 | 4 | 75.00% | 45.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 14.41 | 0.0090 | 5 | 100.00% | 48.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 16.01 | 0.0088 | 4 | 100.00% | 35.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 6.10 | 0.0073 | 4 | 100.00% | 37.5 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 9.67 | 0.0076 | 4 | 75.00% | 37.5 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 5.42 | 0.0073 | 4 | 75.00% | 62.5 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 10.90 | 0.0084 | 4 | 75.00% | 42.5 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 15.89 | 0.0101 | 5 | 80.00% | 38.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 6.37 | 0.0074 | 4 | 75.00% | 40.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 10.79 | 0.0080 | 4 | 75.00% | 30.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 10.28 | 0.0082 | 4 | 75.00% | 42.5 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 10.08 | 0.0079 | 4 | 100.00% | 45.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 11.42 | 0.0077 | 4 | 75.00% | 35.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 21.98 | 0.0091 | 4 | 100.00% | 50.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 10.94 | 0.0086 | 4 | 100.00% | 45.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 6.31 | 0.0067 | 3 | 100.00% | 33.3 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 9.16 | 0.0068 | 3 | 100.00% | 26.7 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 9.27 | 0.0086 | 5 | 100.00% | 42.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 5.54 | 0.0051 | 1 | 100.00% | 20.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 13.11 | 0.0077 | 4 | 75.00% | 30.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 5.86 | 0.0070 | 4 | 100.00% | 30.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✓ | 6.60 | 0.0070 | 4 | 100.00% | 32.5 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 7.03 | 0.0076 | 4 | 75.00% | 42.5 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 6.68 | 0.0066 | 4 | 75.00% | 42.5 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 14.57 | 0.0084 | 4 | 75.00% | 40.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✓ | 15.18 | 0.0085 | 4 | 75.00% | 37.5 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 6.63 | 0.0071 | 4 | 75.00% | 50.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 6.33 | 0.0073 | 4 | 100.00% | 40.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 17.31 | 0.0081 | 4 | 75.00% | 40.0 |
| 50 | Find the maximum possible order for some elemen... | ✗ | 7.05 | 0.0071 | 4 | 100.00% | 40.0 |
