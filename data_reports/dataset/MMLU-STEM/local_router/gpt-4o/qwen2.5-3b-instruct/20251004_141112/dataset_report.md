# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 13
- 准确率: 26.00%
- 平均执行时间: 27.99 秒
- 平均成本: $0.0030

## 任务规划指标

- 平均任务步骤数: 3.03
- 平均压缩比例: 73.14%
- 平均每步骤Token限制: 66.06 tokens

## 理论性能指标

- 平均理论执行时间: 3.752 秒
- 平均顺序执行时间: 5.533 秒
- 平均并行加速比: 1.47x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.125 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 23.142 秒

### 生成速度
- 小模型平均每秒生成token数: 5.21 tokens/s
- 大模型平均每秒生成token数: 13.63 tokens/s
- 路由模型平均每秒生成token数: 6.95 tokens/s
- 总平均每秒生成token数: 25.79 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 22.05 | 0.0163 | 4 | 100.00% | 55.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 45.09 | 0.0027 | 3 | 66.67% | 70.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 28.35 | 0.0049 | 4 | 50.00% | 30.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 11.72 | 0.0019 | 2 | 50.00% | 55.0 |
| 5 | Find the product of the given polynomials in th... | ✗ | 49.13 | 0.0000 | - | - | - |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 30.28 | 0.0041 | 2 | 100.00% | 60.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 15.69 | 0.0106 | 5 | 60.00% | 150.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✓ | 10.68 | 0.0026 | 2 | 50.00% | 100.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 9.46 | 0.0049 | 2 | 100.00% | 125.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 9.77 | 0.0053 | 2 | 100.00% | 150.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 13.88 | 0.0072 | 2 | 50.00% | 200.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✗ | 7.62 | 0.0015 | 6 | 33.33% | 71.7 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 10.21 | 0.0052 | 2 | 100.00% | 25.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 12.28 | 0.0088 | 2 | 100.00% | 100.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 10.02 | 0.0023 | 2 | 100.00% | 55.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 10.33 | 0.0037 | 2 | 50.00% | 30.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 27.53 | 0.0000 | - | - | - |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 23.62 | 0.0000 | - | - | - |
| 19 | The set of all real numbers under the usual mul... | ✗ | 25.55 | 0.0000 | - | - | - |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 23.79 | 0.0102 | 6 | 66.67% | 21.7 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 41.88 | 0.0030 | 2 | 50.00% | 25.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 25.23 | 0.0000 | - | - | - |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 52.90 | 0.0060 | 4 | 100.00% | 25.0 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 53.66 | 0.0000 | - | - | - |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 28.35 | 0.0000 | - | - | - |
| 26 | Let G denoted the set of all n x n non-singular... | ✗ | 8.65 | 0.0038 | 3 | 100.00% | 33.3 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 17.95 | 0.0070 | 3 | 66.67% | 86.7 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 34.70 | 0.0007 | 4 | 50.00% | 40.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 0.00 | 0.0000 | - | - | - |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✗ | 76.46 | 0.0000 | 3 | 66.67% | 100.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 0.00 | 0.0000 | - | - | - |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✗ | 0.00 | 0.0000 | - | - | - |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✗ | 36.82 | 0.0000 | 2 | 50.00% | 100.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 37.74 | 0.0085 | 3 | 100.00% | 30.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 25.30 | 0.0032 | 2 | 50.00% | 50.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 33.71 | 0.0106 | 6 | 50.00% | 48.3 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 39.83 | 0.0000 | - | - | - |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 0.00 | 0.0000 | - | - | - |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 84.81 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 10.47 | 0.0014 | 2 | 50.00% | 50.0 |
| 41 | The set of integers Z with the binary operation... | ✗ | 4.77 | 0.0007 | 1 | 100.00% | 50.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 38.99 | 0.0050 | 3 | 66.67% | 50.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 59.62 | 0.0000 | 3 | 100.00% | 26.7 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 0.00 | 0.0000 | - | - | - |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 0.00 | 0.0000 | - | - | - |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 43.38 | 0.0000 | 2 | 50.00% | 30.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 57.84 | 0.0065 | 4 | 100.00% | 100.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 75.53 | 0.0030 | 3 | 100.00% | 26.7 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 0.00 | 0.0000 | - | - | - |
| 50 | Find the maximum possible order for some elemen... | ✓ | 113.80 | 0.0011 | 5 | 60.00% | 76.0 |
