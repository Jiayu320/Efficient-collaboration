# 问题 18 的理论性能分析报告

## 问题描述

You perform a high-throughput experiment on white lupine to find genes contributing to resistance to the fungal disease anthracnose. As a result, you receive three candidate genes of unknown function – G1, G2, and G3. You create three knock-out mutants, g1, g2, and g3, and a set of double-mutants, g1g2, g1g3, and g2g3. You know that at least one of these genes is a transcription factor acting upstream of (an)other gene(s). You start to test those mutant plants: do they have a higher sensitivity to anthracnose than the wild-type because they cannot produce certain gene products? 
After tests with the pathogen, you receive the following results where 100% is the level of resistance to the pathogen in control; 50% is half of the control’s resistance; 25% is a quarter of the control’s resistance; 0% ‒ all plants show signs of infection:
- resistance of g1: 75% of control
- resistance of g2: 0% from control
- resistance of g3: 50% from control
-resistance of g1g3: 10% from control
- resistance of g2g3: 0% from control
- resistance of g1g2: 0% from control

Which conclusion regarding those genes' interaction can you draw from this experiment?


# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.584 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 7 / 9 | 77.8% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 5.542 | - |
| 最后一个任务执行完成时间 | 7.663 | - |
| 任务总执行时间(累计) | 8.449 | - |
| 流水线加速比 | 2.82x | - |
| 并行效率 | 110.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 8.449 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 21.589 | - |
| 并行总时间 | - | 7.663 | 2.82x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does it mean for a gene to be a transcription factor upstream of other genes? | 大模型 | 1.062 | 2.004 | 0.943 | 2 |
| 2 | Which single-gene mutants show the most resistance (75% vs. 50% vs. 0%)? | 大模型 | 1.666 | 2.574 | 0.908 | 3 |
| 3 | Which double-mutants show resistance (10% vs. 0% vs. 0% vs. 0%)? | 大模型 | 2.312 | 3.220 | 0.908 | 4 |
| 4 | Which single-gene mutants show no resistance (g2, g2g3, g1g2)? | 大模型 | 2.916 | 3.824 | 0.908 | 5 |
| 5 | What is the relationship between g1, g2, and g3 based on the resistance levels? | 大模型 | 3.824 | 4.801 | 0.977 | 6 |
| 6 | Can g1 be a transcription factor based on the results? | 大模型 | 4.801 | 5.744 | 0.943 | 7 |
| 7 | Can g2 or g3 be transcription factors based on the results? | 大模型 | 4.801 | 5.744 | 0.943 | 8 |
| 8 | What is the most plausible gene interaction model? | 大模型 | 5.744 | 6.721 | 0.977 | 9 |
| 9 | Which conclusion about the genes' interaction is most supported by the experimental data? | 大模型 | 6.721 | 7.663 | 0.943 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            6.60s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.06s - 2.00s
步骤 2 |     ########                                               | 1.67s - 2.57s
步骤 3 |           ########                                         | 2.31s - 3.22s
步骤 4 |                #########                                   | 2.92s - 3.82s
步骤 5 |                         ########                           | 3.82s - 4.80s
步骤 6 |                                 #########                  | 4.80s - 5.74s
步骤 7 |                                 #########                  | 4.80s - 5.74s
步骤 8 |                                          #########         | 5.74s - 6.72s
步骤 9 |                                                   #########| 6.72s - 7.66s
```

