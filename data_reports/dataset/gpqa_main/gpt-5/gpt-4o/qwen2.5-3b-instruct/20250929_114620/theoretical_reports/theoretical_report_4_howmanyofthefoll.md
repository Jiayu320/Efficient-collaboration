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
| 路由模型 (gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 14.118 | 100% |
| 规划过程中启动的任务数 | 2 / 3 | 66.7% |
| 规划与执行重叠的任务数 | 2 / 3 | 66.7% |
| 第一个任务规划完成时间 | 8.364 | - |
| 最后一个任务规划完成时间 | 14.059 | - |
| 最后一个任务执行完成时间 | 18.117 | - |
| 任务总执行时间(累计) | 6.415 | - |
| 流水线加速比 | 1.70x | - |
| 并行效率 | 35.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.000 | - |
| 大模型任务 | 2 | 5.415 | - |
| 规划模型 | 1 | 24.400 | - |
| 顺序总时间 | - | 30.815 | - |
| 并行总时间 | - | 18.117 | 1.70x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the precise criteria to determine whether a molecule exhibits optical activity, covering all stereogenic elements (tetrahedral centers, axial, planar, helical, conformational chirality), symmetry elements that cause achirality (mirror planes, inversion centers, improper rotations), and the requirement for configurational stability (e.g., sufficient rotational barriers for atropisomerism)? | 大模型 | 8.364 | 9.930 | 1.565 | 2 |
| 2 | Using the criteria from Step 1, analyze the structures of all eight compounds as a single set: 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene; 2,3,3,3-tetrafluoroprop-1-ene; di(cyclohex-2-en-1-ylidene)methane; 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene; 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene; [1,1'-biphenyl]-3,3'-diol; 8,8-dichlorobicyclo[4.2.0]octan-7-one; cyclopent-2-en-1-one. For each, identify any stereogenic element(s), check for symmetry elements that would make it achiral, consider configurational stability (e.g., atropisomeric barriers), and conclude whether it is optically active. List only the compounds that are optically active, with brief justification. | 大模型 | 13.268 | 17.117 | 3.849 | 3 |
| 3 | Based on the list from Step 2, how many of the eight compounds exhibit optical activity? | 小模型 | 17.117 | 18.117 | 1.000 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            9.75s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 8.36s - 9.93s
步骤 2 |                              #######################       | 13.27s - 17.12s
步骤 3 |                                                     #######| 17.12s - 18.12s
```

