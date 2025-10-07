# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Llama-3.2-1B-Instruct/full/llama_1b_ep1_5e5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 32
- 准确率: 64.00%
- 平均执行时间: 19.74 秒
- 平均成本: $0.0163

## 任务规划指标

- 平均任务步骤数: 4.58
- 平均压缩比例: 73.44%
- 平均每步骤Token限制: 37.17 tokens

## 理论性能指标

- 平均理论执行时间: 4.408 秒
- 平均顺序执行时间: 7.339 秒
- 平均并行加速比: 1.63x
- 理论与实际执行时间比例: 0.22x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.205 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.860 秒

### 生成速度
- 小模型平均每秒生成token数: 36.88 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 19.75 tokens/s
- 总平均每秒生成token数: 56.63 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 24.44 | 0.0100 | 3 | 100.00% | 40.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 13.52 | 0.0074 | 5 | 20.00% | 30.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 30.40 | 0.0293 | 8 | 62.50% | 40.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 22.30 | 0.0494 | 14 | 28.57% | 59.3 |
| 5 | Find the product of the given polynomials in th... | ✗ | 22.78 | 0.0159 | 5 | 80.00% | 28.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 14.96 | 0.0092 | 4 | 75.00% | 27.5 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 15.91 | 0.0083 | 3 | 100.00% | 20.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 11.03 | 0.0079 | 4 | 50.00% | 37.5 |
| 9 | Find the degree for the given field extension Q... | ✓ | 27.95 | 0.0176 | 5 | 100.00% | 38.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 19.71 | 0.0123 | 3 | 100.00% | 46.7 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 15.57 | 0.0070 | 3 | 100.00% | 50.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 8.39 | 0.0012 | 5 | 20.00% | 54.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 20.47 | 0.0079 | 4 | 100.00% | 30.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 19.13 | 0.0308 | 6 | 50.00% | 53.3 |
| 15 | Find the maximum possible order for an element ... | ✓ | 13.66 | 0.0068 | 3 | 100.00% | 23.3 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 12.56 | 0.0051 | 3 | 100.00% | 30.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 6.82 | 0.0005 | 4 | 25.00% | 20.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 15.77 | 0.0078 | 6 | 50.00% | 41.7 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 15.28 | 0.0121 | 6 | 50.00% | 41.7 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✗ | 15.58 | 0.0106 | 3 | 66.67% | 30.0 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 27.55 | 0.0159 | 6 | 66.67% | 41.7 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 21.24 | 0.0260 | 6 | 33.33% | 28.3 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 5.40 | 0.0006 | 3 | 33.33% | 33.3 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 10.55 | 0.0052 | 3 | 100.00% | 20.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 13.39 | 0.0068 | 3 | 66.67% | 33.3 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 18.49 | 0.0113 | 3 | 100.00% | 50.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 17.17 | 0.0096 | 4 | 50.00% | 30.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 15.88 | 0.0189 | 7 | 42.86% | 54.3 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 15.05 | 0.0072 | 3 | 100.00% | 46.7 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 12.50 | 0.0063 | 4 | 75.00% | 45.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 16.84 | 0.0081 | 4 | 75.00% | 30.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 19.27 | 0.0097 | 4 | 100.00% | 42.5 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 18.02 | 0.0073 | 4 | 100.00% | 22.5 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 16.77 | 0.0181 | 6 | 50.00% | 33.3 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 29.09 | 0.0139 | 4 | 100.00% | 40.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 26.35 | 0.0124 | 5 | 100.00% | 24.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 12.31 | 0.0049 | 3 | 100.00% | 23.3 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 17.67 | 0.0137 | 5 | 60.00% | 32.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 18.64 | 0.0224 | 6 | 50.00% | 21.7 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 13.68 | 0.0054 | 3 | 100.00% | 36.7 |
| 41 | The set of integers Z with the binary operation... | ✓ | 110.32 | 0.2341 | 11 | 9.09% | 36.4 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 19.22 | 0.0092 | 3 | 100.00% | 30.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 12.63 | 0.0053 | 3 | 100.00% | 36.7 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 22.39 | 0.0124 | 5 | 80.00% | 36.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 12.73 | 0.0089 | 3 | 66.67% | 56.7 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 25.52 | 0.0091 | 3 | 100.00% | 60.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 29.99 | 0.0085 | 3 | 100.00% | 46.7 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 5.79 | 0.0004 | 1 | 100.00% | 50.0 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 28.50 | 0.0143 | 5 | 80.00% | 40.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 27.58 | 0.0317 | 9 | 55.56% | 36.7 |
