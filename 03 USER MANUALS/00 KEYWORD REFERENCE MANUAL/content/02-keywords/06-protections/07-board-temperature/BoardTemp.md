---
keyword: BoardTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 397
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -40
  - 150
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BoardTemp

**Definition:**

BoardTemp reports the current temperature of the controller board as measured by the on-board temperature sensor. It is a read-only, non-axis status variable that is not saved to flash and is available at all times.

**See also:**

[PwrTemp](PwrTemp.md), [MaxPwrTemp](MaxPwrTemp.md)
