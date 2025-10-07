# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: qwen3-1.7b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 36
- 准确率: 72.00%
- 平均执行时间: 10.72 秒
- 平均成本: $0.0055

## 任务规划指标

- 平均任务步骤数: 4.48
- 平均压缩比例: 87.37%
- 平均每步骤Token限制: 40.21 tokens

## 理论性能指标

- 平均理论执行时间: 4.948 秒
- 平均顺序执行时间: 6.325 秒
- 平均并行加速比: 1.30x
- 理论与实际执行时间比例: 0.46x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.500 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 4.047 秒

### 生成速度
- 小模型平均每秒生成token数: 26.57 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 21.13 tokens/s
- 总平均每秒生成token数: 47.70 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 9.42 | 0.0021 | 4 | 100.00% | 32.5 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 14.98 | 0.0062 | 5 | 100.00% | 32.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 10.84 | 0.0054 | 7 | 100.00% | 27.1 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 7.59 | 0.0022 | 4 | 75.00% | 33.8 |
| 5 | Find the product of the given polynomials in th... | ✓ | 14.10 | 0.0084 | 3 | 100.00% | 58.3 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 11.00 | 0.0021 | 5 | 100.00% | 28.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 9.49 | 0.0023 | 4 | 75.00% | 42.5 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 6.31 | 0.0018 | 4 | 75.00% | 32.5 |
| 9 | Find the degree for the given field extension Q... | ✓ | 6.83 | 0.0014 | 4 | 100.00% | 35.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 7.28 | 0.0017 | 4 | 100.00% | 32.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✓ | 6.73 | 0.0026 | 6 | 66.67% | 46.7 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 12.94 | 0.0116 | 6 | 66.67% | 20.8 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 14.16 | 0.0084 | 7 | 100.00% | 41.4 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 14.88 | 0.0137 | 5 | 100.00% | 70.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 8.06 | 0.0017 | 4 | 100.00% | 35.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 7.26 | 0.0018 | 4 | 75.00% | 32.5 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 8.35 | 0.0015 | 4 | 100.00% | 31.2 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 17.30 | 0.0098 | 6 | 83.33% | 30.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 10.15 | 0.0017 | 6 | 50.00% | 28.3 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 9.10 | 0.0020 | 4 | 75.00% | 35.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 14.40 | 0.0129 | 4 | 100.00% | 40.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 7.31 | 0.0019 | 3 | 100.00% | 56.7 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 12.12 | 0.0067 | 4 | 75.00% | 32.5 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 11.93 | 0.0082 | 6 | 100.00% | 22.5 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 10.01 | 0.0066 | 4 | 75.00% | 37.5 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 10.30 | 0.0051 | 7 | 100.00% | 48.6 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 13.13 | 0.0117 | 4 | 75.00% | 42.5 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 8.15 | 0.0024 | 4 | 100.00% | 80.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 8.76 | 0.0019 | 4 | 75.00% | 40.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 6.59 | 0.0016 | 4 | 75.00% | 35.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 13.12 | 0.0138 | 6 | 66.67% | 33.3 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 14.10 | 0.0072 | 4 | 100.00% | 37.5 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 12.17 | 0.0066 | 4 | 75.00% | 33.8 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 9.19 | 0.0024 | 5 | 100.00% | 46.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 11.72 | 0.0065 | 4 | 100.00% | 60.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 15.23 | 0.0120 | 5 | 80.00% | 46.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 9.10 | 0.0050 | 3 | 100.00% | 31.7 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✓ | 10.99 | 0.0067 | 5 | 100.00% | 68.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 12.11 | 0.0098 | 3 | 100.00% | 35.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 10.28 | 0.0059 | 4 | 75.00% | 35.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 9.16 | 0.0017 | 4 | 100.00% | 43.8 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 13.24 | 0.0073 | 3 | 100.00% | 50.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 12.09 | 0.0120 | 4 | 75.00% | 35.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 11.28 | 0.0068 | 4 | 75.00% | 42.5 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 7.26 | 0.0021 | 5 | 80.00% | 56.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 8.55 | 0.0020 | 4 | 75.00% | 35.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✓ | 12.65 | 0.0076 | 4 | 75.00% | 30.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 7.60 | 0.0023 | 5 | 100.00% | 28.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 14.30 | 0.0059 | 4 | 75.00% | 33.8 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 12.29 | 0.0019 | 4 | 100.00% | 70.0 |
