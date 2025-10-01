# 问题 4 的理论性能分析报告

## 问题描述

how many of the following compounds exhibit optical activity?
1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene
2,3,3,3-tetrafluoroprop-1-ene
di(cyclohex-2-en-1-ylidene)methane
5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene
3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene
[1,1'-biphenyl]-3,3'-diol
8,8-dichlorobicyclo[4.2.0]octan-7-one
cyclopent-2-en-1-one

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gemini-2.5-pro) | 2.510 | 93.75 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 10.147 | 100% |
| 规划过程中启动的任务数 | 2 / 12 | 16.7% |
| 规划与执行重叠的任务数 | 2 / 12 | 16.7% |
| 第一个任务规划完成时间 | 3.075 | - |
| 最后一个任务规划完成时间 | 10.115 | - |
| 最后一个任务执行完成时间 | 67.822 | - |
| 任务总执行时间(累计) | 125.990 | - |
| 流水线加速比 | 2.04x | - |
| 并行效率 | 185.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 64.747 | - |
| 大模型任务 | 8 | 61.243 | - |
| 规划模型 | 1 | 12.344 | - |
| 顺序总时间 | - | 138.334 | - |
| 并行总时间 | - | 67.822 | 2.04x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the structural requirement for a molecule to be optically active, and what are the key symmetry elements (or lack thereof) that determine this property? | 小模型 | 3.075 | 19.262 | 16.187 | 2 |
| 2 | Draw the chemical structure for each of the eight compounds listed in the problem based on their IUPAC names. | 大模型 | 3.523 | 11.179 | 7.655 | 3 |
| 3 | Analyze the structure of 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene. Does it possess a stereocenter? Is the molecule chiral? | 大模型 | 19.262 | 26.917 | 7.655 | 4 |
| 4 | Analyze the structure of 2,3,3,3-tetrafluoroprop-1-ene. Does this molecule have a plane of symmetry? Is it chiral? | 大模型 | 19.262 | 26.917 | 7.655 | 5 |
| 5 | Analyze the structure and 3D geometry of di(cyclohex-2-en-1-ylidene)methane. Does this spirane-like molecule possess a C2 axis or any planes of symmetry? Is it chiral? | 大模型 | 19.262 | 26.917 | 7.655 | 6 |
| 6 | Analyze the structure of 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene. Does the side chain contain a stereocenter? Is the overall molecule chiral? | 大模型 | 19.262 | 26.917 | 7.655 | 7 |
| 7 | Analyze the structure of 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene. Does this allene-type system meet the criteria for axial chirality? Is it chiral? | 大模型 | 19.262 | 26.917 | 7.655 | 8 |
| 8 | Analyze the structure of [1,1'-biphenyl]-3,3'-diol. Is rotation around the central carbon-carbon single bond sufficiently hindered to allow for stable atropisomers? Is the molecule chiral? | 大模型 | 19.262 | 26.917 | 7.655 | 9 |
| 9 | Analyze the structure of 8,8-dichlorobicyclo[4.2.0]octan-7-one. Assuming the most stable cis-ring fusion, does the molecule possess a plane of symmetry? Is it chiral? | 大模型 | 19.262 | 26.917 | 7.655 | 10 |
| 10 | Analyze the structure of cyclopent-2-en-1-one. Is this molecule planar? Does it have a plane of symmetry? Is it chiral? | 小模型 | 19.262 | 35.449 | 16.187 | 1 |
| 11 | Based on the analyses in steps 3 through 10, compile a definitive list of all the compounds that are chiral. | 小模型 | 35.449 | 51.635 | 16.187 | 2 |
| 12 | What is the final total count of optically active compounds from the provided list? | 小模型 | 51.635 | 67.822 | 16.187 | 3 |

## 理论执行甘特图

```
时间轴:
0                                                            64.75s
+------------------------------------------------------------+
步骤 1 |##############                                              | 3.08s - 19.26s
步骤 2 |#######                                                     | 3.52s - 11.18s
步骤 3 |              ########                                      | 19.26s - 26.92s
步骤 4 |              ########                                      | 19.26s - 26.92s
步骤 5 |              ########                                      | 19.26s - 26.92s
步骤 6 |              ########                                      | 19.26s - 26.92s
步骤 7 |              ########                                      | 19.26s - 26.92s
步骤 8 |              ########                                      | 19.26s - 26.92s
步骤 9 |              ########                                      | 19.26s - 26.92s
步骤 10 |              ###############                               | 19.26s - 35.45s
步骤 11 |                             ###############                | 35.45s - 51.64s
步骤 12 |                                            ############### | 51.64s - 67.82s
```

