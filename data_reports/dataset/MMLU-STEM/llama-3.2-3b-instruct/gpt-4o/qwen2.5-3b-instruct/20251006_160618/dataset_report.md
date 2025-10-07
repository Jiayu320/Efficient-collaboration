# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: meta-llama/llama-3.2-3b-instruct
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 21
- 准确率: 42.00%
- 平均执行时间: 47.36 秒
- 平均成本: $0.0005

## 任务规划指标

- 平均任务步骤数: 4.71
- 平均压缩比例: 84.73%
- 平均每步骤Token限制: 31.86 tokens

## 理论性能指标

- 平均理论执行时间: 6.103 秒
- 平均顺序执行时间: 9.115 秒
- 平均并行加速比: 1.52x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.197 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 42.576 秒

### 生成速度
- 小模型平均每秒生成token数: 8.98 tokens/s
- 大模型平均每秒生成token数: 0.76 tokens/s
- 路由模型平均每秒生成token数: 10.43 tokens/s
- 总平均每秒生成token数: 20.17 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 56.41 | 0.0000 | 6 | 100.00% | 31.7 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 56.82 | 0.0000 | 4 | 100.00% | 37.5 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 21.70 | 0.0000 | 1 | 100.00% | 20.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 82.08 | 0.0045 | 4 | 100.00% | 31.2 |
| 5 | Find the product of the given polynomials in th... | ✓ | 50.47 | 0.0000 | 5 | 100.00% | 44.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 54.54 | 0.0039 | 5 | 80.00% | 46.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 63.18 | 0.0000 | 4 | 100.00% | 26.2 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 33.83 | 0.0000 | 9 | 100.00% | 33.3 |
| 9 | Find the degree for the given field extension Q... | ✓ | 63.11 | 0.0031 | 5 | 100.00% | 32.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 31.27 | 0.0000 | 5 | 100.00% | 27.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 25.30 | 0.0000 | 4 | 100.00% | 55.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 91.71 | 0.0000 | 6 | 100.00% | 30.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 140.38 | 0.0015 | 6 | 100.00% | 41.7 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 58.74 | 0.0000 | 5 | 100.00% | 48.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 46.91 | 0.0000 | 6 | 100.00% | 80.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 73.29 | 0.0031 | 6 | 100.00% | 36.7 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 23.56 | 0.0000 | 5 | 100.00% | 12.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 18.66 | 0.0000 | 5 | 100.00% | 28.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 32.22 | 0.0000 | 6 | 50.00% | 28.3 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 35.95 | 0.0000 | 4 | 75.00% | 30.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 35.63 | 0.0000 | 4 | 100.00% | 25.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✗ | 106.13 | 0.0000 | 4 | 75.00% | 42.5 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 21.89 | 0.0000 | 4 | 100.00% | 37.5 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 44.25 | 0.0000 | 6 | 100.00% | 27.5 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 42.81 | 0.0000 | 4 | 75.00% | 37.5 |
| 26 | Let G denoted the set of all n x n non-singular... | ✗ | 46.49 | 0.0000 | 7 | 100.00% | 35.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 78.90 | 0.0000 | 5 | 80.00% | 33.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✗ | 38.33 | 0.0000 | 10 | 70.00% | 33.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 38.94 | 0.0000 | 8 | 87.50% | 43.8 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 38.19 | 0.0000 | 4 | 75.00% | 38.8 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 19.11 | 0.0000 | 4 | 100.00% | 35.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 93.34 | 0.0000 | 5 | 60.00% | 26.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 26.22 | 0.0000 | 5 | 100.00% | 33.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 34.20 | 0.0000 | 7 | 85.71% | 48.6 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 26.45 | 0.0000 | 6 | 83.33% | 30.8 |
| 36 | Find the degree for the given field extension Q... | ✓ | 73.02 | 0.0000 | 4 | 100.00% | 32.5 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 17.74 | 0.0028 | 4 | 75.00% | 15.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 62.48 | 0.0061 | 5 | 100.00% | 60.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 92.14 | 0.0000 | 4 | 100.00% | 12.5 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 25.44 | 0.0015 | 5 | 100.00% | 38.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 29.19 | 0.0000 | 6 | 100.00% | 35.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 33.07 | 0.0000 | 6 | 100.00% | 31.7 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 61.73 | 0.0000 | 4 | 100.00% | 27.5 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 0.00 | 0.0000 | - | - | - |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 91.39 | 0.0000 | 4 | 100.00% | 35.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 35.89 | 0.0000 | 5 | 80.00% | 28.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 23.61 | 0.0000 | 0 | 0.00% | 0.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 23.87 | 0.0000 | 0 | 0.00% | 0.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 23.47 | 0.0000 | 0 | 0.00% | 0.0 |
| 50 | Find the maximum possible order for some elemen... | ✗ | 23.92 | 0.0000 | 0 | 0.00% | 0.0 |
