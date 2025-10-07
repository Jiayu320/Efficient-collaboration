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
- 正确数量: 36
- 准确率: 72.00%
- 平均执行时间: 13.85 秒
- 平均成本: $0.0165

## 任务规划指标

- 平均任务步骤数: 4.02
- 平均压缩比例: 83.97%
- 平均每步骤Token限制: 38.30 tokens

## 理论性能指标

- 平均理论执行时间: 4.507 秒
- 平均顺序执行时间: 6.434 秒
- 平均并行加速比: 1.44x
- 理论与实际执行时间比例: 0.33x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.698 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 3.948 秒

### 生成速度
- 小模型平均每秒生成token数: 37.90 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 21.63 tokens/s
- 总平均每秒生成token数: 59.54 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 18.95 | 0.0195 | 4 | 100.00% | 35.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✓ | 12.72 | 0.0178 | 4 | 100.00% | 30.0 |
| 3 | Find all zeros in the indicated finite field of... | ✗ | 14.55 | 0.0201 | 4 | 100.00% | 35.0 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 11.58 | 0.0167 | 4 | 75.00% | 35.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 11.37 | 0.0164 | 3 | 100.00% | 36.7 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 9.51 | 0.0153 | 4 | 75.00% | 40.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 10.10 | 0.0153 | 4 | 75.00% | 42.5 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 14.15 | 0.0204 | 4 | 100.00% | 35.0 |
| 9 | Find the degree for the given field extension Q... | ✓ | 13.03 | 0.0196 | 4 | 100.00% | 30.0 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 11.95 | 0.0185 | 4 | 100.00% | 42.5 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 12.35 | 0.0178 | 4 | 75.00% | 30.0 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 10.19 | 0.0145 | 4 | 75.00% | 22.5 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 13.30 | 0.0170 | 4 | 100.00% | 30.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 6.55 | 0.0101 | 5 | 20.00% | 28.0 |
| 15 | Find the maximum possible order for an element ... | ✓ | 10.48 | 0.0134 | 4 | 100.00% | 42.5 |
| 16 | Statement 1 | R is a splitting field of some po... | ✓ | 9.31 | 0.0155 | 4 | 75.00% | 45.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 10.25 | 0.0120 | 4 | 100.00% | 25.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 10.04 | 0.0141 | 4 | 100.00% | 35.0 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 17.70 | 0.0175 | 6 | 50.00% | 26.7 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 13.08 | 0.0183 | 4 | 75.00% | 42.5 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 11.78 | 0.0173 | 4 | 75.00% | 45.0 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 21.73 | 0.0172 | 4 | 75.00% | 25.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 20.25 | 0.0154 | 4 | 100.00% | 32.5 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 11.81 | 0.0137 | 3 | 100.00% | 63.3 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 11.81 | 0.0169 | 4 | 75.00% | 52.5 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 7.78 | 0.0086 | 5 | 20.00% | 42.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 14.25 | 0.0213 | 4 | 75.00% | 52.5 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 12.46 | 0.0085 | 3 | 33.33% | 43.3 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 13.74 | 0.0146 | 4 | 75.00% | 40.0 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 12.74 | 0.0169 | 4 | 75.00% | 40.0 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 18.11 | 0.0159 | 4 | 75.00% | 47.5 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 16.49 | 0.0181 | 4 | 100.00% | 50.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 12.74 | 0.0151 | 4 | 75.00% | 37.5 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✗ | 15.27 | 0.0164 | 4 | 100.00% | 42.5 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 17.66 | 0.0208 | 4 | 100.00% | 60.0 |
| 36 | Find the degree for the given field extension Q... | ✓ | 19.66 | 0.0187 | 4 | 100.00% | 27.5 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 14.84 | 0.0118 | 3 | 100.00% | 26.7 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✗ | 17.87 | 0.0240 | 5 | 100.00% | 46.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 15.16 | 0.0184 | 4 | 100.00% | 25.0 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 12.75 | 0.0137 | 4 | 75.00% | 32.5 |
| 41 | The set of integers Z with the binary operation... | ✓ | 15.21 | 0.0164 | 4 | 100.00% | 37.5 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✗ | 17.85 | 0.0152 | 4 | 100.00% | 22.5 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 14.85 | 0.0193 | 4 | 75.00% | 40.0 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 11.29 | 0.0144 | 4 | 75.00% | 47.5 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 12.66 | 0.0183 | 4 | 75.00% | 47.5 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 13.69 | 0.0170 | 4 | 75.00% | 45.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 17.26 | 0.0173 | 4 | 75.00% | 45.0 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 15.87 | 0.0170 | 4 | 100.00% | 42.5 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✓ | 18.96 | 0.0191 | 4 | 100.00% | 37.5 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 14.85 | 0.0175 | 4 | 100.00% | 30.0 |
