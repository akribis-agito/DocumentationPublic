---
keyword: ProgBreakThis
summary: 在当前正在执行的用户程序任务上设置断点。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 429
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
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
# ProgBreakThis

在当前正在执行的用户程序任务上设置断点。

## 概述

`ProgBreakThis` 是一个从正在运行的用户程序内部发出的指令，用于在当前执行位置挂起调用线程。它是 [ProgBreaks](ProgBreaks.md) 的自身目标版本：不是预先加载程序位置以便停止，而是在该行运行时要求程序在*此处*停止。它用于调试，以便可以检查线程并在之后恢复，而不是重置。它是一个非轴指令，不保存至闪存。

## 工作原理

当正在运行的程序执行 `ProgBreakThis` 时，控制器将调用线程标记为无需继续执行更多指令，并将其程序状态更新为"未运行"（除非该线程未加载程序）。执行在此位置停止，线程状态保持完整；使用 [ProgPointer](ProgPointer.md) 查看挂起位置，使用 [ProgCallStack](ProgCallStack.md) 检查调用帧，使用程序快照（[ProgSnapVal](ProgSnapVal.md)）获取捕获的状态。通过 [ProgRun](ProgRun.md) 恢复线程，或通过 [ProgSingle](ProgSingle.md) 单步执行。

`ProgBreakThis` 必须从用户程序内部发出（它作用于"当前"线程）。与 [ProgHaltThis](ProgHaltThis.md) 的区别在于意图：两者都在当前位置停止线程，但 `ProgBreakThis` 是与断点和单步工具配合使用的调试中断。

## 示例

```text
AProgBreakThis       ; break the currently executing task at the next instruction
```

## 另请参阅

- [ProgHaltThis](ProgHaltThis.md) — 停止正在运行的任务
- [ProgReset](ProgReset.md) — 将任务重置至初始状态
- [ProgPointer](ProgPointer.md) — 每个任务的当前指令指针
