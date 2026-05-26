---
keyword: LAmpVBus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 253
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LAmpVBus

**Condition:**

This keyword is only used when AmpType = 4 (reserved setting).

**Definition:**

LAmpVBus reports the bus voltage measurements of built-in linear amplifier, in millivolts.
