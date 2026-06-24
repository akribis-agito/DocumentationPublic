---
keyword: ProgSingle
summary: 对用户程序线程执行单步调试（调试器步入/步过）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 191
attributes:
  access: rw
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
  - 1
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgSingle

对用户程序线程执行单步调试（调试器步入/步过）。

## 概述

`ProgSingle[Thread no.], Step type` 将线程推进一个单步然后将其暂停——这是调试器单步功能的基础，通常由 Agito PCSuite 发出。步进类型用于选择"步入"或"步过"。它与 [ProgBreakThis](ProgBreakThis.md) 设置的断点以及位置读数 [ProgPointer](ProgPointer.md) 和 [ProgLine](ProgLine.md) 配合使用。该命令为非轴命令，不保存至闪存。

## 工作原理

`ProgSingle` 将所选线程重新使能仅执行一步，之后调度器再次将其暂停，并将其 [ProgStat](ProgStat.md) 恢复为 `0`（未运行）。与恢复操作类似，它不会干扰线程的指针或栈，因此单步执行将从线程上次停止的确切位置继续。每次单步开始时，线程的 [ProgError](ProgError.md) 将被清除。

| 步进类型 | 行为 |
|----|----|
| 0 | **步入** — 执行下一条底层指令，然后暂停 |
| 1 | **步过** — 持续执行直到程序指针前进后暂停；这会跳过内部等待循环（例如重复执行同一行的等待条件），而不会停在循环内部 |

当 `ProgSingle` 从通信终端发出时，它会临时忽略位于紧随下一条指令处的断点，以避免在当前位置处被断点阻塞。以下情况下该命令将被拒绝：没有已存储的程序、已存储程序校验和验证失败、线程已在运行中，或线程指针已超过程序末尾。

## 示例

```text
AProgSingle[1],0    ; 步入：执行线程 1 的下一行，然后暂停
AProgSingle[1],1    ; 步过线程 1 中的内部等待循环
```

## 另请参见

- [ProgBreakThis](ProgBreakThis.md) — 在运行中的任务上设置断点
- [ProgPointer](ProgPointer.md) — 每个任务的当前指令指针
- [ProgLine](ProgLine.md) — 当前源码行号
