# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 50
- 正确数量: 18
- 准确率: 36.00%
- 平均执行时间: 35.84 秒
- 平均成本: $0.0132

## 任务规划指标

- 平均任务步骤数: 4.32
- 平均压缩比例: 70.53%
- 平均每步骤Token限制: 67.21 tokens

## 理论性能指标

- 平均理论执行时间: 5.375 秒
- 平均顺序执行时间: 9.708 秒
- 平均并行加速比: 1.79x
- 理论与实际执行时间比例: 0.15x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.438 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 26.684 秒

### 生成速度
- 小模型平均每秒生成token数: 6.25 tokens/s
- 大模型平均每秒生成token数: 28.82 tokens/s
- 路由模型平均每秒生成token数: 11.88 tokens/s
- 总平均每秒生成token数: 46.95 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 17.01 | 0.0126 | 4 | 100.00% | 137.5 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 11.22 | 0.0108 | 2 | 100.00% | 75.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 22.57 | 0.0077 | 4 | 100.00% | 57.5 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 16.27 | 0.0146 | 3 | 100.00% | 53.3 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 37.55 | 0.0116 | 5 | 60.00% | 22.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 13.00 | 0.0154 | 3 | 66.67% | 60.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 10.09 | 0.0085 | 2 | 100.00% | 150.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 95.51 | 0.0167 | 5 | 40.00% | 38.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 96.73 | 0.0063 | 5 | 100.00% | 42.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 26.51 | 0.0165 | 6 | 50.00% | 56.7 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 19.34 | 0.0108 | 5 | 40.00% | 62.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 58.11 | 0.0176 | 5 | 100.00% | 48.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 26.63 | 0.0282 | 5 | 100.00% | 66.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 20.23 | 0.0225 | 4 | 75.00% | 95.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 50.30 | 0.0068 | 3 | 66.67% | 43.3 |
| 16 | Which of the following statements is a correct ... | ✓ | 22.31 | 0.0337 | 7 | 57.14% | 242.9 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 95.33 | 0.0149 | 4 | 100.00% | 60.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 14.14 | 0.0134 | 8 | 37.50% | 41.2 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✓ | 194.00 | 0.0097 | 5 | 100.00% | 28.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 39.76 | 0.0062 | 4 | 25.00% | 42.5 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 8.11 | 0.0043 | 1 | 100.00% | 200.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 31.38 | 0.0341 | 7 | 42.86% | 64.3 |
| 23 | In the last few decades, reverberation mapping,... | ✓ | 31.65 | 0.0104 | 4 | 75.00% | 37.5 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 10.80 | 0.0154 | 3 | 66.67% | 56.7 |
| 25 | Astronomers are studying two binary star system... | ✗ | 89.44 | 0.0170 | 5 | 40.00% | 32.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 11.77 | 0.0091 | 3 | 100.00% | 123.3 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 35.56 | 0.0064 | 4 | 25.00% | 20.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 8.86 | 0.0066 | 4 | 25.00% | 50.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✓ | 12.09 | 0.0071 | 3 | 100.00% | 60.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 52.19 | 0.0045 | 5 | 40.00% | 10.0 |
| 31 | All the following statements about the molecula... | ✗ | 8.33 | 0.0085 | 4 | 25.00% | 122.5 |
| 32 | You are interested in studying a rare type of b... | ✓ | 15.72 | 0.0120 | 5 | 100.00% | 56.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 10.78 | 0.0106 | 3 | 66.67% | 53.3 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 9.13 | 0.0099 | 3 | 66.67% | 26.7 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 43.39 | 0.0205 | 5 | 100.00% | 210.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 26.65 | 0.0061 | 2 | 100.00% | 45.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 66.45 | 0.0060 | 3 | 100.00% | 60.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 37.76 | 0.0110 | 4 | 100.00% | 60.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 65.50 | 0.0211 | 7 | 28.57% | 30.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 21.57 | 0.0044 | 4 | 25.00% | 10.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 62.62 | 0.0064 | 7 | 14.29% | 50.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 17.38 | 0.0202 | 9 | 22.22% | 57.8 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 10.09 | 0.0036 | 1 | 100.00% | 100.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 14.43 | 0.0093 | 3 | 100.00% | 123.3 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 32.60 | 0.0308 | 6 | 83.33% | 58.3 |
| 46 | What is the concentration of calcium ions in a ... | ✓ | 30.91 | 0.0108 | 2 | 100.00% | 35.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 60.48 | 0.0258 | 8 | 37.50% | 50.0 |
| 48 | Which of the following statements about enhance... | ✗ | 49.96 | 0.0086 | 3 | 100.00% | 30.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 8.29 | 0.0142 | 4 | 25.00% | 50.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 21.69 | 0.0209 | 5 | 100.00% | 58.0 |
