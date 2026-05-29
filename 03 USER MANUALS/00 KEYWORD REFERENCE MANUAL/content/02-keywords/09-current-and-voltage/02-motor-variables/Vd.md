---
keyword: Vd
summary: Read-only direct-axis PI-controller output in dq0-domain current control (three-phase only).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 16
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
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# Vd

Read-only direct-axis PI-controller output in dq0-domain current control (three-phase only).

## Overview

`Vd` is the output of the direct (d) axis PI controller in dq0-domain current control, in internal units. It is only applicable for three-phase motors ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4); otherwise `Vd` is 0. `Vd` is also 0 if abc-domain current control is used (see [ControlMode](ControlMode.md)). It is the direct-axis counterpart of [Vq](Vq.md).

## How it works

`Vd` is the output of the direct-axis current PI controller, computed from the error [IdErr](IdErr.md). The integral is accumulated (scaled by the integral gain [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md)) and the proportional term (scaled by the loop gain [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)) is added:

$$
\begin{aligned}
I_{\Sigma} &\mathrel{+}= \text{IdErr} \cdot \text{CurrKi} \cdot 0.001 \cdot a_{aw} \\
\text{Vd} &= (I_{\Sigma} + \text{IdErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

$I_{\Sigma}$ is the running integral; `0.001` is the fixed gain scaling; $a_{aw}$ is the anti-windup gate (0 freezes the integral during voltage saturation, 1 otherwise).

**Vector saturation.** Before the inverse Park transform, `Vd` and [Vq](Vq.md) are limited as a vector against the maximum PWM magnitude. If $\text{Vq}^2 + \text{Vd}^2$ exceeds the squared limit (the limit is multiplied by $\frac{4}{3}$ when the enhanced-speed-range bit of [ControlMode](ControlMode.md) is set), both `Vd` and `Vq` are scaled by the same factor so the sine-wave shape is preserved, and the voltage-saturation status bit in [StatReg](../../07-status-and-faults/StatReg.md) is set.

**Inverse Park.** `Vd` and `Vq` then form the phase voltage commands by the inverse Park transform, using the sine/cosine of the electrical commutation angle θ:

$$
\begin{aligned}
\text{Va} &= \text{Vq} \cdot \sin\theta + \text{Vd} \cdot \cos\theta \\
\text{Vb} &= \text{Vq} \cdot \sin(\theta - 120^\circ) + \text{Vd} \cdot \cos(\theta - 120^\circ) \\
\text{Vc} &= -(\text{Va} + \text{Vb})
\end{aligned}
$$

A common-mode (space-vector) offset is then applied to [Va](Va.md), [Vb](Vb.md), [Vc](Vc.md) before PWM. The current-loop gains [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) and [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) are documented under [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md); this page does not give tuning guidance.

## Examples

```text
AVd                 ; read direct-axis PI output
```

## See also

- [Vq](Vq.md) — quadrature-axis PI-controller output
- [IdErr](IdErr.md) — direct-axis error that drives the d-axis PI
- [Va](Va.md), [Vb](Vb.md), [Vc](Vc.md) — phase voltage commands formed from Vd/Vq by inverse Park
- [ControlMode](ControlMode.md) — selects dq0 vs abc control domain and enhanced speed range
- [StatReg](../../07-status-and-faults/StatReg.md) — reports the voltage-saturation status bit
