# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Llama-3.2-1B-Instruct/full/llama_1b_ep5_5e6
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 31
- 准确率: 62.00%
- 平均执行时间: 12.13 秒
- 平均成本: $0.0091

## 任务规划指标

- 平均任务步骤数: 3.69
- 平均压缩比例: 71.04%
- 平均每步骤Token限制: 34.97 tokens

## 理论性能指标

- 平均理论执行时间: 4.137 秒
- 平均顺序执行时间: 6.117 秒
- 平均并行加速比: 1.51x
- 理论与实际执行时间比例: 0.34x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.211 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 5.039 秒

### 生成速度
- 小模型平均每秒生成token数: 36.19 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 22.12 tokens/s
- 总平均每秒生成token数: 58.31 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 8.42 | 0.0003 | 0 | 0.00% | 0.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✓ | 13.84 | 0.0109 | 3 | 100.00% | 41.7 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 2.57 | 0.0003 | 0 | 0.00% | 0.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 10.46 | 0.0081 | 3 | 100.00% | 56.7 |
| 5 | Find the product of the given polynomials in th... | ✓ | 12.46 | 0.0121 | 4 | 75.00% | 23.8 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 11.64 | 0.0107 | 4 | 75.00% | 37.5 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 15.60 | 0.0163 | 6 | 66.67% | 58.3 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 20.05 | 0.0181 | 5 | 80.00% | 44.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 20.90 | 0.0201 | 6 | 83.33% | 50.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 2.60 | 0.0003 | 0 | 0.00% | 0.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 10.18 | 0.0089 | 4 | 50.00% | 43.8 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 15.60 | 0.0105 | 4 | 100.00% | 43.8 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 15.72 | 0.0105 | 5 | 80.00% | 32.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 17.32 | 0.0218 | 4 | 75.00% | 41.2 |
| 15 | Find the maximum possible order for an element ... | ✓ | 18.41 | 0.0090 | 4 | 100.00% | 35.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 15.69 | 0.0111 | 4 | 100.00% | 41.2 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 13.25 | 0.0064 | 4 | 75.00% | 28.8 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 15.55 | 0.0173 | 4 | 75.00% | 43.8 |
| 19 | The set of all real numbers under the usual mul... | ✗ | 11.32 | 0.0078 | 5 | 60.00% | 40.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 8.43 | 0.0064 | 3 | 66.67% | 50.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 10.07 | 0.0062 | 2 | 100.00% | 50.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 8.28 | 0.0014 | 3 | 100.00% | 31.7 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 12.78 | 0.0089 | 3 | 100.00% | 40.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 17.70 | 0.0126 | 5 | 100.00% | 42.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 10.02 | 0.0058 | 3 | 100.00% | 50.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 10.99 | 0.0079 | 3 | 100.00% | 38.3 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 12.27 | 0.0116 | 6 | 66.67% | 45.8 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 19.03 | 0.0161 | 6 | 100.00% | 35.8 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 0.00 | 0.0000 | - | - | - |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 23.55 | 0.0121 | 5 | 80.00% | 26.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 18.41 | 0.0155 | 6 | 83.33% | 45.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 13.38 | 0.0083 | 4 | 100.00% | 50.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 4.03 | 0.0007 | 3 | 100.00% | 45.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 11.34 | 0.0114 | 4 | 50.00% | 27.5 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 13.08 | 0.0157 | 6 | 50.00% | 43.3 |
| 36 | Find the degree for the given field extension Q... | ✓ | 5.92 | 0.0003 | 0 | 0.00% | 0.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 18.17 | 0.0116 | 8 | 62.50% | 30.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 18.22 | 0.0110 | 5 | 100.00% | 38.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✗ | 3.06 | 0.0002 | 0 | 0.00% | 0.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 9.50 | 0.0080 | 3 | 66.67% | 36.7 |
| 41 | The set of integers Z with the binary operation... | ✓ | 2.99 | 0.0003 | 0 | 0.00% | 0.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 12.77 | 0.0125 | 4 | 75.00% | 37.5 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 13.65 | 0.0106 | 4 | 100.00% | 38.8 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 12.04 | 0.0077 | 4 | 75.00% | 45.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 9.10 | 0.0094 | 4 | 50.00% | 50.0 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 12.81 | 0.0082 | 4 | 100.00% | 43.8 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 14.06 | 0.0119 | 4 | 100.00% | 43.8 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 14.47 | 0.0138 | 5 | 100.00% | 35.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 10.30 | 0.0076 | 5 | 60.00% | 33.0 |
| 50 | Find the maximum possible order for some elemen... | ✗ | 4.51 | 0.0003 | 0 | 0.00% | 0.0 |
