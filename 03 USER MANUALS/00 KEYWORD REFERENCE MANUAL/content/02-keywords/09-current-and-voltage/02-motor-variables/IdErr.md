---
keyword: IdErr
summary: Read-only direct-axis current error (IdRef − Id), three-phase only, in milliamperes.
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
---
# IdErr

Read-only direct-axis current error (IdRef − Id), three-phase only, in milliamperes.

## Overview

`IdErr` is the calculated current error in the direct (d) axis, in milliamperes — the difference between the reference [IdRef](IdRef.md) and the feedback [Id](Id.md). It is only applicable for three-phase motors ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4); for brush and stepper motors `IdErr` is 0. It is the input to the d-axis current PI controller in dq0-domain (vector) current control.

## How it works

`IdErr` is the difference between the d-axis reference and feedback:

$$
\text{IdErr}\ \lbrack mA\rbrack\  = \ \text{IdRef}\ \lbrack mA\rbrack\  - \ \text{Id}\ \lbrack mA\rbrack
$$

It then drives the direct-axis current PI controller, whose output is [Vd](Vd.md). The error is integrated (scaled by the integral gain [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md)) and added to the proportional term (scaled by the loop gain [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)):

$$
\begin{aligned}
I_{\Sigma} &\mathrel{+}= \text{IdErr} \cdot \text{CurrKi} \cdot 0.001 \cdot a_{aw} \\
\text{Vd} &= (I_{\Sigma} + \text{IdErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

Here $I_{\Sigma}$ is the running integral, `0.001` is the fixed gain scaling, and $a_{aw}$ is the anti-windup gate (0 freezes the integral while the output is voltage-saturated, 1 otherwise). Since [IdRef](IdRef.md) is currently always 0, $\text{IdErr} = -\text{Id}$. The gain keywords [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) and [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) are documented under [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md); this page does not give tuning guidance.

## Examples

```text
AIdErr              ; read direct-axis current error (mA)
```

## See also

- [IdRef](IdRef.md) — direct-axis current reference
- [Id](Id.md) — direct-axis feedback current
- [Vd](Vd.md) — direct-axis PI output produced from IdErr
- [IqErr](IqErr.md) — quadrature-axis current error
