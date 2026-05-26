---
keyword: MinVBus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 89
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
  - 11000
  - 90000
  default: 11000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MinVBus

**Definition:**

MinVBus is the minimum allowed bus voltage in mV. If actual bus voltage is under this limit for period longer than MaxVBusTime, axis is disabled, and an error code is thrown to ConFlt.
