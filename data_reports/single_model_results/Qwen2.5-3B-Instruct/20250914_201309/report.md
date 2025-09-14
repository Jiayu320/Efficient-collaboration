# 单模型数据集处理报告

## 模型信息

- 模型: Qwen/Qwen2.5-3B-Instruct
- 延迟 (TTFT): 0.690 秒
- 吞吐量: 64.53 tokens/s

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 超时问题数: 0 (0.00%)
- 有效问题数: 50
- 正确数量: 4
- 准确率(有效问题): 8.00%
- 平均执行时间(有效问题): 16.35 秒
- 平均理论时间(有效问题): 10.83 秒
- 实际/理论时间比率: 1.51x
- 平均成本(有效问题): $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 0.152 秒
- 平均每秒生成token数: 39.65 tokens/s
- 理论每秒生成token数: 64.53 tokens/s
- 实际/理论吞吐量比率: 0.61x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 9.61 | 6.07 | 0.0000 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 24.69 | 14.22 | 0.0000 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 15.06 | 10.42 | 0.0000 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 18.27 | 11.09 | 0.0000 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 14.60 | 9.32 | 0.0000 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 20.52 | 13.68 | 0.0000 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 18.23 | 12.68 | 0.0000 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 21.74 | 14.81 | 0.0000 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 18.96 | 13.40 | 0.0000 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 14.49 | 9.06 | 0.0000 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 14.11 | 9.71 | 0.0000 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 21.78 | 14.98 | 0.0000 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 18.01 | 11.29 | 0.0000 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 22.10 | 15.38 | 0.0000 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 12.46 | 8.17 | 0.0000 |
| 16 | Which of the following statements is a correct ... | ✓ | 18.58 | 12.05 | 0.0000 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 18.67 | 12.44 | 0.0000 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 15.09 | 10.08 | 0.0000 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 22.24 | 14.87 | 0.0000 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 11.70 | 7.65 | 0.0000 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 13.15 | 8.83 | 0.0000 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 22.41 | 14.78 | 0.0000 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 22.07 | 14.36 | 0.0000 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 11.42 | 7.51 | 0.0000 |
| 25 | Astronomers are studying two binary star system... | ✗ | 22.76 | 15.49 | 0.0000 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 9.11 | 5.82 | 0.0000 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 9.41 | 5.00 | 0.0000 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 11.51 | 7.51 | 0.0000 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 10.27 | 6.61 | 0.0000 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 15.37 | 10.84 | 0.0000 |
| 31 | All the following statements about the molecula... | ✗ | 12.88 | 8.61 | 0.0000 |
| 32 | You are interested in studying a rare type of b... | ✗ | 21.49 | 14.92 | 0.0000 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 21.98 | 14.76 | 0.0000 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 19.75 | 12.92 | 0.0000 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 16.17 | 10.61 | 0.0000 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 13.97 | 10.11 | 0.0000 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 17.97 | 12.58 | 0.0000 |
| 38 | Identify the final product produced when cyclob... | ✗ | 12.59 | 7.83 | 0.0000 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 10.27 | 6.73 | 0.0000 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 12.95 | 8.78 | 0.0000 |
| 41 | How many of the following compounds will exhibi... | ✗ | 16.15 | 11.09 | 0.0000 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 12.96 | 8.64 | 0.0000 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 8.81 | 5.80 | 0.0000 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 13.00 | 8.59 | 0.0000 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 22.19 | 15.26 | 0.0000 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 21.06 | 14.20 | 0.0000 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✓ | 21.07 | 14.28 | 0.0000 |
| 48 | Which of the following statements about enhance... | ✗ | 10.93 | 6.89 | 0.0000 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 18.57 | 11.54 | 0.0000 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 14.36 | 9.43 | 0.0000 |
