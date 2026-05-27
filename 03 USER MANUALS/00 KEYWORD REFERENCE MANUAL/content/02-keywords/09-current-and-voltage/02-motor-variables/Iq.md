---
keyword: Iq
summary: Read-only quadrature-axis feedback current (definition varies by motor type), in milliamperes.
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
---
# Iq

Read-only quadrature-axis feedback current (definition varies by motor type), in milliamperes.

## Overview

`Iq` is the quadrature (q) axis feedback current. Its meaning depends on [MotorType](../../02-motor-and-amplifier/MotorType.md). For three-phase motors it is the torque-producing current regulated against [IqRef](IqRef.md) in dq0-domain current control. It is the quadrature-axis counterpart of [Id](Id.md).

## How it works

| Motor type | Description |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | `Iq` equals [Ia](Ia.md). |
| Three-phase motor (MotorType = 3 or 4) | `Iq` is the feedback current after the Park transform in the quadrature axis, in milliamperes. |
| Two-phase stepper motor (MotorType = 6 or 7) | `Iq` equals 0. |

## Examples

```text
AIq                 ; read quadrature-axis feedback current (mA)
```

## See also

- [IqRef](IqRef.md) — quadrature-axis current reference
- [IqErr](IqErr.md) — quadrature-axis current error
- [Id](Id.md) — direct-axis feedback current
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — motor type that determines the definition
