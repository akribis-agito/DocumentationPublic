---
keyword: PosPDUnitFct
summary: 启用全局用户单位时，应用于脉冲方向位置值的比例系数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 818
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
# PosPDUnitFct

启用全局用户单位时，应用于脉冲方向位置值的比例系数。

## 概述

`PosPDUnitFct` 是全局用户单位功能（[UserUnitsEn](UserUnitsEn.md) = 1）下脉冲方向（P/D）位置量的按轴比例系数。它是主反馈 [PosUnitFct](PosUnitFct.md) 的 P/D 对应项：将 P/D 位置计数器 [PDPos](../10-motion/06-motion-mode-pulse-and-direction-pd/PDPos.md) 及 P/D 位置单位分组（[PosPDUnitGrp](PosPDUnitGrp.md)）的其他成员换算为上位机所要显示的工程单位。

该系数仅影响向上位机呈现和接受数值的方式；内部控制计算不受影响。配套的文本标签由 [PosPDUnitUnt](PosPDUnitUnt.md) 设置。

## 工作原理

`PosPDUnitFct` 是一个浮点系数，将内部 P/D 位置单位与显示的用户单位关联，应用于 [PosPDUnitGrp](PosPDUnitGrp.md) 中列出的所有关键字。默认值为 `1`（数值原样呈现）。

该系数保存在闪存中，因此在重新上电后依然保留。

全局用户单位与嵌入式 P/D 缩放 [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) 在同一轴上互斥。对 P/D 位置只能选择其中一种；同时启用两者时，访问受影响的关键字将报告冲突。

此关键字仅在 v5 (central-i) 中可用。

## 示例

```text
APosPDUnitFct=1       ; default — present P/D position unchanged
APosPDUnitFct=0.01    ; present the P/D position scaled by 0.01
APosPDUnitFct[1]      ; read the current P/D position factor
```

## 另请参阅

- [PosPDUnitGrp](PosPDUnitGrp.md) — 由该系数缩放的关键字
- [PosPDUnitUnt](PosPDUnitUnt.md) — P/D 位置量的单位标签
- [PosUnitFct](PosUnitFct.md) — 主反馈位置比例系数
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
- [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) — 嵌入式 P/D 缩放（互斥）
