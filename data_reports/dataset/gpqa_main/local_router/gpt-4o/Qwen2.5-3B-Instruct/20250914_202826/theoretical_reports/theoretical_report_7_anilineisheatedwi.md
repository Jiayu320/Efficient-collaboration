# 问题 7 的理论性能分析报告

## 问题描述

aniline is heated with sulfuric acid, forming product 1.

1 is treated with sodium bicarbonate, followed by sodium nitrite and HCl, forming product 2.

2 is allowed to react with 2-napthol, forming final product 3.

how many distinct nonexchaning hydrogen signals are there in the 1H nmr spectrum of 3?


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
| 规划阶段总时间 (Planner) | 3.688 | 100% |
| 规划过程中启动的任务数 | 4 / 6 | 66.7% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 3.646 | - |
| 最后一个任务执行完成时间 | 5.884 | - |
| 任务总执行时间(累计) | 5.898 | - |
| 流水线加速比 | 2.52x | - |
| 并行效率 | 100.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 5.898 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 14.825 | - |
| 并行总时间 | - | 5.884 | 2.52x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What functional groups are present in product 3? | 大模型 | 0.963 | 1.906 | 0.943 | 2 |
| 2 | What structural differences exist between product 2 and product 3? | 大模型 | 1.906 | 2.918 | 1.012 | 3 |
| 3 | How does the nitro group in product 2 affect hydrogen signals in NMR? | 大模型 | 2.918 | 3.895 | 0.977 | 4 |
| 4 | How does the hydroxyl group in 2-napthol affect hydrogen signals in NMR? | 大模型 | 2.918 | 3.895 | 0.977 | 5 |
| 5 | How many distinct types of hydrogens are present in product 3? | 大模型 | 3.895 | 4.907 | 1.012 | 6 |
| 6 | How many distinct non-exchanging hydrogen signals are there in the 1H NMR spectrum of 3? | 大模型 | 4.907 | 5.884 | 0.977 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.92s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.96s - 1.91s
步骤 2 |           ############                                     | 1.91s - 2.92s
步骤 3 |                       ############                         | 2.92s - 3.90s
步骤 4 |                       ############                         | 2.92s - 3.90s
步骤 5 |                                   #############            | 3.90s - 4.91s
步骤 6 |                                                ############| 4.91s - 5.88s
```

