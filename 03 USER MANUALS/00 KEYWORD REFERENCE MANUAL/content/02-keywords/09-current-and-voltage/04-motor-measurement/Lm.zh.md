---
keyword: Lm
summary: 电机电感测量值，单位为微亨（由 PCSuite 更新）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 374
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 1000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# Lm

电机电感测量值，单位为微亨（由 PCSuite 更新）。

## 概述

`Lm` 记录电机电感测量值，单位为微亨。PCSuite 在运行其电阻与电感测量后更新此值。该值表示相数据还是线间数据由 [RLType](RLType.md) 设置。它是电阻测量值 [Rm](Rm.md) 的电感对应项。

## 工作原理

`Lm` 是一个存储的、闪存存储的轴相关参数，保存以微亨为单位的电感值（有效范围 1 至 1000000 µH，默认 1000 µH）。电阻与电感测量（从 PCSuite 运行）将测得值写入此处，也可通过命令接口读取或设置。该值是记录的测量结果，需与 [RLType](RLType.md)（相数据与线间数据）一起解释，并与 [Rm](Rm.md) 配对。

在 v4 上，`Lm` 是一个控制环不使用的存储测量值。在 central-i v5 上，存储的 `Lm` 值还用于计算感性（L·dI/dt）电压前馈项和交叉耦合补偿项，当启用电压前馈时这些项会被加到电流环输出上。参见 [LmFFWLevel](../../11-control-tuning/05-feedforwards/LmFFWLevel.md) 和 [VoltageFFWOn](../../11-control-tuning/05-feedforwards/VoltageFFWOn.md)。

对于 v5 前馈计算，存储值被视为线间电感：在 3 相无刷电机（旋转或直线）上，应用前会在内部将其减半以获得每相电感，而对于直流有刷电机，存储值则按原样使用。此转换是固定的，不依赖于 [RLType](RLType.md)，后者仅记录测量是如何报告的。

## 示例

```text
ALm                 ; read measured motor inductance (µH)
ALm=1200             ; set the inductance value manually (µH)
```

## 另请参阅

- [Rm](Rm.md) — 测得的电机电阻
- [RLType](RLType.md) — 选择相数据与线间数据测量
