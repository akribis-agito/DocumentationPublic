---
keyword: VecPosFOn
summary: Enables (1) the position filter defined by VecPosFDef on the vector reference output.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 648
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecPosFOn

Enables (1) the position filter defined by VecPosFDef on the vector reference output.

## Overview

`VecPosFOn` enables the position filter on the vector motion reference output. When set to a non-zero value, the filter defined by [VecPosFDef](VecPosFDef.md) is applied to smooth the vector position reference before it reaches the individual axis servo loops; when `0`, the reference passes through unfiltered. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

## Examples

```text
AVecPosFOn=0         ; position filter disabled (default)
AVecPosFOn=1         ; apply the VecPosFDef position filter
```

## See also

- [VecPosFDef](VecPosFDef.md) — filter coefficients applied when enabled
- [VecSpeed](VecSpeed.md) — commanded resultant speed
