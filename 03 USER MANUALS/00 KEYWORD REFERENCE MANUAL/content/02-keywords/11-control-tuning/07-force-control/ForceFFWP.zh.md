---
keyword: ForceFFWP
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 599
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
    can_code: 607
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
summary: 位置维度力前馈增益（仅用于 force-over-PIV 控制）。
---
# ForceFFWP

位置维度力前馈增益（仅用于 force-over-PIV 控制）。

## 概述

`ForceFFWP` 是位置维度力前馈增益。它**仅**在 force-over-PIV 控制（[ForcePIVOn](ForcePIVOn.md) = 1）中使用；在标准力控制（`ForcePIVOn = 0`）中无效。

在 force-over-PIV 模式下，它与经滤波的力参考值相对于进入力运行模式时刻的变化量相乘，结果加至力 PID 输出，然后再将该和值转换为位置参考值：

$$
\text{ForceFFWP term} = \text{ForceFFWP} \cdot (\text{ForceRef} - \text{ForceRef}_{\text{entry}})
$$

其中 `ForceRef` 为经滤波的参考值 [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md)，`ForceRef_entry` 为进入力模式时刻所记录的经滤波参考值。该增益以内部缩放系数 1.0 应用（直接使用输入值）。

值范围为 `0` 至 `2147483647`，默认值为 `0`。该关键字保存至闪存，可在电机使能及运动中修改。

## 工作原理

在 force-over-PIV 控制中，力环为最外环，其输出为内层位置/速度级联的位置参考值。力 PID 输出（P + I + D）与此 `ForceFFWP` 前馈项相加；该和值乘以控制器采样时间后，加至进入力模式时的位置，形成位置参考值，再经软件位置限位（[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) 和 [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)）限幅。将前馈基准设为进入时刻的力参考值，确保在模式切换时该贡献为零，从而实现无扰切换。

### 环路数学

设 $T_s$ 为控制器采样时间，$\text{Pos}_{\text{entry}}$ 为进入力模式时捕获的位置，$\text{ForceRef}_{\text{entry}}$ 为同一时刻捕获的经滤波力参考值，则生成的位置参考值为：

$$
\text{PosRef} = \text{Pos}_{\text{entry}} + T_s \cdot \Big( (P+I+D) + \text{ForceFFWP} \cdot (\text{ForceRef} - \text{ForceRef}_{\text{entry}}) \Big)
$$

随后经 [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) 和 [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) 限幅。括号内的和值乘以 $T_s$ 后加至固定的进入位置 $\text{Pos}_{\text{entry}}$——每个周期从零重新计算，而非累积至前一周期的参考值——因此持续的力环输出使位置参考值保持在与该输出成比例的固定偏置处。在模式进入时，位置误差和力参考值偏差均为零，因此 `PosRef` 从 $\text{Pos}_{\text{entry}}$ 处精确启动。

## 示例

```text
AForcePIVOn[1]=1        ; select force-over-PIV control
AForceFFWP[1]=500       ; set the position-wise force feedforward gain
AForceFFWP[1]           ; read the position-wise force feedforward gain
```

## 另见

- [ForcePIVOn](ForcePIVOn.md) — 须为 1，ForceFFWP 方可生效
- [ForceFFW](ForceFFW.md) — 电流维度力前馈
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — 本增益所作用的经滤波参考值
- [Force control](00-overview.md) — 力环结构概述
