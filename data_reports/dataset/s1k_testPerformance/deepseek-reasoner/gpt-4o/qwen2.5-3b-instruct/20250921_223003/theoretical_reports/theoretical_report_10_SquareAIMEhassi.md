# 问题 10 的理论性能分析报告

## 问题描述

Square $AIME$ has sides of length $10$ units.  Isosceles triangle $GEM$ has base $EM$ , and the area common to triangle $GEM$ and square $AIME$ is $80$ square units.  Find the length of the altitude to $EM$ in $\triangle GEM$ .

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (deepseek-reasoner) | 1.182 | 46.49 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 16.175 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 3.548 | - |
| 最后一个任务规划完成时间 | 16.111 | - |
| 最后一个任务执行完成时间 | 17.254 | - |
| 任务总执行时间(累计) | 8.204 | - |
| 流水线加速比 | 2.17x | - |
| 并行效率 | 47.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 3 | 3.465 | - |
| 大模型任务 | 4 | 4.739 | - |
| 规划模型 | 1 | 29.254 | - |
| 顺序总时间 | - | 37.458 | - |
| 并行总时间 | - | 17.254 | 2.17x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Set up a coordinate system with E at (0,0) and M at (10,0), and the square AIME having vertices at (0,0), (10,0), (10,10), (0,10). Since triangle GEM is isosceles with base EM, place G at (5,g) where g is the altitude to EM and g > 10. What is the coordinates of G? | 小模型 | 3.548 | 4.858 | 1.310 | 2 |
| 2 | Express the height of triangle GEM above the base EM as a function of x. For x in [0,10], h(x) = (g/5) * min(x, 10-x). What is h(x)? | 大模型 | 5.032 | 6.113 | 1.081 | 3 |
| 3 | Find the x-values where the triangle's height h(x) equals the square's height of 10 units. Set (g/5) * min(x,10-x) = 10, so min(x,10-x) = 50/g. Thus, for x in [0,5], x = 50/g, and for x in [5,10], 10-x = 50/g, so x = 10 - 50/g. What are these critical points? | 大模型 | 7.635 | 8.786 | 1.150 | 4 |
| 4 | Compute the area common to the square and triangle by integrating min(10, h(x)) from x=0 to x=10. This is ∫ from 0 to 50/g of (g/5)x dx + ∫ from 50/g to 10-50/g of 10 dx + ∫ from 10-50/g to 10 of (g/5)(10-x) dx. What is the expression for the area? | 大模型 | 10.023 | 11.242 | 1.219 | 5 |
| 5 | Evaluate the integrals. The first integral: (g/5) * (1/2)x^2 from 0 to 50/g = (g/10)(50/g)^2 = 250/g. Similarly, the third integral: (g/10)(50/g)^2 = 250/g. The second integral: 10 * ( (10-50/g) - (50/g) ) = 10 * (10 - 100/g) = 100 - 1000/g. Total area = 250/g + 100 - 1000/g + 250/g = 100 - 500/g. What is the total area? | 大模型 | 13.379 | 14.667 | 1.289 | 6 |
| 6 | Set the common area equal to 80: 100 - 500/g = 80. Solve for g: 100 - 80 = 500/g, so 20 = 500/g, thus g = 500/20 = 25. What is the value of g? | 小模型 | 15.100 | 16.254 | 1.155 | 7 |
| 7 | The length of the altitude to EM in triangle GEM is g, which is 25 units. What is the final answer? | 小模型 | 16.254 | 17.254 | 1.000 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            13.71s
+------------------------------------------------------------+
步骤 1 |#####                                                       | 3.55s - 4.86s
步骤 2 |      #####                                                 | 5.03s - 6.11s
步骤 3 |                 #####                                      | 7.64s - 8.79s
步骤 4 |                            #####                           | 10.02s - 11.24s
步骤 5 |                                           #####            | 13.38s - 14.67s
步骤 6 |                                                  #####     | 15.10s - 16.25s
步骤 7 |                                                       #####| 16.25s - 17.25s
```

