# 问题 26 的理论性能分析报告

## 问题描述

The experimental proof for the chromosomal theory was obtained from…..

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
| 规划阶段总时间 (Planner) | 3.941 | 100% |
| 规划过程中启动的任务数 | 4 / 8 | 50.0% |
| 规划与执行重叠的任务数 | 4 / 8 | 50.0% |
| 第一个任务规划完成时间 | 0.935 | - |
| 最后一个任务规划完成时间 | 3.899 | - |
| 最后一个任务执行完成时间 | 9.795 | - |
| 任务总执行时间(累计) | 9.937 | - |
| 流水线加速比 | 2.21x | - |
| 并行效率 | 101.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.937 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 21.673 | - |
| 并行总时间 | - | 9.795 | 2.21x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the chromosomal theory of inheritance? | 大模型 | 0.935 | 2.090 | 1.155 | 2 |
| 2 | What experiments were conducted to support this theory? | 大模型 | 2.090 | 3.400 | 1.310 | 3 |
| 3 | Which specific experiment provided key evidence? | 大模型 | 3.400 | 4.633 | 1.232 | 4 |
| 4 | How did this experiment demonstrate the chromosomal theory? | 大模型 | 4.633 | 6.020 | 1.387 | 5 |
| 5 | What were the key findings from this experiment? | 大模型 | 6.020 | 7.252 | 1.232 | 6 |
| 6 | How did the results of this experiment prove the chromosomal theory? | 大模型 | 7.252 | 8.562 | 1.310 | 7 |
| 7 | What is the name of this experiment? | 大模型 | 3.449 | 4.527 | 1.077 | 8 |
| 8 | How did this experiment contribute to our understanding of genetics? | 大模型 | 8.562 | 9.795 | 1.232 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            8.86s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.94s - 2.09s
步骤 2 |       #########                                            | 2.09s - 3.40s
步骤 3 |                #########                                   | 3.40s - 4.63s
步骤 7 |                 #######                                    | 3.45s - 4.53s
步骤 4 |                         #########                          | 4.63s - 6.02s
步骤 5 |                                  ########                  | 6.02s - 7.25s
步骤 6 |                                          #########         | 7.25s - 8.56s
步骤 8 |                                                   #########| 8.56s - 9.79s
```

