---
keyword: VecdPosRef
summary: Read-only derivative of the vector position reference (vector velocity), always positive.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 644
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
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# VecdPosRef

Read-only derivative of the vector position reference (vector velocity), always positive.

## Overview

`VecdPosRef` is a status parameter that reports the derivative of the vector motion position reference, i.e. the time derivative of [VecPosRef](VecPosRef.md). It represents the instantaneous speed along the vector path and follows the profile shaped by [VecAccel](VecAccel.md), [VecDecel](VecDecel.md) and [VecSpeed](VecSpeed.md). `VecdPosRef` is always positive.

## Examples

```text
AVecdPosRef         ; read the current speed along the vector path
```

## See also

- [VecPosRef](VecPosRef.md) — the position reference whose derivative this reports
- [VecSpeed](VecSpeed.md) — commanded maximum resultant speed
