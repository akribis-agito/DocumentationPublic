---
keyword: Vq
summary: 只读的交轴 PI 控制器输出，用于 dq0 域电流控制（仅限三相）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 17
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    data_type: float32
    range: null
    scaling: 1.526
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# Vq

只读的交轴 PI 控制器输出，用于 dq0 域电流控制（仅限三相）。

## 概述

`Vq` 是 dq0 域电流控制中交轴 (q 轴) PI 控制器的输出，以内部单位表示。它仅适用于三相电机（[MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 或 4）；否则 `Vq` 为 0。若使用 abc 域电流控制（参见 [ControlMode](ControlMode.md)），`Vq` 同样为 0。它是 [Vd](Vd.md) 的交轴对应量。

## 工作原理

`Vq` 是交轴电流 PI 控制器的输出，由误差 [IqErr](IqErr.md) 计算得出。积分项被累加（按积分增益 [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 缩放），并加上比例项（按环路增益 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 缩放）：

$$
\begin{aligned}
I_{\Sigma} &\mathrel{+}= \text{IqErr} \cdot \text{CurrKi} \cdot 0.001 \cdot a_{aw} \\
\text{Vq} &= (I_{\Sigma} + \text{IqErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

$I_{\Sigma}$ 是运行积分；`0.001` 是固定增益缩放；$a_{aw}$ 是抗饱和门控（电压饱和期间为 0 以冻结积分，否则为 1）。

**电压前馈（v5）。** 当 [VoltageFFWOn](../../11-control-tuning/05-feedforwards/VoltageFFWOn.md) 非零时，q 轴电压前馈 [VqFFW](../../11-control-tuning/05-feedforwards/VqFFW.md) 在 PI 输出形成之后、下述矢量饱和之前立即加到 `Vq` 上。`VqFFW` 携带基于模型的电阻、电感、反电动势及 d-q 交叉耦合项；在默认前馈级别设置下其为零，因此 `Vq` 等于 PI 输出。在 v4 中没有电压前馈，`Vq` 直接为 PI 输出。

**矢量饱和。** 在逆 Park 变换之前，`Vq` 与 [Vd](Vd.md) 作为矢量对照最大 PWM 幅值进行限幅。如果 $\text{Vq}^2 + \text{Vd}^2$ 超过平方限值（当 [ControlMode](ControlMode.md) 的增强速度范围位置位时，该限值乘以 $\frac{4}{3}$），则 `Vq` 和 `Vd` 同时按相同系数缩放以保持正弦波形，并置位 [StatReg](../../07-status-and-faults/StatReg.md) 中的电压饱和状态位。从线性（幅值）角度看，平方限值上的 $\frac{4}{3}$ 对应幅值上的 $\frac{2}{\sqrt{3}} \approx 1.1547$ 系数：在增强速度范围下，`Vq`/`Vd` 矢量可达到 $\text{MaxPWM} \times \frac{2}{\sqrt{3}}$，比未启用时所用的普通 `MaxPWM` 限值（$\text{Vq}^2 + \text{Vd}^2 \le \text{MaxPWM}^2$）的幅值约高 15.5 %——这是标准的空间矢量相对正弦增益，由 [Va](Va.md)/[Vb](Vb.md)/[Vc](Vc.md) 上的共模注入使其可用。

**逆 Park 变换。** `Vq` 与 `Vd` 随后通过逆 Park 变换，使用电气换相角 θ 的正弦/余弦，构成相电压指令：

$$
\begin{aligned}
\text{Va} &= \text{Vq} \cdot \sin\theta + \text{Vd} \cdot \cos\theta \\
\text{Vb} &= \text{Vq} \cdot \sin(\theta - 120^\circ) + \text{Vd} \cdot \cos(\theta - 120^\circ) \\
\text{Vc} &= -(\text{Va} + \text{Vb})
\end{aligned}
$$

当 [ControlMode](ControlMode.md) 的增强速度范围位置位时，在 PWM 之前会对 [Va](Va.md)、[Vb](Vb.md)、[Vc](Vc.md) 施加一个共模（空间矢量）偏移。电流环增益 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 和 [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 记录于 [控制整定 – 电流控制](../../11-control-tuning/06-current-control/00-overview.md)；本页不提供整定指导。

## 示例

```text
AVq                 ; read quadrature-axis PI output
```

## 另请参阅

- [Vd](Vd.md) — 直轴 PI 控制器输出
- [IqErr](IqErr.md) — 驱动 q 轴 PI 的交轴误差
- [Va](Va.md), [Vb](Vb.md), [Vc](Vc.md) — 由 Vq/Vd 经逆 Park 变换形成的相电压指令
- [ControlMode](ControlMode.md) — 选择 dq0 与 abc 控制域以及增强速度范围
- [StatReg](../../07-status-and-faults/StatReg.md) — 报告电压饱和状态位
