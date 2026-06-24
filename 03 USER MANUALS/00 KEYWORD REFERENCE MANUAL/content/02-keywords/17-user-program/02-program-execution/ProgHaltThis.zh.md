---
keyword: ProgHaltThis
summary: 暂停当前正在执行的用户程序任务。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 258
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
# ProgHaltThis

暂停当前正在执行的用户程序任务。

## 概述

`ProgHaltThis` 暂停正在执行它的线程——这是 [ProgHalt](ProgHalt.md) 的"自暂停"形式，后者通过索引指定目标线程。线程可使用该命令挂起自身执行，例如在一次性例程结束时。与一般暂停相同，线程保留其位置和调用栈，可通过 `ProgRun[thread],0` 恢复执行，而非重新启动，这与 [ProgReset](ProgReset.md) 不同。该参数为非轴命令，不保存至闪存。

## 工作原理

`ProgHaltThis` 仅在**从运行中的用户程序内部**发出时有效——从通信终端发送将被拒绝。执行时，它清除当前线程的"执行"标志，使调度器停止调度该线程，并将该线程的 [ProgStat](ProgStat.md) 设置为 `0`（未运行）。线程的程序指针保留在 `ProgHaltThis` 所在行（不向前推进），因此线程不会继续执行后续内容。由于指针停留在暂停行，使用 `ProgRun[thread],0` 恢复线程时会重新执行 `ProgHaltThis` 并再次暂停；若要继续执行后续内容，需先移动指针（例如用 [ProgReset](ProgReset.md) 重置线程并运行所需任务，或运行其他任务）。

## 示例

```text
AProgHaltThis        ; halt the task that issues this command
```

## 另请参阅

- [ProgHalt](ProgHalt.md) — 通过索引暂停线程
- [ProgBreakThis](ProgBreakThis.md) — 在运行中的任务上设置断点
- [ProgReset](ProgReset.md) — 将任务重置至初始状态
- [ProgStatAll](ProgStatAll.md) — 所有任务的综合状态
