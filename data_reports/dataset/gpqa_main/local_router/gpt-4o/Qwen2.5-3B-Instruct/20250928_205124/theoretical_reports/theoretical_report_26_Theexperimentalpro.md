# 问题 26 的理论性能分析报告

## 问题描述

The experimental proof for the chromosomal theory was obtained from…..

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.559 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 0.929 | - |
| 最后一个任务规划完成时间 | 1.543 | - |
| 最后一个任务执行完成时间 | 4.609 | - |
| 任务总执行时间(累计) | 3.680 | - |
| 流水线加速比 | 1.92x | - |
| 并行效率 | 79.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 2 | 2.370 | - |
| 规划模型 | 1 | 5.160 | - |
| 顺序总时间 | - | 8.840 | - |
| 并行总时间 | - | 4.609 | 1.92x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Which organism was central to the experiments that revealed genetic linkage between traits, as demonstrated by Thomas Hunt Morgan? | 小模型 | 0.929 | 2.239 | 1.310 | 2 |
| 2 | What specific experimental observation in Step 1 showed that certain traits (e.g., white eyes and vestigial wings) did not assort independently, violating Mendel's law of independent assortment? | 大模型 | 2.239 | 3.389 | 1.150 | 3 |
| 3 | Given the observation in Step 2, what was the experimental outcome that directly supported the chromosomal theory of inheritance, as this linkage provided concrete evidence genes are located on chromosomes? | 大模型 | 3.389 | 4.609 | 1.219 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.68s
+------------------------------------------------------------+
步骤 1 |#####################                                       | 0.93s - 2.24s
步骤 2 |                     ###################                    | 2.24s - 3.39s
步骤 3 |                                        ####################| 3.39s - 4.61s
```

