---
keyword: MotorTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 400
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
  default: 25
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# MotorTemp

**Definition:**

MotorTemp reports the measured motor temperature from an attached temperature sensor. It is a read-only, axis-related status variable that is not saved to flash.

%%
Needs verification
MotorTemp is flagged NOT_IMPLEMENTED in the current firmware parameter table; confirm hardware support and sensor availability before use.
%%

**See also:**

[MaxMotorTemp](MaxMotorTemp.md), [MotorTempUsed](MotorTempUsed.md), [MotorTempOffset](MotorTempOffset.md)
