---
keyword: ProgExpStackD
summary: 以 64 位浮点数（double）形式读取数值（表达式）栈上的一个值，不弹出该值。
availability:
  standalone: []
  central-i:
  - v5
can_code: 794
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: float64
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgExpStackD

以 64 位浮点数（double）形式读取数值（表达式）栈上的一个值，不弹出该值。

## 概述

`ProgExpStackD` 是 [ProgExpStack](ProgExpStack.md) 的双精度浮点数形式。以线程为索引，它读取数值（表达式）栈上的一个值，并将其解释为 64 位浮点数（double）返回，而不弹出该值。该功能最适用于调试场景——在不干扰栈内容的情况下检查表达式的计算结果。使用 [ProgExpDepth](ProgExpDepth.md) 查询剩余空闲空间，使用 [ProgClrExp](ProgClrExp.md) 清空栈。这是一个非轴数组参数，不保存至闪存。

本关键字自 v5（Central-i）起可用。

## 工作原理

`ProgExpStackD[thread], location` 按位置读取所选线程数值栈上的某个位置，位置从栈底开始计数（位置 `0` 为最深处的值）。读取操作不具破坏性——栈内容和深度保持不变。

与 [ProgExpStack](ProgExpStack.md) 的唯一区别在于返回的数据类型：`ProgExpStackD` 将该位置直接以 64 位浮点数（double）形式返回，而非 32 位整数或原始位模式。底层栈位置相同；各类型形式仅控制位的解释方式，因此应使用与存储值类型相匹配的变体。

有效位置范围为 `0` 到当前最高占用位置；栈最多可容纳 50 个值。读取超过当前栈顶或超出有效范围的位置将引发栈范围错误。[ProgExpDepth](ProgExpDepth.md) 报告剩余空闲槽数，因此最高占用位置为 `50` 减去空闲数量再减一。

## 示例

```text
AProgExpStackD[1],0 ; read the deepest value on thread 1's numeric stack as a double
```

## 参见

- [ProgExpStack](ProgExpStack.md) — 基础（32 位整数）形式
- [ProgExpStackF](ProgExpStackF.md) — 32 位浮点数形式
- [ProgExpStckLL](ProgExpStckLL.md) — 64 位整数形式
- [ProgExpDepth](ProgExpDepth.md) — 数值栈剩余空闲空间
- [ProgClrExp](ProgClrExp.md) — 清空数值栈
