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
| 规划阶段总时间 (Planner) | 6.539 | 100% |
| 规划过程中启动的任务数 | 10 / 11 | 90.9% |
| 规划与执行重叠的任务数 | 10 / 11 | 90.9% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 6.497 | - |
| 最后一个任务执行完成时间 | 7.870 | - |
| 任务总执行时间(累计) | 10.057 | - |
| 流水线加速比 | 3.30x | - |
| 并行效率 | 127.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 11 | 10.057 | - |
| 规划模型 | 1 | 15.949 | - |
| 顺序总时间 | - | 26.007 | - |
| 并行总时间 | - | 7.870 | 3.30x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of C3H symmetry? | 大模型 | 0.963 | 1.837 | 0.873 | 2 |
| 2 | How many carbon atoms and hydrogen atoms are in each molecule? | 大模型 | 1.413 | 2.356 | 0.943 | 3 |
| 3 | What structural features indicate C3H symmetry in molecules? | 大模型 | 1.862 | 2.770 | 0.908 | 4 |
| 4 | What is the structure of triisopropyl borate? | 大模型 | 2.298 | 3.240 | 0.943 | 5 |
| 5 | Does triisopropyl borate have C3H symmetry? | 大模型 | 3.240 | 4.148 | 0.908 | 6 |
| 6 | What is the structure of quinuclidine? | 大模型 | 3.239 | 4.112 | 0.873 | 7 |
| 7 | Does quinuclidine have C3H symmetry? | 大模型 | 4.112 | 5.020 | 0.908 | 8 |
| 8 | What structural features does benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone have? | 大模型 | 4.615 | 5.558 | 0.943 | 9 |
| 9 | Does this molecule have C3H symmetry? | 大模型 | 5.558 | 6.466 | 0.908 | 10 |
| 10 | What structural features does tripheanyleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone have? | 大模型 | 6.020 | 6.962 | 0.943 | 1 |
| 11 | Does this molecule have C3H symmetry? | 大模型 | 6.962 | 7.870 | 0.908 | 2 |

## 理论执行甘特图

```
时间轴:
0                                                            6.91s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.96s - 1.84s
步骤 2 |   #########                                                | 1.41s - 2.36s
步骤 3 |       ########                                             | 1.86s - 2.77s
步骤 4 |           ########                                         | 2.30s - 3.24s
步骤 6 |                   ########                                 | 3.24s - 4.11s
步骤 5 |                   ########                                 | 3.24s - 4.15s
步骤 7 |                           ########                         | 4.11s - 5.02s
步骤 8 |                               ########                     | 4.62s - 5.56s
步骤 9 |                                       ########             | 5.56s - 6.47s
步骤 10 |                                           #########        | 6.02s - 6.96s
步骤 11 |                                                    ########| 6.96s - 7.87s
```

