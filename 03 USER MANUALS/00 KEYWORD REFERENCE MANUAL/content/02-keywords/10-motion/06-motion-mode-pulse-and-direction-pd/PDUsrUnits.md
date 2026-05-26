---
keyword: PDUsrUnits
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 66
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 2147483647
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDUsrUnits

**Definition:**

PDUsrUnits scales the internal PD variables (PDPos and PDVel) from internal unit of counts to user unit, when the user queries for these statuses via communication channel.

For example,

$$
Queried\ PDPos\ \lbrack user\ units\rbrack = \frac{1}{\frac{PDUsrUnits}{65536}\left\lbrack \frac{counts}{user\ units} \right\rbrack\ } \bullet \ Controller\ PDPos\ \lbrack counts\rbrack\ 
$$
