---
keyword: StuckVel
summary: Velocity threshold for motor-stuck detection.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 87
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
  default: 40000
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckVel

Velocity threshold for motor-stuck detection.

## Overview

`StuckVel` is the velocity threshold for motor-stuck detection. The axis is considered **stuck** when its velocity stays below `StuckVel` while the current exceeds [StuckCurr](StuckCurr.md) for at least [StuckTime](StuckTime.md) — i.e. the drive is pushing hard but the motor is not moving.

## Examples

```text
StuckVel=40000      ; stuck if velocity stays below this (user units)
```

## See also

- [StuckCurr](StuckCurr.md) — current threshold for stuck detection
- [StuckTime](StuckTime.md) — duration before declaring stuck
