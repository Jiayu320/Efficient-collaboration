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
| 规划阶段总时间 (Planner) | 8.463 | 100% |
| 规划过程中启动的任务数 | 10 / 12 | 83.3% |
| 规划与执行重叠的任务数 | 10 / 12 | 83.3% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 8.421 | - |
| 最后一个任务执行完成时间 | 10.530 | - |
| 任务总执行时间(累计) | 12.471 | - |
| 流水线加速比 | 2.83x | - |
| 并行效率 | 118.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 5 | 5.077 | - |
| 大模型任务 | 7 | 7.394 | - |
| 规划模型 | 1 | 17.354 | - |
| 顺序总时间 | - | 29.825 | - |
| 并行总时间 | - | 10.530 | 2.83x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of a molecule with C₃H symmetry? | 小模型 | 1.020 | 2.175 | 1.155 | 2 |
| 2 | How many carbon atoms are in triisopropyl borate? | 小模型 | 1.469 | 2.392 | 0.922 | 3 |
| 3 | How many hydrogen atoms are in triisopropyl borate? | 小模型 | 1.919 | 2.841 | 0.922 | 4 |
| 4 | Is triisopropyl borate a molecule with C₃H symmetry based on its structure? | 大模型 | 2.841 | 3.853 | 1.012 | 5 |
| 5 | What is the structure and molecular formula of quinuclidine? | 小模型 | 3.000 | 4.155 | 1.155 | 6 |
| 6 | Is quinuclidine a molecule with C₃H symmetry based on its structure? | 大模型 | 4.155 | 5.167 | 1.012 | 7 |
| 7 | What is the structure and molecular formula of benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone? | 大模型 | 4.461 | 5.542 | 1.081 | 8 |
| 8 | Is benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone a molecule with C₃H symmetry? | 大模型 | 5.542 | 6.623 | 1.081 | 9 |
| 9 | What is the structure and molecular formula of triphe n y l eno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone? | 大模型 | 6.399 | 7.549 | 1.150 | 10 |
| 10 | Is triphe n y l eno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone a molecule with C₃H symmetry? | 大模型 | 7.549 | 8.630 | 1.081 | 1 |
| 11 | Which molecule(s) among the options have C₃H symmetry? | 大模型 | 8.630 | 9.607 | 0.977 | 2 |
| 12 | What is the final answer to the question? | 小模型 | 9.607 | 10.530 | 0.922 | 3 |

## 理论执行甘特图

```
时间轴:
0                                                            9.51s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.02s - 2.17s
步骤 2 |  ######                                                    | 1.47s - 2.39s
步骤 3 |     ######                                                 | 1.92s - 2.84s
步骤 4 |           ######                                           | 2.84s - 3.85s
步骤 5 |            #######                                         | 3.00s - 4.15s
步骤 6 |                   #######                                  | 4.15s - 5.17s
步骤 7 |                     #######                                | 4.46s - 5.54s
步骤 8 |                            #######                         | 5.54s - 6.62s
步骤 9 |                                 ########                   | 6.40s - 7.55s
步骤 10 |                                         #######            | 7.55s - 8.63s
步骤 11 |                                                ######      | 8.63s - 9.61s
步骤 12 |                                                      ######| 9.61s - 10.53s
```

