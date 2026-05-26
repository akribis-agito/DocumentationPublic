---
keyword: PDEncDir
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 63
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# PDEncDir

**Definition:**

PDEncDir configures the direction of PDPos accumulation.

| Value | Descriptions |
|---|---|
| 0 | **Normal direction** PDPos increments by the number of pulses received multiplied by scaling if the direction signal is logic high, and decrements by such value if the direction signal is logic low. |
| 1 | **Inverted direction** PDPos decrements by the number of pulses received multiplied by scaling if the direction signal is logic high, and increments by such value if the direction signal is logic low. |
