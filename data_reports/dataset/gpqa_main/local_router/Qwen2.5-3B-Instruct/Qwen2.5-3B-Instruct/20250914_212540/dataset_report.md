# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: Qwen/Qwen2.5-3B-Instruct
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 100
- 正确数量: 5
- 准确率: 5.00%
- 平均执行时间: 8.76 秒
- 平均成本: $0.0000

## 任务规划指标

- 平均任务步骤数: 7.90
- 平均压缩比例: 66.16%
- 平均每步骤Token限制: 33.12 tokens

## 理论性能指标

- 平均理论执行时间: 7.933 秒
- 平均顺序执行时间: 21.088 秒
- 平均并行加速比: 2.70x
- 理论与实际执行时间比例: 0.91x


## 任务分配统计

- 总任务数: 782
- 小模型执行任务数: 19
- 大模型执行任务数: 763
- 小模型任务占比: 2.43%
- 大模型任务占比: 97.57%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.113 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 8.481 秒

### 生成速度
- 小模型平均每秒生成token数: 3.59 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 50.68 tokens/s
- 总平均每秒生成token数: 54.27 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 7.20 | 0.0000 | 5 | 60.00% | 36.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 8.56 | 0.0000 | 8 | 75.00% | 28.8 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 5.62 | 0.0000 | 4 | 100.00% | 28.8 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 9.93 | 0.0000 | 10 | 30.00% | 25.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 8.74 | 0.0000 | 8 | 62.50% | 28.1 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 8.37 | 0.0000 | 5 | 80.00% | 37.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 6.46 | 0.0000 | 6 | 83.33% | 31.7 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 7.45 | 0.0000 | 7 | 71.43% | 40.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 7.88 | 0.0000 | 8 | 62.50% | 36.2 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 9.50 | 0.0000 | 9 | 33.33% | 37.8 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 8.78 | 0.0000 | 9 | 66.67% | 41.1 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 10.83 | 0.0000 | 9 | 66.67% | 27.2 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 7.03 | 0.0000 | 5 | 100.00% | 49.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 8.54 | 0.0000 | 7 | 85.71% | 30.7 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 10.59 | 0.0000 | 9 | 66.67% | 37.2 |
| 16 | Which of the following statements is a correct ... | ✗ | 8.31 | 0.0000 | 9 | 55.56% | 42.2 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 9.30 | 0.0000 | 9 | 66.67% | 25.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 8.95 | 0.0000 | 9 | 44.44% | 30.6 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 12.47 | 0.0000 | 9 | 55.56% | 28.9 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 9.85 | 0.0000 | 10 | 20.00% | 26.0 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 8.45 | 0.0000 | 8 | 75.00% | 38.8 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 7.84 | 0.0000 | 8 | 75.00% | 24.4 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 9.33 | 0.0000 | 7 | 42.86% | 25.7 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 7.86 | 0.0000 | 8 | 62.50% | 25.6 |
| 25 | Astronomers are studying two binary star system... | ✗ | 7.00 | 0.0000 | 7 | 71.43% | 28.6 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 5.31 | 0.0000 | 5 | 100.00% | 29.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 10.02 | 0.0000 | 9 | 100.00% | 38.3 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 8.60 | 0.0000 | 8 | 50.00% | 26.9 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 9.47 | 0.0000 | 9 | 77.78% | 42.8 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 7.36 | 0.0000 | 7 | 42.86% | 24.3 |
| 31 | All the following statements about the molecula... | ✗ | 9.68 | 0.0000 | 9 | 44.44% | 52.2 |
| 32 | You are interested in studying a rare type of b... | ✗ | 9.04 | 0.0000 | 7 | 57.14% | 41.4 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 9.57 | 0.0000 | 8 | 75.00% | 26.9 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 9.62 | 0.0000 | 8 | 87.50% | 33.8 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 10.21 | 0.0000 | 9 | 100.00% | 36.7 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 8.08 | 0.0000 | 9 | 66.67% | 33.9 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 7.45 | 0.0000 | 7 | 85.71% | 33.6 |
| 38 | Identify the final product produced when cyclob... | ✗ | 9.12 | 0.0000 | 9 | 66.67% | 23.3 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 9.81 | 0.0000 | 9 | 44.44% | 27.8 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 7.21 | 0.0000 | 8 | 50.00% | 30.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 11.75 | 0.0000 | 10 | 30.00% | 29.5 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 8.08 | 0.0000 | 8 | 62.50% | 31.9 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 6.46 | 0.0000 | 6 | 83.33% | 41.7 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✗ | 8.88 | 0.0000 | 9 | 77.78% | 45.6 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 9.03 | 0.0000 | 9 | 66.67% | 46.7 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 7.89 | 0.0000 | 6 | 66.67% | 23.3 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 12.34 | 0.0000 | 8 | 62.50% | 21.9 |
| 48 | Which of the following statements about enhance... | ✗ | 6.31 | 0.0000 | 6 | 66.67% | 35.8 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 9.60 | 0.0000 | 10 | 40.00% | 36.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 8.66 | 0.0000 | 8 | 75.00% | 29.4 |
| 51 | The Michael reaction is a chemical process in o... | ✗ | 9.64 | 0.0000 | 9 | 55.56% | 44.4 |
| 52 | A common approximation made in many-body nuclea... | ✓ | 12.69 | 0.0000 | - | - | - |
| 53 | Consider a uniformly charged metallic ring of r... | ✗ | 7.48 | 0.0000 | 6 | 100.00% | 21.7 |
| 54 | Compounds that have the same molecular formula ... | ✗ | 12.30 | 0.0000 | 12 | 25.00% | 42.5 |
| 55 | Calculate the amount of non-Gaussianity(nG) in ... | ✗ | 10.92 | 0.0000 | 7 | 57.14% | 48.6 |
| 56 | A series of experiments are conducted to unrave... | ✗ | 10.24 | 0.0000 | 9 | 33.33% | 40.0 |
| 57 | A student regrets that he fell asleep during a ... | ✓ | 7.27 | 0.0000 | 7 | 57.14% | 32.1 |
| 58 | In an experiment, a researcher reacted ((2,2-di... | ✓ | 8.39 | 0.0000 | 8 | 62.50% | 30.6 |
| 59 | If an equimolar mixture X of two liquids, which... | ✗ | 8.57 | 0.0000 | 8 | 75.00% | 38.8 |
| 60 | Which of the following issues are the most comm... | ✗ | 8.64 | 0.0000 | 10 | 50.00% | 34.5 |
| 61 | Name reactions in chemistry refer to a specific... | ✗ | 10.63 | 0.0000 | 9 | 55.56% | 32.2 |
| 62 | Enya and John are of normal phenotype but they ... | ✗ | 8.21 | 0.0000 | 9 | 44.44% | 27.2 |
| 63 | You want to cultivate a population of mouse emb... | ✗ | 9.05 | 0.0000 | 9 | 44.44% | 33.3 |
| 64 | Dienes are organic compounds with two adjacent ... | ✗ | 9.64 | 0.0000 | 7 | 71.43% | 30.7 |
| 65 | You are studying a nuclear decay which converts... | ✗ | 9.65 | 0.0000 | 9 | 44.44% | 30.0 |
| 66 | "Oh, I know you," the ribonucleoprotein particl... | ✗ | 9.03 | 0.0000 | 9 | 55.56% | 24.4 |
| 67 | A research group is investigating the productio... | ✗ | 5.73 | 0.0000 | 6 | 66.67% | 48.3 |
| 68 | S)-4-hydroxycyclohex-2-en-1-one is treated with... | ✗ | 9.40 | 0.0000 | 9 | 100.00% | 37.8 |
| 69 | You have prepared an unknown product with the c... | ✗ | 7.60 | 0.0000 | 7 | 85.71% | 32.9 |
| 70 | methyl 2-oxocyclohexane-1-carboxylate is heated... | ✗ | 8.73 | 0.0000 | 9 | 88.89% | 33.9 |
| 71 | A reaction of a liquid organic compound, which ... | ✗ | 6.70 | 0.0000 | 6 | 50.00% | 32.5 |
| 72 | You have an interesting drought-resistant culti... | ✓ | 7.26 | 0.0000 | 6 | 83.33% | 38.3 |
| 73 | A textile dye containing an extensively conjuga... | ✗ | 6.58 | 0.0000 | 6 | 66.67% | 30.0 |
| 74 | toluene is treated with nitric acid and sulfuri... | ✗ | 6.89 | 0.0000 | 6 | 100.00% | 38.3 |
| 75 | When 500 mL of PH3 is decomposed the total volu... | ✗ | 8.61 | 0.0000 | 9 | 77.78% | 23.9 |
| 76 | What is the parallax (in milliarcseconds) of a ... | ✗ | 9.14 | 0.0000 | 9 | 77.78% | 23.9 |
| 77 | What is the energy of the Relativistic Heavy Io... | ✗ | 8.05 | 0.0000 | 8 | 50.00% | 23.8 |
| 78 | An electron is in the spin state (3i, 4). Find ... | ✗ | 7.85 | 0.0000 | 6 | 50.00% | 26.7 |
| 79 | There are two spin 1/2 nuclei in a strong magne... | ✗ | 7.70 | 0.0000 | 8 | 50.00% | 31.2 |
| 80 | Suppose you are studying a system of three nucl... | ✓ | 9.87 | 0.0000 | 9 | 55.56% | 37.8 |
| 81 | Sirius is the brightest star in the sky. The te... | ✗ | 5.68 | 0.0000 | 5 | 80.00% | 29.0 |
| 82 | Consider an electromagnetic wave incident on an... | ✗ | 8.56 | 0.0000 | 8 | 50.00% | 25.0 |
| 83 | Identify the EXO product of the following [4+2]... | ✓ | 7.87 | 0.0000 | 8 | 75.00% | 50.0 |
| 84 | We mix 20 cm3 0.1 M CH₃COOH with 40 cm3 0.02 M ... | ✗ | 8.94 | 0.0000 | 9 | 55.56% | 20.0 |
| 85 | Suppose we have a depolarizing channel operatio... | ✓ | 14.54 | 0.0000 | 6 | 66.67% | 50.0 |
| 86 | In a quantum dialog protocol a 4-mode continuou... | ✗ | 9.82 | 0.0000 | 8 | 75.00% | 50.0 |
| 87 | ChIP-seq detected a highly significant binding ... | ✗ | 10.56 | 0.0000 | 10 | 80.00% | 28.5 |
| 88 | "1,2-Rearrangement reaction in which vicinal di... | ✗ | 7.22 | 0.0000 | 7 | 57.14% | 39.3 |
| 89 | Arrange given compounds (1. Acetophenone, 2. pr... | ✗ | 11.14 | 0.0000 | 10 | 30.00% | 27.0 |
| 90 | Ozonolysis of compound A produces 3-methylcyclo... | ✗ | 5.54 | 0.0000 | 5 | 80.00% | 36.0 |
| 91 | Consider the Y-component of the intrinsic angul... | ✗ | 8.33 | 0.0000 | 7 | 100.00% | 31.4 |
| 92 | You have a 10 uL aliquot of a 10 uM DNA templat... | ✗ | 7.76 | 0.0000 | 6 | 100.00% | 22.5 |
| 93 | Observations of structures located at a distanc... | ✗ | 8.89 | 0.0000 | 7 | 57.14% | 29.3 |
| 94 | Identify the number of 13C-NMR signals produced... | ✗ | 8.42 | 0.0000 | 9 | 100.00% | 28.9 |
| 95 | In autumn, tree leaves get colourful and drop d... | ✗ | 9.10 | 0.0000 | 9 | 55.56% | 49.4 |
| 96 | Substances 1-6 undergo an electrophilic substit... | ✗ | 12.08 | 0.0000 | 9 | 66.67% | 24.4 |
| 97 | Which of the following data sets corresponds to... | ✗ | 7.15 | 0.0000 | 7 | 57.14% | 31.4 |
| 98 | Consider a stack of N optical layers (made of a... | ✗ | 10.52 | 0.0000 | 9 | 77.78% | 26.1 |
| 99 | bicyclo[2.2.2]octan-2-one is irradiated with ul... | ✗ | 7.74 | 0.0000 | 7 | 100.00% | 35.0 |
| 100 | The water and oil contact angles on a smooth cl... | ✗ | 9.07 | 0.0000 | 10 | 60.00% | 22.5 |
