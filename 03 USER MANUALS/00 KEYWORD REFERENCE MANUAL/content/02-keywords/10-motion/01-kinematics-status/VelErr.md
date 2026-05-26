---
keyword: VelErr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 19
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
overrides: {}
---
# VelErr

**Definition:**

VelErr reports the error between velocity reference and feedback, only if the axis is enabled, in position/velocity operation mode, not in open-loop condition and the axis phasing is done. The unit is in terms of main user unit per second.

1.  Under individual (non-gantry) mode

$$
VelErr = VelRef - Vel\lbrack 1\rbrack
$$

2.  Under gantry mode

$$
VelErr = VelRef - GantryVel
$$

Otherwise, VelErr reports 0.

VelErr is generally used for velocity feedback control and motion protection.
