---
keyword: MaxVBus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 92
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
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVBus

**Definition:**

MaxVBus is the maximum allowed bus voltage in mV. If actual bus voltage exceeds this limit for period longer than MaxVBusTime, axis is disabled, and an error code is thrown to ConFlt.
