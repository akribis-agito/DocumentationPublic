---
keyword: IqErr
summary: 只读的交轴电流误差（IqRef − Iq），定义随电机类型而异，单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 23
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
# IqErr

只读的交轴电流误差（IqRef − Iq），定义随电机类型而异，单位为毫安。

## 概述

`IqErr` 是交轴（q 轴）上计算得到的电流误差，单位为毫安。其含义取决于 [MotorType](../../02-motor-and-amplifier/MotorType.md)。对于三相电机，它是 dq0 域电流控制中所用的、产生力矩的误差——即参考值 [IqRef](IqRef.md) 与反馈值 [Iq](Iq.md) 之差。

## 工作原理

| 电机类型 | 说明 |
|---|---|
| 单相/有刷电机（MotorType = 1 或 2） | `IqErr` 等于 [IaErr](IaErr.md)（有刷电机对 A 相闭环）。 |
| 三相电机（MotorType = 3 或 4） | `IqErr` 是 dq0 域电流控制中所用的 q 轴误差：$\text{IqErr}\ [mA] = \text{IqRef}\ [mA] - \text{Iq}\ [mA]$。 |
| 两相步进电机（MotorType = 6 或 7） | `IqErr` 等于 0。 |

对于三相电机，`IqErr` 驱动交轴电流 PI 调节器，其输出为 [Vq](Vq.md)。误差经积分（按积分增益 [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 缩放），再加上比例项（按环路增益 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 缩放）：

$$
\begin{aligned}
I_{\Sigma} &\mathrel{+}= \text{IqErr} \cdot \text{CurrKi} \cdot 0.001 \cdot a_{aw} \\
\text{Vq} &= (I_{\Sigma} + \text{IqErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

其中 $I_{\Sigma}$ 为运行中的积分项，`0.001` 为固定的增益缩放系数，$a_{aw}$ 为抗积分饱和门控（设为 0 可在 [Vq](Vq.md)/[Vd](Vd.md) 组合输出处于电压饱和时冻结积分，否则设为 1）。增益关键字 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 和 [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 在[控制整定 – 电流控制](../../11-control-tuning/06-current-control/00-overview.md)中说明；本页不提供整定指导。

## 示例

```text
AIqErr              ; read quadrature-axis current error (mA)
```

## 另请参阅

- [IqRef](IqRef.md) — 交轴电流参考
- [Iq](Iq.md) — 交轴反馈电流
- [Vq](Vq.md) — 由 IqErr 产生的交轴 PI 输出
- [IaErr](IaErr.md) — 有刷电机中 IqErr 所等于的 A 相误差
- [IdErr](IdErr.md) — 直轴电流误差
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — 决定其定义的电机类型
