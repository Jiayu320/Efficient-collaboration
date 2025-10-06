# 单模型数据集处理报告

## 模型信息

- 模型: qwen2.5-3b-instruct
- 延迟 (TTFT): 0.690 秒
- 吞吐量: 64.53 tokens/s

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 100
- 超时问题数: 0 (0.00%)
- 有效问题数: 100
- 正确数量: 24
- 准确率(有效问题): 24.00%
- 平均执行时间(有效问题): 53.74 秒
- 平均理论时间(有效问题): 10.26 秒
- 实际/理论时间比率: 5.24x
- 平均成本(有效问题): $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 1.419 秒
- 平均每秒生成token数: 11.87 tokens/s
- 理论每秒生成token数: 64.53 tokens/s
- 实际/理论吞吐量比率: 0.18x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 35.84 | 5.01 | 0.0000 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 44.57 | 12.03 | 0.0000 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 31.65 | 5.88 | 0.0000 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 73.40 | 12.30 | 0.0000 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 45.84 | 8.95 | 0.0000 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 79.40 | 15.71 | 0.0000 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 60.09 | 12.19 | 0.0000 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 76.11 | 17.13 | 0.0000 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 43.40 | 7.80 | 0.0000 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 72.21 | 10.42 | 0.0000 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 39.59 | 7.65 | 0.0000 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 98.49 | 12.95 | 0.0000 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 71.18 | 16.19 | 0.0000 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 64.53 | 11.12 | 0.0000 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 42.15 | 5.12 | 0.0000 |
| 16 | Which of the following statements is a correct ... | ✗ | 38.71 | 8.36 | 0.0000 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 87.41 | 19.55 | 0.0000 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 37.92 | 8.38 | 0.0000 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 82.55 | 17.10 | 0.0000 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 60.99 | 10.48 | 0.0000 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 30.37 | 5.66 | 0.0000 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 117.27 | 17.13 | 0.0000 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 115.46 | 18.31 | 0.0000 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 61.70 | 10.13 | 0.0000 |
| 25 | Astronomers are studying two binary star system... | ✗ | 95.77 | 16.28 | 0.0000 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 29.52 | 6.05 | 0.0000 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 40.20 | 7.23 | 0.0000 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 38.51 | 6.04 | 0.0000 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 46.21 | 9.15 | 0.0000 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 67.67 | 12.95 | 0.0000 |
| 31 | All the following statements about the molecula... | ✗ | 41.94 | 6.11 | 0.0000 |
| 32 | You are interested in studying a rare type of b... | ✓ | 18.55 | 2.57 | 0.0000 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 148.50 | 20.08 | 0.0000 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 24.28 | 4.56 | 0.0000 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✓ | 79.07 | 11.40 | 0.0000 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 31.91 | 7.21 | 0.0000 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 33.88 | 8.11 | 0.0000 |
| 38 | Identify the final product produced when cyclob... | ✗ | 23.11 | 6.72 | 0.0000 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 79.55 | 17.60 | 0.0000 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 43.71 | 11.37 | 0.0000 |
| 41 | How many of the following compounds will exhibi... | ✗ | 41.97 | 8.61 | 0.0000 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 37.88 | 6.83 | 0.0000 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 8.61 | 2.05 | 0.0000 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 27.68 | 7.32 | 0.0000 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 67.15 | 17.61 | 0.0000 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 82.77 | 15.30 | 0.0000 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 56.62 | 13.61 | 0.0000 |
| 48 | Which of the following statements about enhance... | ✗ | 16.56 | 6.13 | 0.0000 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 53.77 | 9.77 | 0.0000 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 35.55 | 7.20 | 0.0000 |
| 51 | The Michael reaction is a chemical process in o... | ✓ | 42.77 | 9.69 | 0.0000 |
| 52 | A common approximation made in many-body nuclea... | ✓ | 42.85 | 8.78 | 0.0000 |
| 53 | Consider a uniformly charged metallic ring of r... | ✓ | 50.22 | 11.96 | 0.0000 |
| 54 | Compounds that have the same molecular formula ... | ✗ | 42.36 | 8.48 | 0.0000 |
| 55 | Calculate the amount of non-Gaussianity(nG) in ... | ✓ | 73.73 | 11.12 | 0.0000 |
| 56 | A series of experiments are conducted to unrave... | ✗ | 59.67 | 10.11 | 0.0000 |
| 57 | A student regrets that he fell asleep during a ... | ✗ | 30.45 | 6.04 | 0.0000 |
| 58 | In an experiment, a researcher reacted ((2,2-di... | ✗ | 48.06 | 10.11 | 0.0000 |
| 59 | If an equimolar mixture X of two liquids, which... | ✗ | 66.82 | 12.08 | 0.0000 |
| 60 | Which of the following issues are the most comm... | ✗ | 22.94 | 4.44 | 0.0000 |
| 61 | Name reactions in chemistry refer to a specific... | ✗ | 56.81 | 9.38 | 0.0000 |
| 62 | Enya and John are of normal phenotype but they ... | ✗ | 40.02 | 6.63 | 0.0000 |
| 63 | You want to cultivate a population of mouse emb... | ✗ | 35.77 | 6.89 | 0.0000 |
| 64 | Dienes are organic compounds with two adjacent ... | ✗ | 70.57 | 13.75 | 0.0000 |
| 65 | You are studying a nuclear decay which converts... | ✗ | 54.43 | 8.38 | 0.0000 |
| 66 | "Oh, I know you," the ribonucleoprotein particl... | ✓ | 25.14 | 7.14 | 0.0000 |
| 67 | A research group is investigating the productio... | ✓ | 35.37 | 8.35 | 0.0000 |
| 68 | S)-4-hydroxycyclohex-2-en-1-one is treated with... | ✓ | 36.44 | 10.10 | 0.0000 |
| 69 | You have prepared an unknown product with the c... | ✓ | 47.06 | 9.90 | 0.0000 |
| 70 | methyl 2-oxocyclohexane-1-carboxylate is heated... | ✗ | 41.58 | 9.01 | 0.0000 |
| 71 | A reaction of a liquid organic compound, which ... | ✓ | 48.09 | 8.10 | 0.0000 |
| 72 | You have an interesting drought-resistant culti... | ✗ | 55.76 | 12.92 | 0.0000 |
| 73 | A textile dye containing an extensively conjuga... | ✗ | 58.59 | 9.24 | 0.0000 |
| 74 | toluene is treated with nitric acid and sulfuri... | ✓ | 17.30 | 7.96 | 0.0000 |
| 75 | When 500 mL of PH3 is decomposed the total volu... | ✗ | 43.42 | 9.09 | 0.0000 |
| 76 | What is the parallax (in milliarcseconds) of a ... | ✗ | 42.57 | 7.31 | 0.0000 |
| 77 | What is the energy of the Relativistic Heavy Io... | ✗ | 94.81 | 15.38 | 0.0000 |
| 78 | An electron is in the spin state (3i, 4). Find ... | ✗ | 103.21 | 19.26 | 0.0000 |
| 79 | There are two spin 1/2 nuclei in a strong magne... | ✗ | 31.95 | 6.80 | 0.0000 |
| 80 | Suppose you are studying a system of three nucl... | ✗ | 44.53 | 8.02 | 0.0000 |
| 81 | Sirius is the brightest star in the sky. The te... | ✗ | 31.27 | 7.65 | 0.0000 |
| 82 | Consider an electromagnetic wave incident on an... | ✗ | 89.26 | 16.11 | 0.0000 |
| 83 | Identify the EXO product of the following [4+2]... | ✓ | 53.18 | 10.03 | 0.0000 |
| 84 | We mix 20 cm3 0.1 M CH₃COOH with 40 cm3 0.02 M ... | ✗ | 128.82 | 25.48 | 0.0000 |
| 85 | Suppose we have a depolarizing channel operatio... | ✗ | 51.96 | 11.75 | 0.0000 |
| 86 | In a quantum dialog protocol a 4-mode continuou... | ✗ | 68.86 | 11.97 | 0.0000 |
| 87 | ChIP-seq detected a highly significant binding ... | ✓ | 34.02 | 7.52 | 0.0000 |
| 88 | "1,2-Rearrangement reaction in which vicinal di... | ✓ | 53.53 | 11.69 | 0.0000 |
| 89 | Arrange given compounds (1. Acetophenone, 2. pr... | ✗ | 95.24 | 14.56 | 0.0000 |
| 90 | Ozonolysis of compound A produces 3-methylcyclo... | ✗ | 48.95 | 9.35 | 0.0000 |
| 91 | Consider the Y-component of the intrinsic angul... | ✓ | 45.77 | 11.94 | 0.0000 |
| 92 | You have a 10 uL aliquot of a 10 uM DNA templat... | ✗ | 74.87 | 10.84 | 0.0000 |
| 93 | Observations of structures located at a distanc... | ✗ | 22.44 | 5.04 | 0.0000 |
| 94 | Identify the number of 13C-NMR signals produced... | ✗ | 36.97 | 9.24 | 0.0000 |
| 95 | In autumn, tree leaves get colourful and drop d... | ✗ | 34.51 | 4.53 | 0.0000 |
| 96 | Substances 1-6 undergo an electrophilic substit... | ✗ | 40.97 | 9.34 | 0.0000 |
| 97 | Which of the following data sets corresponds to... | ✓ | 61.21 | 13.99 | 0.0000 |
| 98 | Consider a stack of N optical layers (made of a... | ✗ | 65.80 | 11.80 | 0.0000 |
| 99 | bicyclo[2.2.2]octan-2-one is irradiated with ul... | ✗ | 47.40 | 6.89 | 0.0000 |
| 100 | The water and oil contact angles on a smooth cl... | ✓ | 44.20 | 5.94 | 0.0000 |
