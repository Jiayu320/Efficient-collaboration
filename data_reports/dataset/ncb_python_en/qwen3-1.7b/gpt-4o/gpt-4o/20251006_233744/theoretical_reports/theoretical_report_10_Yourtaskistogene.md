# 问题 10 的理论性能分析报告

## 问题描述

Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Write a program that implements the function of converting a string from UTF-8 encoding to ASCII encoding. The requirements are as follows:

Input a string (UTF-8 encoding).
The program will read the input string character by character and convert each character into the corresponding ASCII code.
Print out the converted ASCII codes one by one.
You can use an appropriate programming language to implement this function. Please note that multi-byte characters in UTF-8 encoding need to be specially handled to ensure correct conversion to the corresponding ASCII code. After calling the utf8_to_ascii function, an ASCII code list will be output, each element of which corresponds to the ASCII code of a character in the input string.

For example, if the input string is "Hello World!", after calling the utf8_to_ascii function, the following ASCII code list will be output:

[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
Where the first element 72 corresponds to the ASCII code of the character H, the second element 101 corresponds to the ASCII code of the character e, and so on.

These ASCII codes can be further used for other operations, such as encryption, conversion, etc.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testutf8_to_ascii:
    def test_hello_world(self):
        assert utf8_to_ascii("Hello, World!") == [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]



Write a program that implements the function of converting a string from UTF-8 encoding to ASCII encoding. The requirements are as follows:

Input a string (UTF-8 encoding).
The program will read the input string character by character and convert each character into the corresponding ASCII code.
Print out the converted ASCII codes one by one.
You can use an appropriate programming language to implement this function. Please note that multi-byte characters in UTF-8 encoding need to be specially handled to ensure correct conversion to the corresponding ASCII code. After calling the utf8_to_ascii function, an ASCII code list will be output, each element of which corresponds to the ASCII code of a character in the input string.

For example, if the input string is "Hello World!", after calling the utf8_to_ascii function, the following ASCII code list will be output:

[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
Where the first element 72 corresponds to the ASCII code of the character H, the second element 101 corresponds to the ASCII code of the character e, and so on.

These ASCII codes can be further used for other operations, such as encryption, conversion, etc.

Test case:


class Testutf8_to_ascii:
    def test_empty_string(self):
        assert utf8_to_ascii("") == None

    def test_invalid_hex_code(self):
        assert utf8_to_ascii("Hello%20Wo%zz") == None

    def test_single_character(self):
        assert utf8_to_ascii("A") == [65]

    def test_special_characters(self):
        assert utf8_to_ascii("!@#$%^&*()_+-=") == [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43, 45, 61]

    def test_unicode_characters(self):
        assert utf8_to_ascii("\u2018\u2019\u201c\u201d") == [8216, 8217, 8220, 8221]

    def test_long_string(self):
        assert utf8_to_ascii("a" * 1000) == [97] * 1000

    def test_invalid_input_type(self):
        assert utf8_to_ascii(123) == None

    def test_invalid_input_encoding(self):
        assert utf8_to_ascii(b"Hello%20World%21") == None


# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (qwen3-1.7b) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.440 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 0.972 | - |
| 最后一个任务规划完成时间 | 1.423 | - |
| 最后一个任务执行完成时间 | 4.908 | - |
| 任务总执行时间(累计) | 3.935 | - |
| 流水线加速比 | 1.10x | - |
| 并行效率 | 80.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.508 | - |
| 大模型任务 | 1 | 1.427 | - |
| 规划模型 | 1 | 1.450 | - |
| 顺序总时间 | - | 5.386 | - |
| 并行总时间 | - | 4.908 | 1.10x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | To assist the following agents, what is your understanding of the question after reviewing it, focusing only on essential information and filtering out all irrelevant details? | 小模型 | 0.972 | 2.053 | 1.081 | 2 |
| 2 | Implement a function that converts a UTF-8 string to ASCII, handling multi-byte characters correctly. | 大模型 | 2.053 | 3.481 | 1.427 | 3 |
| 3 | After reviewing the original question and the thoughts of previous agents, what is the final answer to the question? | 小模型 | 3.481 | 4.908 | 1.427 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.94s
+------------------------------------------------------------+
步骤 1 |################                                            | 0.97s - 2.05s
步骤 2 |                ######################                      | 2.05s - 3.48s
步骤 3 |                                      ######################| 3.48s - 4.91s
```

