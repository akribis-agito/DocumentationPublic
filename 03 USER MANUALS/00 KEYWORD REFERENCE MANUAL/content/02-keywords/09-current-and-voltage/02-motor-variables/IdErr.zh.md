---
keyword: IdErr
summary: 只读的直轴电流误差（IdRef − Id），仅适用于三相电机，单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 22
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# IdErr

只读的直轴电流误差（IdRef − Id），仅适用于三相电机，单位为毫安。

## 概述

`IdErr` 是直轴（d 轴）上计算得到的电流误差，单位为毫安——即参考值 [IdRef](IdRef.md) 与反馈值 [Id](Id.md) 之差。它仅适用于三相电机（[MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 或 4）；对于有刷电机和步进电机，`IdErr` 为 0。它是 dq0 域（矢量）电流控制中 d 轴电流 PI 调节器的输入。

## 工作原理

`IdErr` 是 d 轴参考值与反馈值之差：

$$
\text{IdErr}\ \lbrack mA\rbrack\  = \ \text{IdRef}\ \lbrack mA\rbrack\  - \ \text{Id}\ \lbrack mA\rbrack
$$

随后它驱动直轴电流 PI 调节器，其输出为 [Vd](Vd.md)。误差经积分（按积分增益 [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 缩放），再加上比例项（按环路增益 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 缩放）：

$$
\begin{aligned}
I_{\Sigma} &\mathrel{+}= \text{IdErr} \cdot \text{CurrKi} \cdot 0.001 \cdot a_{aw} \\
\text{Vd} &= (I_{\Sigma} + \text{IdErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

其中 $I_{\Sigma}$ 为运行中的积分项，`0.001` 为固定的增益缩放系数，$a_{aw}$ 为抗积分饱和门控（输出处于电压饱和时取 0 以冻结积分，否则取 1）。由于 [IdRef](IdRef.md) 目前始终为 0，因此 $\text{IdErr} = -\text{Id}$。增益关键字 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 和 [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 在[控制整定 – 电流控制](../../11-control-tuning/06-current-control/00-overview.md)中说明；本页不提供整定指导。

## 示例

```text
AIdErr              ; read direct-axis current error (mA)
```

## 另请参阅

- [IdRef](IdRef.md) — 直轴电流参考
- [Id](Id.md) — 直轴反馈电流
- [Vd](Vd.md) — 由 IdErr 产生的直轴 PI 输出
- [IqErr](IqErr.md) — 交轴电流误差
