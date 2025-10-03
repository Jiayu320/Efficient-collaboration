# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 100
- 正确数量: 21
- 准确率: 21.00%
- 平均执行时间: 37.00 秒
- 平均成本: $0.0186

## 任务规划指标

- 平均任务步骤数: 3.85
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 30.484 秒
- 平均顺序执行时间: 31.688 秒
- 平均并行加速比: 1.04x
- 理论与实际执行时间比例: 0.82x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 4.763 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 9.811 秒

### 生成速度
- 小模型平均每秒生成token数: 22.29 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 5.68 tokens/s
- 总平均每秒生成token数: 27.97 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 37.23 | 0.0081 | 3 | 100.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 34.05 | 0.0142 | 3 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 31.97 | 0.0114 | 4 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 49.95 | 0.0433 | 9 | 100.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 32.87 | 0.0130 | 3 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 42.14 | 0.0238 | 4 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 42.06 | 0.0182 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 39.00 | 0.0243 | 4 | 100.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 33.65 | 0.0147 | 3 | 100.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 32.84 | 0.0145 | 4 | 100.00% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 30.11 | 0.0104 | 3 | 100.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 43.97 | 0.0302 | 6 | 100.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 41.30 | 0.0297 | 3 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 47.47 | 0.0355 | 5 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 30.26 | 0.0099 | 3 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 27.92 | 0.0084 | 3 | 100.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 35.19 | 0.0181 | 3 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 27.44 | 0.0101 | 3 | 100.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 39.59 | 0.0302 | 5 | 100.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 41.19 | 0.0241 | 5 | 100.00% | 0.0 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 34.38 | 0.0155 | 4 | 100.00% | 0.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 27.82 | 0.0113 | 3 | 100.00% | 0.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 32.60 | 0.0143 | 3 | 100.00% | 0.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 31.43 | 0.0140 | 3 | 100.00% | 0.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 41.11 | 0.0302 | 4 | 100.00% | 0.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 28.75 | 0.0063 | 3 | 100.00% | 0.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 26.29 | 0.0072 | 3 | 100.00% | 0.0 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 29.88 | 0.0090 | 4 | 100.00% | 0.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 27.96 | 0.0086 | 3 | 100.00% | 0.0 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 40.71 | 0.0235 | 6 | 100.00% | 0.0 |
| 31 | All the following statements about the molecula... | ✗ | 33.90 | 0.0105 | 3 | 100.00% | 0.0 |
| 32 | You are interested in studying a rare type of b... | ✗ | 34.71 | 0.0134 | 3 | 100.00% | 0.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 39.09 | 0.0189 | 4 | 100.00% | 0.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 41.56 | 0.0288 | 5 | 100.00% | 0.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 43.00 | 0.0230 | 4 | 100.00% | 0.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 32.76 | 0.0120 | 4 | 100.00% | 0.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✓ | 48.16 | 0.0320 | 6 | 100.00% | 0.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 31.86 | 0.0106 | 3 | 100.00% | 0.0 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 30.72 | 0.0145 | 3 | 100.00% | 0.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 45.80 | 0.0243 | 3 | 100.00% | 0.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 41.01 | 0.0275 | 7 | 100.00% | 0.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 35.50 | 0.0199 | 3 | 100.00% | 0.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 28.72 | 0.0082 | 3 | 100.00% | 0.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 28.66 | 0.0103 | 3 | 100.00% | 0.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 50.57 | 0.0323 | 4 | 100.00% | 0.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 34.42 | 0.0166 | 3 | 100.00% | 0.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✓ | 38.56 | 0.0241 | 3 | 100.00% | 0.0 |
| 48 | Which of the following statements about enhance... | ✗ | 39.76 | 0.0215 | 5 | 100.00% | 0.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 30.35 | 0.0104 | 3 | 100.00% | 0.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 34.35 | 0.0119 | 3 | 100.00% | 0.0 |
| 51 | The Michael reaction is a chemical process in o... | ✗ | 58.89 | 0.0541 | 8 | 100.00% | 0.0 |
| 52 | A common approximation made in many-body nuclea... | ✓ | 32.64 | 0.0131 | 3 | 100.00% | 0.0 |
| 53 | Consider a uniformly charged metallic ring of r... | ✓ | 37.32 | 0.0176 | 3 | 100.00% | 0.0 |
| 54 | Compounds that have the same molecular formula ... | ✓ | 33.73 | 0.0174 | 4 | 100.00% | 0.0 |
| 55 | Calculate the amount of non-Gaussianity(nG) in ... | ✗ | 51.63 | 0.0528 | 7 | 100.00% | 0.0 |
| 56 | A series of experiments are conducted to unrave... | ✗ | 39.66 | 0.0222 | 5 | 100.00% | 0.0 |
| 57 | A student regrets that he fell asleep during a ... | ✗ | 31.36 | 0.0055 | 3 | 100.00% | 0.0 |
| 58 | In an experiment, a researcher reacted ((2,2-di... | ✗ | 41.37 | 0.0238 | 4 | 100.00% | 0.0 |
| 59 | If an equimolar mixture X of two liquids, which... | ✗ | 33.55 | 0.0142 | 3 | 100.00% | 0.0 |
| 60 | Which of the following issues are the most comm... | ✗ | 37.05 | 0.0155 | 5 | 100.00% | 0.0 |
| 61 | Name reactions in chemistry refer to a specific... | ✗ | 37.27 | 0.0175 | 4 | 100.00% | 0.0 |
| 62 | Enya and John are of normal phenotype but they ... | ✓ | 28.82 | 0.0107 | 3 | 100.00% | 0.0 |
| 63 | You want to cultivate a population of mouse emb... | ✗ | 31.26 | 0.0138 | 3 | 100.00% | 0.0 |
| 64 | Dienes are organic compounds with two adjacent ... | ✗ | 37.37 | 0.0199 | 3 | 100.00% | 0.0 |
| 65 | You are studying a nuclear decay which converts... | ✗ | 35.91 | 0.0142 | 3 | 100.00% | 0.0 |
| 66 | "Oh, I know you," the ribonucleoprotein particl... | ✗ | 30.57 | 0.0090 | 4 | 100.00% | 0.0 |
| 67 | A research group is investigating the productio... | ✗ | 34.78 | 0.0110 | 3 | 100.00% | 0.0 |
| 68 | S)-4-hydroxycyclohex-2-en-1-one is treated with... | ✗ | 45.78 | 0.0297 | 4 | 100.00% | 0.0 |
| 69 | You have prepared an unknown product with the c... | ✗ | 38.38 | 0.0186 | 3 | 100.00% | 0.0 |
| 70 | methyl 2-oxocyclohexane-1-carboxylate is heated... | ✓ | 25.80 | 0.0071 | 3 | 100.00% | 0.0 |
| 71 | A reaction of a liquid organic compound, which ... | ✗ | 28.75 | 0.0096 | 3 | 100.00% | 0.0 |
| 72 | You have an interesting drought-resistant culti... | ✗ | 34.35 | 0.0185 | 3 | 100.00% | 0.0 |
| 73 | A textile dye containing an extensively conjuga... | ✗ | 29.65 | 0.0109 | 3 | 100.00% | 0.0 |
| 74 | toluene is treated with nitric acid and sulfuri... | ✗ | 37.74 | 0.0188 | 4 | 100.00% | 0.0 |
| 75 | When 500 mL of PH3 is decomposed the total volu... | ✗ | 28.79 | 0.0124 | 3 | 100.00% | 0.0 |
| 76 | What is the parallax (in milliarcseconds) of a ... | ✓ | 30.64 | 0.0144 | 4 | 100.00% | 0.0 |
| 77 | What is the energy of the Relativistic Heavy Io... | ✗ | 32.90 | 0.0173 | 3 | 100.00% | 0.0 |
| 78 | An electron is in the spin state (3i, 4). Find ... | ✗ | 33.90 | 0.0140 | 3 | 100.00% | 0.0 |
| 79 | There are two spin 1/2 nuclei in a strong magne... | ✓ | 36.24 | 0.0126 | 4 | 100.00% | 0.0 |
| 80 | Suppose you are studying a system of three nucl... | ✗ | 31.59 | 0.0162 | 3 | 100.00% | 0.0 |
| 81 | Sirius is the brightest star in the sky. The te... | ✗ | 33.81 | 0.0203 | 4 | 100.00% | 0.0 |
| 82 | Consider an electromagnetic wave incident on an... | ✗ | 33.13 | 0.0152 | 3 | 100.00% | 0.0 |
| 83 | Identify the EXO product of the following [4+2]... | ✗ | 36.22 | 0.0166 | 3 | 100.00% | 0.0 |
| 84 | We mix 20 cm3 0.1 M CH₃COOH with 40 cm3 0.02 M ... | ✓ | 57.15 | 0.0553 | 8 | 100.00% | 0.0 |
| 85 | Suppose we have a depolarizing channel operatio... | ✗ | 32.49 | 0.0162 | 3 | 100.00% | 0.0 |
| 86 | In a quantum dialog protocol a 4-mode continuou... | ✗ | 49.47 | 0.0305 | 4 | 100.00% | 0.0 |
| 87 | ChIP-seq detected a highly significant binding ... | ✓ | 39.39 | 0.0189 | 5 | 100.00% | 0.0 |
| 88 | "1,2-Rearrangement reaction in which vicinal di... | ✗ | 51.51 | 0.0393 | 6 | 100.00% | 0.0 |
| 89 | Arrange given compounds (1. Acetophenone, 2. pr... | ✗ | 46.71 | 0.0376 | 8 | 100.00% | 0.0 |
| 90 | Ozonolysis of compound A produces 3-methylcyclo... | ✗ | 32.31 | 0.0121 | 3 | 100.00% | 0.0 |
| 91 | Consider the Y-component of the intrinsic angul... | ✓ | 37.29 | 0.0201 | 3 | 100.00% | 0.0 |
| 92 | You have a 10 uL aliquot of a 10 uM DNA templat... | ✗ | 38.34 | 0.0168 | 4 | 100.00% | 0.0 |
| 93 | Observations of structures located at a distanc... | ✗ | 28.20 | 0.0105 | 3 | 100.00% | 0.0 |
| 94 | Identify the number of 13C-NMR signals produced... | ✗ | 51.59 | 0.0334 | 6 | 100.00% | 0.0 |
| 95 | In autumn, tree leaves get colourful and drop d... | ✗ | 32.44 | 0.0131 | 3 | 100.00% | 0.0 |
| 96 | Substances 1-6 undergo an electrophilic substit... | ✗ | 51.43 | 0.0229 | 3 | 100.00% | 0.0 |
| 97 | Which of the following data sets corresponds to... | ✗ | 64.77 | 0.0079 | 3 | 100.00% | 0.0 |
| 98 | Consider a stack of N optical layers (made of a... | ✗ | 43.92 | 0.0210 | 5 | 100.00% | 0.0 |
| 99 | bicyclo[2.2.2]octan-2-one is irradiated with ul... | ✗ | 36.90 | 0.0139 | 3 | 100.00% | 0.0 |
| 100 | The water and oil contact angles on a smooth cl... | ✗ | 31.01 | 0.0079 | 3 | 100.00% | 0.0 |
