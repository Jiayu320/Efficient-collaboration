# 问题 96 的理论性能分析报告

## 问题描述

Substances 1-6 undergo an electrophilic substitution reaction with an excess of bromine (it is assumed that only one monobromo derivative is formed):
1) С6H5-CH3
2) C6H5-COOC2H5
3) C6H5-Cl
4) C6H5-NO2
5) C6H5-C2H5
6) C6H5-COOH
C6H5 - means benzene ring
Arrange the substances in order of increasing the weight fraction of the yield of the para-isomer.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.697 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 1.102 | - |
| 最后一个任务规划完成时间 | 1.676 | - |
| 最后一个任务执行完成时间 | 24.068 | - |
| 任务总执行时间(累计) | 22.966 | - |
| 流水线加速比 | 1.05x | - |
| 并行效率 | 95.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 22.966 | - |
| 规划模型 | 1 | 2.209 | - |
| 顺序总时间 | - | 25.175 | - |
| 并行总时间 | - | 24.068 | 1.05x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine the type of substituent on each benzene ring and its effect (activating or deactivating, and ortho/para or meta directing) | 大模型 | 1.102 | 8.757 | 7.655 | 2 |
| 2 | Consider the electronic effects of each substituent that affect the yield of the para-isomer | 大模型 | 8.757 | 16.413 | 7.655 | 3 |
| 3 | Rank the substances based on these effects to determine the order of increasing weight fraction of the para-isomer | 大模型 | 16.413 | 24.068 | 7.655 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            22.97s
+------------------------------------------------------------+
步骤 1 |####################                                        | 1.10s - 8.76s
步骤 2 |                    ####################                    | 8.76s - 16.41s
步骤 3 |                                        ####################| 16.41s - 24.07s
```

