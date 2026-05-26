---
keyword: AOutPort
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 219
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
  - -11905
  - 11905
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutPort

AOutPort defines the output value to analog output in millivolts (mV). The array index corresponds to the index of the analog output. (i.e.: AOutPort\[2\] refers to analog output 2).

AOutPort\[Index\] only takes effect if AOutMode\[Index\] == 0.
