---
keyword: ForceCmdSlope
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 569
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdSlope

**Condition:**

This keyword is only applicable when ForceCmdSrc = 1 or 2.

**Definition:**

ForceCmdSlope defines the slope for transition from the starting ForceRef value to the existing ForceCmdVal array entry. It is in terms of unit per second. Only after the ramping, the timer ForceCmdCntr will begin from 0.
