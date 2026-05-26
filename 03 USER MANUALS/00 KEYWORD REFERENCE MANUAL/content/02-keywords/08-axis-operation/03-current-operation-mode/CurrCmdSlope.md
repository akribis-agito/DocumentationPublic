---
keyword: CurrCmdSlope
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 568
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
# CurrCmdSlope

**Condition:**

This keyword is only applicable when CurrCmdSrc = 1 or 2.

**Definition:**

CurrCmdSlope defines the slope for transition from the starting CurrRef value to the existing CurrCmdVal array entry. It is in terms of milliampere per second. Only after the ramping, the timer CurrCmdCntr will begin from 0.

**Example:**

If

- CurrCmdIndex = 2

- CurrCmdCntr = CurrCmdHTime\[2\] (end of current entry)

- CurrRef = CurrCmdVal\[2\] = 340

- CurrCmdVal\[3\] = -500

- CurrCmdSlope\[3\] = 700,

the ramping from 340mA to -500mA will start and be completed in 1.2 seconds.
