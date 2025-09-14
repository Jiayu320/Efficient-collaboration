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
| 规划阶段总时间 (Planner) | 4.025 | 100% |
| 规划过程中启动的任务数 | 3 / 8 | 37.5% |
| 规划与执行重叠的任务数 | 3 / 8 | 37.5% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 3.983 | - |
| 最后一个任务执行完成时间 | 8.340 | - |
| 任务总执行时间(累计) | 8.402 | - |
| 流水线加速比 | 2.41x | - |
| 并行效率 | 100.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 6 | 6.310 | - |
| 大模型任务 | 2 | 2.093 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 20.138 | - |
| 并行总时间 | - | 8.340 | 2.41x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 小模型 | 0.949 | 1.872 | 0.922 | 2 |
| 2 | What are the necessary conditions for a compound to exhibit optical activity? | 小模型 | 1.872 | 2.949 | 1.077 | 3 |
| 3 | How do we determine if a compound is chiral? | 小模型 | 2.949 | 4.104 | 1.155 | 4 |
| 4 | What is the stereochemistry of each compound provided? | 大模型 | 4.104 | 5.185 | 1.081 | 5 |
| 5 | Which compounds have a chiral center? | 小模型 | 5.185 | 6.340 | 1.155 | 6 |
| 6 | Are there any other factors that could affect optical activity? | 大模型 | 5.185 | 6.197 | 1.012 | 7 |
| 7 | Which compounds actually exhibit optical activity? | 小模型 | 6.340 | 7.418 | 1.077 | 8 |
| 8 | How many compounds in total exhibit optical activity? | 小模型 | 7.418 | 8.340 | 0.922 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            7.39s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.95s - 1.87s
步骤 2 |       #########                                            | 1.87s - 2.95s
步骤 3 |                #########                                   | 2.95s - 4.10s
步骤 4 |                         #########                          | 4.10s - 5.19s
步骤 5 |                                  #########                 | 5.19s - 6.34s
步骤 6 |                                  ########                  | 5.19s - 6.20s
步骤 7 |                                           #########        | 6.34s - 7.42s
步骤 8 |                                                    ########| 7.42s - 8.34s
```

