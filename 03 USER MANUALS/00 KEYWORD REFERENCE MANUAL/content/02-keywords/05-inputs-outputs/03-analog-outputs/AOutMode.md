---
keyword: AOutMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 220
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutMode

**Definition:**

AOutMode defines if the analog outputs are in direct command mode or monitoring mode. The array index corresponds to the index of the analog output. (i.e.: AOutMode\[2\] refers to analog output 2).

The table below shows the value associated to AOutMode.

| Value | Descriptions |
|---|---|
| 0 | Direct command mode |
| CCC | Monitoring mode CCC is the Complex CAN code of the parameter/keyword to be emulated. |
