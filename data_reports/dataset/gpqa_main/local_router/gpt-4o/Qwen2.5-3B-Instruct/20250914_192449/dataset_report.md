# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 8
- 准确率: 16.00%
- 平均执行时间: 17.87 秒
- 平均成本: $0.0000

## 任务规划指标

- 平均任务步骤数: 8.86
- 平均压缩比例: 76.83%
- 平均每步骤Token限制: 29.23 tokens

## 理论性能指标

- 平均理论执行时间: 8.922 秒
- 平均顺序执行时间: 22.464 秒
- 平均并行加速比: 2.57x
- 理论与实际执行时间比例: 0.50x


## 任务分配统计

- 总任务数: 381
- 小模型执行任务数: 296
- 大模型执行任务数: 85
- 小模型任务占比: 77.69%
- 大模型任务占比: 22.31%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.149 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 17.492 秒

### 生成速度
- 小模型平均每秒生成token数: 7.40 tokens/s
- 大模型平均每秒生成token数: 0.09 tokens/s
- 路由模型平均每秒生成token数: 26.62 tokens/s
- 总平均每秒生成token数: 34.11 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 18.27 | 0.0000 | 10 | 80.00% | 27.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 18.01 | 0.0000 | 10 | 90.00% | 18.5 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 14.68 | 0.0000 | 7 | 85.71% | 25.0 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 13.72 | 0.0000 | 8 | 87.50% | 28.8 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 17.97 | 0.0000 | 8 | 62.50% | 41.9 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 15.64 | 0.0000 | 6 | 83.33% | 25.8 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 16.10 | 0.0000 | 8 | 87.50% | 30.6 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 16.72 | 0.0000 | 7 | 71.43% | 27.1 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 20.51 | 0.0001 | - | - | - |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 19.97 | 0.0000 | 10 | 60.00% | 21.5 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 18.20 | 0.0000 | 10 | 70.00% | 28.5 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 13.67 | 0.0000 | 7 | 71.43% | 16.4 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 14.69 | 0.0000 | 7 | 57.14% | 22.1 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 21.98 | 0.0000 | 9 | 100.00% | 33.3 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 19.35 | 0.0000 | 10 | 80.00% | 32.5 |
| 16 | Which of the following statements is a correct ... | ✓ | 18.34 | 0.0000 | 9 | 88.89% | 28.3 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 19.47 | 0.0000 | 10 | 70.00% | 27.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 17.70 | 0.0000 | 8 | 62.50% | 28.8 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 16.84 | 0.0000 | 9 | 77.78% | 23.9 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 18.76 | 0.0000 | 10 | 70.00% | 45.5 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 21.14 | 0.0007 | 10 | 80.00% | 49.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 17.46 | 0.0000 | 6 | 83.33% | 28.3 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 15.20 | 0.0000 | 7 | 57.14% | 17.1 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 18.38 | 0.0000 | 10 | 50.00% | 22.5 |
| 25 | Astronomers are studying two binary star system... | ✗ | 19.75 | 0.0000 | 10 | 70.00% | 23.5 |
| 26 | The experimental proof for the chromosomal theo... | ✓ | 11.28 | 0.0000 | - | - | - |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 16.09 | 0.0000 | 7 | 100.00% | 32.1 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 11.57 | 0.0000 | - | - | - |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 21.57 | 0.0000 | 10 | 100.00% | 29.5 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 19.56 | 0.0001 | - | - | - |
| 31 | All the following statements about the molecula... | ✗ | 18.10 | 0.0000 | 10 | 50.00% | 36.5 |
| 32 | You are interested in studying a rare type of b... | ✓ | 23.55 | 0.0000 | 10 | 90.00% | 32.5 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 18.75 | 0.0000 | 9 | 44.44% | 14.4 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 11.25 | 0.0000 | - | - | - |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 17.95 | 0.0000 | 9 | 100.00% | 25.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 20.35 | 0.0000 | 10 | 100.00% | 44.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 17.01 | 0.0000 | 8 | 75.00% | 36.9 |
| 38 | Identify the final product produced when cyclob... | ✗ | 19.40 | 0.0000 | 10 | 90.00% | 25.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 19.59 | 0.0000 | 10 | 70.00% | 32.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 19.80 | 0.0000 | 10 | 50.00% | 35.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 19.92 | 0.0000 | 10 | 40.00% | 24.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 15.54 | 0.0000 | 7 | 57.14% | 21.4 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 17.96 | 0.0000 | 10 | 100.00% | 31.5 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 12.24 | 0.0000 | - | - | - |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 26.03 | 0.0000 | 10 | 100.00% | 48.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 15.00 | 0.0000 | 7 | 85.71% | 22.9 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 18.70 | 0.0000 | 8 | 75.00% | 25.0 |
| 48 | Which of the following statements about enhance... | ✗ | 19.95 | 0.0005 | 10 | 100.00% | 36.5 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 17.32 | 0.0000 | - | - | - |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 22.28 | 0.0008 | 10 | 80.00% | 31.0 |
