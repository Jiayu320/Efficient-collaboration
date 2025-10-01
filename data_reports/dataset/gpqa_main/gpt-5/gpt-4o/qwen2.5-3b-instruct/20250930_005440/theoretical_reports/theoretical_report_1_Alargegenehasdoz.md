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
| 规划阶段总时间 (Planner) | 14.375 | 100% |
| 规划过程中启动的任务数 | 2 / 7 | 28.6% |
| 规划与执行重叠的任务数 | 2 / 7 | 28.6% |
| 第一个任务规划完成时间 | 7.593 | - |
| 最后一个任务规划完成时间 | 14.316 | - |
| 最后一个任务执行完成时间 | 57.037 | - |
| 任务总执行时间(累计) | 70.650 | - |
| 流水线加速比 | 1.57x | - |
| 并行效率 | 123.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 32.373 | - |
| 大模型任务 | 5 | 38.277 | - |
| 规划模型 | 1 | 18.745 | - |
| 顺序总时间 | - | 89.396 | - |
| 并行总时间 | - | 57.037 | 1.57x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Which gene and protein are being described by the passage that references dozens of exons, central triple helical repeats, and linkage of the cytoskeleton to the sarcolemma and extracellular space? | 大模型 | 7.593 | 15.248 | 7.655 | 2 |
| 2 | What is the molecular consequence of central exon deletions that create out-of-frame peptides in this gene, and how does this lead to disease pathology? | 大模型 | 15.248 | 22.904 | 7.655 | 3 |
| 3 | What is a Morpholino antisense oligonucleotide, and where in the cell does it act? | 小模型 | 9.353 | 25.540 | 16.187 | 4 |
| 4 | How does a Morpholino targeting the 5' end of an out-of-frame exon induce exon skipping and restore an in-frame mRNA—what are the key steps and splicing components involved? | 大模型 | 25.540 | 33.195 | 7.655 | 5 |
| 5 | Which cellular molecules and structures are directly involved in the mechanism of Morpholino-mediated exon skipping (e.g., pre-mRNA, 5' splice site, spliceosome/snRNPs, nucleus)? | 大模型 | 33.195 | 40.850 | 7.655 | 6 |
| 6 | Which common gene-editing, DNA replication, reverse transcription, translation, or extracellular structures are not required for this therapy (e.g., CRISPR-Cas9, DNA polymerase, reverse transcriptase, ribosome, extracellular matrix)? | 大模型 | 33.195 | 40.850 | 7.655 | 7 |
| 7 | Given the provided answer options, which structure is not involved in the proposed Morpholino exon-skipping therapy based on the inclusion list from Step 5 and exclusion list from Step 6? | 小模型 | 40.850 | 57.037 | 16.187 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            49.44s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 7.59s - 15.25s
步骤 3 |  ###################                                       | 9.35s - 25.54s
步骤 2 |         #########                                          | 15.25s - 22.90s
步骤 4 |                     ##########                             | 25.54s - 33.19s
步骤 5 |                               #########                    | 33.19s - 40.85s
步骤 6 |                               #########                    | 33.19s - 40.85s
步骤 7 |                                        ####################| 40.85s - 57.04s
```

