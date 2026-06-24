---
keyword: ProgHaltAll
summary: 暂停所有当前活动的用户程序线程。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 278
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
# ProgHaltAll

暂停所有当前活动的用户程序线程。

## 概述

`ProgHaltAll` 通过单条指令暂停所有用户程序线程。与 [ProgHalt](ProgHalt.md) 相同，暂停并非复位：每个线程保留其程序指针及调用栈，可通过 `ProgRun[thread],0` 恢复执行。若需停止所有线程**并**清除其指针和调用栈，请改用 [ProgResetAll](ProgResetAll.md)。该参数为非轴命令，不保存至闪存。

## 工作原理

`ProgHaltAll` 通过清除所有线程的"执行"标志，将其从调度器中一次性移除，并将每个线程的 [ProgStat](ProgStat.md) 设置为 `0`（未运行）。指针和调用栈均不受影响，因此每个线程的程序状态被冻结在停止处，可通过 `ProgRun[thread],0` 分别恢复执行。该命令需要已加载的用户程序；若未加载程序，则命令被拒绝。

## 示例

```text
AProgHaltAll         ; halt every active user program thread
```

## 另请参阅

- [ProgHalt](ProgHalt.md) — 暂停单个线程
- [ProgHaltThis](ProgHaltThis.md) — 暂停发出该命令的任务
- [ProgResetAll](ProgResetAll.md) — 停止所有线程并重置指针和调用栈
- [ProgStatAll](ProgStatAll.md) — 所有线程的综合状态
