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
| 规划阶段总时间 (Planner) | 5.514 | 100% |
| 规划过程中启动的任务数 | 4 / 10 | 40.0% |
| 规划与执行重叠的任务数 | 4 / 10 | 40.0% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 5.472 | - |
| 最后一个任务执行完成时间 | 9.871 | - |
| 任务总执行时间(累计) | 11.084 | - |
| 流水线加速比 | 2.60x | - |
| 并行效率 | 112.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 10 | 11.084 | - |
| 大模型任务 | 0 | 0.000 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 25.629 | - |
| 并行总时间 | - | 9.871 | 2.60x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the role of the spliceosome in pre-mRNA processing? | 小模型 | 1.020 | 2.175 | 1.155 | 2 |
| 2 | How does the Morpholino molecule specifically target and bind to the 5' end of the out-of-frame exon? | 小模型 | 2.175 | 3.484 | 1.310 | 3 |
| 3 | What effect does Morpholino binding have on the splicing process? | 小模型 | 3.484 | 4.562 | 1.077 | 4 |
| 4 | Which cellular structures are directly involved in the splicing process? | 小模型 | 4.562 | 5.717 | 1.155 | 5 |
| 5 | Which structures are not involved in the splicing process and could remain unaffected by Morpholino? | 小模型 | 5.717 | 6.794 | 1.077 | 6 |
| 6 | Considering the question, what specific structure among the options is not necessary for the proposed therapy? | 小模型 | 6.794 | 8.027 | 1.232 | 7 |
| 7 | Which structures are essential for the splicing process and would be affected if the therapy failed? | 小模型 | 5.717 | 6.872 | 1.155 | 8 |
| 8 | What is the primary goal of the proposed therapy in terms of gene expression? | 小模型 | 8.027 | 9.026 | 1.000 | 9 |
| 9 | Which structure below is not involved in the proposed therapy? | 小模型 | 6.872 | 7.949 | 1.077 | 10 |
| 10 | ? | 小模型 | 9.026 | 9.871 | 0.845 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            8.85s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.02s - 2.17s
步骤 2 |       #########                                            | 2.17s - 3.48s
步骤 3 |                ########                                    | 3.48s - 4.56s
步骤 4 |                        #######                             | 4.56s - 5.72s
步骤 5 |                               ########                     | 5.72s - 6.79s
步骤 7 |                               ########                     | 5.72s - 6.87s
步骤 6 |                                       ########             | 6.79s - 8.03s
步骤 9 |                                       #######              | 6.87s - 7.95s
步骤 8 |                                               #######      | 8.03s - 9.03s
步骤 10 |                                                      ######| 9.03s - 9.87s
```

