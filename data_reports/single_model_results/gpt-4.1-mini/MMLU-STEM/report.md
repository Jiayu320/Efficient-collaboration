# 单模型数据集处理报告

## 模型信息

- 模型: gpt-4.1-mini
- 延迟 (TTFT): 0.700 秒
- 吞吐量: 69.59 tokens/s

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 50
- 超时问题数: 0 (0.00%)
- 有效问题数: 50
- 正确数量: 33
- 准确率(有效问题): 66.00%
- 平均执行时间(有效问题): 9.17 秒
- 平均理论时间(有效问题): 7.11 秒
- 实际/理论时间比率: 1.29x
- 平均成本(有效问题): $0.0007

## 性能指标

- 平均首个令牌响应时间 (TTFT): 2.627 秒
- 平均每秒生成token数: 46.23 tokens/s
- 理论每秒生成token数: 69.59 tokens/s
- 实际/理论吞吐量比率: 0.66x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✓ | 8.49 | 6.36 | 0.0007 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✓ | 12.14 | 12.64 | 0.0014 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 14.59 | 10.99 | 0.0012 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 8.85 | 5.18 | 0.0005 |
| 5 | Find the product of the given polynomials in th... | ✓ | 10.71 | 9.67 | 0.0010 |
| 6 | Statement 1 | If a group has an element of orde... | ✓ | 9.61 | 9.65 | 0.0010 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✓ | 7.15 | 5.46 | 0.0006 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 7.46 | 5.82 | 0.0006 |
| 9 | Find the degree for the given field extension Q... | ✓ | 22.68 | 24.70 | 0.0027 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 8.81 | 8.65 | 0.0009 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 6.57 | 5.49 | 0.0006 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✓ | 7.97 | 5.89 | 0.0006 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✓ | 9.41 | 7.31 | 0.0008 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✓ | 10.80 | 10.37 | 0.0011 |
| 15 | Find the maximum possible order for an element ... | ✓ | 8.81 | 7.68 | 0.0008 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 8.72 | 5.00 | 0.0005 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 6.49 | 3.98 | 0.0004 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 9.57 | 3.86 | 0.0004 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 7.09 | 3.89 | 0.0004 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✓ | 6.26 | 6.12 | 0.0006 |
| 21 | Statement 1 | For finite groups G and H, |G + H... | ✓ | 8.20 | 6.62 | 0.0007 |
| 22 | Find the sum of the given polynomials in the gi... | ✓ | 8.04 | 4.11 | 0.0004 |
| 23 | Statement 1 | Any set of two vectors in R^2 is ... | ✗ | 7.26 | 4.36 | 0.0004 |
| 24 | The set of all nth roots of unity under multipl... | ✓ | 7.20 | 4.28 | 0.0004 |
| 25 | Statement 1 | Every maximal ideal is a prime id... | ✗ | 6.26 | 3.43 | 0.0003 |
| 26 | Let G denoted the set of all n x n non-singular... | ✓ | 6.49 | 5.08 | 0.0005 |
| 27 | Statement 1 | Every group of order 42 has a nor... | ✗ | 8.34 | 6.58 | 0.0007 |
| 28 | Determine whether the polynomial in Z[x] satisf... | ✓ | 11.86 | 8.06 | 0.0009 |
| 29 | Statement 1 | The image of a group of 6 element... | ✗ | 8.93 | 5.96 | 0.0006 |
| 30 | Statement 1 | The homomorphic image of a cyclic... | ✓ | 7.16 | 5.04 | 0.0005 |
| 31 | Statement 1 | If H is a subgroup of a group G a... | ✗ | 7.88 | 5.14 | 0.0005 |
| 32 | If (G, .) is a group such that (ab)^-1 = a^-1b^... | ✓ | 11.36 | 11.12 | 0.0012 |
| 33 | Statement 1 | In a finite dimensional vector sp... | ✓ | 5.03 | 3.06 | 0.0003 |
| 34 | Some group (G, 0) is known to be abelian. Then ... | ✓ | 7.35 | 7.87 | 0.0008 |
| 35 | Statement 1 | If T: V -> W is a linear transfor... | ✗ | 9.73 | 8.01 | 0.0009 |
| 36 | Find the degree for the given field extension Q... | ✓ | 13.32 | 9.11 | 0.0010 |
| 37 | Compute the product in the given ring. (20)(-8)... | ✓ | 6.08 | 2.98 | 0.0003 |
| 38 | Determine whether the polynomial in Z[x] satisf... | ✓ | 11.86 | 9.59 | 0.0010 |
| 39 | Find the generator for the finite field Z_7.  A... | ✓ | 10.91 | 7.99 | 0.0008 |
| 40 | Statement 1 | Every permutation is a cycle. Sta... | ✗ | 4.38 | 2.61 | 0.0002 |
| 41 | The set of integers Z with the binary operation... | ✓ | 6.17 | 3.90 | 0.0004 |
| 42 | Find the characteristic of the ring Z_3 x 3Z.  ... | ✓ | 10.26 | 6.25 | 0.0006 |
| 43 | Statement 1 | Some abelian group of order 45 ha... | ✗ | 6.25 | 6.19 | 0.0007 |
| 44 | Statement 1 | Every integral domain with charac... | ✗ | 7.00 | 4.52 | 0.0005 |
| 45 | Let A and B be sets, f: A -> B and g: B -> A be... | ✓ | 13.87 | 8.14 | 0.0009 |
| 46 | Statement 1 | For any two groups G and G', ther... | ✗ | 6.12 | 3.85 | 0.0004 |
| 47 | Statement 1 | A homomorphism may have an empty ... | ✗ | 7.18 | 5.61 | 0.0006 |
| 48 | Find all c in Z_3 such that Z_3[x]/(x^3 + x^2 +... | ✗ | 18.70 | 20.69 | 0.0023 |
| 49 | Statement 1 | If a R is an integral domain, the... | ✗ | 8.73 | 5.07 | 0.0005 |
| 50 | Find the maximum possible order for some elemen... | ✓ | 14.48 | 11.65 | 0.0012 |
