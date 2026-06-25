---
keyword: AuxModRev
summary: 辅助编码器的取模旋转除数（当前固件未实现）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 71
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: aux_user_units
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AuxModRev

辅助编码器的取模旋转除数（当前固件未实现）。

## 概述

`AuxModRev` 是辅助编码器的取模旋转除数，是主编码器 [ModRev](../04-modulo-mode/ModRev.md) 的辅助编码器对应项。当设置为非零值时，它用于将辅助编码器位置环绕到范围 $[0,\ \text{AuxModRev} - 1]$。它是一个轴范围参数，保存至闪存，在电机使能或运动中无法更改。

> **可用性：** `AuxModRev` 在当前固件中被标记为 `not_implemented`。该参数已定义并存储，但控制环不对其进行处理——逐周期的取模环绕仅作用于主编码器（[Pos](../../10-motion/01-kinematics-status/Pos.md)）。因此设置 `AuxModRev` 对辅助反馈（[AuxPos](../../10-motion/01-kinematics-status/AuxPos.md)）没有影响。取模模式目前仅在主编码器上受支持；如需辅助编码器取模，请联系 Agito。

## 示例

```text
AAuxModRev          ; query the configured auxiliary modulo divisor
```

## 另请参阅

- [ModRev](../04-modulo-mode/ModRev.md) — 主编码器取模除数（已实现的对应项）
- [AuxPos](../../10-motion/01-kinematics-status/AuxPos.md) — 辅助编码器反馈位置
