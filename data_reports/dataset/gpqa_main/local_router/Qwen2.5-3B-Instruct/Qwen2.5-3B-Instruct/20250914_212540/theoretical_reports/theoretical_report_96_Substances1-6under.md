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
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.360 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 6 / 9 | 66.7% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 5.317 | - |
| 最后一个任务执行完成时间 | 8.506 | - |
| 任务总执行时间(累计) | 9.619 | - |
| 流水线加速比 | 2.68x | - |
| 并行效率 | 113.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 9.619 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 22.760 | - |
| 并行总时间 | - | 8.506 | 2.68x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the general rule for electrophilic substitution at the meta position in aromatic compounds? | 大模型 | 1.062 | 2.217 | 1.155 | 2 |
| 2 | Which of the given compounds have electron-donating groups that stabilize the positive charge? | 大模型 | 1.581 | 2.659 | 1.077 | 3 |
| 3 | Which of the given compounds have electron-withdrawing groups that destabilize the positive charge? | 大模型 | 2.115 | 3.193 | 1.077 | 4 |
| 4 | Which compounds are activated (electron-donating) at the meta position? | 大模型 | 2.659 | 3.659 | 1.000 | 5 |
| 5 | Which compounds are deactivated (electron-withdrawing) at the meta position? | 大模型 | 3.197 | 4.197 | 1.000 | 6 |
| 6 | What is the relative meta-directing ability of the groups in each compound? | 大模型 | 4.197 | 5.351 | 1.155 | 7 |
| 7 | What is the relative order of the meta-directing ability of the groups in the six compounds? | 大模型 | 5.351 | 6.429 | 1.077 | 8 |
| 8 | What is the order of increasing para-isomer yield based on meta-directing ability? | 大模型 | 6.429 | 7.506 | 1.077 | 9 |
| 9 | What is the final order of increasing weight fraction of para-isomer? | 大模型 | 7.506 | 8.506 | 1.000 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            7.44s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.06s - 2.22s
步骤 2 |    ########                                                | 1.58s - 2.66s
步骤 3 |        #########                                           | 2.12s - 3.19s
步骤 4 |            ########                                        | 2.66s - 3.66s
步骤 5 |                 ########                                   | 3.20s - 4.20s
步骤 6 |                         #########                          | 4.20s - 5.35s
步骤 7 |                                  #########                 | 5.35s - 6.43s
步骤 8 |                                           ########         | 6.43s - 7.51s
步骤 9 |                                                   #########| 7.51s - 8.51s
```

