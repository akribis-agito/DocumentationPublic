---
keyword: AInGain
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 217
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
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# AInGain

AInGain is the actual analog input gain multiplied by 65536. The multiplication is needed to allow representation of fractions by only using integers. The array index corresponds to the index of the analog input (i.e.: AInGain\[1\] refers to analog input 1).

The input ($u$) and output ($y$) relation of the gain block is as follows.

$$
y = \frac{AInGain}{65536}u
$$

To have unity gain, user should set AInGain=65536.
