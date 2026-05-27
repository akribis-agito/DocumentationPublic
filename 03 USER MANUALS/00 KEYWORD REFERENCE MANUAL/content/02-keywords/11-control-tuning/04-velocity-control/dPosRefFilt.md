---
keyword: dPosRefFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 106
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
  - 20000
  - 1000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# dPosRefFilt

**Definition:**

dPosRefFilt is the cutoff frequency of first-order low-pass filter applied to the derivative of position reference. The unit is in Hz/100. For example, if the cut-off frequency is 4500Hz, then dPosRefFilt = 450000.

**Note:**

The low-pass filter will be ignored if cut-off frequency is more than 8192Hz.
