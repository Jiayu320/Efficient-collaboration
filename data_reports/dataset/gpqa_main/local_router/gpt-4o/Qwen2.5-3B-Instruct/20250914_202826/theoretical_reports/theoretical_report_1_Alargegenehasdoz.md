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
| 规划阶段总时间 (Planner) | 3.843 | 100% |
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 3.801 | - |
| 最后一个任务执行完成时间 | 5.931 | - |
| 任务总执行时间(累计) | 7.083 | - |
| 流水线加速比 | 2.94x | - |
| 并行效率 | 119.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 7.083 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 17.414 | - |
| 并行总时间 | - | 5.931 | 2.94x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the central mechanism of the proposed therapy? | 大模型 | 0.963 | 2.045 | 1.081 | 2 |
| 2 | Which components of the gene are affected by the central exon deletions? | 大模型 | 2.045 | 3.056 | 1.012 | 3 |
| 3 | What is the function of pre-mRNA in gene expression? | 大模型 | 1.890 | 2.833 | 0.943 | 4 |
| 4 | How does the Morpholino molecule specifically target the 5' end of the out-of-frame exon? | 大模型 | 2.480 | 3.527 | 1.046 | 5 |
| 5 | What cellular processes are disrupted by the spliceosome binding? | 大模型 | 2.930 | 3.942 | 1.012 | 6 |
| 6 | Which cellular structures are typically involved in mRNA splicing? | 大模型 | 3.942 | 4.953 | 1.012 | 7 |
| 7 | Which structure is not involved in the proposed therapy? | 大模型 | 4.953 | 5.931 | 0.977 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            4.97s
+------------------------------------------------------------+
步骤 1 |#############                                               | 0.96s - 2.04s
步骤 3 |           ###########                                      | 1.89s - 2.83s
步骤 2 |             ############                                   | 2.04s - 3.06s
步骤 4 |                  ############                              | 2.48s - 3.53s
步骤 5 |                       ############                         | 2.93s - 3.94s
步骤 6 |                                   #############            | 3.94s - 4.95s
步骤 7 |                                                ############| 4.95s - 5.93s
```

