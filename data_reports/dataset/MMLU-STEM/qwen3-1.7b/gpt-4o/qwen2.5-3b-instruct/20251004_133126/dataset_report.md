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
- 正确数量: 25
- 准确率: 50.00%
- 平均执行时间: 27.07 秒
- 平均成本: $0.0072

## 任务规划指标

- 平均任务步骤数: 4.27
- 平均压缩比例: 91.08%
- 平均每步骤Token限制: 46.29 tokens

## 理论性能指标

- 平均理论执行时间: 4.980 秒
- 平均顺序执行时间: 6.085 秒
- 平均并行加速比: 1.23x
- 理论与实际执行时间比例: 0.18x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.212 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 19.278 秒

### 生成速度
- 小模型平均每秒生成token数: 3.42 tokens/s
- 大模型平均每秒生成token数: 31.06 tokens/s
- 路由模型平均每秒生成token数: 9.06 tokens/s
- 总平均每秒生成token数: 43.55 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 20.51 | 0.0121 | 3 | 100.00% | 10.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 11.16 | 0.0052 | 2 | 100.00% | 150.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 101.82 | 0.0058 | 5 | 80.00% | 28.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 11.47 | 0.0041 | 2 | 100.00% | 10.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 7.99 | 0.0044 | 1 | 100.00% | 100.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✓ | 24.27 | 0.0165 | 8 | 100.00% | 10.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 15.54 | 0.0087 | 4 | 100.00% | 10.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 11.19 | 0.0097 | 4 | 75.00% | 10.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 10.40 | 0.0067 | 1 | 100.00% | 100.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 20.54 | 0.0108 | 4 | 100.00% | 302.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 16.60 | 0.0076 | 4 | 100.00% | 100.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 33.10 | 0.0028 | 5 | 100.00% | 10.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 113.36 | 0.0033 | 4 | 75.00% | 10.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 114.55 | 0.0158 | 7 | 100.00% | 74.3 |
| 15 | Find the maximum possible order for an element ... | ✓ | 6.67 | 0.0027 | 2 | 100.00% | 115.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 8.58 | 0.0054 | 4 | 50.00% | 10.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 4.76 | 0.0010 | 1 | 100.00% | 10.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 11.30 | 0.0077 | 4 | 100.00% | 32.5 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 35.81 | 0.0066 | 5 | 100.00% | 82.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 15.34 | 0.0090 | 5 | 80.00% | 10.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 16.20 | 0.0114 | 4 | 100.00% | 10.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 7.60 | 0.0026 | 2 | 100.00% | 55.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 10.29 | 0.0049 | 3 | 100.00% | 10.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 29.34 | 0.0250 | 11 | 100.00% | 10.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 69.04 | 0.0100 | 7 | 71.43% | 61.4 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 53.18 | 0.0124 | 9 | 100.00% | 80.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 40.45 | 0.0082 | 6 | 66.67% | 85.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 77.60 | 0.0068 | 6 | 100.00% | 10.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 13.13 | 0.0101 | 6 | 83.33% | 100.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 6.99 | 0.0031 | 2 | 100.00% | 10.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 9.86 | 0.0018 | 2 | 100.00% | 10.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 15.87 | 0.0076 | 4 | 100.00% | 20.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 9.29 | 0.0053 | 5 | 60.00% | 100.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 9.44 | 0.0056 | 3 | 100.00% | 10.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 8.38 | 0.0047 | 2 | 100.00% | 20.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 7.78 | 0.0045 | 1 | 100.00% | 100.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 8.75 | 0.0041 | 3 | 100.00% | 10.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 72.28 | 0.0069 | 6 | 100.00% | 121.7 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 0.00 | 0.0000 | - | - | - |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 14.92 | 0.0061 | 5 | 80.00% | 10.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 16.52 | 0.0027 | 3 | 66.67% | 10.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 21.52 | 0.0044 | 4 | 50.00% | 10.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 54.71 | 0.0037 | 4 | 100.00% | 55.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 19.39 | 0.0110 | 6 | 100.00% | 10.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 12.41 | 0.0077 | 4 | 75.00% | 10.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 15.40 | 0.0086 | 5 | 100.00% | 46.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 17.25 | 0.0102 | 7 | 100.00% | 10.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 8.82 | 0.0055 | 2 | 100.00% | 15.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 95.65 | 0.0122 | 6 | 100.00% | 70.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 16.69 | 0.0062 | 6 | 50.00% | 15.0 |
