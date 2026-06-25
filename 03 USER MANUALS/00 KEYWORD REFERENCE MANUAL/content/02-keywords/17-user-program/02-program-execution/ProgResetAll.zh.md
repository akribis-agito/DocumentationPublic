---
keyword: ProgResetAll
summary: 停止所有正在运行的线程，并重置每个指针和栈。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 192
attributes:
  access: rw
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
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgResetAll

停止所有正在运行的线程，并重置每个指针和栈。

## 概述

`ProgResetAll` 将整个用户程序系统恢复到初始状态，重置每个线程的程序指针，并清空所有调用栈和数值栈。它是 [ProgReset](ProgReset.md) 的全局形式：`ProgReset` 将单个线程恢复到初始状态，而 `ProgResetAll` 则通过一条指令清除整个程序状态。与 [ProgHaltAll](ProgHaltAll.md) 相比，后者仅挂起线程而不清除其状态。该命令为非轴命令，不保存至闪存。

## 工作原理

`ProgResetAll` 仅在**没有任何线程运行**时才会执行。它首先检查每个线程；若有任何一个线程仍处于活动状态，则该命令将被拒绝并返回错误，且不做任何更改。请在发出此命令前先使用 [ProgHaltAll](ProgHaltAll.md) 停止所有线程。若控制器中没有已存储的程序，该命令同样会被拒绝。

执行成功时，它将重新初始化完整的程序状态：每个线程的指针被复位到主程序起始位置，所有调用栈和数值栈被清空，各线程的错误被清除，每个线程的 [ProgStat](ProgStat.md) 恢复为 `0`（未运行）。这是在执行新的 [ProgRun](ProgRun.md) 之前，将所有线程恢复到已知起始点的最干净的方式。

## 示例

```text
AProgHaltAll         ; 首先停止所有线程...
AProgResetAll        ; ...然后重置所有指针和栈
```

## 另请参阅

- [ProgReset](ProgReset.md) — 重置单个线程
- [ProgHaltAll](ProgHaltAll.md) — 停止所有线程（ProgResetAll 执行前必须调用）
- [ProgStatAll](ProgStatAll.md) — 所有线程的综合状态
