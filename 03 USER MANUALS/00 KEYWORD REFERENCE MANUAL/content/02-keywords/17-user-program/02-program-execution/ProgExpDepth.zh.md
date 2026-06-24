---
keyword: ProgExpDepth
summary: 报告线程数值（表达式）栈中剩余的空闲空间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 205
attributes:
  access: ro
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
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgExpDepth

报告线程数值（表达式）栈中剩余的空闲空间。

## 概述

`ProgExpDepth` 是一个底层用户程序关键字，按线程索引，报告线程数值（表达式）栈中剩余空闲（可用）槽位的数量。刚清除的栈报告值为 50（其完整容量），每压入一个值减少一。它主要用作调试辅助工具，与 [ProgExpStack](ProgExpStack.md)（在不弹出的情况下读取值）和 [ProgClrExp](ProgClrExp.md)（清除栈）配合使用。该参数为非轴数组参数，不保存至闪存。

## 工作原理

每个线程都有自己的数值栈，最多可持有 50 个值，用于构建和评估表达式（参见 [PushParam](../03-stack-operation/PushParam.md)、[PushConstant](../03-stack-operation/PushConstant.md)、[Math](Math.md) 和 [PopParam](../03-stack-operation/PopParam.md)）。`ProgExpDepth[thread]` 返回*空闲*槽位数——容量（50）减去当前已使用的槽位数——因此在已清除或平衡的栈上从 `50` 开始，每压入一个值减少一，每弹出一个值增加一。

正确平衡的表达式会使栈保持原状。因此，检查 `ProgExpDepth` 是确认表达式序列是否平衡的最快方法——一系列压入和弹出操作后值不符合预期，表明存在缺失的 [PopParam](../03-stack-operation/PopParam.md) 或多余的压入操作，否则将留下陈旧的操作数。

## 示例

```text
AProgExpDepth[1]    ; free numeric-stack slots for thread 1 (50 when empty, 49 with one value)
```

## 另请参阅

- [ProgExpStack](ProgExpStack.md) — 在不弹出的情况下读取数值栈上的值
- [ProgClrExp](ProgClrExp.md) — 清除数值栈
- [Math](Math.md) — 对数值栈上的值执行操作
