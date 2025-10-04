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
- 正确数量: 20
- 准确率: 40.00%
- 平均执行时间: 41.83 秒
- 平均成本: $0.0040

## 任务规划指标

- 平均任务步骤数: 3.36
- 平均压缩比例: 70.80%
- 平均每步骤Token限制: 57.79 tokens

## 理论性能指标

- 平均理论执行时间: 3.742 秒
- 平均顺序执行时间: 5.821 秒
- 平均并行加速比: 1.54x
- 理论与实际执行时间比例: 0.09x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.370 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 30.389 秒

### 生成速度
- 小模型平均每秒生成token数: 4.91 tokens/s
- 大模型平均每秒生成token数: 14.47 tokens/s
- 路由模型平均每秒生成token数: 7.39 tokens/s
- 总平均每秒生成token数: 26.78 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 24.80 | 0.0065 | 3 | 100.00% | 50.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 78.91 | 0.0095 | 4 | 75.00% | 30.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 21.01 | 0.0055 | 2 | 100.00% | 60.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 18.10 | 0.0021 | 2 | 50.00% | 100.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 38.58 | 0.0045 | 1 | 100.00% | 100.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 78.20 | 0.0022 | 3 | 100.00% | 30.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 76.73 | 0.0047 | 4 | 75.00% | 50.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 44.35 | 0.0026 | 4 | 75.00% | 45.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 51.69 | 0.0000 | 1 | 100.00% | 50.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 102.35 | 0.0153 | 8 | 25.00% | 35.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 38.56 | 0.0081 | 4 | 75.00% | 22.5 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 49.33 | 0.0000 | - | - | - |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 48.89 | 0.0036 | 4 | 50.00% | 20.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 19.81 | 0.0091 | 2 | 100.00% | 60.0 |
| 15 | Find the maximum possible order for an element ... | ✓ | 8.63 | 0.0034 | 2 | 100.00% | 25.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 6.69 | 0.0026 | 3 | 100.00% | 53.3 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 28.15 | 0.0000 | - | - | - |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 28.68 | 0.0000 | 2 | 50.00% | 10.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 41.78 | 0.0000 | - | - | - |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 14.15 | 0.0058 | 3 | 66.67% | 116.7 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 85.96 | 0.0030 | 5 | 40.00% | 42.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 31.98 | 0.0000 | - | - | - |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 85.77 | 0.0000 | 2 | 100.00% | 15.0 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 22.90 | 0.0108 | 6 | 16.67% | 100.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 64.89 | 0.0000 | 4 | 50.00% | 150.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 39.88 | 0.0165 | 10 | 60.00% | 70.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 13.61 | 0.0015 | 2 | 50.00% | 55.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 77.47 | 0.0029 | 6 | 100.00% | 16.7 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 77.03 | 0.0064 | 5 | 80.00% | 26.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 62.26 | 0.0069 | 4 | 50.00% | 75.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 12.39 | 0.0021 | 2 | 50.00% | 55.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 36.49 | 0.0015 | 2 | 50.00% | 150.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 32.89 | 0.0018 | 2 | 50.00% | 125.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 8.28 | 0.0060 | 2 | 100.00% | 55.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 29.19 | 0.0036 | 2 | 50.00% | 100.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 47.06 | 0.0034 | 3 | 66.67% | 33.3 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 28.19 | 0.0000 | - | - | - |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 44.29 | 0.0031 | 4 | 100.00% | 47.5 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 43.83 | 0.0000 | 2 | 50.00% | 100.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 21.71 | 0.0018 | 2 | 50.00% | 10.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 26.49 | 0.0011 | 2 | 100.00% | 40.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 56.09 | 0.0000 | - | - | - |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 85.99 | 0.0084 | 6 | 50.00% | 38.3 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 57.97 | 0.0063 | 5 | 80.00% | 50.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 32.76 | 0.0070 | 4 | 50.00% | 75.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 22.03 | 0.0027 | 2 | 50.00% | 50.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 38.75 | 0.0049 | 5 | 80.00% | 68.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 61.53 | 0.0026 | 3 | 100.00% | 33.3 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 13.90 | 0.0021 | 2 | 50.00% | 50.0 |
| 50 | Find the maximum possible order for some elemen... | ✗ | 10.76 | 0.0061 | 2 | 100.00% | 55.0 |
