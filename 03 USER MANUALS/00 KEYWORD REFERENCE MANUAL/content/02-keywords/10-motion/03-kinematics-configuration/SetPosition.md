---
keyword: SetPosition
summary: Redefines the axis position to a given value without moving the motor.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 154
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# SetPosition

Redefines the axis position to a given value without moving the motor.

## Overview

`SetPosition` immediately sets the axis position reference and feedback registers to the specified value without commanding any motion. It is used to define a new coordinate origin or to recover from a position discrepancy. Because it rewrites the reference, it cannot be issued while the axis is in motion. To clear an accumulated position error instead of redefining the coordinate, see [ZeroPosErr](ZeroPosErr.md). It is an axis-related command function.

## Examples

```text
SetPosition=0       ; redefine current position as zero
SetPosition=50000   ; redefine current position as 50000
```

## See also

- [ZeroPosErr](ZeroPosErr.md) — zero the position error rather than redefine the coordinate
