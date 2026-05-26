---
keyword: StuckCurr
summary: Current threshold for motor-stuck detection.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 86
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
  - 64000
  default: 4000
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckCurr

Current threshold for motor-stuck detection.

## Overview

`StuckCurr` is the current threshold used for motor-stuck detection. The stuck condition triggers when the current exceeds `StuckCurr` while velocity stays below [StuckVel](StuckVel.md) for at least [StuckTime](StuckTime.md).

## Examples

```text
StuckCurr=4000      ; current above which a non-moving motor counts as stuck (mA)
```

## See also

- [StuckVel](StuckVel.md) — velocity threshold
- [StuckTime](StuckTime.md) — duration before declaring stuck
