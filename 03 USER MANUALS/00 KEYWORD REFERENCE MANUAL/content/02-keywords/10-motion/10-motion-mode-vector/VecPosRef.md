---
keyword: VecPosRef
summary: Read-only running position along the vector path (0 to VecAbsTrgt), always positive.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 643
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
overrides: {}
---
# VecPosRef

Read-only running position along the vector path (0 to VecAbsTrgt), always positive.

## Overview

`VecPosRef` is a status parameter that reports the current position reference of the vector motion profile, measured along the vector path. It starts from a value of 0 and, upon end of motion, reaches the value of [VecAbsTrgt](VecAbsTrgt.md). `VecPosRef` is always positive. Its time derivative is reported by [VecdPosRef](VecdPosRef.md).

## Examples

```text
VecPosRef?          ; read the current position along the vector path
```

## See also

- [VecAbsTrgt](VecAbsTrgt.md) — total path distance (end value of `VecPosRef`)
- [VecdPosRef](VecdPosRef.md) — derivative of `VecPosRef` (path speed)
