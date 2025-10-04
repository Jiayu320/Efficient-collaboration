# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-0.6b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 50
- 正确数量: 24
- 准确率: 48.00%
- 平均执行时间: 12.16 秒
- 平均成本: $0.0046

## 任务规划指标

- 平均任务步骤数: 2.20
- 平均压缩比例: 80.75%
- 平均每步骤Token限制: 44.73 tokens

## 理论性能指标

- 平均理论执行时间: 2.854 秒
- 平均顺序执行时间: 4.059 秒
- 平均并行加速比: 1.32x
- 理论与实际执行时间比例: 0.23x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.216 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 7.513 秒

### 生成速度
- 小模型平均每秒生成token数: 2.82 tokens/s
- 大模型平均每秒生成token数: 39.01 tokens/s
- 路由模型平均每秒生成token数: 8.58 tokens/s
- 总平均每秒生成token数: 50.42 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 10.20 | 0.0018 | 1 | 100.00% | 15.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 8.60 | 0.0049 | 2 | 100.00% | 35.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 11.25 | 0.0026 | 1 | 100.00% | 12.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 10.86 | 0.0055 | 1 | 100.00% | 90.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 9.07 | 0.0031 | 1 | 100.00% | 80.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 11.17 | 0.0153 | 3 | 33.33% | 76.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 10.60 | 0.0034 | 1 | 100.00% | 10.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 8.62 | 0.0044 | 1 | 100.00% | 20.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 5.82 | 0.0000 | 3 | 100.00% | 11.7 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 2.26 | 0.0000 | 2 | 50.00% | 275.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 5.00 | 0.0009 | 1 | 100.00% | 20.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 6.18 | 0.0038 | 1 | 100.00% | 40.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 8.41 | 0.0151 | 3 | 33.33% | 80.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✓ | 53.71 | 0.0109 | 4 | 25.00% | 11.2 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 8.83 | 0.0015 | 3 | 100.00% | 86.7 |
| 16 | Which of the following statements is a correct ... | ✓ | 11.03 | 0.0006 | 2 | 100.00% | 80.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 8.60 | 0.0099 | 2 | 50.00% | 27.5 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 5.87 | 0.0035 | 1 | 100.00% | 20.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✓ | 18.54 | 0.0058 | 8 | 62.50% | 30.6 |
| 20 | which of the following molecules has c3h symmet... | ✓ | 15.26 | 0.0043 | 1 | 100.00% | 50.0 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 6.24 | 0.0023 | 3 | 33.33% | 12.3 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 14.86 | 0.0047 | 1 | 100.00% | 20.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 8.44 | 0.0168 | 4 | 25.00% | 45.0 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 10.49 | 0.0079 | 2 | 100.00% | 20.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 8.15 | 0.0172 | 3 | 33.33% | 10.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 27.81 | 0.0017 | 4 | 25.00% | 12.5 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 13.66 | 0.0035 | 1 | 100.00% | 50.0 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 5.81 | 0.0030 | 1 | 100.00% | 15.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 24.69 | 0.0007 | 3 | 66.67% | 18.3 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 9.23 | 0.0013 | 2 | 100.00% | 60.0 |
| 31 | All the following statements about the molecula... | ✗ | 21.21 | 0.0012 | 4 | 50.00% | 17.5 |
| 32 | You are interested in studying a rare type of b... | ✓ | 9.10 | 0.0043 | 4 | 100.00% | 20.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✓ | 17.56 | 0.0002 | 4 | 75.00% | 25.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 17.90 | 0.0081 | 4 | 25.00% | 28.2 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 12.01 | 0.0042 | 1 | 100.00% | 30.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 20.87 | 0.0018 | 2 | 100.00% | 10.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 8.76 | 0.0025 | 1 | 100.00% | 30.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 13.66 | 0.0046 | 2 | 50.00% | 13.0 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 16.00 | 0.0149 | 4 | 50.00% | 287.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 37.76 | 0.0070 | 4 | 75.00% | 112.5 |
| 41 | How many of the following compounds will exhibi... | ✗ | 10.47 | 0.0047 | 1 | 100.00% | 8.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 9.23 | 0.0062 | 2 | 50.00% | 35.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 3.50 | 0.0003 | 1 | 100.00% | 20.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 5.00 | 0.0003 | 1 | 100.00% | 20.0 |
| 45 | Consider the extension of the Standard Model gi... | ✓ | 3.01 | 0.0000 | 4 | 25.00% | 126.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 14.00 | 0.0053 | 1 | 100.00% | 10.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 2.29 | 0.0000 | 1 | 200.00% | 30.0 |
| 48 | Which of the following statements about enhance... | ✗ | 6.94 | 0.0007 | 1 | 100.00% | 20.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 9.52 | 0.0022 | 1 | 100.00% | 20.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 10.02 | 0.0044 | 1 | 100.00% | 40.0 |
