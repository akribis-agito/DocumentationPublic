---
keyword: ProgExpStack
summary: 在不弹出数值（表达式）栈的情况下读取其上的值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 204
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 51
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgExpStack

在不弹出数值（表达式）栈的情况下读取其上的值。

## 概述

`ProgExpStack` 是一个底层用户程序关键字，按线程索引，用于在不弹出的情况下读取数值（表达式）栈上的值。它最常用于调试，在不破坏栈的前提下检查表达式的运算结果。使用 [ProgExpDepth](ProgExpDepth.md) 查看当前存在多少值，使用 [ProgClrExp](ProgClrExp.md) 清除栈。该参数为非轴数组参数，不保存至闪存。

## 工作原理

`ProgExpStack[thread], location` 通过位置索引读取所选线程数值栈上的某个位置，从栈底开始计数（位置 `0` 为最深的值）。读取操作是非破坏性的——栈内容和深度均不改变。

有效位置从 `0` 到最高已占用位置；栈最多可持有 50 个值。读取超过当前栈顶或超出有效范围的位置将引发栈范围错误。[ProgExpDepth](ProgExpDepth.md) 报告剩余空闲槽位数，因此最高已占用位置为 `50` 减去空闲数再减一。持有浮点值的位置以原始位模式返回，由上位机解释为浮点数；相应的变体关键字可将相同位置直接读取为浮点、64 位整数或双精度格式。

## 示例

```text
AProgExpStack[1],0  ; read the deepest value on thread 1's numeric stack
```

## 另请参阅

- [ProgExpDepth](ProgExpDepth.md) — 数值栈中剩余的空闲空间
- [ProgClrExp](ProgClrExp.md) — 清除数值栈
- [PopParam](../03-stack-operation/PopParam.md) — 将栈顶值弹出至参数
