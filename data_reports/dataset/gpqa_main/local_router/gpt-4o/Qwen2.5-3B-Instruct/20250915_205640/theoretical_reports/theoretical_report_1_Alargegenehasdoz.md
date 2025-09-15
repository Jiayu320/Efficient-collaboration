# 问题 1 的理论性能分析报告

## 问题描述

A large gene has dozens of exons, of which the central ones code for folded triple helical repeats that connect the cytoskeleton with sarcolemma and extracellular space. Each exon usually codes for one folded triple alpha helix. The most common mutations of the gene are central exon deletions that create out-of-frame peptides and progressive degenerative organ waste. A solution is to deliver a Morpholino that recognizes the 5' end of the out-of-frame exon in pre-mRNA. The molecule prevents binding of the spliceosome and creates exon skipping and in-frame joining. Several missing exons are well tolerated by an organism. Which structure below is not involved in the proposed therapy?

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
| 规划阶段总时间 (Planner) | 3.871 | 100% |
| 规划过程中启动的任务数 | 5 / 6 | 83.3% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 1.090 | - |
| 最后一个任务规划完成时间 | 3.829 | - |
| 最后一个任务执行完成时间 | 5.699 | - |
| 任务总执行时间(累计) | 5.483 | - |
| 流水线加速比 | 2.53x | - |
| 并行效率 | 96.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 5.483 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 14.410 | - |
| 并行总时间 | - | 5.699 | 2.53x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the role of the spliceosome in gene expression and how does it affect exon processing? | 大模型 | 1.090 | 2.033 | 0.943 | 2 |
| 2 | How does Morpholino function as an antisense oligonucleotide in RNA processing? | 大模型 | 2.033 | 2.941 | 0.908 | 3 |
| 3 | What specific RNA sequence does the Morpholino molecule target to achieve exon skipping? | 大模型 | 2.941 | 3.814 | 0.873 | 4 |
| 4 | Which RNA components are directly involved in the recognition and processing of pre-mRNA exons? | 大模型 | 2.941 | 3.849 | 0.908 | 5 |
| 5 | Which RNA structures are typically involved in the splicing process and how might they be affected by Morpholino? | 大模型 | 3.849 | 4.791 | 0.943 | 6 |
| 6 | Considering the question, which RNA structure is not directly involved in the mechanism of the proposed therapy? | 大模型 | 4.791 | 5.699 | 0.908 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.61s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.09s - 2.03s
步骤 2 |            ############                                    | 2.03s - 2.94s
步骤 3 |                        ###########                         | 2.94s - 3.81s
步骤 4 |                        ###########                         | 2.94s - 3.85s
步骤 5 |                                   #############            | 3.85s - 4.79s
步骤 6 |                                                ############| 4.79s - 5.70s
```

