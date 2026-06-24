---
keyword: VelUnitFct
summary: 内部速度单位与所选速度工程单位之间的比例因子。
availability:
  standalone: []
  central-i:
  - v5
can_code: 806
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
# VelUnitFct

内部速度单位与所选速度工程单位之间的比例因子。

## 概述

`VelUnitFct` 保存将控制器内部速度单位与您所需**速度**工程单位关联的浮点比例因子。该单一因子适用于速度单位组中的所有关键字（参见 [VelUnitGrp](VelUnitGrp.md)），其所代表的工程单位由 [VelUnitUnt](VelUnitUnt.md) 标注。该因子作为全局工程单位功能的一部分生效，该功能通过 [UserUnitsEn](UserUnitsEn.md) 按轴开启。

本关键字仅适用于 central-i v5 及以上版本。

## 工作原理

`VelUnitFct` 是一个存储在闪存中的逐轴双精度因子。默认值为 `1`，表示相对于控制器内部速度单位不进行任何缩放。将其设置为内部速度单位与您用 [VelUnitUnt](VelUnitUnt.md) 标注的工程单位之间的换算关系，以确保整个速度组的呈现保持一致。

单一因子覆盖整个速度组，因此速度、速度误差、参考值、阈值以及 [VelUnitGrp](VelUnitGrp.md) 列出的其他成员均共用相同的换算关系。

> 注意：固件将此因子存储为速度工程单位的配置；该因子对显示/接受值的应用由全局工程单位功能与 [UserUnitsEn](UserUnitsEn.md) 共同处理。无论此设置如何，控制环始终在内部单位下运行。

## 示例

```text
AVelUnitFct[1]=1.0        ; 默认——速度组不进行缩放
AVelUnitFct[1]=0.001      ; 速度组的示例因子
AVelUnitFct[1]            ; 读取当前速度因子
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 因子 / 单位模型
- [VelUnitGrp](VelUnitGrp.md) — 本因子适用的关键字
- [VelUnitUnt](VelUnitUnt.md) — 速度单位标签
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [PosUnitFct](PosUnitFct.md) · [AccUnitFct](AccUnitFct.md) · [FrcUnitFct](FrcUnitFct.md) — 其他量的因子
