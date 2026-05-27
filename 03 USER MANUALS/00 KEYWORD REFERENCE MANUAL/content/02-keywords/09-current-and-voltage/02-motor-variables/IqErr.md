---
keyword: IqErr
summary: Read-only quadrature-axis current error (IqRef − Iq), definition varies by motor type, in milliamperes.
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
---
# IqErr

Read-only quadrature-axis current error (IqRef − Iq), definition varies by motor type, in milliamperes.

## Overview

`IqErr` is the calculated current error in the quadrature (q) axis, in milliamperes. Its meaning depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). For three-phase motors it is the torque-producing error used in dq0-domain current control — the difference between the reference [IqRef](IqRef.md) and the feedback [Iq](Iq.md).

## How it works

| Motor type | Description |
|---|---|
| Single-phase / brush motor (MotorType = 1 or 2) | `IqErr` equals [IaErr](IaErr.md) (brush motors close the loop on phase A). |
| Three-phase motor (MotorType = 3 or 4) | `IqErr` is the q-axis error used in dq0-domain current control: $IqErr\ [mA] = IqRef\ [mA] - Iq\ [mA]$. |
| Two-phase stepper motor (MotorType = 6 or 7) | `IqErr` equals 0. |

For three-phase motors, `IqErr` drives the quadrature-axis current PI controller, whose output is [Vq](Vq.md). The firmware integrates the error (scaled by CurrKi) and adds it to the proportional term (scaled by CurrGain):

$$
\begin{aligned}
IqIntegral &\mathrel{+}= IqErr \cdot CurrKi \cdot 0.001 \cdot noClamp \\
Vq &= (IqIntegral + IqErr) \cdot CurrGain \cdot 0.001
\end{aligned}
$$

Here `0.001` is the fixed gain scaling applied in firmware, and `noClamp` is the anti-windup flag (set to 0 to freeze the integral while the combined [Vq](Vq.md)/[Vd](Vd.md) output is voltage-saturated, 1 otherwise). The gain keywords CurrGain and CurrKi are documented under [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md); this page does not give tuning guidance.

## Examples

```text
AIqErr              ; read quadrature-axis current error (mA)
```

## See also

- [IqRef](IqRef.md) — quadrature-axis current reference
- [Iq](Iq.md) — quadrature-axis feedback current
- [Vq](Vq.md) — quadrature-axis PI output produced from IqErr
- [IaErr](IaErr.md) — phase A error that IqErr equals for brush motors
- [IdErr](IdErr.md) — direct-axis current error
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines the definition
