# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 12
- 准确率: 24.00%
- 平均执行时间: 47.22 秒
- 平均成本: $0.0135

## 任务规划指标

- 平均任务步骤数: 1.82
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 127.44 tokens

## 理论性能指标

- 平均理论执行时间: 13.279 秒
- 平均顺序执行时间: 20.353 秒
- 平均并行加速比: 1.59x
- 理论与实际执行时间比例: 0.28x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 10.013 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 12.548 秒

### 生成速度
- 小模型平均每秒生成token数: 0.61 tokens/s
- 大模型平均每秒生成token数: 7.29 tokens/s
- 路由模型平均每秒生成token数: 10.02 tokens/s
- 总平均每秒生成token数: 17.92 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 62.06 | 0.0178 | 2 | 100.00% | 110.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 53.11 | 0.0076 | 2 | 100.00% | 0.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 86.50 | 0.0169 | 3 | 100.00% | 76.7 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 41.99 | 0.0184 | 2 | 100.00% | 150.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 70.65 | 0.0124 | 2 | 100.00% | 90.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 42.10 | 0.0122 | 1 | 100.00% | 250.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 32.03 | 0.0164 | 2 | 100.00% | 120.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✓ | 31.49 | 0.0069 | 1 | 100.00% | 0.0 |
| 9 | Find the degree for the given field extension Q... | ✗ | 29.58 | 0.0164 | 2 | 100.00% | 130.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 43.38 | 0.0128 | 2 | 100.00% | 80.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 41.28 | 0.0120 | 1 | 100.00% | 250.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✗ | 26.34 | 0.0104 | 1 | 100.00% | 120.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 64.09 | 0.0126 | 4 | 100.00% | 30.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 88.58 | 0.0142 | 1 | 100.00% | 180.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 49.55 | 0.0155 | 2 | 100.00% | 150.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 71.43 | 0.0189 | 2 | 100.00% | 180.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✗ | 30.61 | 0.0057 | 1 | 100.00% | 40.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 71.25 | 0.0107 | 3 | 100.00% | 36.7 |
| 19 | The set of all real numbers under the usual mul... | ✗ | 29.22 | 0.0098 | 1 | 100.00% | 120.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 51.17 | 0.0130 | 1 | 100.00% | 300.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✗ | 50.09 | 0.0118 | 2 | 100.00% | 110.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 26.65 | 0.0096 | 1 | 100.00% | 120.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 33.69 | 0.0170 | 2 | 100.00% | 120.0 |
| 24 | The set of all nth roots of unity under multipl... | ✗ | 40.22 | 0.0170 | 3 | 100.00% | 100.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✓ | 63.09 | 0.0120 | 1 | 100.00% | 220.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✗ | 51.95 | 0.0111 | 1 | 100.00% | 160.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 30.86 | 0.0131 | 1 | 100.00% | 220.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 42.97 | 0.0189 | 2 | 100.00% | 130.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 55.91 | 0.0159 | 2 | 100.00% | 150.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 47.08 | 0.0119 | 1 | 100.00% | 180.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 32.52 | 0.0122 | 1 | 100.00% | 200.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✗ | 27.23 | 0.0066 | 2 | 100.00% | 0.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 40.81 | 0.0112 | 1 | 100.00% | 180.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 43.70 | 0.0131 | 1 | 100.00% | 180.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 38.68 | 0.0119 | 1 | 100.00% | 200.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 62.06 | 0.0236 | 4 | 100.00% | 70.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 32.32 | 0.0098 | 2 | 100.00% | 70.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 59.87 | 0.0200 | 5 | 100.00% | 47.0 |
| 39 | Find the generator for the finite field Z_7. Se... | ✗ | 89.75 | 0.0178 | 3 | 100.00% | 90.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 51.17 | 0.0142 | 2 | 100.00% | 100.0 |
| 41 | The set of integers Z with the binary operation... | ✗ | 37.49 | 0.0122 | 2 | 100.00% | 45.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z. S... | ✗ | 45.40 | 0.0162 | 2 | 100.00% | 100.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 28.44 | 0.0100 | 1 | 100.00% | 160.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 44.91 | 0.0121 | 1 | 100.00% | 220.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 49.38 | 0.0077 | 2 | 100.00% | 0.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 49.26 | 0.0167 | 2 | 100.00% | 150.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 39.94 | 0.0114 | 1 | 100.00% | 220.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 58.10 | 0.0190 | 2 | 100.00% | 90.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 32.16 | 0.0117 | 1 | 100.00% | 220.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 38.67 | 0.0212 | 3 | 100.00% | 106.7 |
