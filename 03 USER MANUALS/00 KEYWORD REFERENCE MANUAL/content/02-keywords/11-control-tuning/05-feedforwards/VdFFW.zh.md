---
keyword: VdFFW
summary: 只读直轴电压前馈输出，叠加至 d 轴电压指令。
availability:
  standalone: []
  central-i:
  - v5
can_code: 851
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range: null
  default: 0
  scaling: 1.526
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VdFFW

只读直轴电压前馈输出，叠加至 d 轴电压指令。

> 从 central-i v5 起可用。

## 概述

`VdFFW` 是直轴（d 轴）电压前馈输出。它是控制器根据电机电气模型估算出的、每个控制周期驱动指令 d 轴电流所需的基于模型的 d 轴电压。当 [VoltageFFWOn](VoltageFFWOn.md) 使能电压前馈时，`VdFFW` 在电压矢量限幅并变换为相电压之前，被叠加至 d 轴电流 PI 输出 [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md)。它是 [VqFFW](VqFFW.md) 的 d 轴对应量。

`VdFFW` 为只读，以与 [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) 相同的内部 PWM 百分比单位报告。无论是否使能前馈，均会计算该值；其叠加至控制环的操作由 [VoltageFFWOn](VoltageFFWOn.md) 控制。

## 工作原理

每个控制周期，`VdFFW` 是在 d 轴电流参考 [IdRef](../../../02-keywords/09-current-and-voltage/02-motor-variables/IdRef.md) 上求值的电机模型电压项之和：

$$
\text{VdFFW} = R_{\text{ffw}}\,i_{d,\text{ref}} + L_{\text{ffw}}\,f_s\,(i_{d,\text{ref}} - i_{d,\text{ref,prev}}) - X_{\text{ffw}}\,i_{q,\text{ref}}\,\omega
$$

各项依次为：

| 项 | 物理作用 | 由以下参数设定 |
|------|---------------|--------|
| $R_{\text{ffw}}\,i_{d,\text{ref}}$ | 阻性压降：将指令 d 轴电流推过绕组电阻所需的电压 | [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) 乘以 [RmFFWLevel](RmFFWLevel.md) |
| $L_{\text{ffw}}\,f_s\,(i_{d,\text{ref}} - i_{d,\text{ref,prev}})$ | 感性项（L·di/dt）：以指令速率改变 d 轴电流所需的电压，使用一个控制周期内参考电流的变化量（$f_s$ 为控制采样频率） | [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) 乘以 [LmFFWLevel](LmFFWLevel.md) |
| $-X_{\text{ffw}}\,i_{q,\text{ref}}\,\omega$ | 交叉耦合：q 轴电流耦合至 d 轴的速度相关分量，符号与 q 轴交叉项相反 | 由 [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md)（每相电感）、母线电压及电气周期结合电机转速推导得出。与 L·di/dt 感性项不同，**不**受 [LmFFWLevel](LmFFWLevel.md) 缩放。 |

d 轴前馈不含反电动势项：速度比例反电动势电压仅作用于 q 轴，体现在 [VqFFW](VqFFW.md) 中。

若 [VoltageFFWOn](VoltageFFWOn.md) 非零，`VdFFW` 将叠加至 d 轴 PI 输出 [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md)。所得 d 轴和 q 轴电压作为矢量联合限幅至最大 PWM 幅值，再变换为相电压（饱和及逆 Park 变换详情见 [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md)）。d 轴前馈不适用于有刷电机，因为有刷电机仅在单轴上进行控制。

电流环复位时，`VdFFW` 被清零。使用默认电平缩放（[RmFFWLevel](RmFFWLevel.md)、[LmFFWLevel](LmFFWLevel.md) 默认为 0）时，阻性项和感性项均为零（`VdFFW` 无反电动势项），但 d-q 交叉耦合项由 [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md)、母线电压和电气周期决定（而非由 `LmFFWLevel` 决定），因此在运动过程中可为非零值。只有在静止（零速）或 q 轴参考电流为零时，`VdFFW` 才读取为 0；该交叉项仅在 [VoltageFFWOn](VoltageFFWOn.md) 非零时才被叠加至 d 轴电压。

## 示例

```text
AVdFFW               ; read the d-axis voltage feedforward output
```

## 另请参阅

- [VqFFW](VqFFW.md) — 交轴电压前馈输出（含反电动势项）
- [VoltageFFWOn](VoltageFFWOn.md) — 控制 VdFFW 是否被应用的主使能开关
- [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) — VdFFW 叠加至的 d 轴 PI 输出
- [IdRef](../../../02-keywords/09-current-and-voltage/02-motor-variables/IdRef.md) — 阻性项和感性项使用的 d 轴电流参考
- [RmFFWLevel](RmFFWLevel.md) / [LmFFWLevel](LmFFWLevel.md) — 阻性项和感性项的电平缩放
