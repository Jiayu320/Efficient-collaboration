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
| 规划阶段总时间 (Planner) | 5.500 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 5.458 | - |
| 最后一个任务执行完成时间 | 7.255 | - |
| 任务总执行时间(累计) | 10.472 | - |
| 流水线加速比 | 3.25x | - |
| 并行效率 | 144.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 10.472 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 23.612 | - |
| 并行总时间 | - | 7.255 | 3.25x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does it mean for a gene to be a transcription factor acting upstream of other genes? | 大模型 | 1.076 | 2.231 | 1.155 | 2 |
| 2 | Which mutants show no resistance (0%) compared to the wild-type? | 大模型 | 1.553 | 2.631 | 1.077 | 3 |
| 3 | Which mutants show resistance but not as much as the wild-type? | 大模型 | 2.017 | 3.094 | 1.077 | 4 |
| 4 | Which double mutants show resistance that is not completely suppressed by either parent mutant? | 大模型 | 3.094 | 4.249 | 1.155 | 5 |
| 5 | Does gene G2 appear to be a transcription factor based on its knockout effect? | 大模型 | 3.098 | 4.331 | 1.232 | 6 |
| 6 | Is gene G3 a transcription factor based on its knockout effect? | 大模型 | 3.604 | 4.836 | 1.232 | 7 |
| 7 | What does the resistance level of g1g3 (10%) suggest about the interaction between G1 and G3? | 大模型 | 4.249 | 5.404 | 1.155 | 8 |
| 8 | What does the resistance level of g2g3 (0%) suggest about the interaction between G2 and G3? | 大模型 | 4.868 | 6.023 | 1.155 | 9 |
| 9 | Based on the results, which conclusion about the gene interactions can be drawn? | 大模型 | 6.023 | 7.255 | 1.232 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            6.18s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.08s - 2.23s
步骤 2 |    ###########                                             | 1.55s - 2.63s
步骤 3 |         ##########                                         | 2.02s - 3.09s
步骤 4 |                   ###########                              | 3.09s - 4.25s
步骤 5 |                   ############                             | 3.10s - 4.33s
步骤 6 |                        ############                        | 3.60s - 4.84s
步骤 7 |                              ############                  | 4.25s - 5.40s
步骤 8 |                                    ############            | 4.87s - 6.02s
步骤 9 |                                                ########### | 6.02s - 7.26s
```

