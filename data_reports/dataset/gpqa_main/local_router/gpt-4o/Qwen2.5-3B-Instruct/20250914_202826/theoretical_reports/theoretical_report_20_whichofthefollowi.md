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
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.947 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 6.904 | - |
| 最后一个任务执行完成时间 | 8.008 | - |
| 任务总执行时间(累计) | 9.841 | - |
| 流水线加速比 | 3.05x | - |
| 并行效率 | 122.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 9.841 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 24.386 | - |
| 并行总时间 | - | 8.008 | 3.05x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of C3H symmetry? | 大模型 | 0.963 | 1.906 | 0.943 | 2 |
| 2 | How many carbon atoms are in triisopropyl borate? | 大模型 | 1.413 | 2.321 | 0.908 | 3 |
| 3 | How many hydrogen atoms are in triisopropyl borate? | 大模型 | 1.862 | 2.770 | 0.908 | 4 |
| 4 | Does triisopropyl borate have a plane of symmetry? | 大模型 | 2.770 | 3.748 | 0.977 | 5 |
| 5 | What is the structure of quinuclidine? | 大模型 | 2.803 | 3.815 | 1.012 | 6 |
| 6 | Does quinuclidine have a plane of symmetry? | 大模型 | 3.815 | 4.792 | 0.977 | 7 |
| 7 | What is the structure of benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone? | 大模型 | 4.124 | 5.170 | 1.046 | 8 |
| 8 | Does benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone have a plane of symmetry? | 大模型 | 5.170 | 6.182 | 1.012 | 9 |
| 9 | What is the structure of tripheNYleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone? | 大模型 | 5.949 | 6.996 | 1.046 | 10 |
| 10 | Does tripheNYleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone have a plane of symmetry? | 大模型 | 6.996 | 8.008 | 1.012 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            7.04s
+------------------------------------------------------------+
步骤 1 |########                                                    | 0.96s - 1.91s
步骤 2 |   ########                                                 | 1.41s - 2.32s
步骤 3 |       ########                                             | 1.86s - 2.77s
步骤 4 |               ########                                     | 2.77s - 3.75s
步骤 5 |               #########                                    | 2.80s - 3.82s
步骤 6 |                        ########                            | 3.82s - 4.79s
步骤 7 |                          #########                         | 4.12s - 5.17s
步骤 8 |                                   #########                | 5.17s - 6.18s
步骤 9 |                                          #########         | 5.95s - 7.00s
步骤 10 |                                                   #########| 7.00s - 8.01s
```

