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
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.301 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.258 | - |
| 最后一个任务执行完成时间 | 7.318 | - |
| 任务总执行时间(累计) | 8.665 | - |
| 流水线加速比 | 3.17x | - |
| 并行效率 | 118.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 8.665 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 23.210 | - |
| 并行总时间 | - | 7.318 | 3.17x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 1.788 | 0.839 | 2 |
| 2 | Is 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene chiral? | 大模型 | 1.788 | 2.731 | 0.943 | 3 |
| 3 | Is 2,3,3,3-tetrafluoroprop-1-ene chiral? | 大模型 | 2.143 | 2.982 | 0.839 | 4 |
| 4 | Is di(cyclohex-2-en-1-ylidene)methane chiral? | 大模型 | 2.705 | 3.578 | 0.873 | 5 |
| 5 | Is 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene chiral? | 大模型 | 3.337 | 4.245 | 0.908 | 6 |
| 6 | Is 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene chiral? | 大模型 | 3.983 | 4.891 | 0.908 | 7 |
| 7 | Is [1,1'-biphenyl]-3,3'-diol chiral? | 大模型 | 4.531 | 5.370 | 0.839 | 8 |
| 8 | Is 8,8-dichlorobicyclo[4.2.0]octan-7-one chiral? | 大模型 | 5.177 | 6.016 | 0.839 | 9 |
| 9 | Is cyclopent-2-en-1-one chiral? | 大模型 | 5.640 | 6.479 | 0.839 | 10 |
| 10 | How many of these compounds exhibit optical activity? | 大模型 | 6.479 | 7.318 | 0.839 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.37s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.95s - 1.79s
步骤 2 |       #########                                            | 1.79s - 2.73s
步骤 3 |           ########                                         | 2.14s - 2.98s
步骤 4 |                ########                                    | 2.71s - 3.58s
步骤 5 |                      #########                             | 3.34s - 4.25s
步骤 6 |                            #########                       | 3.98s - 4.89s
步骤 7 |                                 ########                   | 4.53s - 5.37s
步骤 8 |                                       ########             | 5.18s - 6.02s
步骤 9 |                                            ########        | 5.64s - 6.48s
步骤 10 |                                                    ########| 6.48s - 7.32s
```

