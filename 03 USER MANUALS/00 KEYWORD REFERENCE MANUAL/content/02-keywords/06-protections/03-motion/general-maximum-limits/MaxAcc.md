---
keyword: MaxAcc
summary: Maximum allowable acceleration/deceleration, checked before a motion starts.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 81
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# MaxAcc

Maximum allowable acceleration/deceleration, checked before a motion starts.

## Overview

`MaxAcc` defines the maximum allowable acceleration/deceleration. It is checked **before** a motion is started: if the commanded acceleration or deceleration exceeds the limit, a command error is reported and recorded in `ErrLog` (the motion is not started). Unlike the velocity/error trips, this is a pre-motion validation rather than a runtime disable.

## Examples

```text
AMaxAcc=2000000      ; reject motions whose accel/decel exceeds this
```

## See also

- [MaxVel](MaxVel.md) — runtime velocity trip
