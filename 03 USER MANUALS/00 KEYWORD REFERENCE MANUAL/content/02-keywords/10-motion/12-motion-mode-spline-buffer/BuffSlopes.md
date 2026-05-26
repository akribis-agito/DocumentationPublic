---
keyword: BuffSlopes
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

**Definition:**

BuffSlopes is an array of up to three values that specify the velocity slopes (derivatives) imposed at the start and end of the spline buffer trajectory when BuffEdgeMode requires them. Setting these values controls the entry and exit velocity of the spline profile. It is an axis-related array saved to flash and can be changed at any time.

**See also:**

[BuffEdgeMode](BuffEdgeMode.md), [BuffPos](BuffPos.md), [BuffCalc](BuffCalc.md)
