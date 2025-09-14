# 问题 20 的理论性能分析报告

## 问题描述

which of the following molecules has c3h symmetry?
triisopropyl borate
quinuclidine
benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone
triphenyleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone

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
| 规划阶段总时间 (Planner) | 5.346 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 5.303 | - |
| 最后一个任务执行完成时间 | 7.094 | - |
| 任务总执行时间(累计) | 9.317 | - |
| 流水线加速比 | 2.97x | - |
| 并行效率 | 131.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.317 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 21.053 | - |
| 并行总时间 | - | 7.094 | 2.97x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of C3H symmetry? | 大模型 | 0.963 | 2.118 | 1.155 | 2 |
| 2 | How many carbon atoms are in each molecule? | 大模型 | 1.371 | 2.448 | 1.077 | 3 |
| 3 | How many hydrogen atoms are in each molecule? | 大模型 | 1.778 | 2.856 | 1.077 | 4 |
| 4 | Does triisopropyl borate have a central carbon with three identical methyl groups? | 大模型 | 2.448 | 3.681 | 1.232 | 5 |
| 5 | Does quinuclidine have a central carbon with three identical atoms? | 大模型 | 2.856 | 4.010 | 1.155 | 6 |
| 6 | Does benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone have a central carbon with three identical atoms? | 大模型 | 3.787 | 5.096 | 1.310 | 7 |
| 7 | Does triphenyleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone have a central carbon with three identical atoms? | 大模型 | 4.784 | 6.094 | 1.310 | 8 |
| 8 | Which molecule has C3H symmetry? | 大模型 | 6.094 | 7.094 | 1.000 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            6.13s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.96s - 2.12s
步骤 2 |   ###########                                              | 1.37s - 2.45s
步骤 3 |       ###########                                          | 1.78s - 2.86s
步骤 4 |              ############                                  | 2.45s - 3.68s
步骤 5 |                  ###########                               | 2.86s - 4.01s
步骤 6 |                           #############                    | 3.79s - 5.10s
步骤 7 |                                     #############          | 4.78s - 6.09s
步骤 8 |                                                  ##########| 6.09s - 7.09s
```

