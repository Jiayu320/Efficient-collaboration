# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 8
- 准确率: 16.00%
- 平均执行时间: 33.28 秒
- 平均成本: $0.0163

## 任务规划指标

- 平均任务步骤数: 3.64
- 平均压缩比例: 83.87%
- 平均每步骤Token限制: 61.39 tokens

## 理论性能指标

- 平均理论执行时间: 4.383 秒
- 平均顺序执行时间: 10.349 秒
- 平均并行加速比: 2.37x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.568 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 19.172 秒

### 生成速度
- 小模型平均每秒生成token数: 20.00 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 34.59 tokens/s
- 总平均每秒生成token数: 54.59 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 27.03 | 0.0122 | 3 | 100.00% | 56.7 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 17.40 | 0.0086 | 2 | 100.00% | 75.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 23.87 | 0.0129 | 4 | 100.00% | 35.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 42.78 | 0.0449 | 10 | 30.00% | 58.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 30.22 | 0.0161 | 3 | 100.00% | 83.3 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 22.56 | 0.0139 | 3 | 100.00% | 46.7 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 25.61 | 0.0190 | 4 | 100.00% | 80.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 24.26 | 0.0244 | 5 | 60.00% | 50.0 |
| 9 | In a parallel universe where a magnet can have ... | ✓ | 20.85 | 0.0113 | 3 | 66.67% | 50.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 29.96 | 0.0227 | 5 | 60.00% | 62.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 18.44 | 0.0108 | 2 | 100.00% | 65.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 33.55 | 0.0202 | 4 | 100.00% | 60.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 29.16 | 0.0138 | 2 | 100.00% | 85.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 25.84 | 0.0165 | 3 | 66.67% | 70.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 31.08 | 0.0138 | 3 | 100.00% | 63.3 |
| 16 | Which of the following statements is a correct ... | ✗ | 19.89 | 0.0092 | 2 | 100.00% | 85.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 20.09 | 0.0076 | 2 | 100.00% | 75.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 26.25 | 0.0146 | 3 | 100.00% | 60.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 31.94 | 0.0355 | 9 | 55.56% | 41.1 |
| 20 | which of the following molecules has c3h symmet... | ✓ | 31.26 | 0.0192 | 4 | 100.00% | 65.0 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 22.27 | 0.0124 | 3 | 100.00% | 83.3 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 67.14 | 0.0190 | 3 | 100.00% | 73.3 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 30.07 | 0.0178 | 3 | 66.67% | 60.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 23.06 | 0.0172 | 5 | 40.00% | 22.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 36.82 | 0.0241 | 5 | 60.00% | 56.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 33.04 | 0.0073 | 2 | 100.00% | 60.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✓ | 54.90 | 0.0110 | 3 | 100.00% | 70.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 140.45 | 0.0190 | 4 | 100.00% | 60.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 119.95 | 0.0079 | 2 | 100.00% | 60.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 25.35 | 0.0106 | 3 | 100.00% | 30.0 |
| 31 | All the following statements about the molecula... | ✗ | 28.91 | 0.0193 | 6 | 33.33% | 55.0 |
| 32 | You are interested in studying a rare type of b... | ✓ | 15.03 | 0.0034 | 1 | 100.00% | 70.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 28.82 | 0.0116 | 3 | 66.67% | 46.7 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 22.70 | 0.0096 | 2 | 100.00% | 45.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 37.42 | 0.0171 | 4 | 100.00% | 80.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 23.06 | 0.0112 | 3 | 66.67% | 56.7 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 28.14 | 0.0139 | 3 | 66.67% | 86.7 |
| 38 | Identify the final product produced when cyclob... | ✗ | 29.85 | 0.0151 | 4 | 100.00% | 72.5 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 37.65 | 0.0228 | 4 | 75.00% | 75.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 37.23 | 0.0206 | 5 | 100.00% | 56.0 |
| 41 | How many of the following compounds will exhibi... | ✓ | 33.71 | 0.0329 | 8 | 25.00% | 58.8 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✓ | 31.47 | 0.0122 | 3 | 100.00% | 70.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 19.12 | 0.0033 | 1 | 100.00% | 70.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 24.93 | 0.0121 | 3 | 100.00% | 63.3 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 47.07 | 0.0400 | 7 | 71.43% | 60.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 21.26 | 0.0101 | 2 | 100.00% | 25.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 31.36 | 0.0226 | 4 | 75.00% | 60.0 |
| 48 | Which of the following statements about enhance... | ✗ | 25.24 | 0.0111 | 3 | 66.67% | 70.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 23.15 | 0.0143 | 3 | 66.67% | 53.3 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 33.01 | 0.0176 | 4 | 75.00% | 55.0 |
