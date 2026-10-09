---
keyword: VelAuxUnitGrp
summary: 共享辅助速度用户单位缩放和标签的辅助编码器速度关键字只读列表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 820
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
last_updated: '2026-10-10'
doc_revision: '2026.06'
language: zh-CN
---
# VelAuxUnitGrp

共享辅助速度用户单位缩放和标签的辅助编码器速度关键字只读列表。

## 概述

当某轴启用全局用户单位（[UserUnitsEn](UserUnitsEn.md) = 1）时，每个物理量都以各量的比例系数和自由文本单位标签向上位机呈现。`VelAuxUnitGrp` 是**辅助编码器速度**量的成员列表：它告知上位机哪些关键字由 [VelAuxUnitFct](VelAuxUnitFct.md) 统一缩放，并由 [VelAuxUnitUnt](VelAuxUnitUnt.md) 标注。

它是主反馈 [VelUnitGrp](VelUnitGrp.md) 的辅助编码器对应项，适用于辅助反馈速度 [AuxVel](../10-motion/01-kinematics-status/AuxVel.md)。

`VelAuxUnitGrp` 为只读且固定：控制器在启动时填充该数组，您只能读取以发现组成员，不能对其进行编辑。

## 工作原理

该关键字是一个非轴数组。每个已填充的元素保存辅助速度单位组的一个成员。数组从 1 开始索引；元素 [0] 不存在。数组有一个保留槽，因此 `array_size` 为 2 时，最高可用索引为 1。

| 索引 | 成员关键字 |
|-------|----------------|
| [1]   | AuxVel（辅助反馈速度） |

每个元素返回成员关键字的内部命令代码（范围 0–1023）。值为 0 表示该槽未使用。

此分组由上位机显示/单位层使用；不改变内部控制计算。这些关键字的比例系数和标签分别来自 [VelAuxUnitFct](VelAuxUnitFct.md) 和 [VelAuxUnitUnt](VelAuxUnitUnt.md)。

仅当访问的关键字使用嵌入式 `UsrUnits`、`AuxUsrUnits` 或 `PDUsrUnits` 缩放、属于相应的全局单位组，且该轴同时设置了 `UserUnitsEn = 1` 和非默认嵌入式比例时，才触发错误 `338`。在 AGM800-EC 上，`AuxVel` 和 `PDVel` 使用固定时间域缩放，不会触发此冲突。仍使用嵌入式缩放的位置关键字继续受此检查约束。完整换算列表见 [AGM800-EC 时间与单位](../01-system/03-timing/AGM800-EC-units.zh.md)。

此关键字仅在 v5（central-i）版本可用。

## 示例

```text
AVelAuxUnitGrp[1]    ; 读取辅助速度组的成员命令代码
```

## 另请参阅

- [VelAuxUnitFct](VelAuxUnitFct.md) — 辅助速度量的比例系数
- [VelAuxUnitUnt](VelAuxUnitUnt.md) — 辅助速度量的单位标签
- [VelUnitGrp](VelUnitGrp.md) — 主反馈速度单位组
- [UserUnitsEn](UserUnitsEn.md) — 每轴启用全局用户单位功能
- [AuxVel](../10-motion/01-kinematics-status/AuxVel.md) — 辅助反馈速度
