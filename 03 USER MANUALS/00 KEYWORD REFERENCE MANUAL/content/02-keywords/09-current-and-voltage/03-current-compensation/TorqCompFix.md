---
keyword: TorqCompFix
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 390
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -5000
  - 5000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# TorqCompFix

**Condition:**

TorqCompFix is only applicable when OperationMode = 2 or 3 (velocity or position operation mode) and TorqCompMode = 1 to 5.

**Definition:**

TorqCompFix is a user-defined array for the loop’s current compensation at a fixed value. The TorqCompFix entry in use depends on the TorqCompMode value.
