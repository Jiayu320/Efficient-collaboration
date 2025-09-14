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
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.725 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 5.683 | - |
| 最后一个任务执行完成时间 | 7.649 | - |
| 任务总执行时间(累计) | 9.929 | - |
| 流水线加速比 | 3.02x | - |
| 并行效率 | 129.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.922 | - |
| 大模型任务 | 8 | 9.007 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 23.070 | - |
| 并行总时间 | - | 7.649 | 3.02x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does it mean for a gene to be a transcription factor acting upstream of other genes? | 大模型 | 1.076 | 2.231 | 1.155 | 2 |
| 2 | Which of the single mutants (g1, g2, g3) show the highest resistance? | 大模型 | 1.638 | 2.638 | 1.000 | 3 |
| 3 | Which of the single mutants (g1, g2, g3) show the lowest resistance? | 大模型 | 2.199 | 3.199 | 1.000 | 4 |
| 4 | Which of the double mutants (g1g2, g1g3, g2g3) show the highest resistance? | 大模型 | 2.846 | 3.923 | 1.077 | 5 |
| 5 | Which of the double mutants (g1g2, g1g3, g2g3) show the lowest resistance? | 大模型 | 3.492 | 4.569 | 1.077 | 6 |
| 6 | What is the resistance level of the wild-type plants? | 小模型 | 3.927 | 4.849 | 0.922 | 7 |
| 7 | How do the resistance levels of the single mutants compare to the wild-type? | 大模型 | 4.849 | 6.004 | 1.155 | 8 |
| 8 | How do the resistance levels of the double mutants compare to the wild-type and to each other? | 大模型 | 5.107 | 6.339 | 1.232 | 9 |
| 9 | Can we determine which specific gene(s) are transcription factors based on these results? | 大模型 | 6.339 | 7.649 | 1.310 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            6.57s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.08s - 2.23s
步骤 2 |     #########                                              | 1.64s - 2.64s
步骤 3 |          #########                                         | 2.20s - 3.20s
步骤 4 |                #########                                   | 2.85s - 3.92s
步骤 5 |                      #########                             | 3.49s - 4.57s
步骤 6 |                          ########                          | 3.93s - 4.85s
步骤 7 |                                  ##########                | 4.85s - 6.00s
步骤 8 |                                    ############            | 5.11s - 6.34s
步骤 9 |                                                ############| 6.34s - 7.65s
```

