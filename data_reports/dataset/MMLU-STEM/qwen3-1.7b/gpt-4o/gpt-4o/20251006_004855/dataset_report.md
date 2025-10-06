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
- 正确数量: 37
- 准确率: 74.00%
- 平均执行时间: 8.09 秒
- 平均成本: $0.0072

## 任务规划指标

- 平均任务步骤数: 3.18
- 平均压缩比例: 66.97%
- 平均每步骤Token限制: 22.37 tokens

## 理论性能指标

- 平均理论执行时间: 2.845 秒
- 平均顺序执行时间: 4.201 秒
- 平均并行加速比: 1.46x
- 理论与实际执行时间比例: 0.35x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.208 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 1.667 秒

### 生成速度
- 小模型平均每秒生成token数: 51.22 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 14.60 tokens/s
- 总平均每秒生成token数: 65.82 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 12.16 | 0.0141 | 3 | 66.67% | 20.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 8.59 | 0.0083 | 2 | 100.00% | 27.5 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 7.85 | 0.0083 | 2 | 100.00% | 17.5 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✓ | 6.36 | 0.0053 | 3 | 33.33% | 23.3 |
| 5 | Find the product of the given polynomials in th... | ✓ | 5.76 | 0.0049 | 1 | 100.00% | 30.0 |
| 6 | Statement 1 | If a group has an element of orde... | ✓ | 13.55 | 0.0137 | 5 | 100.00% | 25.0 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 10.85 | 0.0110 | 4 | 75.00% | 22.5 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 6.15 | 0.0067 | 3 | 33.33% | 16.7 |
| 9 | Find the degree for the given field extension Q... | ✓ | 6.44 | 0.0046 | 1 | 100.00% | 20.0 |
| 10 | Find all zeros in the indicated finite field of... | ✗ | 7.82 | 0.0042 | 3 | 100.00% | 20.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 5.80 | 0.0052 | 3 | 33.33% | 23.3 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 8.62 | 0.0087 | 5 | 40.00% | 17.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 9.66 | 0.0072 | 3 | 100.00% | 16.7 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 7.62 | 0.0072 | 1 | 100.00% | 30.0 |
| 15 | Find the maximum possible order for an element ... | ✗ | 6.72 | 0.0030 | 3 | 66.67% | 25.0 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 6.53 | 0.0037 | 2 | 50.00% | 22.5 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 5.42 | 0.0024 | 1 | 100.00% | 25.0 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 7.01 | 0.0045 | 2 | 100.00% | 22.5 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 7.39 | 0.0068 | 5 | 40.00% | 16.0 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 8.54 | 0.0075 | 4 | 50.00% | 22.5 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 9.90 | 0.0115 | 4 | 50.00% | 22.5 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 5.45 | 0.0031 | 1 | 100.00% | 25.0 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✓ | 6.73 | 0.0045 | 3 | 66.67% | 20.0 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 9.13 | 0.0125 | 6 | 33.33% | 20.0 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 9.27 | 0.0071 | 4 | 75.00% | 22.5 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 11.25 | 0.0105 | 5 | 80.00% | 21.0 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✓ | 14.42 | 0.0200 | 5 | 60.00% | 26.0 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 15.11 | 0.0138 | 5 | 100.00% | 16.0 |
| 29 | Statement 1 | The image of a group of 6 element... | ✓ | 6.19 | 0.0046 | 3 | 33.33% | 21.7 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 7.39 | 0.0060 | 4 | 50.00% | 22.5 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✓ | 11.82 | 0.0142 | 6 | 50.00% | 27.5 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 6.73 | 0.0053 | 3 | 66.67% | 25.0 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 6.05 | 0.0039 | 3 | 66.67% | 21.7 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 8.21 | 0.0042 | 3 | 66.67% | 25.0 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 6.48 | 0.0061 | 4 | 25.00% | 22.5 |
| 36 | Find the degree for the given field extension Q... | ✓ | 6.74 | 0.0055 | 1 | 100.00% | 20.0 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✗ | 5.60 | 0.0028 | 1 | 100.00% | 20.0 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✓ | 7.60 | 0.0064 | 5 | 40.00% | 16.0 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 7.03 | 0.0075 | 2 | 50.00% | 22.5 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✓ | 5.38 | 0.0046 | 3 | 33.33% | 23.3 |
| 41 | The set of integers Z with the binary operation... | ✓ | 4.71 | 0.0018 | 1 | 100.00% | 20.0 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✓ | 7.64 | 0.0052 | 4 | 50.00% | 16.2 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 6.07 | 0.0057 | 2 | 50.00% | 22.5 |
| 44 | Statement 1 | Every integral domain with charac... | ✓ | 10.12 | 0.0085 | 4 | 50.00% | 23.8 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 9.08 | 0.0082 | 4 | 50.00% | 22.5 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✓ | 7.49 | 0.0061 | 5 | 40.00% | 28.0 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 6.20 | 0.0061 | 3 | 33.33% | 23.3 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✓ | 9.67 | 0.0075 | 2 | 100.00% | 27.5 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 8.36 | 0.0097 | 5 | 40.00% | 16.0 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 9.64 | 0.0109 | 2 | 100.00% | 35.0 |
