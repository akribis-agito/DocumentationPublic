---
keyword: Iq
summary: 只读的交轴反馈电流（定义随电机类型而异），单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 12
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
# Iq

只读的交轴反馈电流（定义随电机类型而异），单位为毫安。

## 概述

`Iq` 是交轴（q 轴）反馈电流。q 轴与转子磁链正交，因此对于三相电机，`Iq` 是产生力矩的分量（其直轴对应分量 [Id](Id.md) 为磁通/磁场分量）。其含义取决于 [MotorType](../../02-motor-and-amplifier/MotorType.md)。对于三相电机，它在 dq0 域（矢量）电流控制中相对于 [IqRef](IqRef.md) 进行调节。

## 工作原理

| 电机类型 | 说明 |
|----|----|
| 单相/有刷电机（MotorType = 1 或 2） | `Iq` 等于 [Ia](Ia.md)（无变换；有刷电机仅对 A 相闭环）。 |
| 三相电机（MotorType = 3 或 4） | `Iq` 是对所测相电流进行 Clarke + Park 组合变换后的交轴电流（见下文）。 |
| 两相步进电机（MotorType = 6 或 7） | `Iq` 等于 0。 |

对于三相电机，`Iq` 由所测相电流 [Ia](Ia.md) 和 [Ib](Ib.md) 利用电气换相角 θ 的正弦/余弦计算得出（分别在换相角处以及 θ − 120° 处求值）：

$$
\text{Iq}\ \lbrack mA\rbrack = \frac{2}{\sqrt 3}\left(\text{Ia} \cdot \cos(\theta - 120^\circ) - \text{Ib} \cdot \cos\theta\right)
$$

系数 $\frac{2}{\sqrt3} \approx 1.1547$ 按式中所示应用。θ 是来自换相/自动定相逻辑的电气换相角。直轴对应分量 [Id](Id.md) 使用相应的正弦项。

在旋转 dq 坐标系中，q 轴承载产生力矩的分量，并与 d 轴上的转子磁链正交。Iq 和 Id 是所测电流矢量在此旋转坐标系上的投影，以 θ 为索引：

![dq rotating frame: d axis aligned with the rotor flux, q axis 90 degrees ahead, both rotating with the electrical angle theta relative to the stationary abc axes](dq-rotating-frame.svg)

![FOC current loop](foc-current-loop.svg)

## 示例

```text
AIq                 ; read quadrature-axis feedback current (mA)
```

## 另请参阅

- [IqRef](IqRef.md) — 交轴电流参考
- [IqErr](IqErr.md) — 交轴电流误差（IqRef − Iq），输入至电流 PI 调节器
- [Id](Id.md) — 直轴（磁通/磁场）反馈电流
- [Vq](Vq.md) — 交轴 PI 输出，送入逆 Park 变换
- [Ia](Ia.md)、[Ib](Ib.md) — 用于推导 Iq 的所测相电流
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — 决定其定义的电机类型
