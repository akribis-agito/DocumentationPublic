---
keyword: ProgClrCall
summary: 清空用户程序线程的程序调用栈。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 275
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgClrCall

清空用户程序线程的程序调用栈。

## 概述

`ProgClrCall` 是一个以线程为索引的指令，用于清空用户程序线程的程序调用栈，丢弃所有待处理的函数返回地址和暂存参数。它是 [ProgClrExp](ProgClrExp.md) 的调用栈对应版本——后者清空数值（表达式）栈。它是一个非轴指令，不保存至闪存。

## 工作原理

`ProgClrCall[thread]` 一步清空所选线程的调用栈：将栈标记为无已占用槽，并将当前帧引用重置至栈底。执行后，[ProgCallDepth](ProgCallDepth.md) 报告完整的 100 个空闲槽，[ProgCallStack](ProgCallStack.md) 显示无已占用内容。

清空操作仅重置调用栈的记账信息；它本身不重定向执行。由于它会放弃所有待处理的返回地址，后续的 [Return](Return.md) 将遇到空栈并引发错误。通常应将其与 [ProgClrExp](ProgClrExp.md) 以及程序指针的重置（参见 [ProgReset](ProgReset.md) / [ProgResetAll](ProgResetAll.md)）配合使用，以将线程恢复至已知的干净状态，而不是在正常调用序列的中途使用。

## 示例

```text
AProgClrCall[1]     ; clear the call stack of thread 1
```

## 另请参阅

- [ProgCallStack](ProgCallStack.md) — 程序调用栈内容
- [ProgCallDepth](ProgCallDepth.md) — 调用栈中剩余的空闲空间
- [ProgClrExp](ProgClrExp.md) — 清空数值（表达式）栈
- [ProgResetAll](ProgResetAll.md) — 停止所有线程并重置指针和各调用栈
