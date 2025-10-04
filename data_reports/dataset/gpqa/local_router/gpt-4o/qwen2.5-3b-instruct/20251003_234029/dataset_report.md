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
- 正确数量: 22
- 准确率: 44.00%
- 平均执行时间: 29.76 秒
- 平均成本: $0.0141

## 任务规划指标

- 平均任务步骤数: 4.98
- 平均压缩比例: 66.79%
- 平均每步骤Token限制: 75.24 tokens

## 理论性能指标

- 平均理论执行时间: 5.870 秒
- 平均顺序执行时间: 11.349 秒
- 平均并行加速比: 1.87x
- 理论与实际执行时间比例: 0.20x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.298 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 20.678 秒

### 生成速度
- 小模型平均每秒生成token数: 5.18 tokens/s
- 大模型平均每秒生成token数: 31.17 tokens/s
- 路由模型平均每秒生成token数: 15.76 tokens/s
- 总平均每秒生成token数: 52.12 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 12.92 | 0.0072 | 4 | 25.00% | 52.5 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 10.64 | 0.0093 | 2 | 100.00% | 25.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 15.31 | 0.0166 | 9 | 33.33% | 55.6 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 10.67 | 0.0102 | 8 | 12.50% | 50.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 22.72 | 0.0177 | 5 | 60.00% | 24.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 11.26 | 0.0156 | 3 | 66.67% | 53.3 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 21.57 | 0.0149 | 4 | 100.00% | 125.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 90.58 | 0.0271 | 5 | 60.00% | 40.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 32.36 | 0.0240 | 12 | 33.33% | 75.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 17.91 | 0.0159 | 6 | 33.33% | 66.7 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 32.19 | 0.0128 | 6 | 66.67% | 100.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✓ | 51.72 | 0.0173 | 5 | 80.00% | 40.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 107.38 | 0.0124 | 5 | 60.00% | 48.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 29.48 | 0.0309 | 6 | 100.00% | 75.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 32.67 | 0.0077 | 3 | 66.67% | 25.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 15.74 | 0.0138 | 5 | 100.00% | 134.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 15.62 | 0.0262 | 6 | 50.00% | 31.7 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 35.42 | 0.0148 | 6 | 66.67% | 18.3 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 203.59 | 0.0108 | 10 | 40.00% | 23.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 33.81 | 0.0206 | 9 | 33.33% | 160.0 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 7.14 | 0.0062 | 2 | 100.00% | 110.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 13.23 | 0.0209 | 5 | 60.00% | 120.0 |
| 23 | In the last few decades, reverberation mapping,... | ✓ | 76.49 | 0.0162 | 5 | 100.00% | 46.0 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 9.56 | 0.0127 | 3 | 66.67% | 166.7 |
| 25 | Astronomers are studying two binary star system... | ✓ | 24.05 | 0.0100 | 3 | 66.67% | 40.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 8.63 | 0.0074 | 2 | 100.00% | 225.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✓ | 14.98 | 0.0224 | 10 | 40.00% | 100.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 7.18 | 0.0066 | 4 | 25.00% | 30.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✓ | 12.92 | 0.0109 | 3 | 100.00% | 70.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 54.95 | 0.0079 | 4 | 25.00% | 10.0 |
| 31 | All the following statements about the molecula... | ✗ | 28.44 | 0.0113 | 5 | 100.00% | 28.0 |
| 32 | You are interested in studying a rare type of b... | ✓ | 14.40 | 0.0143 | 5 | 80.00% | 100.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 10.46 | 0.0048 | 1 | 100.00% | 100.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 7.34 | 0.0047 | 2 | 100.00% | 20.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✓ | 19.13 | 0.0166 | 4 | 100.00% | 100.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 28.77 | 0.0122 | 5 | 100.00% | 66.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 16.34 | 0.0079 | 2 | 100.00% | 65.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 23.22 | 0.0156 | 4 | 100.00% | 142.5 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 12.56 | 0.0129 | 2 | 50.00% | 300.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 30.93 | 0.0144 | 7 | 28.57% | 45.7 |
| 41 | How many of the following compounds will exhibi... | ✗ | 25.99 | 0.0174 | 12 | 16.67% | 36.7 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 15.72 | 0.0159 | 5 | 60.00% | 154.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 5.53 | 0.0032 | 1 | 100.00% | 100.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 22.62 | 0.0164 | 6 | 66.67% | 56.7 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 50.96 | 0.0108 | 3 | 66.67% | 46.7 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 31.35 | 0.0054 | 2 | 100.00% | 50.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 20.21 | 0.0272 | 4 | 50.00% | 60.0 |
| 48 | Which of the following statements about enhance... | ✗ | 10.08 | 0.0090 | 4 | 25.00% | 55.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 16.00 | 0.0169 | 3 | 66.67% | 46.7 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 65.28 | 0.0232 | 12 | 58.33% | 49.2 |
