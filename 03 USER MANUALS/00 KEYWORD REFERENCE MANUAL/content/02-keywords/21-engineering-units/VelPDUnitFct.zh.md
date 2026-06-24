---
keyword: VelPDUnitFct
summary: 启用全局用户单位时，应用于脉冲方向速度值的比例因子。
availability:
  standalone: []
  central-i:
  - v5
can_code: 824
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VelPDUnitFct

启用全局用户单位时，应用于脉冲方向速度值的比例因子。

## 概述

`VelPDUnitFct` 是在全局用户单位功能（[UserUnitsEn](UserUnitsEn.md) = 1）下，脉冲/方向（P/D）速度量的逐轴比例因子。它是主反馈 [VelUnitFct](VelUnitFct.md) 的 P/D 对应项：将 P/D 速度 [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md)（P/D 速度单位组 [VelPDUnitGrp](VelPDUnitGrp.md) 的成员）缩放为您希望上位机显示的工程单位。

该因子仅影响向上位机呈现值的方式，不影响内部控制计算。对应的文本标签由 [VelPDUnitUnt](VelPDUnitUnt.md) 设置。

## 工作原理

`VelPDUnitFct` 是一个浮点因子，用于将内部 P/D 速度单位与显示用户单位关联，应用于 [VelPDUnitGrp](VelPDUnitGrp.md) 中列出的每个关键字。默认值为 `1`（值不经缩放直接呈现）。

该因子存储在闪存中，因此在重新上电后保持有效。

全局用户单位与嵌入式 P/D 缩放 [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) 在同一轴上互斥。若 `UserUnitsEn` 已开启且 `PDUsrUnits` 设置为非默认缩放，则读写受影响的成员关键字（脉冲/方向速度 [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md)）将被拒绝，并返回错误 `338`。设置 `VelPDUnitFct` 本身不受此冲突限制。

本关键字仅适用于 v5（central-i）及以上版本。

## 示例

```text
AVelPDUnitFct=1       ; 默认——P/D 速度不经缩放直接呈现
AVelPDUnitFct=0.01    ; 以 0.01 的比例呈现 P/D 速度
AVelPDUnitFct[1]      ; 读取当前 P/D 速度因子
```

## 另请参阅

- [VelPDUnitGrp](VelPDUnitGrp.md) — 由本因子缩放的关键字
- [VelPDUnitUnt](VelPDUnitUnt.md) — P/D 速度量的单位标签
- [VelUnitFct](VelUnitFct.md) — 主反馈速度比例因子
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
- [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) — 嵌入式 P/D 缩放（互斥）
