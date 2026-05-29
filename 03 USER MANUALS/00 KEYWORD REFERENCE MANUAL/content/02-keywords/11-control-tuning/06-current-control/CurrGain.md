---
keyword: CurrGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 104
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
  - 200000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# CurrGain

Proportional gain of the current loop.

## Overview

`CurrGain` is the proportional gain of the current loop — the innermost loop of the control cascade. It multiplies the sum of the current error and the current-error integral to produce the commanded voltage. `CurrGain` and the integral gain [CurrKi](CurrKi.md) together form the current-loop PI controller.

The same `CurrGain` is applied to every current channel that the motor type requires:

| Motor type | Channels controlled by `CurrGain` |
|---|---|
| Voice-coil / brush (single-phase) | Phase A |
| Stepper (two-phase) | Phase A and phase B |
| Three-phase, dq0-domain (vector) control | Quadrature (q) and direct (d) axes |
| Three-phase, abc-domain control | Phase A and phase B |

## How it works

For each controlled channel the current-error integral is accumulated (scaled by [CurrKi](CurrKi.md)), the current error is added to it, and the proportional gain `CurrGain` multiplies the sum to form the channel voltage command. Taking the quadrature axis of a three-phase motor as the example (the current error is [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md), the output voltage is [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)):

$$
\begin{aligned}
\text{Integral} &\mathrel{+}= \text{IqErr} \cdot \text{CurrKi} \cdot 0.001 \cdot \text{noClamp} \\
\text{Vq} &= (\text{Integral} + \text{IqErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

Here `0.001` is the fixed gain scaling applied to both `CurrGain` and `CurrKi`, and `noClamp` is the anti-windup factor (see [CurrKi](CurrKi.md)). The other current channels use the identical structure with their own error and voltage terms.

### Scaling, range and default

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer | 32-bit float |
| Range | 0 to 200000 | 0 to 200000 |
| Default | 0 | 0 |
| Gain scaling | 0.001 | 0.001 |

## Examples

```text
ACurrGain=15000      ; set current-loop proportional gain
ACurrGain            ; read back the gain
```

### Worked example: q-axis voltage from a current error

With `CurrGain = 15000`, `CurrKi = 0` and an instantaneous q-axis error `IqErr = 200` (current units, with no accumulated integral), the q-axis voltage command produced by the current PI is:

`Vq = (0 + 200) x 15000 x 0.001 = 3000` (voltage units)

If the integral term has built up to, say, `Integral = 500`, the voltage becomes `(500 + 200) x 15000 x 0.001 = 10500`. The same arithmetic with `CurrGain = 0` produces zero voltage from any error and the loop becomes open.

## See also

- [CurrKi](CurrKi.md) — current-loop integral gain (completes the PI controller)
- [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md) — quadrature-axis current error the gain acts on
- [IaErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IaErr.md) / [IbErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IbErr.md) — phase-domain errors the same gain acts on
- [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) — quadrature-axis voltage the PI produces
- [ControlMode](../../../02-keywords/09-current-and-voltage/02-motor-variables/ControlMode.md) — selects dq0 vs abc current-control domain
- [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) — bit 22 (voltage saturation) shows when the PI output is clamped by [MaxPWM](../../../02-keywords/06-protections/02-current-and-voltage/MaxPWM.md)
- [VelGain](../04-velocity-control/VelGain.md) — proportional gain of the next loop out (velocity) feeding this current loop
