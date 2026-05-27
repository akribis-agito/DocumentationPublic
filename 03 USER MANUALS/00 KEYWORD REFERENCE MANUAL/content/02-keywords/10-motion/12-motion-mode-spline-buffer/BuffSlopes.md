---
keyword: BuffSlopes
summary: Edge velocity slopes imposed on the spline buffer trajectory when required.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 546
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# BuffSlopes

Edge velocity slopes imposed on the spline buffer trajectory when required.

## Overview

`BuffSlopes` is an array of up to three values that specify the velocity slopes (derivatives) imposed at the start and end of the spline buffer trajectory when [BuffEdgeMode](BuffEdgeMode.md) calls for specified-slope edges. Setting these values controls the entry and exit velocity of the spline profile. It is saved to flash and can be changed at any time.

## Examples

```text
ABuffSlopes[1]=0     ; start-edge slope
ABuffSlopes[2]=0     ; end-edge slope
```

## See also

- [BuffEdgeMode](BuffEdgeMode.md) — selects when these slopes are applied
- [BuffPos](BuffPos.md) — waypoint positions
- [BuffCalc](BuffCalc.md) — pre-compute the spline coefficients
