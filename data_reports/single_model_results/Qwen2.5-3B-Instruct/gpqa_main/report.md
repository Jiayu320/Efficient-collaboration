# 单模型数据集处理报告

## 模型信息

- 模型: Qwen/Qwen2.5-3B-Instruct
- 延迟 (TTFT): 0.690 秒
- 吞吐量: 64.53 tokens/s

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 100
- 超时问题数: 0 (0.00%)
- 有效问题数: 100
- 正确数量: 6
- 准确率(有效问题): 6.00%
- 平均执行时间(有效问题): 17.34 秒
- 平均理论时间(有效问题): 11.09 秒
- 实际/理论时间比率: 1.56x
- 平均成本(有效问题): $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 0.121 秒
- 平均每秒生成token数: 38.70 tokens/s
- 理论每秒生成token数: 64.53 tokens/s
- 实际/理论吞吐量比率: 0.60x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 12.62 | 8.35 | 0.0000 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 16.62 | 11.21 | 0.0000 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 12.55 | 8.61 | 0.0000 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 21.07 | 15.41 | 0.0000 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 21.72 | 14.44 | 0.0000 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 19.65 | 13.89 | 0.0000 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 14.97 | 10.28 | 0.0000 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 21.72 | 15.01 | 0.0000 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 13.31 | 8.10 | 0.0000 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 12.83 | 8.62 | 0.0000 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 20.27 | 13.04 | 0.0000 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 21.67 | 14.36 | 0.0000 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 21.61 | 13.69 | 0.0000 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 21.79 | 15.81 | 0.0000 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 12.81 | 9.12 | 0.0000 |
| 16 | Which of the following statements is a correct ... | ✗ | 12.92 | 8.67 | 0.0000 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 21.95 | 14.36 | 0.0000 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 14.01 | 9.83 | 0.0000 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 21.94 | 14.39 | 0.0000 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 13.99 | 9.71 | 0.0000 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 14.95 | 10.86 | 0.0000 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 21.81 | 15.24 | 0.0000 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 21.74 | 14.08 | 0.0000 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 13.35 | 9.41 | 0.0000 |
| 25 | Astronomers are studying two binary star system... | ✗ | 19.61 | 13.71 | 0.0000 |
| 26 | The experimental proof for the chromosomal theo... | ✓ | 7.43 | 4.83 | 0.0000 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✓ | 16.25 | 8.22 | 0.0000 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 12.02 | 7.66 | 0.0000 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 12.45 | 7.93 | 0.0000 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 21.59 | 14.79 | 0.0000 |
| 31 | All the following statements about the molecula... | ✗ | 9.56 | 6.42 | 0.0000 |
| 32 | You are interested in studying a rare type of b... | ✗ | 15.88 | 10.92 | 0.0000 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 22.13 | 14.44 | 0.0000 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 19.40 | 12.92 | 0.0000 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 22.05 | 15.74 | 0.0000 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 10.01 | 6.63 | 0.0000 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 20.24 | 14.33 | 0.0000 |
| 38 | Identify the final product produced when cyclob... | ✗ | 11.37 | 7.80 | 0.0000 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 17.31 | 12.37 | 0.0000 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 13.41 | 9.49 | 0.0000 |
| 41 | How many of the following compounds will exhibi... | ✗ | 14.66 | 10.20 | 0.0000 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 13.89 | 9.69 | 0.0000 |
| 43 | A paper you are reading about the seesaw mechan... | ✗ | 6.41 | 3.73 | 0.0000 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 11.93 | 8.22 | 0.0000 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 16.37 | 11.00 | 0.0000 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 21.98 | 14.87 | 0.0000 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 22.35 | 14.96 | 0.0000 |
| 48 | Which of the following statements about enhance... | ✗ | 12.61 | 8.64 | 0.0000 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 23.65 | 15.01 | 0.0000 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 15.97 | 10.67 | 0.0000 |
| 51 | The Michael reaction is a chemical process in o... | ✗ | 17.56 | 11.83 | 0.0000 |
| 52 | A common approximation made in many-body nuclea... | ✗ | 12.13 | 8.50 | 0.0000 |
| 53 | Consider a uniformly charged metallic ring of r... | ✓ | 16.85 | 10.86 | 0.0000 |
| 54 | Compounds that have the same molecular formula ... | ✗ | 12.56 | 8.13 | 0.0000 |
| 55 | Calculate the amount of non-Gaussianity(nG) in ... | ✗ | 22.17 | 15.29 | 0.0000 |
| 56 | A series of experiments are conducted to unrave... | ✗ | 15.13 | 10.48 | 0.0000 |
| 57 | A student regrets that he fell asleep during a ... | ✗ | 10.69 | 6.90 | 0.0000 |
| 58 | In an experiment, a researcher reacted ((2,2-di... | ✗ | 13.20 | 8.83 | 0.0000 |
| 59 | If an equimolar mixture X of two liquids, which... | ✗ | 20.96 | 13.30 | 0.0000 |
| 60 | Which of the following issues are the most comm... | ✗ | 12.75 | 8.59 | 0.0000 |
| 61 | Name reactions in chemistry refer to a specific... | ✗ | 18.66 | 10.47 | 0.0000 |
| 62 | Enya and John are of normal phenotype but they ... | ✗ | 12.51 | 7.65 | 0.0000 |
| 63 | You want to cultivate a population of mouse emb... | ✗ | 24.91 | 9.83 | 0.0000 |
| 64 | Dienes are organic compounds with two adjacent ... | ✗ | 20.21 | 13.12 | 0.0000 |
| 65 | You are studying a nuclear decay which converts... | ✗ | 18.93 | 12.24 | 0.0000 |
| 66 | "Oh, I know you," the ribonucleoprotein particl... | ✗ | 20.13 | 7.93 | 0.0000 |
| 67 | A research group is investigating the productio... | ✗ | 18.73 | 8.75 | 0.0000 |
| 68 | S)-4-hydroxycyclohex-2-en-1-one is treated with... | ✗ | 16.40 | 10.25 | 0.0000 |
| 69 | You have prepared an unknown product with the c... | ✗ | 19.68 | 12.67 | 0.0000 |
| 70 | methyl 2-oxocyclohexane-1-carboxylate is heated... | ✗ | 22.62 | 13.60 | 0.0000 |
| 71 | A reaction of a liquid organic compound, which ... | ✗ | 16.07 | 9.79 | 0.0000 |
| 72 | You have an interesting drought-resistant culti... | ✗ | 16.91 | 10.28 | 0.0000 |
| 73 | A textile dye containing an extensively conjuga... | ✓ | 14.88 | 8.98 | 0.0000 |
| 74 | toluene is treated with nitric acid and sulfuri... | ✗ | 23.46 | 9.91 | 0.0000 |
| 75 | When 500 mL of PH3 is decomposed the total volu... | ✗ | 15.22 | 8.86 | 0.0000 |
| 76 | What is the parallax (in milliarcseconds) of a ... | ✗ | 19.23 | 12.72 | 0.0000 |
| 77 | What is the energy of the Relativistic Heavy Io... | ✗ | 21.90 | 13.82 | 0.0000 |
| 78 | An electron is in the spin state (3i, 4). Find ... | ✗ | 14.41 | 9.32 | 0.0000 |
| 79 | There are two spin 1/2 nuclei in a strong magne... | ✗ | 30.51 | 15.60 | 0.0000 |
| 80 | Suppose you are studying a system of three nucl... | ✓ | 15.90 | 10.50 | 0.0000 |
| 81 | Sirius is the brightest star in the sky. The te... | ✗ | 19.49 | 12.76 | 0.0000 |
| 82 | Consider an electromagnetic wave incident on an... | ✗ | 22.00 | 15.35 | 0.0000 |
| 83 | Identify the EXO product of the following [4+2]... | ✗ | 13.53 | 7.71 | 0.0000 |
| 84 | We mix 20 cm3 0.1 M CH₃COOH with 40 cm3 0.02 M ... | ✗ | 26.45 | 14.30 | 0.0000 |
| 85 | Suppose we have a depolarizing channel operatio... | ✗ | 22.22 | 15.27 | 0.0000 |
| 86 | In a quantum dialog protocol a 4-mode continuou... | ✗ | 21.33 | 14.28 | 0.0000 |
| 87 | ChIP-seq detected a highly significant binding ... | ✗ | 14.89 | 9.12 | 0.0000 |
| 88 | "1,2-Rearrangement reaction in which vicinal di... | ✗ | 23.75 | 15.43 | 0.0000 |
| 89 | Arrange given compounds (1. Acetophenone, 2. pr... | ✗ | 19.11 | 11.32 | 0.0000 |
| 90 | Ozonolysis of compound A produces 3-methylcyclo... | ✗ | 16.95 | 11.12 | 0.0000 |
| 91 | Consider the Y-component of the intrinsic angul... | ✗ | 23.40 | 14.17 | 0.0000 |
| 92 | You have a 10 uL aliquot of a 10 uM DNA templat... | ✗ | 16.51 | 9.85 | 0.0000 |
| 93 | Observations of structures located at a distanc... | ✗ | 20.59 | 14.20 | 0.0000 |
| 94 | Identify the number of 13C-NMR signals produced... | ✗ | 15.84 | 10.45 | 0.0000 |
| 95 | In autumn, tree leaves get colourful and drop d... | ✗ | 16.42 | 6.61 | 0.0000 |
| 96 | Substances 1-6 undergo an electrophilic substit... | ✗ | 12.35 | 7.79 | 0.0000 |
| 97 | Which of the following data sets corresponds to... | ✗ | 19.49 | 11.94 | 0.0000 |
| 98 | Consider a stack of N optical layers (made of a... | ✗ | 18.52 | 13.15 | 0.0000 |
| 99 | bicyclo[2.2.2]octan-2-one is irradiated with ul... | ✗ | 14.87 | 8.78 | 0.0000 |
| 100 | The water and oil contact angles on a smooth cl... | ✗ | 8.63 | 5.04 | 0.0000 |
