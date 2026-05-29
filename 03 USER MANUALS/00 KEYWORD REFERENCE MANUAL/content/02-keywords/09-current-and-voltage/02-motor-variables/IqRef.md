---
keyword: IqRef
summary: Read-only quadrature-axis current reference (definition varies by motor type), in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 30
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# IqRef

Read-only quadrature-axis current reference (definition varies by motor type), in milliamperes.

## Overview

`IqRef` is the reference current of the quadrature (q) axis, in milliamperes. Its derivation depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). For three-phase motors it is the torque-producing reference, derived from [CurrRefCtrl](CurrRefCtrl.md) after direction correction and regulated against the feedback [Iq](Iq.md).

## How it works

| Motor type | Description |
|----|----|
| Single-phase / brush motor (MotorType = 1 or 2) | `IqRef` equals [IaRef](IaRef.md) (both equal the direction-corrected current command). |
| Three-phase motor (MotorType = 3 or 4) | `IqRef` equals the final motor current command after direction correction. It is used in dq0-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | `IqRef` equals 0. |

In the three-phase current loop the firmware assigns the q-axis reference directly from the direction-corrected motor current command:

$$
IqRef\ \lbrack mA\rbrack = \pm\,CurrRef
$$

where the sign is set by [CurrDir](CurrDir.md) (`+` for the normal direction, `−` for the inverted direction). `CurrRef` is the [final motor current command](CurrRef.md) after the loops, compensation and injection; on the loop side it traces back to [CurrRefCtrl](CurrRefCtrl.md). The d-axis reference [IdRef](IdRef.md) is held at 0, so all commanded current is on the torque-producing q axis. `IqRef` is then differenced with the feedback [Iq](Iq.md) to form [IqErr](IqErr.md).

![FOC current loop](foc-current-loop.svg)

## Examples

```text
AIqRef              ; read quadrature-axis current reference (mA)
```

## See also

- [Iq](Iq.md) — quadrature-axis feedback current
- [IqErr](IqErr.md) — quadrature-axis current error (IqRef − Iq)
- [IdRef](IdRef.md) — direct-axis current reference (held at 0)
- [CurrRef](CurrRef.md) — final motor current command that IqRef is taken from (clamped against [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)/[ContCL](../../06-protections/02-current-and-voltage/ContCL.md))
- [CurrRefCtrl](CurrRefCtrl.md) — loop-side current reference (before decoupling/compensation)
- [CurrDir](CurrDir.md) — sets the sign of the direction correction
- [IaRef](IaRef.md) — phase A reference that IqRef equals for brush motors
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 21 reports current saturation upstream of IqRef
