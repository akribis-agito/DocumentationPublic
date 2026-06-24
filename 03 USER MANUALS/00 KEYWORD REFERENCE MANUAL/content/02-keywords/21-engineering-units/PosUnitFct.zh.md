---
keyword: PosUnitFct
summary: 内部位置单位与所选位置工程单位之间的比例系数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 803
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
# PosUnitFct

内部位置单位与所选位置工程单位之间的比例系数。

## 概述

`PosUnitFct` 保存一个浮点型比例系数，用于将控制器内部位置单位与您希望使用的**位置**工程单位相关联。该单一系数适用于位置单位组中的所有关键字（参见 [PosUnitGrp](PosUnitGrp.md)），其所代表的工程单位由 [PosUnitUnt](PosUnitUnt.md) 标注。该系数作为全局工程单位功能的一部分生效，通过 [UserUnitsEn](UserUnitsEn.md) 在每个轴上单独开启。

此关键字仅在 central-i v5 中可用。

## 工作原理

`PosUnitFct` 是一个每轴存储于闪存的双精度比例系数。其默认值为 `1`，表示相对于控制器内部位置单位不进行任何重新缩放。将其设置为所需值，以将内部位置单位与通过 [PosUnitUnt](PosUnitUnt.md) 标注的工程单位关联，从而使整个位置组的显示保持一致。

单一系数覆盖整个位置组，因此位置、位置误差、参考值、目标值、限值以及 [PosUnitGrp](PosUnitGrp.md) 中列出的其他成员均共享同一换算关系。

> 注意：固件将此系数作为位置工程单位的配置存储；系数对显示/接受值的实际应用由全局工程单位功能与 [UserUnitsEn](UserUnitsEn.md) 共同处理。换算方向和舍入规则由上位机/单位层决定，而非内部控制环重新缩放——无论此设置如何，控制环始终在内部单位中运行。

## 示例

```text
APosUnitFct[1]=1.0        ; default — no rescaling of the position group
APosUnitFct[1]=0.001      ; example factor for the position group
APosUnitFct[1]            ; read the current position factor
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 系数 / 单位模型
- [PosUnitGrp](PosUnitGrp.md) — 此系数适用的关键字
- [PosUnitUnt](PosUnitUnt.md) — 位置单位标签
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [VelUnitFct](VelUnitFct.md) · [AccUnitFct](AccUnitFct.md) · [FrcUnitFct](FrcUnitFct.md) — 其他量的比例系数
