---
keyword: Vq
summary: Read-only quadrature-axis PI-controller output in dq0-domain current control (three-phase only).
availability:
  standalone:
  - v4
  central-i:
  - v4
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
  scaling: 1.0
  implemented: final
overrides: {}
---
# Vq

Read-only quadrature-axis PI-controller output in dq0-domain current control (three-phase only).

## Overview

`Vq` is the output of the quadrature (q) axis PI controller in dq0-domain current control, in internal units. It is only applicable for three-phase motors ([MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4); otherwise `Vq` is 0. `Vq` is also 0 if abc-domain current control is used (see [ControlMode](ControlMode.md)). It is the quadrature-axis counterpart of [Vd](Vd.md).

## How it works

For dq0-domain current control, [Vd](Vd.md) and `Vq` form the phase voltage commands ([Va](Va.md), [Vb](Vb.md), [Vc](Vc.md)) by the inverse Park transform.

## Examples

```text
Vq?                 ; read quadrature-axis PI output
```

## See also

- [Vd](Vd.md) — direct-axis PI-controller output
- [Va](Va.md), [Vb](Vb.md), [Vc](Vc.md) — phase voltage commands formed from Vd/Vq
- [ControlMode](ControlMode.md) — selects dq0 vs abc control domain
