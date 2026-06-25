---
keyword: LockEventInit
summary: 通过学习固件到硬件的捕获偏移来初始化统一的锁存/事件配置（仅模式 1）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 832
attributes:
  access: ro
  scope: axis
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# LockEventInit

通过学习固件到硬件的捕获偏移来初始化统一的锁存/事件配置；仅当 [LockEventMode](LockEventMode.md) = 1 时有意义。

> 仅自 v5（central-i）起可用。

## 概述

`LockEventInit` 是统一锁存/事件方案（[LockEventMode](LockEventMode.md) = 1）所使用的命令关键字。运行它时，控制器对内部硬件捕获计数器采样，并针对所配置的捕获源计算它与控制器侧位置之间的偏移：当主编码器为源时使用主编码器位置（`Pos`），对于虚拟编码器和辅助编码器源则使用虚拟编码器值（`VEncValue`）。正是该偏移使得捕获位置能够以你在其他地方所用的相同单位和参考来报告。

在模式 1 中，此步骤由你负责：在锁存/事件源完全配置好且轴静止后、武装 [LockEn](LockEn-AuxLockEn.md) 或 [EventOn](../../18-event-generation/EventOn.md) 之前，运行一次 `LockEventInit`。在传统模式（[LockEventMode](LockEventMode.md) = 0）中，控制器在功能被武装时自动学习此偏移，因此该命令在那里不被使用。

## 工作原理

仅当所配置的捕获源使用增量式或 AqB 主编码器、虚拟编码器或辅助编码器源时，`LockEventInit` 才计算偏移（并将 [LockEventStat](LockEventStat.md) 驱动为 `1`）。如果选择主编码器作为源但它是绝对式编码器（例如 SSI、EnDat 或 SinCos），命令返回成功但*不会*计算偏移，并使 [LockEventStat](LockEventStat.md) 保持不变——因此请务必在武装前确认 [LockEventStat](LockEventStat.md) 实际读数为 `1`。

当满足上述前提条件（模式 1、适用的捕获源以及静止的源）时，控制器将：

1. 读取当前硬件捕获计数器。
2. 针对所配置源的匹配控制器侧位置计算偏移：主编码器源使用主编码器位置，虚拟编码器和辅助编码器源使用虚拟编码器值。
3. 将锁存/事件子系统标记为已初始化，并将 [LockEventStat](LockEventStat.md) 设置为 `1`（就绪）。（此步骤取决于所配置的源和编码器类型；参见上述前提条件。）

由于偏移是在你运行命令的时刻采样的，因此运行命令时捕获源必须静止；否则学习到的偏移将与后续捕获不匹配。

### 行为说明

- **仅模式 1。** 在 [LockEventMode](LockEventMode.md) = 0（传统模式）下运行 `LockEventInit` 无效，并以错误 334 被拒绝，因为在该模式下偏移已自动学习。仅在选择模式 1 后使用它。
- **模式 1 中武装前必需。** 在 [LockEventMode](LockEventMode.md) = 1 时，若在运行 `LockEventInit` 之前尝试武装 [LockEn](LockEn-AuxLockEn.md) = 1 或 [EventOn](../../18-event-generation/EventOn.md) = 1，将以错误 335（偏移未初始化）被拒绝。请先运行 `LockEventInit`，然后再武装。
- **配置更改后需重新运行。** 初始化后对捕获源的任何更改都会使学习到的偏移失效。对 `EncSinCosHWEn`（编码器/锁存事件捕获源选择器）的更改会被自动检测到并将 [LockEventStat](LockEventStat.md) 复位为未初始化状态，但控制器无法检测每一种情况。作为规则，在对锁存/事件源配置进行任何更改之后、源开始运动之前，重新运行 `LockEventInit`。

## 示例

```text
ALockEventMode=1      ; select the unified lock/event scheme
ALockSrc=16           ; configure the capture source/edge (central-i main encoder index)
                      ; ... make sure the axis is stationary ...
ALockEventInit        ; learn the firmware/hardware offset
ALockEventStat        ; verify this reads 1 (initialized and ready) before arming
ALockEn=1             ; now allowed; arm event-based feedback logging
```

## 另请参阅

- [LockEventMode](LockEventMode.md) — 选择传统模式与统一模式（本命令适用于模式 1）
- [LockEventStat](LockEventStat.md) — 报告是否已完成初始化
- [LockEn](LockEn-AuxLockEn.md) — 武装基于事件的反馈记录
- [LockSrc](LockSrc-AuxLockSrc.md) — 选择触发源和边沿
- [EventOn](../../18-event-generation/EventOn.md) — 武装事件生成
