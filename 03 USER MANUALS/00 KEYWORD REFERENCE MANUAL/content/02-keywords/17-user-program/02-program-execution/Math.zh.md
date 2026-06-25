---
keyword: Math
summary: 低级用户程序操作码，对数值栈顶执行数学运算。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 206
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 32
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    array_size: 113
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Math

低级用户程序操作码，对数值栈顶执行数学运算。

## 概述

`Math` 是一个低级用户程序关键字。`Math` 周围的语法通常由 PC Suite 在编译期间自动生成，因此很少手动编写。`Math` 对数值栈的顶部一个或两个值执行所请求的操作——操作数必须先压入栈（参见 [PushParam](../03-stack-operation/PushParam.md) 和 [PushConstant](../03-stack-operation/PushConstant.md)），结果再压回栈中。当 `Math` 通过通信调用时，结果也通过通信通道返回。

每种操作存在多种类型变体，由操作索引选择：32 位整数集（下方第一张表中列出的操作），以及更高索引处对应的 32 位浮点数、64 位整数和 64 位双精度浮点数集。编译器选择与操作数类型匹配的变体。超越函数（三角函数、对数、指数、倒数）只在浮点数和双精度变体中有意义——不在整数集上求值。类型转换操作也可用，用于就地在四种数值类型之间转换值。

> **注意：** `Pop1` 是从栈中弹出的第一个值（"栈顶"值）；`Pop2` 是弹出的第二个值。

## 工作原理

索引选择执行哪种操作及操作的数据类型；操作数个数决定弹出多少个值。基础（32 位整数）操作如下：

| 索引 | 操作 | 公式 | 操作数个数 |
|----|----|----|----|
| 1 | 加法 | Result = Pop1 + Pop2 | 2 |
| 2 | 减法 | Result = Pop2 − Pop1 | 2 |
| 3 | 乘法 | Result = Pop1 × Pop2 | 2 |
| 4 | 除法 | Result = Pop2 / Pop1（整数除法；除以 0 为错误） | 2 |
| 5 | 取反 | Result = −Pop1 | 1 |
| 7 | 取模 | Result = Pop2 % Pop1（余数；除以 0 为错误） | 2 |
| 8 | 幂运算 | Result = Pop2 的 Pop1 次方（Pop1 必须 ≥ 0） | 2 |
| 9 | 平方根 | Result = √(Pop1)（Pop1 必须 ≥ 0） | 1 |
| 17 | 按位取反 | Result = ~Pop1 | 1 |
| 18 | 按位与 | Result = Pop2 &amp; Pop1 | 2 |
| 19 | 按位或 | Result = Pop2 \| Pop1 | 2 |
| 20 | 按位异或 | Result = Pop2 ^ Pop1（^ 为异或，同 C 语言） | 2 |
| 21 | 左移 | Result = Pop1 &lt;&lt; Pop2 | 2 |
| 22 | 右移 | Result = Pop1 &gt;&gt; Pop2 | 2 |
| 23 | 绝对值 | Result = abs(Pop1) | 1 |
| 28 | 逻辑与 | Result = (Pop1 != 0) AND (Pop2 != 0) | 2 |
| 29 | 逻辑或 | Result = (Pop1 != 0) OR (Pop2 != 0) | 2 |
| 30 | 逻辑非 | Result = (Pop1 == 0) | 1 |
| 31 | 指针所指值 | Result = 操作码为 Pop1 的参数的值 | 1 |

> **整数集限制：** 倒数（`1 / Pop1`）、三角函数、对数、以 10 为底的对数和指数无整数结果——索引 `6`（倒数）报告"操作未实现"，整数集上的三角/对数索引不产生值。请使用浮点数或双精度变体（见下文）。

> **"指针所指值"（索引 `31`）：** `Pop1` 被视为编码参数引用，所指参数按线程自身的轴选择（[ChooseAxis](ChooseAxis.md)）解析——与 [PushParam](../03-stack-operation/PushParam.md) 和 [PopParam](../03-stack-operation/PopParam.md) 使用的轴解析方式相同。读取前先验证引用：若编码码超出范围、解析出的轴超出范围、数组索引超出该参数范围，或引用指向的是指令或函数而非可读参数，则操作被拒绝。Central-i v5 的类型化集为浮点数、64 位整数和双精度分别添加了"指针所指值"变体，均执行相同的轴解析与验证。

更高的索引范围为其他数据类型重复操作集并添加类型转换。**以下仅适用于 Central-i v5**：在 v4（单机和 Central-i）上，最大操作索引为 `31`，选择 `32` 及以上的任何索引将被拒绝为超出范围的操作。

| 索引范围 | 数据类型/用途 | 适用版本 |
|----|----|----|
| 32–53 | 32 位浮点运算（完整算术、弧度三角函数、对数、以 10 为底对数、指数、双参数反正切、取模、幂、倒数、平方根、绝对值） | 仅 v5 |
| 54–58 | 32 位整数与浮点数互转；浮点数的四舍五入、向下取整和向上取整 | 仅 v5 |
| 59–77 | 64 位整数运算（算术、位运算、移位、逻辑、平方根、绝对值） | 仅 v5 |
| 78–99 | 64 位双精度浮点运算（与浮点集覆盖相同） | 仅 v5 |
| 100–109 | 32 位整数、64 位整数、浮点数和双精度之间的类型转换 | 仅 v5 |
| 110–112 | 双精度的四舍五入、向下取整和向上取整 | 仅 v5 |

整数变体中的值为整数；在浮点数和双精度变体中，操作数和结果携带其浮点表示。确保使用与操作数类型匹配的变体是程序（通常是编译器）的责任。

**结果范围检查。** 每种操作的结果在压入前均针对其结果类型的幅值限制进行检查；若结果超出范围，操作将以运行时"结果超出范围"错误停止，而不是静默地回绕或饱和。在 v4 上，结果以更高精度计算，然后在缩窄并压入前针对有符号 32 位范围（约 ±21 亿）进行测试。在 Central-i v5 上，检查按结果类型进行——32 位整数、64 位整数、32 位浮点数和双精度结果各自针对其类型的幅值限制进行测试。在所有情况下，控制器还在压入结果前验证数值栈有空间，若栈已满则以栈满错误停止。

## 示例

```text
; Compute 3 + 4 (operations normally emitted by the PC Suite compiler)
APushConstant=3      ; push first operand
APushConstant=4      ; push second operand
AMath[1]             ; index 1 = Add (32-bit integer), result 7 is pushed back to the stack
```

## 另请参阅

- [PushParam](../03-stack-operation/PushParam.md) — 将参数值压入数值栈
- [PushConstant](../03-stack-operation/PushConstant.md) — 将常量压入数值栈
- [PopParam](../03-stack-operation/PopParam.md) — 将栈顶值弹出到参数中
- [ProgExpStack](ProgExpStack.md) — 不弹出而读取数值栈顶
