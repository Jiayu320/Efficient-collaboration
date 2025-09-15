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
- 正确数量: 6
- 准确率: 12.00%
- 平均执行时间: 13.66 秒
- 平均成本: $0.0020

## 任务规划指标

- 平均任务步骤数: 7.76
- 平均压缩比例: 64.87%
- 平均每步骤Token限制: 35.26 tokens

## 理论性能指标

- 平均理论执行时间: 6.741 秒
- 平均顺序执行时间: 19.016 秒
- 平均并行加速比: 2.84x
- 理论与实际执行时间比例: 0.49x


## 任务分配统计

- 总任务数: 388
- 小模型执行任务数: 7
- 大模型执行任务数: 381
- 小模型任务占比: 1.80%
- 大模型任务占比: 98.20%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.686 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 10.476 秒

### 生成速度
- 小模型平均每秒生成token数: 1.93 tokens/s
- 大模型平均每秒生成token数: 4.87 tokens/s
- 路由模型平均每秒生成token数: 35.70 tokens/s
- 总平均每秒生成token数: 42.50 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 14.24 | 0.0015 | 7 | 57.14% | 40.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 10.65 | 0.0021 | 5 | 80.00% | 29.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 13.29 | 0.0013 | 9 | 66.67% | 31.7 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 13.67 | 0.0014 | 10 | 30.00% | 38.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 12.42 | 0.0012 | 9 | 44.44% | 35.6 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 16.01 | 0.0039 | 6 | 100.00% | 43.3 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 11.21 | 0.0015 | 6 | 83.33% | 35.8 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 12.21 | 0.0026 | 7 | 57.14% | 34.3 |
| 9 | In a parallel universe where a magnet can have ... | ✓ | 18.52 | 0.0033 | 9 | 66.67% | 47.8 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✓ | 12.13 | 0.0000 | 10 | 30.00% | 29.5 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 12.99 | 0.0009 | 9 | 55.56% | 37.8 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✓ | 12.80 | 0.0017 | 8 | 62.50% | 28.8 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 16.16 | 0.0044 | 6 | 83.33% | 43.3 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 12.61 | 0.0000 | 9 | 55.56% | 37.2 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 18.90 | 0.0011 | 10 | 50.00% | 34.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 16.40 | 0.0034 | 8 | 87.50% | 36.9 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 12.66 | 0.0019 | 8 | 62.50% | 31.2 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 19.22 | 0.0026 | 9 | 55.56% | 29.4 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✓ | 12.35 | 0.0014 | 8 | 75.00% | 30.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 14.18 | 0.0000 | 10 | 20.00% | 36.0 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 9.56 | 0.0024 | 5 | 60.00% | 49.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 12.25 | 0.0026 | 8 | 62.50% | 34.4 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 11.09 | 0.0023 | 5 | 80.00% | 28.0 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 11.52 | 0.0012 | 8 | 50.00% | 28.1 |
| 25 | Astronomers are studying two binary star system... | ✗ | 11.24 | 0.0008 | 8 | 62.50% | 28.8 |
| 26 | The experimental proof for the chromosomal theo... | ✓ | 11.88 | 0.0015 | 6 | 100.00% | 39.2 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 29.32 | 0.0006 | 5 | 80.00% | 35.0 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 12.55 | 0.0010 | 7 | 57.14% | 28.6 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 12.29 | 0.0017 | 6 | 83.33% | 38.3 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 11.16 | 0.0000 | 9 | 44.44% | 25.6 |
| 31 | All the following statements about the molecula... | ✗ | 12.58 | 0.0011 | 9 | 33.33% | 37.8 |
| 32 | You are interested in studying a rare type of b... | ✓ | 9.58 | 0.0008 | 6 | 50.00% | 37.5 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✓ | 8.48 | 0.0011 | 4 | 75.00% | 25.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 15.44 | 0.0035 | 8 | 87.50% | 29.4 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 18.25 | 0.0053 | 10 | 100.00% | 39.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 10.91 | 0.0007 | 9 | 44.44% | 31.1 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 13.11 | 0.0018 | 7 | 85.71% | 30.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 15.40 | 0.0025 | 8 | 87.50% | 33.1 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 13.33 | 0.0024 | 10 | 50.00% | 38.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 10.60 | 0.0009 | 9 | 44.44% | 33.9 |
| 41 | How many of the following compounds will exhibi... | ✗ | 13.39 | 0.0012 | 9 | 33.33% | 37.8 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✓ | 19.74 | 0.0063 | 9 | 77.78% | 31.1 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 9.82 | 0.0013 | 5 | 80.00% | 42.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 14.78 | 0.0025 | 9 | 66.67% | 41.1 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 13.57 | 0.0026 | 9 | 55.56% | 40.0 |
| 46 | What is the concentration of calcium ions in a ... | ✓ | 9.79 | 0.0008 | 6 | 50.00% | 22.5 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 11.02 | 0.0028 | 6 | 66.67% | 27.5 |
| 48 | Which of the following statements about enhance... | ✗ | 14.91 | 0.0021 | 8 | 87.50% | 41.2 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 17.22 | 0.0060 | 9 | 77.78% | 51.1 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 15.75 | 0.0027 | 8 | 87.50% | 48.8 |
