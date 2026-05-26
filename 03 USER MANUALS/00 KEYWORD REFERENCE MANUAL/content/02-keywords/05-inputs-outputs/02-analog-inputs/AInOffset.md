---
keyword: AInOffset
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 216
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AInOffset

AInOffset defines the offset value (in millivolts) that is added to the analog input. The array index corresponds to the index of the analog input (i.e.: AInOffset\[3\] refers to analog input 3).

The input ($u$) and output ($y$) relation of the offset block is as follows.

$$
y = u + AInOffset
$$
