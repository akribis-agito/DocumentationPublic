---
keyword: BuffSplineMod
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 544
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
  - 1
  - 3
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffSplineMod

**Definition:**

BuffSplineMod selects the spline interpolation mode used when executing the buffer profile. Different values choose between cubic spline types or polynomial modes that affect the shape of the motion between waypoints. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[BuffPos](BuffPos.md), [BuffTime](BuffTime.md), [BuffCalc](BuffCalc.md)
