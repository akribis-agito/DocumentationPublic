---
keyword: Rm
summary: 电机电阻测量值，单位为毫欧（由 PCSuite 更新）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 373
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
  - 100000
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
# Rm

电机电阻测量值，单位为毫欧（由 PCSuite 更新）。

## 概述

`Rm` 记录电机电阻测量值，单位为毫欧。PCSuite 在运行其电阻与电感测量后更新该值。该值代表相数据还是线间数据由 [RLType](RLType.md) 设置。它是电感测量值 [Lm](Lm.md) 的电阻对应项。

## 工作原理

`Rm` 是一个存储的、闪存存储的轴相关参数，保存一个以毫欧为单位的电阻值（有效范围 1 至 100000 mΩ，默认 1000 mΩ）。电阻与电感测量（从 PCSuite 运行）将测得值写入此处，也可通过命令接口读取或设置。该值是所记录的测量结果，需与 [RLType](RLType.md)（相数据与线间数据）一同解释，并与 [Lm](Lm.md) 配对。

在 v4 上，控制环不会用 `Rm` 直接驱动电流环——它仅是一个存储的测量值。在 central-i v5 上，所存储的 `Rm` 值还用于计算电阻性（R·i）电压前馈项，当电压前馈启用时该项被加入电流环输出。参见 [RmFFWLevel](../../11-control-tuning/05-feedforwards/RmFFWLevel.md) 和 [VoltageFFWOn](../../11-control-tuning/05-feedforwards/VoltageFFWOn.md)。

在 v5 前馈计算中，所存储的值被视为线间电阻：在三相无刷电机（旋转或直线）上，它在内部被减半以得到每相电阻后再应用，而对于直流有刷电机则原样使用所存储的值。该转换是固定的，不依赖于 [RLType](RLType.md)，后者仅记录测量结果是如何报告的。

## 示例

```text
ARm                 ; read measured motor resistance (mΩ)
ARm=1500             ; set the resistance value manually (mΩ)
```

## 另请参阅

- [Lm](Lm.md) — 测得的电机电感
- [RLType](RLType.md) — 选择相数据与线间数据测量
