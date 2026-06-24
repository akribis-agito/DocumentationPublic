---
keyword: PosAuxUnitFct
summary: 启用全局用户单位时，应用于辅助编码器位置值的比例系数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 815
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
# PosAuxUnitFct

启用全局用户单位时，应用于辅助编码器位置值的比例系数。

## 概述

`PosAuxUnitFct` 是全局用户单位功能（[UserUnitsEn](UserUnitsEn.md) = 1）下辅助编码器位置量的按轴比例系数。它是主反馈 [PosUnitFct](PosUnitFct.md) 的辅助编码器对应项：将辅助位置 [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) 及辅助位置单位分组（[PosAuxUnitGrp](PosAuxUnitGrp.md)）的其他成员换算为上位机所要显示的工程单位。

该系数仅影响向上位机呈现和接受数值的方式；内部控制计算不受影响。配套的文本标签由 [PosAuxUnitUnt](PosAuxUnitUnt.md) 设置。

## 工作原理

`PosAuxUnitFct` 是一个浮点系数，将内部辅助位置单位与显示的用户单位关联，应用于 [PosAuxUnitGrp](PosAuxUnitGrp.md) 中列出的所有关键字。默认值为 `1`（数值原样呈现）。

该系数保存在闪存中，因此在重新上电后依然保留。

全局用户单位与嵌入式辅助缩放 [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 在同一轴上互斥。对辅助反馈只能选择其中一种；同时启用两者时，访问受影响的关键字将报告冲突。

此关键字仅在 v5 (central-i) 中可用。

## 示例

```text
APosAuxUnitFct=1       ; 默认——辅助位置原样呈现
APosAuxUnitFct=0.001   ; 将辅助位置缩放 0.001 后呈现
APosAuxUnitFct[1]      ; 读取当前辅助位置系数
```

## 另请参阅

- [PosAuxUnitGrp](PosAuxUnitGrp.md) — 由该系数缩放的关键字
- [PosAuxUnitUnt](PosAuxUnitUnt.md) — 辅助位置量的单位标签
- [PosUnitFct](PosUnitFct.md) — 主反馈位置比例系数
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
- [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 嵌入式辅助缩放（互斥）
