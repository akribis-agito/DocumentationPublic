---
keyword: ProgReset
summary: 将用户程序任务重置为初始状态。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 295
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ProgReset

将用户程序任务重置为初始状态。

## 概述

`ProgReset[Thread no.]` 将单个用户程序线程恢复至初始状态。与 [ProgHalt](ProgHalt.md) 仅挂起线程以便从同一位置恢复不同，重置会清除线程的进度，使后续的 [ProgRun](ProgRun.md) 从任务起始处重新开始。若要一次性重置所有线程并清除所有指针和栈，请使用 [ProgResetAll](ProgResetAll.md)。这是一个非轴指令，不保存至闪存。

## 工作原理

`ProgReset` 以**线程编号**（`[1]` 至 `[8]`，或 Central-i 主控上的 `[12]`）为索引。重置一个线程将执行以下操作：

- 将其程序指针重置回主程序（任务 1）的起始位置。
- 清除其调用栈和数值栈。
- 清除任何等待状态和待处理的单步执行标志。
- 清除该线程的 [ProgError](ProgError.md) 值。

重置**线程 1** 还会额外禁用用户程序事件系统并清除所有事件使能和状态，因为主线程拥有事件。

若没有已存储的程序、线程索引超过最高线程编号，或线程当前正在运行，则该指令将被拒绝 —— 请先使用 [ProgHalt](ProgHalt.md) 停止线程。重置后线程保持停止状态；下一次 [ProgRun](ProgRun.md) 将选择其执行的任务。

## 示例

```text
AProgReset[1]       ; reset thread 1 to its initial state (must not be running)
```

## 另请参阅

- [ProgRun](ProgRun.md) — 重置后运行线程
- [ProgHalt](ProgHalt.md) — 暂停线程（保留其位置，与重置不同）
- [ProgResetAll](ProgResetAll.md) — 停止所有线程并重置指针和栈
- [ProgStat](ProgStat.md) — 线程的运行状态
- [ProgStatAll](ProgStatAll.md) — 所有线程的综合状态
