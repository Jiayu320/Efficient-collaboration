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
| 规划阶段总时间 (Planner) | 6.385 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.992 | - |
| 最后一个任务规划完成时间 | 6.343 | - |
| 最后一个任务执行完成时间 | 7.726 | - |
| 任务总执行时间(累计) | 10.929 | - |
| 流水线加速比 | 3.30x | - |
| 并行效率 | 141.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 10.929 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 25.474 | - |
| 并行总时间 | - | 7.726 | 3.30x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does C3H symmetry mean in molecular structure terms? | 大模型 | 0.992 | 2.146 | 1.155 | 2 |
| 2 | How many carbon atoms are in triisopropyl borate? | 大模型 | 1.441 | 2.441 | 1.000 | 3 |
| 3 | How many hydrogen atoms are in triisopropyl borate? | 大模型 | 1.890 | 2.890 | 1.000 | 4 |
| 4 | Does triisopropyl borate have a plane of symmetry? | 大模型 | 2.340 | 3.495 | 1.155 | 5 |
| 5 | How many carbon atoms are in quinuclidine? | 大模型 | 2.775 | 3.775 | 1.000 | 6 |
| 6 | How many hydrogen atoms are in quinuclidine? | 大模型 | 3.211 | 4.211 | 1.000 | 7 |
| 7 | Does quinuclidine have a plane of symmetry? | 大模型 | 3.646 | 4.801 | 1.155 | 8 |
| 8 | How many carbon atoms are in benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone? | 大模型 | 4.531 | 5.686 | 1.155 | 9 |
| 9 | How many hydrogen atoms are in benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone? | 大模型 | 5.416 | 6.571 | 1.155 | 10 |
| 10 | Does benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone have a plane of symmetry? | 大模型 | 6.571 | 7.726 | 1.155 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.73s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 0.99s - 2.15s
步骤 2 |    ########                                                | 1.44s - 2.44s
步骤 3 |        ########                                            | 1.89s - 2.89s
步骤 4 |            ##########                                      | 2.34s - 3.49s
步骤 5 |               #########                                    | 2.78s - 3.78s
步骤 6 |                   #########                                | 3.21s - 4.21s
步骤 7 |                       ##########                           | 3.65s - 4.80s
步骤 8 |                               ##########                   | 4.53s - 5.69s
步骤 9 |                                       ##########           | 5.42s - 6.57s
步骤 10 |                                                 ###########| 6.57s - 7.73s
```

