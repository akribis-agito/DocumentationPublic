---
keyword: FrcUnitFct
summary: 内部力单位与所选力工程单位之间的缩放因子。
availability:
  standalone: []
  central-i:
  - v5
can_code: 812
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
# FrcUnitFct

内部力单位与所选力工程单位之间的缩放因子。

## 概述

`FrcUnitFct` 存储浮点缩放因子，用于将控制器的内部力单位与您希望使用的**力**工程单位相关联。该单一因子适用于力单位组中的每个关键字（参见 [FrcUnitGrp](FrcUnitGrp.md)），其所代表的工程单位由 [FrcUnitUnt](FrcUnitUnt.md) 标注。该因子作为全局工程单位功能的一部分生效，该功能通过 [UserUnitsEn](UserUnitsEn.md) 按轴启用。

该关键字仅在 central-i v5 中可用。

## 工作原理

`FrcUnitFct` 是每轴的双精度因子，保存至闪存。其默认值为 `1`，表示相对于控制器内部力单位不进行任何缩放。将其设置为内部力单位与您用 [FrcUnitUnt](FrcUnitUnt.md) 标注的工程单位之间的换算关系，从而使整个力组的值保持一致呈现。

单一因子覆盖整个力组，因此力指令、参考值、反馈、误差以及 [FrcUnitGrp](FrcUnitGrp.md) 列出的其他成员均共用同一换算关系。

> 注意：固件将该因子作为力工程单位的配置存储；因子对显示/接受值的实际作用由全局工程单位功能与 [UserUnitsEn](UserUnitsEn.md) 共同处理。无论此设置如何，控制环始终以内部单位运行。

## 示例

```text
AFrcUnitFct[1]=1.0        ; default — no rescaling of the force group
AFrcUnitFct[1]=0.001      ; example factor for the force group
AFrcUnitFct[1]            ; read the current force factor
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 系数 / 单位模型
- [FrcUnitGrp](FrcUnitGrp.md) — 该因子适用的关键字
- [FrcUnitUnt](FrcUnitUnt.md) — 力单位标签
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [PosUnitFct](PosUnitFct.md) · [VelUnitFct](VelUnitFct.md) · [AccUnitFct](AccUnitFct.md) — 其他物理量因子
