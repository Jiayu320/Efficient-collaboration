# 数据集处理报告

## 模型配置

- 小模型: gpt-4.1-mini
- 大模型: gpt-4.1-mini
- 路由模型: saves/Llama-3.2-1B-Instruct/full/Llama-3-2-1B_ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 50
- 正确数量: 28
- 准确率: 56.00%
- 平均执行时间: 13.31 秒
- 平均成本: $0.0090

## 任务规划指标

- 平均任务步骤数: 4.12
- 平均压缩比例: 93.90%
- 平均每步骤Token限制: 50.73 tokens

## 理论性能指标

- 平均理论执行时间: 6.507 秒
- 平均顺序执行时间: 8.467 秒
- 平均并行加速比: 1.31x
- 理论与实际执行时间比例: 0.49x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.308 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 7.101 秒

### 生成速度
- 小模型平均每秒生成token数: 31.29 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 29.22 tokens/s
- 总平均每秒生成token数: 60.51 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 16.49 | 0.0092 | 4 | 100.00% | 50.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 6.24 | 0.0077 | 4 | 100.00% | 35.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 8.91 | 0.0071 | 3 | 100.00% | 46.7 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 28.78 | 0.0127 | 4 | 75.00% | 50.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 10.28 | 0.0087 | 4 | 100.00% | 50.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 6.07 | 0.0075 | 4 | 100.00% | 50.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 6.01 | 0.0079 | 5 | 100.00% | 58.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 17.38 | 0.0089 | 3 | 100.00% | 43.3 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 5.94 | 0.0077 | 4 | 100.00% | 47.5 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 15.67 | 0.0107 | 4 | 75.00% | 47.5 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 14.14 | 0.0093 | 4 | 100.00% | 50.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✓ | 15.51 | 0.0083 | 4 | 100.00% | 45.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 30.74 | 0.0121 | 4 | 100.00% | 105.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 5.99 | 0.0080 | 4 | 100.00% | 50.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 13.07 | 0.0086 | 4 | 100.00% | 47.5 |
| 16 | Which of the following statements is a correct ... | ✓ | 6.17 | 0.0069 | 3 | 100.00% | 63.3 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 5.77 | 0.0067 | 3 | 100.00% | 40.0 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 6.69 | 0.0093 | 6 | 83.33% | 46.7 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 11.24 | 0.0089 | 6 | 100.00% | 53.3 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 15.53 | 0.0085 | 4 | 100.00% | 47.5 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 5.82 | 0.0068 | 3 | 100.00% | 63.3 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 7.29 | 0.0081 | 4 | 100.00% | 55.0 |
| 23 | In the last few decades, reverberation mapping,... | ✓ | 6.12 | 0.0074 | 3 | 100.00% | 43.3 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 7.04 | 0.0080 | 4 | 100.00% | 37.5 |
| 25 | Astronomers are studying two binary star system... | ✗ | 9.12 | 0.0080 | 4 | 100.00% | 42.5 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 6.01 | 0.0073 | 4 | 100.00% | 42.5 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 9.83 | 0.0090 | 3 | 100.00% | 66.7 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 12.02 | 0.0086 | 4 | 100.00% | 37.5 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 5.84 | 0.0077 | 4 | 100.00% | 45.0 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 8.46 | 0.0075 | 4 | 100.00% | 35.0 |
| 31 | All the following statements about the molecula... | ✗ | 14.86 | 0.0119 | 6 | 50.00% | 46.7 |
| 32 | You are interested in studying a rare type of b... | ✓ | 15.12 | 0.0087 | 4 | 100.00% | 52.5 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✓ | 15.91 | 0.0086 | 3 | 100.00% | 36.7 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 13.56 | 0.0094 | 4 | 100.00% | 35.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 37.82 | 0.0152 | 5 | 100.00% | 46.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 12.36 | 0.0087 | 4 | 100.00% | 47.5 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✓ | 6.85 | 0.0084 | 5 | 80.00% | 62.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 17.61 | 0.0092 | 4 | 100.00% | 57.5 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 17.18 | 0.0112 | 4 | 75.00% | 42.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 30.78 | 0.0121 | 5 | 100.00% | 64.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 29.48 | 0.0116 | 4 | 75.00% | 90.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 18.60 | 0.0090 | 4 | 75.00% | 42.5 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 11.48 | 0.0080 | 4 | 100.00% | 37.5 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 5.80 | 0.0086 | 5 | 80.00% | 44.0 |
| 45 | Consider the extension of the Standard Model gi... | ✓ | 25.50 | 0.0116 | 4 | 100.00% | 112.5 |
| 46 | What is the concentration of calcium ions in a ... | ✓ | 20.38 | 0.0101 | 4 | 100.00% | 45.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 10.88 | 0.0093 | 6 | 66.67% | 50.0 |
| 48 | Which of the following statements about enhance... | ✓ | 15.11 | 0.0094 | 5 | 60.00% | 50.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 14.52 | 0.0095 | 4 | 100.00% | 32.5 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 7.50 | 0.0075 | 4 | 100.00% | 47.5 |
