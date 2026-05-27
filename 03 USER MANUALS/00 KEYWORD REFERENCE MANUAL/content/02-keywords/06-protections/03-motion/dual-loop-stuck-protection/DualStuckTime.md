---
keyword: DualStuckTime
summary: Consecutive cycles the dual-loop feedback mismatch may persist before tripping.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 158
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2147483647
  default: 4096
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualStuckTime

Consecutive cycles the dual-loop feedback mismatch may persist before tripping.

## Overview

`DualStuckTime` is the maximum number of consecutive controller cycles (1 cycle ≈ 61 µs) for which the velocity difference between the two dual-loop feedbacks may exceed [DualStuckVel](DualStuckVel.md). If `DualStuckVel` is exceeded for `DualStuckTime` consecutive cycles, the axis is disabled and an error is reported.

## Examples

```text
ADualStuckTime=4096  ; cycles the feedback mismatch may persist before tripping
```

## See also

- [DualStuckVel](DualStuckVel.md) — the tolerated velocity-difference threshold
