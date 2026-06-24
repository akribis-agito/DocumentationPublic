---
keyword: PosAuxUnitGrp
summary: 共享辅助位置用户单位缩放和标签的辅助编码器位置关键字只读列表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 814
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 5
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
# PosAuxUnitGrp

共享辅助位置用户单位缩放和标签的辅助编码器位置关键字只读列表。

## 概述

当轴的全局用户单位功能启用后（[UserUnitsEn](UserUnitsEn.md) = 1），每个物理量（位置、速度、加速度、力，以及辅助编码器/脉冲方向变体）均以每量专属的比例系数和自由文本单位标签向上位机呈现。`PosAuxUnitGrp` 是**辅助编码器位置**量的成员列表：它告知上位机哪些关键字共同由 [PosAuxUnitFct](PosAuxUnitFct.md) 缩放，并由 [PosAuxUnitUnt](PosAuxUnitUnt.md) 标注。

它是主反馈 [PosUnitGrp](PosUnitGrp.md) 的辅助编码器对应项，适用于辅助反馈位置 [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) 及由其派生的其他辅助位置类型值。

`PosAuxUnitGrp` 为只读且固定：控制器在启动时填充它，因此只能读取以发现分组成员，不能编辑。

## 工作原理

该关键字为非轴数组。每个已填充的元素保存辅助位置单位分组中的一个成员。数组采用 1 索引；元素 [0] 不存在。数组有一个保留槽，因此 `array_size` 为 5 时，最高可用索引为 4。

| 索引 | 成员关键字 |
|------|-----------|
| [1]  | AuxPos（辅助反馈位置） |
| [2]  | AuxIndexPos（辅助索引捕获位置） |
| [3]  | AuxModRev（辅助取模每转） |
| [4]  | AuxEncAbsVal（辅助绝对式编码器值） |

每个元素返回成员关键字的内部指令码（范围 0–1023）。值为 0 表示该槽未使用。

该分组由上位机显示/单位层使用；不会改变内部控制计算。这些关键字的比例系数和标签来自 [PosAuxUnitFct](PosAuxUnitFct.md) 和 [PosAuxUnitUnt](PosAuxUnitUnt.md)。

全局用户单位与嵌入式辅助缩放 [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 在同一轴上互斥。若 `UserUnitsEn` 已开启且 `AuxUsrUnits` 也设置了非默认缩放，则访问该分组中具有辅助用户单位缩放的成员时将报告冲突。该检查仅涵盖携带辅助用户单位缩放的成员（AuxPos、AuxIndexPos、AuxModRev）；AuxEncAbsVal 列于此处仅供参考，不受用户单位缩放影响，访问时不会触发冲突。

此关键字仅在 v5 (central-i) 中可用。

## 示例

```text
APosAuxUnitGrp[1]    ; 读取辅助位置分组第一个成员的指令码
APosAuxUnitGrp[4]    ; 读取第四个成员的指令码
```

## 另请参阅

- [PosAuxUnitFct](PosAuxUnitFct.md) — 辅助位置量的比例系数
- [PosAuxUnitUnt](PosAuxUnitUnt.md) — 辅助位置量的单位标签
- [PosUnitGrp](PosUnitGrp.md) — 主反馈位置单位分组
- [UserUnitsEn](UserUnitsEn.md) — 按轴启用全局用户单位功能
- [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) — 辅助反馈位置
