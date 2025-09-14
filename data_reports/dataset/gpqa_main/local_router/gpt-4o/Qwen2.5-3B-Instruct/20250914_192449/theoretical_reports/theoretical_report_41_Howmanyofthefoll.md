# 问题 41 的理论性能分析报告

## 问题描述

How many of the following compounds will exhibit optical activity?

(Z)-1-chloro-2-methylbut-1-ene
(3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione
(2R,3S)-2,3-dimethylsuccinic acid
(2R,3R)-2,3-dimethylsuccinic acid
(R)-cyclohex-3-en-1-ol
(1s,3s,5s)-cyclohexane-1,3,5-triol
1-cyclopentyl-3-methylbutan-1-one

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
| 规划阶段总时间 (Planner) | 6.244 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.202 | - |
| 最后一个任务执行完成时间 | 7.788 | - |
| 任务总执行时间(累计) | 10.619 | - |
| 流水线加速比 | 3.23x | - |
| 并行效率 | 136.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 10 | 10.619 | - |
| 大模型任务 | 0 | 0.000 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 25.164 | - |
| 并行总时间 | - | 7.788 | 3.23x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 小模型 | 0.949 | 2.027 | 1.077 | 2 |
| 2 | What is the general rule for optical activity in chiral molecules? | 小模型 | 2.027 | 3.027 | 1.000 | 3 |
| 3 | Is (Z)-1-chloro-2-methylbut-1-ene chiral? | 小模型 | 3.027 | 4.027 | 1.000 | 4 |
| 4 | Is (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione chiral? | 小模型 | 3.027 | 4.182 | 1.155 | 5 |
| 5 | Is (2R,3S)-2,3-dimethylsuccinic acid chiral? | 小模型 | 3.323 | 4.400 | 1.077 | 6 |
| 6 | Is (2R,3R)-2,3-dimethylsuccinic acid chiral? | 小模型 | 3.871 | 4.871 | 1.000 | 7 |
| 7 | Is (R)-cyclohex-3-en-1-ol chiral? | 小模型 | 4.376 | 5.454 | 1.077 | 8 |
| 8 | Is (1s,3s,5s)-cyclohexane-1,3,5-triol chiral? | 小模型 | 5.022 | 6.022 | 1.000 | 9 |
| 9 | Is 1-cyclopentyl-3-methylbutan-1-one chiral? | 小模型 | 5.556 | 6.634 | 1.077 | 10 |
| 10 | How many compounds in the list are chiral and exhibit optical activity? | 小模型 | 6.634 | 7.788 | 1.155 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.84s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 0.95s - 2.03s
步骤 2 |         #########                                          | 2.03s - 3.03s
步骤 3 |                  ########                                  | 3.03s - 4.03s
步骤 4 |                  ##########                                | 3.03s - 4.18s
步骤 5 |                    ##########                              | 3.32s - 4.40s
步骤 6 |                         #########                          | 3.87s - 4.87s
步骤 7 |                              #########                     | 4.38s - 5.45s
步骤 8 |                                   #########                | 5.02s - 6.02s
步骤 9 |                                        #########           | 5.56s - 6.63s
步骤 10 |                                                 ###########| 6.63s - 7.79s
```

