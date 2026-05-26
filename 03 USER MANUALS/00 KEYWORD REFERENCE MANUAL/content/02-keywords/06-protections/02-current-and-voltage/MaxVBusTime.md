---
keyword: MaxVBusTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 93
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVBusTime

**Definition:**

MaxVBusTime defines the maximum out-of-range time of bus voltage under the MinVBus and MaxVBus limits.
