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
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.188 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 8 / 10 | 80.0% |
| 第一个任务规划完成时间 | 1.006 | - |
| 最后一个任务规划完成时间 | 6.146 | - |
| 最后一个任务执行完成时间 | 7.970 | - |
| 任务总执行时间(累计) | 9.184 | - |
| 流水线加速比 | 2.98x | - |
| 并行效率 | 115.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 9.184 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 23.729 | - |
| 并行总时间 | - | 7.970 | 2.98x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does the C3H formula indicate about the molecular structure? | 大模型 | 1.006 | 1.914 | 0.908 | 2 |
| 2 | What is the general structure of triisopropyl borate? | 大模型 | 1.455 | 2.328 | 0.873 | 3 |
| 3 | Does triisopropyl borate have a central carbon atom with three isopropyl groups and one hydrogen? | 大模型 | 2.328 | 3.236 | 0.908 | 4 |
| 4 | What is the structure of quinuclidine? | 大模型 | 2.480 | 3.319 | 0.839 | 5 |
| 5 | Does quinuclidine have a C3H symmetry? | 大模型 | 3.319 | 4.262 | 0.943 | 6 |
| 6 | What is the structure of benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone? | 大模型 | 3.815 | 4.792 | 0.977 | 7 |
| 7 | Does this molecule have a C3H symmetry? | 大模型 | 4.792 | 5.734 | 0.943 | 8 |
| 8 | What is the structure of triphe nyleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone? | 大模型 | 5.177 | 6.154 | 0.977 | 9 |
| 9 | Does this molecule have a C3H symmetry? | 大模型 | 6.154 | 7.097 | 0.943 | 10 |
| 10 | Which molecule among the options has C3H symmetry? | 大模型 | 7.097 | 7.970 | 0.873 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.96s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.01s - 1.91s
步骤 2 |   ########                                                 | 1.46s - 2.33s
步骤 3 |           ########                                         | 2.33s - 3.24s
步骤 4 |            #######                                         | 2.48s - 3.32s
步骤 5 |                   #########                                | 3.32s - 4.26s
步骤 6 |                        ########                            | 3.81s - 4.79s
步骤 7 |                                ########                    | 4.79s - 5.73s
步骤 8 |                                   #########                | 5.18s - 6.15s
步骤 9 |                                            ########        | 6.15s - 7.10s
步骤 10 |                                                    ########| 7.10s - 7.97s
```

