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
| 规划阶段总时间 (Planner) | 13.921 | 100% |
| 规划过程中启动的任务数 | 1 / 6 | 16.7% |
| 规划与执行重叠的任务数 | 1 / 6 | 16.7% |
| 第一个任务规划完成时间 | 7.534 | - |
| 最后一个任务规划完成时间 | 13.861 | - |
| 最后一个任务执行完成时间 | 45.811 | - |
| 任务总执行时间(累计) | 45.932 | - |
| 流水线加速比 | 1.40x | - |
| 并行效率 | 100.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 45.932 | - |
| 规划模型 | 1 | 18.053 | - |
| 顺序总时间 | - | 63.986 | - |
| 并行总时间 | - | 45.811 | 1.40x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Which gene fits the description of having a central rod domain composed of spectrin-like triple helical repeats that connect the actin cytoskeleton to the sarcolemma and extracellular matrix? | 大模型 | 7.534 | 15.189 | 7.655 | 2 |
| 2 | What is the typical consequence of central exon deletions in this gene, and why do out-of-frame deletions lead to progressive degenerative disease? | 大模型 | 15.189 | 22.845 | 7.655 | 3 |
| 3 | What is a Morpholino antisense oligonucleotide, and by what mechanism does it modulate pre-mRNA splicing to induce exon skipping at a 5' splice site? | 大模型 | 22.845 | 30.500 | 7.655 | 4 |
| 4 | Which molecular structures and components are directly involved in Morpholino-induced exon skipping targeting pre-mRNA in the nucleus (e.g., pre-mRNA, 5' splice site, snRNPs, spliceosome, exons/introns, nuclear compartment)? | 大模型 | 30.500 | 38.155 | 7.655 | 5 |
| 5 | Which cellular structures or pathways are not required or directly involved in this therapy mechanism (e.g., CRISPR-Cas9 genome editing machinery, RNAi RISC complex, RNase H, reverse transcriptase, DNA polymerases, ribosomes, extracellular matrix receptors) and why? | 大模型 | 30.500 | 38.155 | 7.655 | 6 |
| 6 | Given the provided answer options in the original problem, which option corresponds to a structure not involved in Morpholino-mediated exon skipping therapy, based on the involved vs. not-involved sets identified in Steps 4 and 5? | 大模型 | 38.155 | 45.811 | 7.655 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            38.28s
+------------------------------------------------------------+
步骤 1 |############                                                | 7.53s - 15.19s
步骤 2 |            ###########                                     | 15.19s - 22.84s
步骤 3 |                       #############                        | 22.84s - 30.50s
步骤 4 |                                    ############            | 30.50s - 38.16s
步骤 5 |                                    ############            | 30.50s - 38.16s
步骤 6 |                                                ############| 38.16s - 45.81s
```

