---
keyword: BuffEdgeMode
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

**Definition:**

BuffEdgeMode selects the boundary condition behaviour at the start and end of the spline buffer trajectory. It determines whether the spline enforces zero velocity, specified slope (via BuffSlopes), or free-end conditions at the trajectory edges. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[BuffSlopes](BuffSlopes.md), [BuffPos](BuffPos.md), [BuffCalc](BuffCalc.md)
