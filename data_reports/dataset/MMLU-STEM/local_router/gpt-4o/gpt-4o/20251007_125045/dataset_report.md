# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Llama-3.2-1B-Instruct/full/Llama-3-2-1B_ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 正确数量: 34
- 准确率: 68.00%
- 平均执行时间: 12.12 秒
- 平均成本: $0.0173

## 任务规划指标

- 平均任务步骤数: 4.04
- 平均压缩比例: 84.10%
- 平均每步骤Token限制: 37.60 tokens

## 理论性能指标

- 平均理论执行时间: 4.488 秒
- 平均顺序执行时间: 6.470 秒
- 平均并行加速比: 1.45x
- 理论与实际执行时间比例: 0.37x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.217 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 4.846 秒

### 生成速度
- 小模型平均每秒生成token数: 44.82 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 24.25 tokens/s
- 总平均每秒生成token数: 69.06 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 19.70 | 0.0199 | 4 | 100.00% | 30.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 15.88 | 0.0171 | 4 | 100.00% | 27.5 |
| 3 | Find all zeros in the indicated finite field of... | ✗ | 12.76 | 0.0198 | 4 | 100.00% | 47.5 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 9.01 | 0.0155 | 4 | 75.00% | 30.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 12.25 | 0.0187 | 4 | 100.00% | 37.5 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 11.32 | 0.0201 | 4 | 75.00% | 42.5 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 11.21 | 0.0159 | 4 | 75.00% | 45.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 10.87 | 0.0190 | 4 | 75.00% | 42.5 |
| 9 | Find the degree for the given field extension Q... | ✓ | 13.33 | 0.0158 | 4 | 100.00% | 30.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 16.21 | 0.0245 | 6 | 83.33% | 30.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 11.83 | 0.0171 | 4 | 75.00% | 37.5 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 9.86 | 0.0142 | 4 | 75.00% | 27.5 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 14.98 | 0.0182 | 4 | 100.00% | 32.5 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 22.41 | 0.0329 | 5 | 100.00% | 32.0 |
| 15 | Find the maximum possible order for an element ... | ✓ | 13.05 | 0.0178 | 4 | 100.00% | 35.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✓ | 10.16 | 0.0158 | 4 | 75.00% | 40.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 8.58 | 0.0099 | 4 | 50.00% | 25.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✗ | 6.48 | 0.0095 | 5 | 20.00% | 36.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 4.71 | 0.0060 | 1 | 100.00% | 40.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 9.27 | 0.0157 | 4 | 75.00% | 52.5 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 11.74 | 0.0148 | 4 | 75.00% | 40.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 9.96 | 0.0130 | 3 | 100.00% | 33.3 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 9.77 | 0.0143 | 4 | 75.00% | 40.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 13.75 | 0.0166 | 4 | 75.00% | 40.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 10.66 | 0.0163 | 4 | 75.00% | 40.0 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 12.25 | 0.0202 | 6 | 66.67% | 46.7 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 10.14 | 0.0180 | 4 | 75.00% | 60.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 14.58 | 0.0191 | 4 | 100.00% | 40.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 10.42 | 0.0132 | 3 | 100.00% | 40.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 10.16 | 0.0139 | 4 | 75.00% | 42.5 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 11.98 | 0.0169 | 4 | 75.00% | 30.0 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 16.80 | 0.0224 | 5 | 100.00% | 44.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 9.99 | 0.0127 | 4 | 75.00% | 30.0 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 15.19 | 0.0217 | 5 | 60.00% | 40.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 12.98 | 0.0184 | 4 | 100.00% | 37.5 |
| 36 | Find the degree for the given field extension Q... | ✓ | 13.40 | 0.0194 | 4 | 100.00% | 35.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 10.74 | 0.0140 | 3 | 100.00% | 33.3 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✓ | 14.80 | 0.0215 | 5 | 100.00% | 44.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 11.65 | 0.0163 | 3 | 100.00% | 23.3 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 9.76 | 0.0127 | 4 | 75.00% | 35.0 |
| 41 | The set of integers Z with the binary operation... | ✓ | 11.24 | 0.0162 | 4 | 100.00% | 42.5 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 11.14 | 0.0147 | 4 | 100.00% | 25.0 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 10.71 | 0.0179 | 4 | 75.00% | 40.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 10.11 | 0.0164 | 4 | 75.00% | 35.0 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✗ | 11.77 | 0.0207 | 4 | 75.00% | 37.5 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 12.20 | 0.0177 | 4 | 75.00% | 37.5 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✓ | 15.39 | 0.0198 | 4 | 75.00% | 30.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 16.63 | 0.0247 | 4 | 100.00% | 42.5 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 8.66 | 0.0145 | 4 | 75.00% | 50.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 13.64 | 0.0219 | 4 | 100.00% | 45.0 |
