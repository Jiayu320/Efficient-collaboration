# 问题 1 的理论性能分析报告

## 问题描述

A large gene has dozens of exons, of which the central ones code for folded triple helical repeats that connect the cytoskeleton with sarcolemma and extracellular space. Each exon usually codes for one folded triple alpha helix. The most common mutations of the gene are central exon deletions that create out-of-frame peptides and progressive degenerative organ waste. A solution is to deliver a Morpholino that recognizes the 5' end of the out-of-frame exon in pre-mRNA. The molecule prevents binding of the spliceosome and creates exon skipping and in-frame joining. Several missing exons are well tolerated by an organism. Which structure below is not involved in the proposed therapy?

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
| 规划阶段总时间 (Planner) | 2.986 | 100% |
| 规划过程中启动的任务数 | 3 / 5 | 60.0% |
| 规划与执行重叠的任务数 | 3 / 5 | 60.0% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 2.944 | - |
| 最后一个任务执行完成时间 | 5.700 | - |
| 任务总执行时间(累计) | 6.239 | - |
| 流水线加速比 | 2.41x | - |
| 并行效率 | 109.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 6.239 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 13.762 | - |
| 并行总时间 | - | 5.700 | 2.41x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the central mechanism of the proposed therapy involving Morpholino? | 大模型 | 1.020 | 2.330 | 1.310 | 2 |
| 2 | What are the key components of the pre-mRNA process that the Morpholino targets? | 大模型 | 2.330 | 3.562 | 1.232 | 3 |
| 3 | What is the role of spliceosomes in RNA processing? | 大模型 | 2.003 | 3.158 | 1.155 | 4 |
| 4 | Which RNA structures are typically involved in exon recognition and splicing? | 大模型 | 3.158 | 4.390 | 1.232 | 5 |
| 5 | Which structure is not involved in the proposed therapy mechanism? | 大模型 | 4.390 | 5.700 | 1.310 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.68s
+------------------------------------------------------------+
步骤 1 |################                                            | 1.02s - 2.33s
步骤 3 |            ###############                                 | 2.00s - 3.16s
步骤 2 |                ################                            | 2.33s - 3.56s
步骤 4 |                           ################                 | 3.16s - 4.39s
步骤 5 |                                           #################| 4.39s - 5.70s
```

