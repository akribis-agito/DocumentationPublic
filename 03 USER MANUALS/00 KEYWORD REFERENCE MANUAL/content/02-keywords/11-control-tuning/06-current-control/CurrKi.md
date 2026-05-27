---
keyword: CurrKi
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 105
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
# CurrKi

Integral gain of the current loop, with anti-windup.

## Overview

`CurrKi` is the integral gain of the current loop. It multiplies the current error before it is accumulated into the current-error integral. Together with the proportional gain [CurrGain](CurrGain.md) it forms the current-loop PI controller, the innermost loop of the control cascade. The integral term drives the steady-state current error toward zero.

As with `CurrGain`, the same `CurrKi` is applied to every current channel that the motor type requires (phase A for brush motors; phases A and B for steppers and abc-domain three-phase control; the q and d axes for dq0-domain vector control).

## How it works

Each control cycle the current error is scaled by `CurrKi` and added to the running integral; the proportional path then adds the raw error and multiplies by [CurrGain](CurrGain.md) to form the channel voltage. Taking the quadrature axis of a three-phase motor as the example (error [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md), output [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)):

$$
\begin{aligned}
Integral &\mathrel{+}= IqErr \times CurrKi \times 0.001 \times noClamp \\
Vq &= (Integral + IqErr) \times CurrGain \times 0.001
\end{aligned}
$$

`0.001` is the fixed gain scaling applied to both `CurrKi` and `CurrGain`.

### Anti-windup

`noClamp` is the anti-windup factor multiplying the integral increment:

- `noClamp = 1` — normal operation, the integral accumulates.
- `noClamp = 0` — the integral is frozen (its increment is zeroed for that cycle).

The integral is frozen when the output is in voltage saturation and the integration would push the output further into saturation (the output and the current error have the same sign). Voltage saturation is detected on the combined output magnitude — for dq0-domain control on the [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)/[Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) vector against the maximum PWM magnitude — and is reported by the voltage-saturation status bit in [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md). When saturation clears, normal integration resumes.

### Scaling, range and default

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer | 32-bit float |
| Range | 0 to 200000 | 0 to 200000 |
| Default | 0 | 0 |
| Gain scaling | 0.001 | 0.001 |

## Examples

```text
ACurrKi=8000         ; set current-loop integral gain
ACurrKi              ; read back the gain
```

## See also

- [CurrGain](CurrGain.md) — current-loop proportional gain (completes the PI controller)
- [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md) — quadrature-axis current error the gain integrates
- [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) / [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) — voltages the PI produces
- [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) — reports the voltage-saturation status bit
