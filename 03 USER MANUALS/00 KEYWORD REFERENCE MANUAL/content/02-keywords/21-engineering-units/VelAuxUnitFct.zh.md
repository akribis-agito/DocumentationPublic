---
keyword: VelAuxUnitFct
summary: 启用全局用户单位时应用于辅助编码器速度值的比例系数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 821
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VelAuxUnitFct

启用全局用户单位时应用于辅助编码器速度值的比例系数。

## 概述

`VelAuxUnitFct` 是全局用户单位功能（[UserUnitsEn](UserUnitsEn.md) = 1）下辅助编码器速度量的每轴比例系数。它是主反馈 [VelUnitFct](VelUnitFct.md) 的辅助编码器对应项：将辅助速度 [AuxVel](../10-motion/01-kinematics-status/AuxVel.md)（辅助速度单位组 [VelAuxUnitGrp](VelAuxUnitGrp.md) 的成员）缩放到您希望上位机显示的工程单位。

该系数仅影响向上位机呈现数值的方式；内部控制计算不受影响。配套的文本标签通过 [VelAuxUnitUnt](VelAuxUnitUnt.md) 设置。

## 工作原理

`VelAuxUnitFct` 是一个浮点型系数，用于将内部辅助速度单位与显示的用户单位相关联，应用于 [VelAuxUnitGrp](VelAuxUnitGrp.md) 中列出的每个关键字。默认值为 `1`（值原样呈现）。

该系数存储于闪存，因此在重新上电后保持不变。

全局用户单位与嵌入式辅助缩放 [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 在同一轴上互斥。辅助反馈只能使用其中一个；若两者同时启用，访问受影响的关键字时将产生冲突。

此关键字仅在 v5（central-i）及以上版本可用。

## 示例

```text
AVelAuxUnitFct=1       ; 默认——辅助速度原样呈现
AVelAuxUnitFct=0.001   ; 将辅助速度按 0.001 缩放呈现
AVelAuxUnitFct[1]      ; 读取当前辅助速度系数
```

## 另请参阅

- [VelAuxUnitGrp](VelAuxUnitGrp.md) — 由此系数缩放的关键字
- [VelAuxUnitUnt](VelAuxUnitUnt.md) — 辅助速度量的单位标签
- [VelUnitFct](VelUnitFct.md) — 主反馈速度比例系数
- [UserUnitsEn](UserUnitsEn.md) — 每轴启用全局用户单位功能
- [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 嵌入式辅助缩放（互斥）
