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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.918 | 100% |
| 规划过程中启动的任务数 | 2 / 3 | 66.7% |
| 规划与执行重叠的任务数 | 2 / 3 | 66.7% |
| 第一个任务规划完成时间 | 1.043 | - |
| 最后一个任务规划完成时间 | 1.901 | - |
| 最后一个任务执行完成时间 | 4.124 | - |
| 任务总执行时间(累计) | 3.866 | - |
| 流水线加速比 | 2.62x | - |
| 并行效率 | 93.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 3.866 | - |
| 规划模型 | 1 | 6.926 | - |
| 顺序总时间 | - | 10.792 | - |
| 并行总时间 | - | 4.124 | 2.62x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Is the resistance of g2 mutants (0%) and all double mutants containing g2 (g1g2, g2g3) equal to 0%, confirming g2 causes hypersensitivity in all combinations? | 大模型 | 1.043 | 2.262 | 1.219 | 2 |
| 2 | Do the resistance values of g1 (75%) and g3 (50%) multiply to 37.5%, and does the resistance of g1g3 (10%) equal 37.5% of 25% (the hypothetical resistance of g3 in a non-g1 context)? | 大模型 | 1.478 | 2.766 | 1.289 | 3 |
| 3 | Given that g2 causes hypersensitivity in all combinations and g1/g3 resistance multiplies to 10%, what is the conclusion about the interaction: are g1 and g3 transcriptionally regulated by g2, with g3 downstream of g1 (or vice versa)? | 大模型 | 2.766 | 4.124 | 1.358 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.08s
+------------------------------------------------------------+
步骤 1 |#######################                                     | 1.04s - 2.26s
步骤 2 |        #########################                           | 1.48s - 2.77s
步骤 3 |                                 ###########################| 2.77s - 4.12s
```

