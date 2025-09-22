# 问题 10 的理论性能分析报告

## 问题描述

Square $AIME$ has sides of length $10$ units.  Isosceles triangle $GEM$ has base $EM$ , and the area common to triangle $GEM$ and square $AIME$ is $80$ square units.  Find the length of the altitude to $EM$ in $\triangle GEM$ .

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (openai/gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 13.268 | 100% |
| 规划过程中启动的任务数 | 4 / 4 | 100.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 8.918 | - |
| 最后一个任务规划完成时间 | 13.209 | - |
| 最后一个任务执行完成时间 | 20.864 | - |
| 任务总执行时间(累计) | 30.622 | - |
| 流水线加速比 | 2.62x | - |
| 并行效率 | 146.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 4 | 30.622 | - |
| 规划模型 | 1 | 24.143 | - |
| 顺序总时间 | - | 54.765 | - |
| 并行总时间 | - | 20.864 | 2.62x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Adopt coordinates with E=(0,0), M=(10,0), square region S={ (x,y): 0≤x≤10, 0≤y≤10 }, and apex G=(5,h) (h>0) so triangle GEM is isosceles with base EM; using points (0,0)→(5,h) and (10,0)→(5,h), what are x_left(y) and x_right(y), and hence w(y)=x_right−x_left? | 大模型 | 8.918 | 16.573 | 7.655 | 2 |
| 2 | Using w(y) from Step 1, express the overlap area A(h) between the triangle and the square as a piecewise function: if h≤10, A(h)=(1/2)·10·h=5h; if h≥10, A(h)=∫₀¹⁰ [10−(10/h)y] dy=100−500/h; are these two formulas correct? | 大模型 | 10.915 | 18.570 | 7.655 | 3 |
| 3 | Impose the condition A(h)=80; first test the h≤10 branch: solve 5h=80 to get h=16 and check consistency with h≤10—does this contradiction force h>10? | 大模型 | 12.180 | 19.836 | 7.655 | 4 |
| 4 | Use the h≥10 branch from Step 2: set 100−500/h=80 and solve for h; what is the resulting altitude length h? | 大模型 | 13.209 | 20.864 | 7.655 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            11.95s
+------------------------------------------------------------+
步骤 1 |######################################                      | 8.92s - 16.57s
步骤 2 |          ######################################            | 10.91s - 18.57s
步骤 3 |                ######################################      | 12.18s - 19.84s
步骤 4 |                     #######################################| 13.21s - 20.86s
```

