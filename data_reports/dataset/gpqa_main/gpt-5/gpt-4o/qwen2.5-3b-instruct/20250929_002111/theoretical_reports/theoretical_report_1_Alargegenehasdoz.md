# 问题 1 的理论性能分析报告

## 问题描述

A large gene has dozens of exons, of which the central ones code for folded triple helical repeats that connect the cytoskeleton with sarcolemma and extracellular space. Each exon usually codes for one folded triple alpha helix. The most common mutations of the gene are central exon deletions that create out-of-frame peptides and progressive degenerative organ waste. A solution is to deliver a Morpholino that recognizes the 5' end of the out-of-frame exon in pre-mRNA. The molecule prevents binding of the spliceosome and creates exon skipping and in-frame joining. Several missing exons are well tolerated by an organism. Which structure below is not involved in the proposed therapy?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 11.172 | 100% |
| 规划过程中启动的任务数 | 4 / 5 | 80.0% |
| 规划与执行重叠的任务数 | 4 / 5 | 80.0% |
| 第一个任务规划完成时间 | 7.316 | - |
| 最后一个任务规划完成时间 | 11.113 | - |
| 最后一个任务执行完成时间 | 13.167 | - |
| 任务总执行时间(累计) | 6.851 | - |
| 流水线加速比 | 2.05x | - |
| 并行效率 | 52.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.155 | - |
| 大模型任务 | 3 | 4.696 | - |
| 规划模型 | 1 | 20.110 | - |
| 顺序总时间 | - | 26.961 | - |
| 并行总时间 | - | 13.167 | 2.05x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the detailed mechanism by which Morpholino antisense oligonucleotides induce exon skipping in pre-mRNA splicing? | 大模型 | 7.316 | 8.882 | 1.565 | 2 |
| 2 | Based on the mechanism from Step 1, which cellular molecules and complexes are directly required or interacted with during this therapy (e.g., types of RNA, splice sites, nuclear machinery)? | 大模型 | 8.882 | 10.447 | 1.565 | 3 |
| 3 | What are the specific candidate structures listed in the answer options that need to be evaluated for involvement in the proposed therapy? | 小模型 | 9.333 | 10.333 | 1.000 | 4 |
| 4 | For each candidate structure from Step 3, does it directly participate in or is it required by the mechanism/components identified in Step 2? | 大模型 | 10.447 | 12.013 | 1.565 | 5 |
| 5 | Which candidate structure(s) identified in Step 4 are not involved in the proposed therapy? | 小模型 | 12.013 | 13.167 | 1.155 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            5.85s
+------------------------------------------------------------+
步骤 1 |################                                            | 7.32s - 8.88s
步骤 2 |                ################                            | 8.88s - 10.45s
步骤 3 |                    ##########                              | 9.33s - 10.33s
步骤 4 |                                ################            | 10.45s - 12.01s
步骤 5 |                                                ############| 12.01s - 13.17s
```

