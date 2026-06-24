---
keyword: VelPDUnitGrp
summary: 只读列表，列出共享 P/D 速度用户单位缩放和标签的脉冲方向速度关键字。
availability:
  standalone: []
  central-i:
  - v5
can_code: 823
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VelPDUnitGrp

只读列表，列出共享 P/D 速度用户单位缩放和标签的脉冲方向速度关键字。

## 概述

当轴的全局用户单位功能已启用（[UserUnitsEn](UserUnitsEn.md) = 1）时，每个物理量均以每量比例因子和自由文本单位标签向上位机呈现。`VelPDUnitGrp` 是**脉冲/方向（P/D）速度**量的成员列表：它告知上位机哪些关键字由 [VelPDUnitFct](VelPDUnitFct.md) 统一缩放并由 [VelPDUnitUnt](VelPDUnitUnt.md) 统一标注。

它是主反馈 [VelUnitGrp](VelUnitGrp.md) 的 P/D 对应项，适用于脉冲/方向速度 [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md)。

`VelPDUnitGrp` 为只读且固定：控制器在启动时填充该值，因此只需读取以发现组成员，无需编辑。

## 工作原理

本关键字为非轴数组。每个已填充的元素保存 P/D 速度单位组的一个成员。数组从 1 开始索引；元素 [0] 不存在。数组有一个保留槽位，因此 `array_size` 为 2 时，最高可用索引为 1。

| 索引 | 成员关键字 |
|-------|----------------|
| [1]   | PDVel（脉冲/方向速度） |

每个元素返回成员关键字的内部命令码（范围 0–1023）。值为 0 表示该槽位未使用。

此分组由上位机显示/单位层使用，不影响内部控制计算。这些关键字的比例因子和标签来自 [VelPDUnitFct](VelPDUnitFct.md) 和 [VelPDUnitUnt](VelPDUnitUnt.md)。

全局用户单位与嵌入式 P/D 缩放 [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) 在同一轴上互斥。若 `UserUnitsEn` 已开启且 `PDUsrUnits` 也设置为非默认缩放，则读写本组成员（脉冲/方向速度 [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md)）将被拒绝，并返回错误 `338`。成员列表关键字本身不受影响，仅其成员受限。将 `PDUsrUnits` 恢复默认值或将 `UserUnitsEn` 重置为 0 可解除冲突。

本关键字仅适用于 v5（central-i）及以上版本。

## 示例

```text
AVelPDUnitGrp[1]    ; 读取 P/D 速度组的成员命令码
```

## 另请参阅

- [VelPDUnitFct](VelPDUnitFct.md) — P/D 速度量的比例因子
- [VelPDUnitUnt](VelPDUnitUnt.md) — P/D 速度量的单位标签
- [VelUnitGrp](VelUnitGrp.md) — 主反馈速度单位组
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
- [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md) — 脉冲/方向速度
