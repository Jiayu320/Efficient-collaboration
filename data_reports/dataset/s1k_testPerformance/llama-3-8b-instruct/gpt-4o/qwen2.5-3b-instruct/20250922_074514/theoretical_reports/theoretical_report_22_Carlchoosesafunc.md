# 问题 22 的理论性能分析报告

## 问题描述

Carl chooses a *functional expression**  $E$  which is a finite nonempty string formed from a set  $x_1, x_2, \dots$  of variables and applications of a function  $f$ , together with addition, subtraction, multiplication (but not division), and fixed real constants. He then considers the equation  $E = 0$ , and lets  $S$  denote the set of functions  $f \colon \mathbb R \to \mathbb R$  such that the equation holds for any choices of real numbers  $x_1, x_2, \dots$ . (For example, if Carl chooses the functional equation  $$  f(2f(x_1)+x_2) - 2f(x_1)-x_2 = 0,  $$  then  $S$  consists of one function, the identity function.

(a) Let  $X$  denote the set of functions with domain  $\mathbb R$  and image exactly  $\mathbb Z$ . Show that Carl can choose his functional equation such that  $S$  is nonempty but  $S \subseteq X$ .

(b) Can Carl choose his functional equation such that  $|S|=1$  and  $S \subseteq X$ ?

*These can be defined formally in the following way: the set of functional expressions is the minimal one (by inclusion) such that (i) any fixed real constant is a functional expression, (ii) for any positive integer  $i$ , the variable  $x_i$  is a functional expression, and (iii) if  $V$  and  $W$  are functional expressions, then so are  $f(V)$ ,  $V+W$ ,  $V-W$ , and  $V \cdot W$ .

*Proposed by Carl Schildkraut*

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (meta-llama/llama-3-8b-instruct) | 0.645 | 86.95 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.578 | 100% |
| 规划过程中启动的任务数 | 3 / 4 | 75.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 1.335 | - |
| 最后一个任务规划完成时间 | 3.543 | - |
| 最后一个任务执行完成时间 | 5.370 | - |
| 任务总执行时间(累计) | 4.035 | - |
| 流水线加速比 | 1.94x | - |
| 并行效率 | 75.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.000 | - |
| 大模型任务 | 3 | 3.035 | - |
| 规划模型 | 1 | 6.407 | - |
| 顺序总时间 | - | 10.443 | - |
| 并行总时间 | - | 5.370 | 1.94x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Create a functional expression that involves only addition and multiplication of variables and functions. For example, let E = f(x_1*x_2) + x_3*x_4. | 小模型 | 1.335 | 2.335 | 1.000 | 2 |
| 2 | Make the functional expression symmetric by using the fact that f(x*y) = f(x)*f(y). | 大模型 | 2.335 | 3.347 | 1.012 | 3 |
| 3 | Construct the functional expression in such a way that it has a unique solution in the set of functions with integer values. For example, let E = f(x_1*x_2) + f(x_3*x_4). | 大模型 | 3.347 | 4.359 | 1.012 | 4 |
| 4 | Verify that the solution is indeed in the set of functions with integer values. For example, let f(x) = x mod 1. This function satisfies the equation E = 0 for any choice of real numbers x_1, x_2, x_3, and x_4. | 大模型 | 4.359 | 5.370 | 1.012 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            4.04s
+------------------------------------------------------------+
步骤 1 |##############                                              | 1.34s - 2.34s
步骤 2 |              ###############                               | 2.34s - 3.35s
步骤 3 |                             ###############                | 3.35s - 4.36s
步骤 4 |                                            ################| 4.36s - 5.37s
```

