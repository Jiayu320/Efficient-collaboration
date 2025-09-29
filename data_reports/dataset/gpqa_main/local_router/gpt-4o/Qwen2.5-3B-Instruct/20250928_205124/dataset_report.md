# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 6
- 准确率: 12.00%
- 平均执行时间: 37.07 秒
- 平均成本: $0.0112

## 任务规划指标

- 平均任务步骤数: 4.60
- 平均压缩比例: 81.73%
- 平均每步骤Token限制: 59.36 tokens

## 理论性能指标

- 平均理论执行时间: 5.334 秒
- 平均顺序执行时间: 12.397 秒
- 平均并行加速比: 2.35x
- 理论与实际执行时间比例: 0.14x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.543 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 27.084 秒

### 生成速度
- 小模型平均每秒生成token数: 1.65 tokens/s
- 大模型平均每秒生成token数: 14.32 tokens/s
- 路由模型平均每秒生成token数: 33.81 tokens/s
- 总平均每秒生成token数: 49.78 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 32.64 | 0.0106 | 4 | 100.00% | 55.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 39.64 | 0.0051 | 4 | 100.00% | 47.5 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 45.19 | 0.0027 | 4 | 100.00% | 40.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 52.24 | 0.0201 | 9 | 22.22% | 60.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 45.78 | 0.0130 | 5 | 80.00% | 62.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 40.11 | 0.0155 | 4 | 100.00% | 72.5 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 37.74 | 0.0142 | 5 | 100.00% | 70.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 32.86 | 0.0078 | 4 | 75.00% | 50.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 38.61 | 0.0072 | 4 | 100.00% | 50.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 33.55 | 0.0155 | 5 | 60.00% | 74.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 32.24 | 0.0141 | 5 | 80.00% | 60.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 33.82 | 0.0096 | 5 | 80.00% | 50.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 41.22 | 0.0148 | 4 | 100.00% | 57.5 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 40.68 | 0.0121 | 3 | 100.00% | 73.3 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 32.66 | 0.0095 | 4 | 100.00% | 50.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 32.29 | 0.0121 | 4 | 100.00% | 67.5 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 34.68 | 0.0063 | 3 | 100.00% | 43.3 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 33.31 | 0.0180 | 5 | 100.00% | 66.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 40.47 | 0.0078 | 7 | 57.14% | 37.1 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 36.80 | 0.0283 | 9 | 33.33% | 87.8 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 24.09 | 0.0070 | 3 | 100.00% | 80.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 36.33 | 0.0058 | 4 | 100.00% | 37.5 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 23.49 | 0.0036 | 2 | 50.00% | 45.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 31.46 | 0.0091 | 3 | 66.67% | 63.3 |
| 25 | Astronomers are studying two binary star system... | ✗ | 70.86 | 0.0077 | 3 | 100.00% | 56.7 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 43.55 | 0.0047 | 3 | 100.00% | 56.7 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 35.21 | 0.0045 | 4 | 100.00% | 45.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 28.07 | 0.0117 | 4 | 75.00% | 82.5 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 30.64 | 0.0146 | 5 | 60.00% | 72.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 28.73 | 0.0111 | 4 | 50.00% | 65.0 |
| 31 | All the following statements about the molecula... | ✗ | 36.50 | 0.0111 | 7 | 42.86% | 47.1 |
| 32 | You are interested in studying a rare type of b... | ✗ | 28.58 | 0.0076 | 3 | 100.00% | 80.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 37.97 | 0.0091 | 3 | 100.00% | 60.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 35.74 | 0.0021 | 4 | 75.00% | 27.5 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 33.62 | 0.0154 | 5 | 100.00% | 72.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 26.00 | 0.0071 | 3 | 100.00% | 63.3 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 36.50 | 0.0126 | 5 | 80.00% | 60.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 33.44 | 0.0120 | 5 | 100.00% | 66.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 52.86 | 0.0151 | 6 | 83.33% | 53.3 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 33.60 | 0.0079 | 3 | 100.00% | 60.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 63.08 | 0.0185 | 8 | 25.00% | 67.5 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 35.02 | 0.0107 | 4 | 50.00% | 72.5 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 27.22 | 0.0041 | 2 | 100.00% | 65.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 28.11 | 0.0105 | 4 | 100.00% | 70.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 36.81 | 0.0106 | 4 | 75.00% | 50.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 31.49 | 0.0107 | 3 | 100.00% | 70.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 52.33 | 0.0077 | 6 | 50.00% | 41.7 |
| 48 | Which of the following statements about enhance... | ✗ | 27.65 | 0.0073 | 4 | 100.00% | 55.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 52.79 | 0.0417 | 14 | 35.71% | 45.7 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 35.49 | 0.0159 | 5 | 80.00% | 64.0 |
