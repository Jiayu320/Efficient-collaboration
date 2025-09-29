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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.037 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 0.989 | - |
| 最后一个任务规划完成时间 | 3.020 | - |
| 最后一个任务执行完成时间 | 5.192 | - |
| 任务总执行时间(累计) | 9.292 | - |
| 流水线加速比 | 3.22x | - |
| 并行效率 | 179.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 7 | 7.982 | - |
| 规划模型 | 1 | 7.420 | - |
| 顺序总时间 | - | 16.712 | - |
| 并行总时间 | - | 5.192 | 3.22x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does (Z)-1-chloro-2-methylbut-1-ene possess a plane of symmetry or non-planar asymmetry that would prevent optical isomerism? | 大模型 | 0.989 | 2.139 | 1.150 | 2 |
| 2 | Does (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione have a symmetry plane or fused-ring conformation eliminating optical isomerism? | 大模型 | 1.364 | 2.583 | 1.219 | 3 |
| 3 | How many chiral centers does (2R,3S)-2,3-dimethylsuccinic acid have, and does it possess a plane of symmetry or meso configuration? | 大模型 | 1.662 | 2.743 | 1.081 | 4 |
| 4 | How many chiral centers does (2R,3R)-2,3-dimethylsuccinic acid have, and does it possess a plane of symmetry or meso configuration? | 大模型 | 1.961 | 3.042 | 1.081 | 5 |
| 5 | Is (R)-cyclohex-3-en-1-ol chiral and does it lack a plane of symmetry for optical isomerism? | 大模型 | 2.216 | 3.367 | 1.150 | 6 |
| 6 | Does (1s,3s,5s)-cyclohexane-1,3,5-triol have a symmetry plane or achiral conformation? | 大模型 | 2.499 | 3.649 | 1.150 | 7 |
| 7 | Does 1-cyclopentyl-3-methylbutan-1-one have chiral centers and no molecular symmetry? | 大模型 | 2.732 | 3.883 | 1.150 | 8 |
| 8 | Count the compounds from Steps 1-7 where optical isomers are possible. What is this count? | 小模型 | 3.883 | 5.192 | 1.310 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            4.20s
+------------------------------------------------------------+
步骤 1 |################                                            | 0.99s - 2.14s
步骤 2 |     #################                                      | 1.36s - 2.58s
步骤 3 |         ################                                   | 1.66s - 2.74s
步骤 4 |             ################                               | 1.96s - 3.04s
步骤 5 |                 ################                           | 2.22s - 3.37s
步骤 6 |                     ################                       | 2.50s - 3.65s
步骤 7 |                        #################                   | 2.73s - 3.88s
步骤 8 |                                         ###################| 3.88s - 5.19s
```

