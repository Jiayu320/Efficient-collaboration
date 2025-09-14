# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 4
- 准确率: 8.00%
- 平均执行时间: 17.73 秒
- 平均成本: $0.0014

## 任务规划指标

- 平均任务步骤数: 8.76
- 平均压缩比例: 79.99%
- 平均每步骤Token限制: 29.33 tokens

## 理论性能指标

- 平均理论执行时间: 8.224 秒
- 平均顺序执行时间: 21.025 秒
- 平均并行加速比: 2.58x
- 理论与实际执行时间比例: 0.46x


## 任务分配统计

- 总任务数: 438
- 小模型执行任务数: 6
- 大模型执行任务数: 432
- 小模型任务占比: 1.37%
- 大模型任务占比: 98.63%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.131 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 17.457 秒

### 生成速度
- 小模型平均每秒生成token数: 0.82 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 31.34 tokens/s
- 总平均每秒生成token数: 32.17 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 18.61 | 0.0012 | 10 | 90.00% | 41.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 11.55 | 0.0007 | 5 | 80.00% | 18.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 13.30 | 0.0010 | 6 | 100.00% | 35.8 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 20.05 | 0.0013 | 10 | 30.00% | 19.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 13.66 | 0.0011 | 6 | 83.33% | 43.3 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 15.69 | 0.0016 | 8 | 87.50% | 36.2 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 14.85 | 0.0010 | 8 | 100.00% | 31.9 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 15.92 | 0.0013 | 7 | 71.43% | 22.1 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 17.17 | 0.0010 | 9 | 77.78% | 40.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 21.91 | 0.0014 | 10 | 50.00% | 28.0 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 18.59 | 0.0013 | 10 | 70.00% | 27.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 17.51 | 0.0013 | 9 | 66.67% | 18.9 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 16.08 | 0.0018 | 8 | 75.00% | 20.6 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 20.75 | 0.0022 | 10 | 100.00% | 34.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 21.34 | 0.0016 | 10 | 100.00% | 27.5 |
| 16 | Which of the following statements is a correct ... | ✗ | 12.76 | 0.0009 | 6 | 100.00% | 30.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 18.18 | 0.0012 | 10 | 80.00% | 34.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 19.82 | 0.0020 | 10 | 60.00% | 36.5 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 18.20 | 0.0021 | 9 | 66.67% | 23.9 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 20.34 | 0.0017 | 10 | 30.00% | 26.5 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 18.25 | 0.0012 | 10 | 100.00% | 46.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 15.40 | 0.0014 | 8 | 75.00% | 25.6 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 14.79 | 0.0014 | 7 | 57.14% | 15.7 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 16.81 | 0.0015 | 10 | 70.00% | 21.5 |
| 25 | Astronomers are studying two binary star system... | ✗ | 19.19 | 0.0018 | 9 | 77.78% | 35.6 |
| 26 | The experimental proof for the chromosomal theo... | ✓ | 17.08 | 0.0011 | 10 | 100.00% | 21.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 15.05 | 0.0009 | 6 | 100.00% | 15.8 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 18.17 | 0.0015 | 10 | 100.00% | 35.5 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 16.36 | 0.0012 | 9 | 88.89% | 26.7 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 16.53 | 0.0012 | 10 | 60.00% | 20.0 |
| 31 | All the following statements about the molecula... | ✗ | 19.44 | 0.0012 | 10 | 60.00% | 41.0 |
| 32 | You are interested in studying a rare type of b... | ✓ | 18.64 | 0.0011 | 9 | 88.89% | 32.8 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 17.57 | 0.0011 | 10 | 90.00% | 18.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 19.00 | 0.0012 | 10 | 90.00% | 17.5 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 18.37 | 0.0015 | 10 | 100.00% | 22.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 19.48 | 0.0013 | 10 | 90.00% | 52.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 19.08 | 0.0016 | 8 | 100.00% | 43.8 |
| 38 | Identify the final product produced when cyclob... | ✗ | 18.95 | 0.0010 | 10 | 90.00% | 30.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 19.19 | 0.0015 | 10 | 50.00% | 21.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 17.06 | 0.0011 | 9 | 100.00% | 28.9 |
| 41 | How many of the following compounds will exhibi... | ✗ | 22.18 | 0.0015 | 10 | 30.00% | 22.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 16.01 | 0.0014 | 7 | 100.00% | 23.6 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 8.92 | 0.0005 | 3 | 100.00% | 40.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✗ | 24.30 | 0.0013 | 10 | 90.00% | 36.5 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 19.77 | 0.0017 | 9 | 66.67% | 32.2 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 16.34 | 0.0021 | 7 | 100.00% | 29.3 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 24.23 | 0.0033 | 10 | 80.00% | 23.0 |
| 48 | Which of the following statements about enhance... | ✗ | 19.39 | 0.0011 | 10 | 100.00% | 52.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 14.01 | 0.0011 | 6 | 66.67% | 22.5 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 20.47 | 0.0014 | 10 | 60.00% | 21.0 |
