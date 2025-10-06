# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-0.6b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 14
- 准确率: 28.00%
- 平均执行时间: 33.57 秒
- 平均成本: $0.0018

## 任务规划指标

- 平均任务步骤数: 1.85
- 平均压缩比例: 75.41%
- 平均每步骤Token限制: 34.65 tokens

## 理论性能指标

- 平均理论执行时间: 2.354 秒
- 平均顺序执行时间: 3.090 秒
- 平均并行加速比: 1.30x
- 理论与实际执行时间比例: 0.07x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.298 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 25.885 秒

### 生成速度
- 小模型平均每秒生成token数: 3.52 tokens/s
- 大模型平均每秒生成token数: 11.69 tokens/s
- 路由模型平均每秒生成token数: 5.52 tokens/s
- 总平均每秒生成token数: 20.73 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 33.39 | 0.0037 | 1 | 100.00% | 10.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 6.64 | 0.0041 | 1 | 100.00% | 120.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 12.93 | 0.0153 | 3 | 33.33% | 60.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 34.42 | 0.0038 | 2 | 100.00% | 17.5 |
| 5 | Find the product of the given polynomials in th... | ✗ | 23.82 | 0.0041 | 2 | 100.00% | 120.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 31.87 | 0.0025 | 2 | 50.00% | 12.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 16.79 | 0.0019 | 2 | 50.00% | 20.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✓ | 27.31 | 0.0015 | 2 | 50.00% | 17.5 |
| 9 | Find the degree for the given field extension Q... | ✓ | 30.20 | 0.0045 | 1 | 100.00% | 60.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 35.48 | 0.0067 | 2 | 50.00% | 80.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 10.28 | 0.0018 | 2 | 50.00% | 20.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 45.85 | 0.0020 | 2 | 100.00% | 7.5 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 32.06 | 0.0000 | 1 | 100.00% | 20.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 17.86 | 0.0000 | 4 | 25.00% | 88.8 |
| 15 | Find the maximum possible order for an element ... | ✗ | 29.59 | 0.0032 | 1 | 100.00% | 72.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 39.32 | 0.0015 | 2 | 100.00% | 13.5 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 17.77 | 0.0000 | 3 | 33.33% | 60.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 22.77 | 0.0000 | - | - | - |
| 19 | The set of all real numbers under the usual mul... | ✗ | 50.10 | 0.0000 | - | - | - |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 33.99 | 0.0025 | 2 | 50.00% | 12.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 84.12 | 0.0000 | 2 | 100.00% | 25.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 53.69 | 0.0000 | - | - | - |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 7.04 | 0.0013 | 2 | 50.00% | 15.0 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 42.60 | 0.0000 | - | - | - |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 32.00 | 0.0009 | 2 | 100.00% | 20.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✗ | 29.27 | 0.0000 | 1 | 100.00% | 30.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 53.00 | 0.0011 | 2 | 50.00% | 10.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 24.98 | 0.0037 | 2 | 100.00% | 15.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 27.90 | 0.0000 | 2 | 50.00% | 30.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 11.42 | 0.0020 | 2 | 50.00% | 20.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 17.66 | 0.0010 | 2 | 100.00% | 12.5 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✗ | 76.13 | 0.0000 | - | - | - |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✗ | 15.42 | 0.0000 | 2 | 50.00% | 80.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 68.24 | 0.0007 | 2 | 100.00% | 20.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 35.91 | 0.0018 | 2 | 50.00% | 15.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 21.24 | 0.0021 | 1 | 100.00% | 40.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 27.59 | 0.0000 | - | - | - |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 37.33 | 0.0031 | 2 | 50.00% | 17.5 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 67.85 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 23.98 | 0.0008 | 2 | 100.00% | 7.5 |
| 41 | The set of integers Z with the binary operation... | ✓ | 25.34 | 0.0000 | 1 | 100.00% | 10.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 91.16 | 0.0000 | - | - | - |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 23.15 | 0.0030 | 2 | 50.00% | 19.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 38.98 | 0.0010 | 2 | 100.00% | 10.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 35.96 | 0.0000 | 2 | 50.00% | 10.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 0.00 | 0.0000 | - | - | - |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 20.55 | 0.0023 | 2 | 100.00% | 25.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 51.83 | 0.0000 | 1 | 100.00% | 16.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 58.99 | 0.0014 | 2 | 50.00% | 12.5 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 22.89 | 0.0035 | 1 | 100.00% | 150.0 |
