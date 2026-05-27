---
keyword: BuffEdgeMode
summary: Selects the boundary condition at the start and end of the spline buffer trajectory.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 545
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
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffEdgeMode

Selects the boundary condition at the start and end of the spline buffer trajectory.

## Overview

`BuffEdgeMode` selects the boundary-condition behaviour at the start and end of the spline buffer trajectory. It determines how the spline is constrained at the trajectory edges — for example enforcing zero velocity, using a specified slope from [BuffSlopes](BuffSlopes.md), or a free-end condition. The range is 0 to 2 with a default of 1. It is saved to flash and can be changed at any time.

> **Documentation pending:** The exact boundary condition selected by each value (0–2) was not available in the source reference. Verify the mode codes against current firmware before relying on specific values.

## Examples

```text
BuffEdgeMode=1      ; default edge condition
```

## See also

- [BuffSlopes](BuffSlopes.md) — edge slopes used when required by this mode
- [BuffPos](BuffPos.md) — waypoint positions
- [BuffCalc](BuffCalc.md) — pre-compute the spline coefficients
