# 问题 10 的理论性能分析报告

## 问题描述

Square $AIME$ has sides of length $10$ units.  Isosceles triangle $GEM$ has base $EM$ , and the area common to triangle $GEM$ and square $AIME$ is $80$ square units.  Find the length of the altitude to $EM$ in $\triangle GEM$ .

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (deepseek-chat) | 1.600 | 31.97 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 12.954 | 100% |
| 规划过程中启动的任务数 | 6 / 6 | 100.0% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 3.445 | - |
| 最后一个任务规划完成时间 | 12.861 | - |
| 最后一个任务执行完成时间 | 14.011 | - |
| 任务总执行时间(累计) | 6.992 | - |
| 流水线加速比 | 2.53x | - |
| 并行效率 | 49.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 5 | 5.682 | - |
| 规划模型 | 1 | 28.438 | - |
| 顺序总时间 | - | 35.429 | - |
| 并行总时间 | - | 14.011 | 2.53x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Since EM is both the base of the isosceles triangle and a side of the square, and the triangle is isosceles, where must vertex G be located relative to the square? | 小模型 | 3.445 | 4.755 | 1.310 | 2 |
| 2 | The area common to the triangle and square is 80, meaning 20 units of the square are outside the triangle. What portion of the square is this, and where is it located relative to the triangle's boundary? | 大模型 | 5.479 | 6.560 | 1.081 | 3 |
| 3 | For an isosceles triangle with base EM of length 10 and altitude h, what is the equation of the line from vertex G to the right endpoint of EM? | 大模型 | 7.136 | 8.217 | 1.081 | 4 |
| 4 | Using the equation from Step 3, at what height y above EM does the triangle's boundary intersect the vertical line at x=5 (the right edge of the left half of the square)? | 大模型 | 9.044 | 10.195 | 1.150 | 5 |
| 5 | The area of the square above the triangle's boundary can be found by integration. For the right half of the square (x from 5 to 10), what is the area above the triangle's boundary? | 大模型 | 11.078 | 12.297 | 1.219 | 6 |
| 6 | Due to symmetry, the total area outside the triangle is twice the area found in Step 5. Set this equal to 20 and solve for the altitude h of the triangle. | 大模型 | 12.861 | 14.011 | 1.150 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            10.57s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 3.45s - 4.76s
步骤 2 |           ######                                           | 5.48s - 6.56s
步骤 3 |                    #######                                 | 7.14s - 8.22s
步骤 4 |                               #######                      | 9.04s - 10.19s
步骤 5 |                                           #######          | 11.08s - 12.30s
步骤 6 |                                                     #######| 12.86s - 14.01s
```

