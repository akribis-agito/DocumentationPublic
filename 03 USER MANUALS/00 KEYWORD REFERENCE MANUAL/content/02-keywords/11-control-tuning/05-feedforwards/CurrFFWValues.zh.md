---
keyword: CurrFFWValues
summary: 只读的前馈电流：滤波后的总量及其各组成部分，单位为 mA。
availability:
  standalone: []
  central-i:
  - v5
can_code: 856
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 7
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# CurrFFWValues

只读的前馈电流：滤波后的总量及其各组成部分，单位为 mA。

## 概述

`CurrFFWValues` 用于读回轴的前馈电流。它是只读参数，不保存到闪存。单位为 mA。

| 索引 | 值 |
|---|---|
| `CurrFFWValues[1]` | 经过前馈滤波器后、加入电流参考的前馈总电流。**包含摩擦电流。** |
| `CurrFFWValues[2]` | 速度前馈项（[VelFFW](VelFFW.md)） |
| `CurrFFWValues[3]` | 加速度前馈项（[AccFFW](AccFFW.md)） |
| `CurrFFWValues[4]` | 加加速度（Jerk）前馈项 |
| `CurrFFWValues[5]` | 保留（读数为 0） |
| `CurrFFWValues[6]` | 前馈滤波器*之前*的摩擦前馈电流（仅 AGM800 和 AGM800-EC） |

## 工作原理

索引 6 是摩擦前馈环节经 [FricLim](../../../03-special-features/friction-compensation/FricLim.md) 钳位后的输出。它取代 5.3.0-rc4 中的 `FricCurr`。当该环节关闭或未运行时（例如电流模式），读数为 0。

索引 1 是前馈滤波器（[FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md)）的输出。摩擦电流与速度、加速度前馈项一起经过该滤波器，因此索引 1 包含摩擦。`FFFiltOn` = 0 时，索引 1 即为简单求和。`FFFiltOn` = 1 时，在换向处索引 1 滞后于索引 6。在 CNC 前馈跳过的两个控制周期内，进入滤波器的前馈（包括摩擦）被清零，因此索引 1 下降——`FFFiltOn` = 0 时直接降为 0——而索引 2 至 6 保持其值。在速度模式以及 [ForcePIVOn](../07-force-control/ForcePIVOn.md) = 1 的力模式下，不使用速度和加速度前馈项，索引 1 只承载摩擦。

在速度环不形成电流参考的模式下（例如电流模式），索引 1 保持其上一次的值。

在没有摩擦前馈环节的产品上，数组到索引 5 为止。

## 示例

```text
ACurrFFWValues[6]     ; 滤波器之前的摩擦电流，mA
ACurrFFWValues[1]     ; 滤波器之后的前馈总电流，mA
```

## 另请参阅

- [摩擦前馈](../../../03-special-features/friction-compensation/00-overview.md) — 摩擦环节
- [FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md) — 前馈滤波器
- [VelFFW](VelFFW.md) / [AccFFW](AccFFW.md) — 参考前馈增益
