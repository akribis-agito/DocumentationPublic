---
keyword: LockEventStat
summary: 报告 lock/event 子系统的初始化状态。
availability:
  standalone: []
  central-i:
  - v5
can_code: 833
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LockEventStat

报告 lock/event 子系统的初始化状态。

> 仅 v5（central-i）起可用。

## 概述

`LockEventStat` 是一个只读状态，用于告知你 lock/event 子系统是否已就绪可被使能。它反映了在当前 [LockEventMode](LockEventMode.md) 下固件到硬件的捕获偏移量是如何处理的，以及在统一模式下所需的 [LockEventInit](LockEventInit.md) 步骤是否已完成。

在运行统一方案时，将其用作使能 [LockEn](LockEn-AuxLockEn.md) 或 [EventOn](../../18-event-generation/EventOn.md) 之前的前提条件检查。

## 工作原理

每当写入 [LockEventMode](LockEventMode.md)、每当 [LockEventInit](LockEventInit.md) 完成、以及每当配置更改影响到捕获源时，`LockEventStat` 都会被重新计算。

| 值 | 含义 |
|-------|---------|
| 0 | 传统模式（[LockEventMode](LockEventMode.md) = 0）。无需手动初始化 —— 偏移量在 Lock 或 Event 使能时自动学习。 |
| 1 | 统一模式（[LockEventMode](LockEventMode.md) = 1）且已初始化：[LockEventInit](LockEventInit.md) 已运行，子系统已就绪可使能。 |
| -1 | 统一模式（[LockEventMode](LockEventMode.md) = 1）但尚未初始化：在使能 Lock 或 Event 之前请运行 [LockEventInit](LockEventInit.md)。 |

当 [LockEventMode](LockEventMode.md) 被设置为 `1` 且自上电以来尚未计算偏移量时，或当某次配置更改使先前已计算的偏移量失效时，会出现 `-1` 读数。具体而言，对 `EncSinCosHWEn`（编码器/lock-event 捕获源选择器）的更改会被自动检测到，并将该状态返回为 `-1`。在该状态下，使能 [LockEn](LockEn-AuxLockEn.md) 或 [EventOn](../../18-event-generation/EventOn.md) 将被拒绝，直到运行 [LockEventInit](LockEventInit.md)。

## 示例

```text
ALockEventMode=1      ; select the unified scheme
ALockEventStat        ; reads -1 until LockEventInit has been run
ALockEventInit        ; learn the offset (axis stationary)
ALockEventStat        ; now reads 1 (ready to arm)
ALockEventMode=0      ; revert to legacy mode
ALockEventStat        ; reads 0 (no manual init needed)
```

## 参见

- [LockEventMode](LockEventMode.md) —— 选择传统模式与统一模式
- [LockEventInit](LockEventInit.md) —— 执行将该状态驱动至 `1` 的初始化
- [LockEn](LockEn-AuxLockEn.md) —— 使能基于事件的反馈记录
- [EventOn](../../18-event-generation/EventOn.md) —— 使能事件生成
