# 单模型数据集处理报告

## 模型信息

- 模型: gpt-4.1-mini
- 延迟 (TTFT): 0.700 秒
- 吞吐量: 69.59 tokens/s

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 50
- 超时问题数: 0 (0.00%)
- 有效问题数: 50
- 正确数量: 28
- 准确率(有效问题): 56.00%
- 平均执行时间(有效问题): 16.03 秒
- 平均理论时间(有效问题): 12.64 秒
- 实际/理论时间比率: 1.27x
- 平均成本(有效问题): $0.0014

## 性能指标

- 平均首个令牌响应时间 (TTFT): 5.678 秒
- 平均每秒生成token数: 50.42 tokens/s
- 理论每秒生成token数: 69.59 tokens/s
- 实际/理论吞吐量比率: 0.72x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 8.27 | 7.63 | 0.0008 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 12.74 | 11.06 | 0.0012 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 12.97 | 9.14 | 0.0010 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 21.34 | 17.96 | 0.0020 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 24.47 | 23.10 | 0.0026 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 24.17 | 20.75 | 0.0023 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 26.14 | 20.08 | 0.0022 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 15.60 | 12.50 | 0.0014 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 9.50 | 5.96 | 0.0006 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✓ | 9.34 | 8.13 | 0.0010 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 12.26 | 7.66 | 0.0008 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 23.24 | 16.05 | 0.0018 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 24.53 | 19.41 | 0.0022 |
| 14 | A quantum mechanical particle of mass m moves i... | ✓ | 18.66 | 12.22 | 0.0013 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 11.54 | 8.26 | 0.0009 |
| 16 | Which of the following statements is a correct ... | ✓ | 10.29 | 6.63 | 0.0007 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 19.43 | 12.30 | 0.0013 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 15.72 | 17.33 | 0.0020 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 34.06 | 21.81 | 0.0024 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 15.55 | 9.58 | 0.0011 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 12.45 | 8.82 | 0.0010 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 15.88 | 16.58 | 0.0019 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 13.75 | 10.28 | 0.0011 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 15.06 | 9.88 | 0.0011 |
| 25 | Astronomers are studying two binary star system... | ✓ | 24.22 | 19.68 | 0.0022 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 6.96 | 4.16 | 0.0005 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✓ | 28.94 | 25.40 | 0.0031 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 16.01 | 13.10 | 0.0015 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 16.48 | 11.81 | 0.0013 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 12.50 | 7.44 | 0.0008 |
| 31 | All the following statements about the molecula... | ✗ | 16.93 | 10.03 | 0.0012 |
| 32 | You are interested in studying a rare type of b... | ✓ | 10.51 | 6.42 | 0.0007 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✓ | 14.67 | 14.42 | 0.0016 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 11.13 | 6.75 | 0.0007 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 24.70 | 22.60 | 0.0025 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 10.33 | 8.09 | 0.0009 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 28.53 | 24.41 | 0.0027 |
| 38 | Identify the final product produced when cyclob... | ✗ | 17.10 | 14.65 | 0.0016 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 15.98 | 14.78 | 0.0017 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 14.75 | 9.71 | 0.0011 |
| 41 | How many of the following compounds will exhibi... | ✗ | 17.29 | 16.42 | 0.0018 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 14.95 | 11.79 | 0.0013 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 7.94 | 3.62 | 0.0004 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 6.85 | 4.78 | 0.0005 |
| 45 | Consider the extension of the Standard Model gi... | ✓ | 13.86 | 16.02 | 0.0020 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 14.58 | 9.68 | 0.0010 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 20.92 | 21.00 | 0.0023 |
| 48 | Which of the following statements about enhance... | ✗ | 7.89 | 8.03 | 0.0009 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 7.70 | 5.14 | 0.0006 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 12.95 | 8.92 | 0.0010 |
