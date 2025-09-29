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
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 7.508 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 1.427 | - |
| 最后一个任务规划完成时间 | 7.466 | - |
| 最后一个任务执行完成时间 | 8.985 | - |
| 任务总执行时间(累计) | 9.068 | - |
| 流水线加速比 | 2.10x | - |
| 并行效率 | 100.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.155 | - |
| 大模型任务 | 7 | 7.913 | - |
| 规划模型 | 1 | 9.826 | - |
| 顺序总时间 | - | 18.894 | - |
| 并行总时间 | - | 8.985 | 2.10x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the configuration (R/S) of the chiral center in 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene, considering the priority order of substituents? | 大模型 | 1.427 | 2.577 | 1.150 | 2 |
| 2 | Does 2,3,3,3-tetrafluoroprop-1-ene exhibit plane-polarized light rotation due to a chiral center? Verify with Cahn-Ingold-Prelog rules. | 大模型 | 2.284 | 3.434 | 1.150 | 3 |
| 3 | What is the configuration (R/S) of the chiral center in di(cyclohex-2-en-1-ylidene)methane, given the internal alkenylidene structure? | 大模型 | 3.126 | 4.207 | 1.081 | 4 |
| 4 | What is the configuration (R/S) of the chiral center in 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene, considering the internal alkenylidene structure? | 大模型 | 4.039 | 5.190 | 1.150 | 5 |
| 5 | What is the configuration (R/S) of the chiral center in 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene, given the internal alkenylidene structure? | 大模型 | 4.966 | 6.117 | 1.150 | 6 |
| 6 | What is the configuration (R/S) of the chiral center in [1,1'-biphenyl]-3,3'-diol, given the symmetrical biphenyl structure? | 大模型 | 5.753 | 6.834 | 1.081 | 7 |
| 7 | What is the configuration (R/S) of the chiral center in 8,8-dichlorobicyclo[4.2.0]octan-7-one, given the internal alkenylidene structure? | 大模型 | 6.680 | 7.830 | 1.150 | 8 |
| 8 | Based on the configurations from Steps 1-7, how many compounds exhibit optical activity (R ≠ S)? | 小模型 | 7.830 | 8.985 | 1.155 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            7.56s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.43s - 2.58s
步骤 2 |      #########                                             | 2.28s - 3.43s
步骤 3 |             #########                                      | 3.13s - 4.21s
步骤 4 |                    #########                               | 4.04s - 5.19s
步骤 5 |                            #########                       | 4.97s - 6.12s
步骤 6 |                                  ########                  | 5.75s - 6.83s
步骤 7 |                                         #########          | 6.68s - 7.83s
步骤 8 |                                                  ##########| 7.83s - 8.98s
```

