---
keyword: BuffCalc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 547
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffCalc

**Definition:**

BuffCalc is a command that pre-computes the spline coefficients from the waypoint data in BuffPos and BuffTime before motion begins. It must be called after loading the waypoint arrays and before issuing a Begin command in spline buffer mode. It is an axis-related command function that cannot be issued while the axis is in motion.

**See also:**

[BuffPos](BuffPos.md), [BuffTime](BuffTime.md), [BuffSplineMod](BuffSplineMod.md), [BuffStatus](BuffStatus.md)
