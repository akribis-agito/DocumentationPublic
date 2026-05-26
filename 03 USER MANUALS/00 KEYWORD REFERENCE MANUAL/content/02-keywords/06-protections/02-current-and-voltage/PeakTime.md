---
keyword: PeakTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 53
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
  - 3000
  default: 500
  scaling: 1.0
  implemented: final
overrides: {}
---
# PeakTime

**Definition:**

PeakTime defines the maximum time allowed at the peak current. It is used together with ContCL and PeakCL to define time constant in I2t protection. If motor’s trip time is rated at trip current that is different from the peak current, please refer to [Current and Power](#motion-1) protection section to calculate the equivalent peak current time according to trip curve formula.
