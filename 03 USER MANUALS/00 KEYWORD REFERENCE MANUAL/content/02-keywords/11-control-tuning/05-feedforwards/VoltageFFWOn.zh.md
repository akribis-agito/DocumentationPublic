---
keyword: VoltageFFWOn
summary: 电流/电压环中电压前馈的主使能开关。
availability:
  standalone: []
  central-i:
  - v5
can_code: 852
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VoltageFFWOn

电流/电压环中电压前馈的主使能开关。

> 从 central-i v5 起可用。

## 概述

`VoltageFFWOn` 用于开启或关闭轴的电压前馈。电压前馈是一种基于模型的项，它根据电机电气模型（电阻、电感和反电动势）估算驱动指令电流所需的电机端电压，并在电流 PI 控制器之前将其叠加。通过提前提供大部分所需电压，可减少电流环跟踪参考值的工作量，从而改善高速和快速电流变化下的电流跟踪性能。

`VoltageFFWOn = 0`（默认）时，不向电流环输出叠加前馈电压。`VoltageFFWOn = 1` 时，计算得到的前馈量叠加至环路电压指令。

前馈输出 [VqFFW](VqFFW.md) 和 [VdFFW](VdFFW.md) 始终被计算，无论该开关状态如何均可读取；`VoltageFFWOn` 仅控制它们是否实际被叠加至电压指令。

## 工作原理

每个控制周期，控制器根据电机模型的三个物理分量计算前馈电压：

- 阻性项：将指令电流推过绕组电阻（R·i）所需的电压，由 [RmFFWLevel](RmFFWLevel.md) 缩放；
- 感性项：以指令速率改变电流（L·di/dt）所需的电压，由 [LmFFWLevel](LmFFWLevel.md) 缩放；
- 反电动势项：运动电机产生的速度比例电压，由 [BEMFConst](BEMFConst.md) 乘以 [BEMFFFWLevel](BEMFFFWLevel.md) 得出。

这些分量被组合为交轴和直轴前馈输出 [VqFFW](VqFFW.md) 和 [VdFFW](VdFFW.md)。`VoltageFFWOn = 1` 时，这些输出在合并电压矢量限幅至 PWM 幅值并变换为相电压之前，被分别叠加至 q 轴和 d 轴 PI 输出 [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) 和 [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md)。对于有刷电机，q 轴前馈以相同方式叠加至单相电压指令。

| 值 | 含义 |
|-------|---------|
| 0 | 电压前馈禁用（默认）。前馈输出仍然计算且可读取，但不被应用。 |
| 1 | 电压前馈使能。计算得到的前馈量叠加至电流环电压指令。 |

`VoltageFFWOn` 为闪存存储参数，轴运动时不可更改（电机使能但静止时可更改）。

## 示例

```text
AVoltageFFWOn=1      ; enable voltage feedforward
AVoltageFFWOn        ; read back the enable state
AVoltageFFWOn=0      ; disable voltage feedforward
```

## 另请参阅

- [VqFFW](VqFFW.md) / [VdFFW](VdFFW.md) — 计算得到的 q 轴和 d 轴前馈电压输出
- [RmFFWLevel](RmFFWLevel.md) — 阻性（R·i）前馈项的电平
- [LmFFWLevel](LmFFWLevel.md) — 感性（L·di/dt）前馈项的电平
- [BEMFConst](BEMFConst.md) / [BEMFFFWLevel](BEMFFFWLevel.md) — 反电动势常数及其前馈电平
- [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) / [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) — 前馈叠加至的电流 PI 输出
