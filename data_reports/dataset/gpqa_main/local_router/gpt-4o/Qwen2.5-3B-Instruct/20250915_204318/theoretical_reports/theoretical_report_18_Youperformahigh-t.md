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
| 规划阶段总时间 (Planner) | 5.935 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 7 / 9 | 77.8% |
| 第一个任务规划完成时间 | 1.160 | - |
| 最后一个任务规划完成时间 | 5.893 | - |
| 最后一个任务执行完成时间 | 9.054 | - |
| 任务总执行时间(累计) | 10.801 | - |
| 流水线加速比 | 2.64x | - |
| 并行效率 | 119.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 5.085 | - |
| 大模型任务 | 5 | 5.717 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 23.941 | - |
| 并行总时间 | - | 9.054 | 2.64x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does each mutant (g1, g2, g3) resistance level indicate about the function of these genes? | 小模型 | 1.160 | 2.625 | 1.465 | 2 |
| 2 | What does each double mutant (g1g2, g1g3, g2g3) resistance level indicate about the interaction between the genes? | 小模型 | 1.876 | 3.341 | 1.465 | 3 |
| 3 | Which single mutants show a resistance level different from the wild-type (control) plants? | 小模型 | 2.625 | 3.702 | 1.077 | 4 |
| 4 | Which double mutants show a resistance level different from the wild-type (control) plants? | 小模型 | 3.341 | 4.419 | 1.077 | 5 |
| 5 | What can we infer about the upstream gene(s) from the results of the single mutants? | 大模型 | 3.702 | 4.783 | 1.081 | 6 |
| 6 | What can we infer about the downstream gene(s) from the results of the double mutants? | 大模型 | 4.419 | 5.500 | 1.081 | 7 |
| 7 | How do the results of the double mutants support the idea that at least one gene is a transcription factor? | 大模型 | 5.500 | 6.650 | 1.150 | 8 |
| 8 | What conclusion can we draw about the functional relationship between G1, G2, and G3 based on the experiment results? | 大模型 | 6.650 | 7.904 | 1.254 | 9 |
| 9 | Which of the three candidate genes is likely to be a transcription factor based on the experimental data? | 大模型 | 7.904 | 9.054 | 1.150 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            7.89s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.16s - 2.62s
步骤 2 |     ###########                                            | 1.88s - 3.34s
步骤 3 |           ########                                         | 2.62s - 3.70s
步骤 4 |                ########                                    | 3.34s - 4.42s
步骤 5 |                   ########                                 | 3.70s - 4.78s
步骤 6 |                        ########                            | 4.42s - 5.50s
步骤 7 |                                #########                   | 5.50s - 6.65s
步骤 8 |                                         ##########         | 6.65s - 7.90s
步骤 9 |                                                   #########| 7.90s - 9.05s
```

