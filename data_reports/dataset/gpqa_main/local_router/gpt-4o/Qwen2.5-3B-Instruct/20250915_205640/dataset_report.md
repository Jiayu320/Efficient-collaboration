# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 7
- 准确率: 14.00%
- 平均执行时间: 15.79 秒
- 平均成本: $0.0023

## 任务规划指标

- 平均任务步骤数: 8.44
- 平均压缩比例: 78.84%
- 平均每步骤Token限制: 31.18 tokens

## 理论性能指标

- 平均理论执行时间: 7.949 秒
- 平均顺序执行时间: 20.406 秒
- 平均并行加速比: 2.59x
- 理论与实际执行时间比例: 0.50x


## 任务分配统计

- 总任务数: 422
- 小模型执行任务数: 9
- 大模型执行任务数: 413
- 小模型任务占比: 2.13%
- 大模型任务占比: 97.87%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.774 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.836 秒

### 生成速度
- 小模型平均每秒生成token数: 0.98 tokens/s
- 大模型平均每秒生成token数: 4.55 tokens/s
- 路由模型平均每秒生成token数: 35.27 tokens/s
- 总平均每秒生成token数: 40.80 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 14.88 | 0.0015 | 6 | 83.33% | 25.8 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 11.96 | 0.0016 | 6 | 83.33% | 18.3 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 17.48 | 0.0023 | 10 | 100.00% | 25.0 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 17.42 | 0.0060 | 8 | 87.50% | 55.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 15.56 | 0.0025 | 6 | 83.33% | 27.5 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 15.74 | 0.0026 | 9 | 66.67% | 31.1 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 14.99 | 0.0019 | 7 | 100.00% | 30.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 15.06 | 0.0026 | 7 | 100.00% | 25.7 |
| 9 | In a parallel universe where a magnet can have ... | ✓ | 13.54 | 0.0017 | 7 | 85.71% | 30.7 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 14.07 | 0.0007 | 9 | 66.67% | 29.4 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 16.15 | 0.0023 | 10 | 70.00% | 29.5 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✓ | 16.93 | 0.0040 | 9 | 88.89% | 23.3 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 17.78 | 0.0023 | 9 | 55.56% | 35.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 20.50 | 0.0032 | 9 | 88.89% | 35.6 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 18.66 | 0.0043 | 10 | 100.00% | 33.5 |
| 16 | Which of the following statements is a correct ... | ✓ | 18.31 | 0.0026 | 9 | 100.00% | 35.6 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 14.30 | 0.0011 | 10 | 60.00% | 24.0 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 19.62 | 0.0051 | 10 | 90.00% | 35.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 15.79 | 0.0010 | 10 | 40.00% | 28.5 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 13.67 | 0.0012 | 11 | 27.27% | 25.9 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 15.67 | 0.0010 | 10 | 60.00% | 46.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 14.62 | 0.0009 | 10 | 60.00% | 23.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 12.95 | 0.0027 | 5 | 100.00% | 25.0 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 12.93 | 0.0009 | 8 | 62.50% | 26.2 |
| 25 | Astronomers are studying two binary star system... | ✗ | 14.63 | 0.0029 | 7 | 71.43% | 34.3 |
| 26 | The experimental proof for the chromosomal theo... | ✓ | 20.71 | 0.0015 | 8 | 100.00% | 22.5 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✓ | 12.98 | 0.0015 | 6 | 100.00% | 24.2 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 10.85 | 0.0008 | 6 | 66.67% | 30.8 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 17.69 | 0.0025 | 10 | 100.00% | 25.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 12.13 | 0.0009 | 9 | 44.44% | 20.0 |
| 31 | All the following statements about the molecula... | ✗ | 18.03 | 0.0034 | 7 | 100.00% | 50.0 |
| 32 | You are interested in studying a rare type of b... | ✗ | 22.14 | 0.0040 | 10 | 100.00% | 60.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✓ | 11.00 | 0.0011 | 6 | 66.67% | 20.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 19.18 | 0.0026 | 8 | 87.50% | 30.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 17.02 | 0.0031 | 9 | 100.00% | 22.2 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 13.16 | 0.0012 | 10 | 60.00% | 29.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 15.47 | 0.0023 | 8 | 87.50% | 28.1 |
| 38 | Identify the final product produced when cyclob... | ✗ | 14.25 | 0.0019 | 7 | 100.00% | 26.4 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 14.04 | 0.0021 | 10 | 40.00% | 44.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✓ | 14.01 | 0.0006 | 8 | 50.00% | 29.4 |
| 41 | How many of the following compounds will exhibi... | ✗ | 14.81 | 0.0012 | 10 | 30.00% | 26.5 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✓ | 14.56 | 0.0023 | 7 | 100.00% | 37.1 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 19.41 | 0.0036 | 10 | 100.00% | 49.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✗ | 19.02 | 0.0031 | 10 | 80.00% | 31.5 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 18.06 | 0.0038 | 9 | 77.78% | 45.6 |
| 46 | What is the concentration of calcium ions in a ... | ✓ | 17.60 | 0.0033 | 9 | 88.89% | 22.2 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 13.45 | 0.0018 | 7 | 71.43% | 27.9 |
| 48 | Which of the following statements about enhance... | ✗ | 13.76 | 0.0018 | 6 | 100.00% | 40.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 17.03 | 0.0035 | 10 | 90.00% | 28.5 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 15.81 | 0.0014 | 10 | 70.00% | 30.0 |
