---
keyword: DynBrkRef
summary: 设置动态制动的最大强度（短接占空比上限）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 404
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range: null
  default: null
  scaling: 2.288
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# DynBrkRef

设置动态制动的最大强度——即相短接占空比的上限。

## 概述

当[动态制动](Dynamicbrake.md)接入时，轴以可变占空比短接电机相：占空比越高，制动越强。`DynBrkRef` 设置该占空比的**上限**——即允许轴施加的最强制动。当制动电流接近电流限制时，轴会自动将实际占空比从该上限向下缩放，因此 `DynBrkRef` 是一个最大值，而非固定值。

该值以制动强度表示，其中 **1000 对应最大（100%）短接占空比**。较小的值按比例将制动上限设得更弱；0 即使在设置了 [DynBrakeOn](DynBrakeOn.md) 时也会禁用制动。

## 工作原理

在动态制动接入期间，轴每个控制周期都会根据电流限制下方剩余的余量重新计算短接占空比：

$$
\text{duty} = \frac{\text{PeakCL}_{limited} - |\text{MotorCurr}|}{\text{PeakCL}_{limited}} \times \text{DynBrkRef} \times scaler
$$

- 结果被钳位至范围 `[0, DynBrkRef]`，因此当制动电流向 [PeakCL](../02-current-and-voltage/PeakCL.md)/[ContCL](../02-current-and-voltage/ContCL.md) 限制上升时，所施加的占空比会自动回退，以将电流保持在限制范围内。
- `scaler` 是固定的软启动斜坡（从较低值开始，并在数个周期内逐步升至满值），因此制动是逐渐接入而非阶跃式接入的。该斜坡不可由用户配置。
- **母线电压保护：** 如果母线电压达到其上限（[MaxVBus](../02-current-and-voltage/MaxVBus.md) 持续 [MaxVBusTime](../02-current-and-voltage/MaxVBusTime.md)，或绝对限制 [MaxVBusAbs](../02-current-and-voltage/MaxVBusAbs.md)），占空比将被强制为 0，以避免将更多再生能量泵入已经偏高的母线。

因此 `DynBrkRef` 是余量公式向下缩放的起点——即最强制动的上限。将其设得越高，制动在电流限制以内就越强；无论该值为何，控制器都不会超出电流限制。

> **没有单独的接入速度设置：** 制动升压的软启动“速度”在固件中固定，不作为关键字暴露。仅制动强度上限（`DynBrkRef`）和使能开关（[DynBrakeOn](DynBrakeOn.md)）可由用户配置。

## 示例

```text
ADynBrakeOn=1
ADynBrkRef=1000         ; allow full-strength braking (100% duty ceiling)
ADynBrkRef             ; read back the configured ceiling
ADynBrkRef=500          ; cap braking at roughly half strength
```

## 参见

- [Dynamic brake](Dynamicbrake.md) — 动态制动机制概述
- [DynBrakeOn](DynBrakeOn.md) — 使能动态制动
- [PeakCL](../02-current-and-voltage/PeakCL.md) / [ContCL](../02-current-and-voltage/ContCL.md) — 限制制动的电流限值
- [MaxVBus](../02-current-and-voltage/MaxVBus.md) / [MaxVBusAbs](../02-current-and-voltage/MaxVBusAbs.md) — 强制占空比为 0 的母线电压上限
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 28 报告动态制动激活
