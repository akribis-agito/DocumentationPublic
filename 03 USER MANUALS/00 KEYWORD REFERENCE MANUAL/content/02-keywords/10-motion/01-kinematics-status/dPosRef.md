---
keyword: dPosRef
summary: Velocity reference, the filtered derivative of the position reference PosRef.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 155
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
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
# dPosRef

Velocity reference, the filtered derivative of the position reference PosRef.

## Overview

`dPosRef` is the velocity reference, computed as the filtered derivative of the position reference [PosRef](PosRef.md). The filter is a first-order low-pass filter defined by `dPosRefFilt`.

`dPosRef` is the *velocity reference* and must not be confused with [VelRef](VelRef.md), the *velocity-loop reference/input*. `VelRef` is the sum of the position-controller output and the scaled velocity reference, whereas `dPosRef` is purely the derivative of `PosRef`.

## Examples

```text
AdPosRef            ; read the current velocity reference
```

## See also

- [PosRef](PosRef.md) — position reference, the source of this derivative
- [VelRef](VelRef.md) — velocity-loop reference/input (a different signal)
