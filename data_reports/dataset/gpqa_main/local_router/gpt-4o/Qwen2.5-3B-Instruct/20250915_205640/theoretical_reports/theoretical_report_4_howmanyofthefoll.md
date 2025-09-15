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
| 规划阶段总时间 (Planner) | 4.475 | 100% |
| 规划过程中启动的任务数 | 5 / 8 | 62.5% |
| 规划与执行重叠的任务数 | 5 / 8 | 62.5% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 4.433 | - |
| 最后一个任务执行完成时间 | 8.793 | - |
| 任务总执行时间(累计) | 8.925 | - |
| 流水线加速比 | 2.35x | - |
| 并行效率 | 101.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 8.925 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 20.661 | - |
| 并行总时间 | - | 8.793 | 2.35x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 2.030 | 1.081 | 2 |
| 2 | What is the requirement for a compound to have chirality centers? | 大模型 | 2.030 | 3.111 | 1.081 | 3 |
| 3 | How do we identify potential chirality centers in each compound? | 大模型 | 3.111 | 4.193 | 1.081 | 4 |
| 4 | What is the effect of functional groups like double bonds and rings on chirality? | 大模型 | 3.111 | 4.262 | 1.150 | 5 |
| 5 | How do we determine if a compound is chiral or achiral based on the identified centers? | 大模型 | 4.262 | 5.412 | 1.150 | 6 |
| 6 | Which compounds have chiral centers that are not protected by symmetry? | 大模型 | 5.412 | 6.631 | 1.219 | 7 |
| 7 | How do we assess the overall optical activity of each compound? | 大模型 | 6.631 | 7.782 | 1.150 | 8 |
| 8 | What is the final answer to the question of how many compounds exhibit optical activity? | 大模型 | 7.782 | 8.793 | 1.012 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            7.84s
+------------------------------------------------------------+
步骤 1 |########                                                    | 0.95s - 2.03s
步骤 2 |        ########                                            | 2.03s - 3.11s
步骤 3 |                ########                                    | 3.11s - 4.19s
步骤 4 |                #########                                   | 3.11s - 4.26s
步骤 5 |                         #########                          | 4.26s - 5.41s
步骤 6 |                                  #########                 | 5.41s - 6.63s
步骤 7 |                                           #########        | 6.63s - 7.78s
步骤 8 |                                                    ########| 7.78s - 8.79s
```

