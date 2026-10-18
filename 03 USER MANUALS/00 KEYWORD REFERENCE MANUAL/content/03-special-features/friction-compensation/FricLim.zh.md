---
keyword: FricLim
summary: 整个摩擦环节的钳位，单位为 PeakCL 的 %（由 StribLim 更名）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 925
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100
  default: 40
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricLim

整个摩擦环节的钳位，单位为 PeakCL 的 %（由 StribLim 更名）。

## 概述

`FricLim` 把摩擦前馈电流限制在 [PeakCL](../../02-keywords/06-protections/02-current-and-voltage/PeakCL.md) 的 ±`FricLim` %。适用于 AGM800 和 AGM800-EC（central-i v5）。它取代 5.3.0-rc4 中的 `StribLim`（CAN 代码不变）。取值范围为 0 至 100，默认值为 40。轴运动中不能更改。

## 工作原理

钳位作用于环节的总输出——所选模型加上象限切换冲击——在其加入前馈通路之前。它跟随 `PeakCL`：更改 `PeakCL` 时，钳位随之改变。`FricLim=0` 关闭摩擦输出。

钳位位于前馈滤波器之前。当 [FFFiltOn](../../02-keywords/11-control-tuning/05-feedforwards/FFFiltOn.md) = 1 且滤波器存在高于单位增益的峰值时，滤波后的摩擦电流可能短暂超过 `FricLim`。

固件不会报告钳位正在限幅。`FricLim` 目前保持现状；摩擦环节是否需要单独的钳位尚待确定（Firmware-Main #1423）。

## 示例

```text
AFricLim=40        ; 摩擦电流限制为 PeakCL 的 40%
```

## 另请参阅

- [PeakCL](../../02-keywords/06-protections/02-current-and-voltage/PeakCL.md)
- [CurrFFWValues](../../02-keywords/11-control-tuning/05-feedforwards/CurrFFWValues.md) — 索引 6 显示钳位后的摩擦电流
- [摩擦前馈](00-overview.md)
