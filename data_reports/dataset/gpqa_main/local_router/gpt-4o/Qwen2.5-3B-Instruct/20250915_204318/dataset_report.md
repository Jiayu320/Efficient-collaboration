# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 18
- 准确率: 36.00%
- 平均执行时间: 14.15 秒
- 平均成本: $0.0010

## 任务规划指标

- 平均任务步骤数: 8.42
- 平均压缩比例: 78.76%
- 平均每步骤Token限制: 31.01 tokens

## 理论性能指标

- 平均理论执行时间: 8.238 秒
- 平均顺序执行时间: 21.006 秒
- 平均并行加速比: 2.56x
- 理论与实际执行时间比例: 0.58x


## 任务分配统计

- 总任务数: 404
- 小模型执行任务数: 200
- 大模型执行任务数: 204
- 小模型任务占比: 49.50%
- 大模型任务占比: 50.50%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.386 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 12.385 秒

### 生成速度
- 小模型平均每秒生成token数: 4.32 tokens/s
- 大模型平均每秒生成token数: 2.57 tokens/s
- 路由模型平均每秒生成token数: 38.08 tokens/s
- 总平均每秒生成token数: 44.96 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 16.90 | 0.0008 | 6 | 50.00% | 29.2 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 19.04 | 0.0011 | 10 | 90.00% | 22.5 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 14.62 | 0.0007 | 8 | 100.00% | 35.0 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 13.18 | 0.0000 | 11 | 45.45% | 33.6 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 14.04 | 0.0008 | 9 | 77.78% | 29.4 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 15.22 | 0.0031 | 7 | 85.71% | 35.7 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 14.60 | 0.0006 | 8 | 100.00% | 28.8 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 12.96 | 0.0000 | 9 | 77.78% | 21.1 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 18.41 | 0.0012 | 10 | 100.00% | 36.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 13.82 | 0.0000 | 10 | 40.00% | 32.0 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 13.42 | 0.0000 | 8 | 87.50% | 25.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 11.72 | 0.0000 | 7 | 85.71% | 24.3 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 15.41 | 0.0014 | 7 | 100.00% | 33.6 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 21.12 | 0.0020 | 10 | 80.00% | 53.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 16.62 | 0.0042 | 10 | 90.00% | 27.5 |
| 16 | Which of the following statements is a correct ... | ✓ | 15.77 | 0.0020 | 10 | 70.00% | 33.5 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 17.62 | 0.0011 | 10 | 100.00% | 32.5 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 16.81 | 0.0038 | 9 | 66.67% | 49.4 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 12.43 | 0.0000 | 10 | 60.00% | 26.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 17.56 | 0.0014 | 12 | 33.33% | 35.8 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 15.89 | 0.0007 | 10 | 50.00% | 35.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 13.90 | 0.0010 | 9 | 77.78% | 28.3 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 9.28 | 0.0014 | 4 | 75.00% | 30.0 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 12.55 | 0.0000 | 10 | 50.00% | 32.5 |
| 25 | Astronomers are studying two binary star system... | ✗ | 12.67 | 0.0000 | 8 | 75.00% | 29.4 |
| 26 | The experimental proof for the chromosomal theo... | ✓ | 9.70 | 0.0000 | - | - | - |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 6.97 | 0.0000 | 3 | 100.00% | 23.3 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 11.80 | 0.0008 | 8 | 75.00% | 26.2 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✓ | 11.84 | 0.0000 | 7 | 100.00% | 31.4 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 13.03 | 0.0000 | 10 | 70.00% | 27.5 |
| 31 | All the following statements about the molecula... | ✗ | 12.76 | 0.0010 | 6 | 66.67% | 50.0 |
| 32 | You are interested in studying a rare type of b... | ✗ | 15.28 | 0.0012 | 10 | 90.00% | 29.5 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 10.17 | 0.0000 | 8 | 75.00% | 16.2 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 10.10 | 0.0000 | - | - | - |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 12.90 | 0.0000 | 10 | 100.00% | 18.5 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 13.05 | 0.0000 | 10 | 60.00% | 25.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 11.66 | 0.0000 | 6 | 100.00% | 32.5 |
| 38 | Identify the final product produced when cyclob... | ✗ | 15.03 | 0.0011 | 8 | 100.00% | 28.1 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 16.38 | 0.0029 | 10 | 80.00% | 34.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 15.03 | 0.0019 | 8 | 87.50% | 40.6 |
| 41 | How many of the following compounds will exhibi... | ✓ | 15.32 | 0.0036 | 8 | 100.00% | 36.2 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✓ | 13.62 | 0.0000 | 9 | 66.67% | 36.1 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 15.95 | 0.0012 | 6 | 100.00% | 36.7 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 18.80 | 0.0022 | 9 | 100.00% | 30.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 12.45 | 0.0014 | 7 | 57.14% | 28.6 |
| 46 | What is the concentration of calcium ions in a ... | ✓ | 11.16 | 0.0000 | 8 | 75.00% | 21.2 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 12.27 | 0.0010 | 5 | 80.00% | 20.0 |
| 48 | Which of the following statements about enhance... | ✗ | 12.52 | 0.0015 | 6 | 100.00% | 42.5 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 14.52 | 0.0009 | 10 | 70.00% | 28.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 19.63 | 0.0000 | 10 | 60.00% | 26.5 |
