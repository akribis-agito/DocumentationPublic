---
keyword: ECAMGap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 304
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -8000000
  - 8000000
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMGap

**Definition:**

ECAMGap is used to define the linear interval of the master values. It is an array of size 10, where each element corresponds to a cam pattern.

Its absolute value equals to the linear spacing between successive master values, that correspond to successive GenData indices in the cam pattern look-up table. In a simple example where ECAMCycles = 1, ECAMGap = 2000, ECAMStart ≤ 400 and ECAMEnd ≥ 401, if GenData\[400\] corresponds to master position of 6554, GenData\[401\] willcorrespond to master position of 8554.

If ECAMGap is positive, the order of the cam pattern follows ascending order, where if master position increases, the corresponding GenData index will increase as well. If ECAMGap is negative, the order of the pattern will be inverted, that is if master position increases, the corresponding GenData index will decrease.

Please refer to the figures in [Motion mode – Electronic cam (ECAM)](../../../02-keywords/10-motion/08-motion-mode-electronic-cam-ecam/00-overview.md) for more information on the ordering logics.
