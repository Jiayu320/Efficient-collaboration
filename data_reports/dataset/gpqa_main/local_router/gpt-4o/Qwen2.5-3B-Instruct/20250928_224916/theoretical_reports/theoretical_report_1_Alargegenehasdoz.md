# 问题 1 的理论性能分析报告

## 问题描述

A large gene has dozens of exons, of which the central ones code for folded triple helical repeats that connect the cytoskeleton with sarcolemma and extracellular space. Each exon usually codes for one folded triple alpha helix. The most common mutations of the gene are central exon deletions that create out-of-frame peptides and progressive degenerative organ waste. A solution is to deliver a Morpholino that recognizes the 5' end of the out-of-frame exon in pre-mRNA. The molecule prevents binding of the spliceosome and creates exon skipping and in-frame joining. Several missing exons are well tolerated by an organism. Which structure below is not involved in the proposed therapy?

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
| 规划阶段总时间 (Planner) | 1.668 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 0.967 | - |
| 最后一个任务规划完成时间 | 1.651 | - |
| 最后一个任务执行完成时间 | 4.418 | - |
| 任务总执行时间(累计) | 3.451 | - |
| 流水线加速比 | 2.22x | - |
| 并行效率 | 78.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 3.451 | - |
| 规划模型 | 1 | 6.339 | - |
| 顺序总时间 | - | 9.790 | - |
| 并行总时间 | - | 4.418 | 2.22x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What RNA structural element is specifically targeted by Morpholino oligomers to prevent spliceosome binding at the 5' end of an exon? | 大模型 | 0.967 | 2.186 | 1.219 | 2 |
| 2 | Which structural component is not involved in the therapy: (A) DNA double helix, (B) Spliceosomal protein complex, (C) mRNA secondary structure, or (D) 5' splice site consensus sequence? | 大模型 | 2.186 | 3.337 | 1.150 | 3 |
| 3 | Based on the mechanism of Morpholino action and the involvement of pre-mRNA processing, which option (A, B, C, or D) describes a structure not part of the therapy? | 大模型 | 3.337 | 4.418 | 1.081 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.45s
+------------------------------------------------------------+
步骤 1 |#####################                                       | 0.97s - 2.19s
步骤 2 |                     ####################                   | 2.19s - 3.34s
步骤 3 |                                         ###################| 3.34s - 4.42s
```

