---
keyword: PosPDUnitGrp
summary: 共享 P/D 位置用户单位缩放和标签的脉冲方向位置关键字只读列表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 817
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PosPDUnitGrp

共享 P/D 位置用户单位缩放和标签的脉冲方向位置关键字只读列表。

## 概述

当轴的全局用户单位功能启用后（[UserUnitsEn](UserUnitsEn.md) = 1），每个物理量均以每量专属的比例系数和自由文本单位标签向上位机呈现。`PosPDUnitGrp` 是**脉冲方向（P/D）位置**量的成员列表：它告知上位机哪些关键字共同由 [PosPDUnitFct](PosPDUnitFct.md) 缩放，并由 [PosPDUnitUnt](PosPDUnitUnt.md) 标注。

它是主反馈 [PosUnitGrp](PosUnitGrp.md) 的 P/D 对应项，适用于脉冲方向位置计数器 [PDPos](../10-motion/06-motion-mode-pulse-and-direction-pd/PDPos.md) 及预置该计数器的指令。

`PosPDUnitGrp` 为只读且固定：控制器在启动时填充它，因此只能读取以发现分组成员，不能编辑。

## 工作原理

该关键字为非轴数组。每个已填充的元素保存 P/D 位置单位分组中的一个成员。数组采用 1 索引；元素 [0] 不存在。数组有一个保留槽，因此 `array_size` 为 3 时，最高可用索引为 2。

| 索引 | 成员关键字 |
|------|-----------|
| [1]  | PDPos（脉冲方向位置计数器） |
| [2]  | SetPDPos（预置/重置 P/D 位置） |

每个元素返回成员关键字的内部指令码（范围 0–1023）。值为 0 表示该槽未使用。

该分组由上位机显示/单位层使用；不会改变内部控制计算。这些关键字的比例系数和标签来自 [PosPDUnitFct](PosPDUnitFct.md) 和 [PosPDUnitUnt](PosPDUnitUnt.md)。

全局用户单位与嵌入式 P/D 缩放 [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) 在同一轴上互斥。若 `UserUnitsEn` 已开启且 `PDUsrUnits` 也设置了非默认缩放，则访问该分组中的成员时将报告冲突。

此关键字仅在 v5 (central-i) 中可用。

## 示例

```text
APosPDUnitGrp[1]    ; read the first member command code of the P/D position group
APosPDUnitGrp[2]    ; read the second member command code
```

## 另请参阅

- [PosPDUnitFct](PosPDUnitFct.md) — P/D 位置量的比例系数
- [PosPDUnitUnt](PosPDUnitUnt.md) — P/D 位置量的单位标签
- [PosUnitGrp](PosUnitGrp.md) — 主反馈位置单位分组
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
- [PDPos](../10-motion/06-motion-mode-pulse-and-direction-pd/PDPos.md) — 脉冲方向位置计数器
