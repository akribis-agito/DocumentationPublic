---
keyword: VecPosFDef
summary: Array defining the position-filter coefficients applied to the vector reference output.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 647
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: false
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
# VecPosFDef

Array defining the position-filter coefficients applied to the vector reference output.

## Overview

`VecPosFDef` is a 6-element array that defines the position-filter configuration applied to the vector motion reference output. It specifies the filter coefficients (or parameters) used to smooth the vector position reference before it is fed to the individual axis servo loops, reducing jerk transmitted to the mechanics. The filter only takes effect when it is enabled by [VecPosFOn](VecPosFOn.md). It is an axis-related array saved to flash, and cannot be changed while the axis is in motion.

## Examples

```text
VecPosFDef[1]=0     ; first filter coefficient (1-indexed array element)
VecPosFDef[1]?      ; read the first filter coefficient
```

## See also

- [VecPosFOn](VecPosFOn.md) — enables/disables this position filter
- [VecSpeed](VecSpeed.md) — commanded resultant speed
