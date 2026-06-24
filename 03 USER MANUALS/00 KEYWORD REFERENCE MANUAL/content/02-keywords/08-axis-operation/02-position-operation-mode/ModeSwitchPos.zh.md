---
keyword: ModeSwitchPos
summary: 记录轴进入或退出位置模式时的位置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 438
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ModeSwitchPos

记录轴进入或退出位置模式时的位置。

## 概述

`ModeSwitchPos` 是一个只读数组，记录在位置模式与电流/力模式之间每次切换时捕获的位置反馈（[Pos](../../10-motion/01-kinematics-status/Pos.md)）。每个元素仅在其自身对应的切换发生时写入，随后保持该值直至下一次此类切换，因此这两个元素一起给出最近一次模式切换的"来源"和"目标"反馈。这些值会在每条切换路径上自动锁存——直接的 [GoToPosMode](GoToPosMode.md)/`GoToCurrMode`/`GoToForceMode` 命令、内部反馈阈值切换（[PosPosFlag](PosPosFlag.md)/[PosPosTh](PosPosTh.md)），以及 [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 数字量输入切换。

## 工作原理

`ModeSwitchPos` 是一个 1 索引数组（大小为 3；仅使用索引 1 和 2——索引 0 为保留项且不可访问）：

| 索引 | 锁存值（切换时的 `Pos`） |
|-------|------------------------------------------|
| 1     | 轴**退出**位置模式（即进入电流或力模式）时的位置 |
| 2     | 轴**进入**位置模式时的位置 |

- **索引 1** 在 `OperationMode` 变为电流（1）或力（4）的任何路径下写入：`GoToCurrMode`、`GoToForceMode`、内部自动切换至电流/力，以及 `DInMode` 下降沿切换。
- **索引 2** 在 `OperationMode` 变为位置（3）的任何路径下写入：`GoToPosMode`、内部阈值/计划结束切换，以及 `DInMode` 上升沿切换。

索引 1（力模式进入位置）在内部还用作力环在 force-over-PIV 控制期间生成的位置参考的锚点，这正是使后续切换回位置模式实现无冲击的原因。

## 版本间的变化

在 **v5（central-i）** 中位置流水线为 64 位，因此 `ModeSwitchPos` 以前言中所示的更大范围存储 64 位反馈值；记录行为不变。**v5 仅适用于 central-i**，因此在 standalone 上 `ModeSwitchPos` 仍为 v4 的 32 位值。

## 示例

```text
AModeSwitchPos[1]   ; Pos recorded when the axis left position mode (entered current/force)
AModeSwitchPos[2]   ; Pos recorded when the axis entered position mode
```

### 边界情况

- **索引 0** — 无效；有效索引为 `ModeSwitchPos[1]` 和 `ModeSwitchPos[2]`。`ModeSwitchPos[0]` 不存在。
- **只读** — 写入将被拒绝。
- **从未切换** — 在首次切换发生之前，对应索引为 `0`。应将 `0` 视为"未记录切换"，而非"轴曾处于零位"。
- **速度 ↔ 速度** — 仅涉及速度模式的切换（例如经由 [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 代码 16 的位置 → 速度，或速度 → 位置）**不会**更新任何一个索引；`ModeSwitchPos` 仅跟踪位置 ↔ 电流/力。
- **直接对 `OperationMode` 赋值** — 在电机失能时直接写入 [OperationMode](../01-general-keywords/OperationMode.md) 并不总是执行相同的路径；特别是，直接赋值可能不会更新 `ModeSwitchPos`。请使用 `GoTo*` 命令或输入驱动的路径以确保锁存。
- **电机失能** — 索引反映最后锁存的值；它们**不会**被电机失能复位。
- **Force-over-PIV 锚点** — `ModeSwitchPos[1]` 同时充当力控制期间生成的合成位置参考的锚点；改变力模式进入位置即改变该锚点。
- **平台** — v5 central-i 扩展为 64 位；v4（standalone 和 central-i）为 32 位。

## 参见

- [GoToPosMode](GoToPosMode.md) — 记录索引 2（进入位置模式）
- [PosPosFlag](PosPosFlag.md) / [PosPosTh](PosPosTh.md) — 同样记录该切换的内部阈值切换
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 被锁存的反馈值
- [OperationMode](../01-general-keywords/OperationMode.md) — 当前激活的控制模式
