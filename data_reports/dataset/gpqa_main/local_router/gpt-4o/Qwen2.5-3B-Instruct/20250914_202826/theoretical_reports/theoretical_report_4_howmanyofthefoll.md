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
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.708 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.666 | - |
| 最后一个任务执行完成时间 | 8.044 | - |
| 任务总执行时间(累计) | 9.980 | - |
| 流水线加速比 | 3.05x | - |
| 并行效率 | 124.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 9.980 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 24.525 | - |
| 并行总时间 | - | 8.044 | 3.05x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 1.892 | 0.943 | 2 |
| 2 | Does 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene have a plane of symmetry? | 大模型 | 1.892 | 2.904 | 1.012 | 3 |
| 3 | Does 2,3,3,3-tetrafluoroprop-1-ene have a plane of symmetry? | 大模型 | 2.256 | 3.267 | 1.012 | 4 |
| 4 | Does di(cyclohex-2-en-1-ylidene)methane have a plane of symmetry? | 大模型 | 2.874 | 3.885 | 1.012 | 5 |
| 5 | Does 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene have a plane of symmetry? | 大模型 | 3.562 | 4.574 | 1.012 | 6 |
| 6 | Does 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene have a plane of symmetry? | 大模型 | 4.264 | 5.276 | 1.012 | 7 |
| 7 | Does [1,1'-biphenyl]-3,3'-diol have a plane of symmetry? | 大模型 | 4.868 | 5.880 | 1.012 | 8 |
| 8 | Does 8,8-dichlorobicyclo[4.2.0]octan-7-one have a plane of symmetry? | 大模型 | 5.570 | 6.582 | 1.012 | 9 |
| 9 | Does cyclopent-2-en-1-one have a plane of symmetry? | 大模型 | 6.090 | 7.102 | 1.012 | 10 |
| 10 | Which compounds exhibit optical activity? | 大模型 | 7.102 | 8.044 | 0.943 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            7.09s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.95s - 1.89s
步骤 2 |       #########                                            | 1.89s - 2.90s
步骤 3 |           ########                                         | 2.26s - 3.27s
步骤 4 |                ########                                    | 2.87s - 3.89s
步骤 5 |                      ########                              | 3.56s - 4.57s
步骤 6 |                            ########                        | 4.26s - 5.28s
步骤 7 |                                 ########                   | 4.87s - 5.88s
步骤 8 |                                       ########             | 5.57s - 6.58s
步骤 9 |                                           #########        | 6.09s - 7.10s
步骤 10 |                                                    ########| 7.10s - 8.04s
```

