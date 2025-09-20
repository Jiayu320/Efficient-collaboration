# 问题 10 的理论性能分析报告

## 问题描述

Square $AIME$ has sides of length $10$ units.  Isosceles triangle $GEM$ has base $EM$ , and the area common to triangle $GEM$ and square $AIME$ is $80$ square units.  Find the length of the altitude to $EM$ in $\triangle GEM$ .

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (claude-3-5-sonnet-latest) | 1.338 | 51.49 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 10.077 | 100% |
| 规划过程中启动的任务数 | 9 / 9 | 100.0% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 2.367 | - |
| 最后一个任务规划完成时间 | 10.019 | - |
| 最后一个任务执行完成时间 | 11.100 | - |
| 任务总执行时间(累计) | 9.245 | - |
| 流水线加速比 | 2.53x | - |
| 并行效率 | 83.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 9.245 | - |
| 规划模型 | 1 | 18.816 | - |
| 顺序总时间 | - | 28.061 | - |
| 并行总时间 | - | 11.100 | 2.53x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the coordinates of the vertices of square AIME if we place it on a coordinate system with A at the origin and sides along the axes? | 大模型 | 2.367 | 3.310 | 0.943 | 2 |
| 2 | Since triangle GEM is isosceles with base EM, what constraint does this place on the location of point G relative to E and M? | 大模型 | 3.319 | 4.296 | 0.977 | 3 |
| 3 | If E and M are vertices of the square, which specific vertices must they be to form a base of the isosceles triangle? | 大模型 | 4.232 | 5.243 | 1.012 | 4 |
| 4 | What is the area of the entire isosceles triangle GEM in terms of the coordinates of G, E, and M? | 大模型 | 5.243 | 6.290 | 1.046 | 5 |
| 5 | What portion of triangle GEM lies outside the square AIME? | 大模型 | 6.290 | 7.371 | 1.081 | 6 |
| 6 | If the area common to triangle GEM and square AIME is 80 square units, and we know the total area of triangle GEM from Step 4, what is the area of the portion of GEM that lies outside the square? | 大模型 | 7.371 | 8.417 | 1.046 | 7 |
| 7 | Using the constraint that the area common to GEM and AIME is 80 square units, what can we determine about the coordinates of point G? | 大模型 | 8.417 | 9.533 | 1.116 | 8 |
| 8 | What is the length of base EM of the isosceles triangle? | 大模型 | 8.951 | 9.893 | 0.943 | 9 |
| 9 | Using the coordinates of G found in Step 7 and the base length from Step 8, what is the length of the altitude from G to base EM? | 大模型 | 10.019 | 11.100 | 1.081 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            8.73s
+------------------------------------------------------------+
步骤 1 |######                                                      | 2.37s - 3.31s
步骤 2 |      #######                                               | 3.32s - 4.30s
步骤 3 |            #######                                         | 4.23s - 5.24s
步骤 4 |                   #######                                  | 5.24s - 6.29s
步骤 5 |                          ########                          | 6.29s - 7.37s
步骤 6 |                                  #######                   | 7.37s - 8.42s
步骤 7 |                                         ########           | 8.42s - 9.53s
步骤 8 |                                             ######         | 8.95s - 9.89s
步骤 9 |                                                    ####### | 10.02s - 11.10s
```

