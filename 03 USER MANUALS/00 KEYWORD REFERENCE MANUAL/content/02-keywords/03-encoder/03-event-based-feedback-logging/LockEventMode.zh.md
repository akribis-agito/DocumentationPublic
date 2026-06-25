---
keyword: LockEventMode
summary: '选择 lock/event 工作模式：传统自动初始化 (0) 或需要 LockEventInit 的统一方案 (1)。'
availability:
  standalone: []
  central-i:
  - v5
can_code: 831
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -1
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# LockEventMode

选择 lock/event 工作模式：传统自动初始化（`0`）或需要 [LockEventInit](LockEventInit.md) 的统一方案（`1`）。

> 仅 v5（central-i）起可用。

## 概述

`LockEventMode` 用于选择基于事件的反馈记录（“位置锁存”/“捕获”）和事件生成功能如何获取它们所需的偏移量，该偏移量位于你在控制器中回读的值（例如 `Pos`、`AuxPos` 或 `VEncValue`）与执行锁存的内部硬件捕获计数器之间。该计数器从任意偏移量开始计数，因此固件必须先学习一次这个差值，然后才能以你期望的单位报告捕获到的位置。

学习该偏移量有两种方式：

- **模式 0（传统/向后兼容）** —— 偏移量在你使能该功能的那一刻自动学习，即当 [LockEn](LockEn-AuxLockEn.md) 或 [EventOn](../../18-event-generation/EventOn.md) 从 `0` 跳变到 `1` 时。这与早期固件的行为一致，因此现有配置可保持不变继续工作。
- **模式 1（统一方案）** —— 偏移量*不会*在使能时学习。相反，你需要在轴静止时、于使能 Lock 或 Event 之前，自行运行 [LockEventInit](LockEventInit.md) 命令。这使你能够精确控制何时采样偏移量，当捕获源在你原本会使能的那一刻可能正在运动时，这一点尤为重要。

该设置存储于闪存中，因此所选模式可在重新上电后保留。默认值为 `0`（传统行为）。

> **仅支持 `0` 和 `1` 两个工作值。** 尽管该关键字的数值范围下探至 `-1`，但 `-1` 并不是有效的工作模式：在该模式下，使能时没有自动偏移量学习，没有 [LockEventInit](LockEventInit.md) 初始化，使能也不被阻止。这种组合可能导致捕获偏移量未被计算，从而产生错误的捕获位置，因此不应使用 `-1`。

## 工作原理

| 值 | 含义 |
|-------|---------|
| 0 | 传统/向后兼容模式。固件到硬件的偏移量在 Lock 或 Event 使能时自动学习。无需手动初始化；[LockEventStat](LockEventStat.md) 报告 `0`。 |
| 1 | 统一模式。在使能 Lock 或 Event 之前，你必须运行 [LockEventInit](LockEventInit.md)（轴静止）来学习偏移量。未运行该命令即使能将被以错误 335 拒绝。 |

### 对状态关键字的影响

写入 `LockEventMode` 会立即重新评估 [LockEventStat](LockEventStat.md)：

- 设置 `LockEventMode=0` 会将状态置为 `0`（传统模式，就绪）。
- 设置 `LockEventMode=1` 时，如果自上电以来偏移量已被计算，则将状态置为 `1`；如果尚未计算，则置为“未初始化”状态 —— 此时你必须在使能前运行 [LockEventInit](LockEventInit.md)。

### 何时需要重新初始化（模式 1）

任何改变捕获源的配置更改都会使先前学习到的偏移量失效。具体而言，对 `EncSinCosHWEn`（编码器/lock-event 捕获源选择器）的更改会清除“已初始化”条件，并将 [LockEventStat](LockEventStat.md) 返回至未初始化状态，因此在使能前必须重新运行 [LockEventInit](LockEventInit.md)。固件只能自动检测其中某些更改，因此作为通用规则，应在对 lock/event 源配置进行任何更改之后、且在捕获源开始运动之前运行 [LockEventInit](LockEventInit.md)。

## 示例

```text
ALockEventMode=1      ; select the unified lock/event scheme
ALockEventInit        ; learn the firmware/hardware offset (axis stationary)
ALockEn=1             ; now allowed; arm event-based feedback logging
ALockEventMode=0      ; revert to legacy auto-initialize behavior
ALockEventMode        ; read back the configured mode
```

## 另请参阅

- [LockEventInit](LockEventInit.md) —— 运行模式 1 所需的手动偏移量初始化
- [LockEventStat](LockEventStat.md) —— 报告 lock/event 子系统是否已初始化
- [LockEn](LockEn-AuxLockEn.md) —— 使能基于事件的反馈记录
- [LockSrc](LockSrc-AuxLockSrc.md) —— 选择触发源和触发边沿
- [EventOn](../../18-event-generation/EventOn.md) —— 使能事件生成
