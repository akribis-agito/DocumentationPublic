---
keyword: MaxVel
summary: Maximum closed-loop velocity; exceeding it (+25% buffer) disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 80
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVel

Maximum closed-loop velocity; exceeding it (+25% buffer) disables the axis.

## Overview

`MaxVel` is the maximum allowable velocity in closed-loop operation, with an additional 25% buffer before the trip. If the absolute value of `Vel[1]` exceeds `MaxVel × 125%`, the axis is **instantaneously** disabled and an error is reported to the fault register `ConFlt`.

## Examples

```text
AMaxVel=500000       ; maximum velocity (user units)
```

## See also

- [MaxVelErr](MaxVelErr.md) — velocity-error trip
- [MaxAcc](MaxAcc.md) — acceleration limit (checked before motion)
