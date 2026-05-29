---
keyword: EncAbsErrTime
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 423
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
  - -1
  - 10000
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    implemented: partial
---
# EncAbsErrTime

<!-- body pending -->
