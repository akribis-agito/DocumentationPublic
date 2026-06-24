---
keyword: ForceKi
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 578
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 力环 PID 控制器的积分增益。
---
# ForceKi

力环 PID 控制器的积分增益。

## 概述

`ForceKi` 是力控制环中标准形式 PID 控制器的积分（I）项。它适用于两种力控制结构（标准模式和由 [ForcePIVOn](ForcePIVOn.md) 选择的力叠加 PIV 模式），内部缩放系数固定为 1E-3。

每个控制周期，积分器按 `ForceKi` 缩放的增益力误差进行累积：

$$
\text{integrator} = \text{integrator} + \text{gained error} \cdot \text{ForceKi} \cdot 0.001
$$

其中，*gained error* 为经过 [ForceGain](ForceGain.md) 阶段后的力误差。积分器的值是 PID 输出的 I 分量。

取值范围为 `0` 至 `2147483647`，默认值为 `0`。该关键字保存至闪存，可在电机使能且运动中时修改。

## 工作原理

累积过程包含抗积分饱和机制：每个周期添加的增量乘以环路钳位标志，因此当下游环路（标准模式下为速度环和电流环；力叠加 PIV 模式下为位置/速度级联和电流环）在限值处饱和时，积分器停止向加深饱和方向累积。这可防止输出被限幅时积分项发生饱和。

在标准力控制（[ForcePIVOn](ForcePIVOn.md) = 0）下，钳位标志为速度环和电流环的钳位标志。在力叠加 PIV 控制（[ForcePIVOn](ForcePIVOn.md) = 1）下，增量还受到一个专用力环钳位标志的门控，该标志与生成的位置参考相关联：该标志在每个周期置位（允许累积），仅在位置参考被保持在 [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) 而增益力误差仍为正时，或被保持在 [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) 而增益力误差仍为负时清除。这可防止力指令持续推向软件位置限位时力积分器发生饱和。

## 示例

```text
AForceKi[1]=50          ; set the force-loop integral gain
AForceKi[1]             ; read the force-loop integral gain
```

## 另请参阅

- [ForceGain](ForceGain.md) — 力环比例增益（提供此项累积的增益误差）
- [ForceKd](ForceKd.md) — 力环微分增益
- [ForcePIVOn](ForcePIVOn.md) — 选择力控制结构（决定哪些下游限制钳位该积分器）
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — 环路驱动趋零的误差
- [StatReg](../../07-status-and-faults/StatReg.md) — 饱和位显示下游环路被钳位时（抗饱和已介入）
- [Force control](00-overview.md) — 力环结构概述
