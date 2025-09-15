# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: Qwen/Qwen2.5-3B-Instruct
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 1
- 准确率: 2.00%
- 平均执行时间: 8.66 秒
- 平均成本: $0.0000

## 任务规划指标

- 平均任务步骤数: 7.88
- 平均压缩比例: 61.29%
- 平均每步骤Token限制: 33.45 tokens

## 理论性能指标

- 平均理论执行时间: 7.869 秒
- 平均顺序执行时间: 21.060 秒
- 平均并行加速比: 2.73x
- 理论与实际执行时间比例: 0.91x


## 任务分配统计

- 总任务数: 386
- 小模型执行任务数: 11
- 大模型执行任务数: 375
- 小模型任务占比: 2.85%
- 大模型任务占比: 97.15%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.111 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 8.385 秒

### 生成速度
- 小模型平均每秒生成token数: 3.14 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 50.34 tokens/s
- 总平均每秒生成token数: 53.48 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 1.18 | 0.0000 | - | - | - |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 7.13 | 0.0000 | 6 | 50.00% | 26.7 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 5.90 | 0.0000 | 5 | 60.00% | 42.0 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 11.38 | 0.0000 | 10 | 30.00% | 38.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 8.01 | 0.0000 | 7 | 42.86% | 37.1 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 8.97 | 0.0000 | 7 | 100.00% | 25.7 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 8.51 | 0.0000 | 6 | 83.33% | 35.8 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 9.47 | 0.0000 | 8 | 62.50% | 36.2 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 8.96 | 0.0000 | 8 | 50.00% | 33.8 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 8.89 | 0.0000 | 9 | 33.33% | 41.1 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 9.42 | 0.0000 | 9 | 44.44% | 25.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 9.66 | 0.0000 | 8 | 75.00% | 28.1 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 10.78 | 0.0000 | 8 | 87.50% | 45.6 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 12.33 | 0.0000 | 9 | 88.89% | 47.8 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 10.99 | 0.0000 | 9 | 55.56% | 31.7 |
| 16 | Which of the following statements is a correct ... | ✗ | 7.60 | 0.0000 | 8 | 62.50% | 36.2 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 7.26 | 0.0000 | 7 | 71.43% | 31.4 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 9.54 | 0.0000 | 9 | 33.33% | 26.7 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 11.38 | 0.0000 | 10 | 40.00% | 26.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 9.96 | 0.0000 | 8 | 37.50% | 30.6 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 6.77 | 0.0000 | 6 | 50.00% | 27.5 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 9.15 | 0.0000 | 9 | 55.56% | 23.9 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 9.07 | 0.0000 | 6 | 66.67% | 40.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 9.36 | 0.0000 | 8 | 50.00% | 22.5 |
| 25 | Astronomers are studying two binary star system... | ✗ | 9.74 | 0.0000 | 9 | 55.56% | 27.8 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 6.67 | 0.0000 | 8 | 87.50% | 35.6 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 6.70 | 0.0000 | 5 | 80.00% | 32.0 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 8.54 | 0.0000 | 9 | 22.22% | 28.3 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 9.47 | 0.0000 | 8 | 87.50% | 33.1 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 10.44 | 0.0000 | 10 | 40.00% | 23.0 |
| 31 | All the following statements about the molecula... | ✗ | 7.63 | 0.0000 | 7 | 71.43% | 45.7 |
| 32 | You are interested in studying a rare type of b... | ✓ | 8.30 | 0.0000 | 8 | 62.50% | 41.2 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 6.14 | 0.0000 | 5 | 60.00% | 22.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 8.55 | 0.0000 | 8 | 87.50% | 30.6 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 9.99 | 0.0000 | 9 | 77.78% | 28.9 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 8.13 | 0.0000 | 9 | 66.67% | 33.9 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 6.94 | 0.0000 | 7 | 85.71% | 32.9 |
| 38 | Identify the final product produced when cyclob... | ✗ | 8.06 | 0.0000 | 8 | 75.00% | 33.8 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 10.59 | 0.0000 | 9 | 44.44% | 37.2 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 8.24 | 0.0000 | 8 | 50.00% | 39.4 |
| 41 | How many of the following compounds will exhibi... | ✗ | 11.56 | 0.0000 | 9 | 22.22% | 30.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✓ | 7.04 | 0.0000 | 6 | 66.67% | 28.3 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 5.38 | 0.0000 | 4 | 75.00% | 43.8 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 9.05 | 0.0000 | 8 | 75.00% | 55.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 7.72 | 0.0000 | 8 | 62.50% | 35.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 7.84 | 0.0000 | 8 | 62.50% | 26.9 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 10.52 | 0.0000 | 10 | 30.00% | 30.0 |
| 48 | Which of the following statements about enhance... | ✗ | 9.29 | 0.0000 | 8 | 87.50% | 42.5 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 8.88 | 0.0000 | 10 | 50.00% | 32.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 9.80 | 0.0000 | 8 | 87.50% | 30.6 |
