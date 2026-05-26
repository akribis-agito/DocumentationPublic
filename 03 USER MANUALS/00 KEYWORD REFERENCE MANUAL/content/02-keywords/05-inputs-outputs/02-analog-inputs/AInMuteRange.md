---
keyword: AInMuteRange
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 377
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
# AInMuteRange

AInMuteRange defines the second analog deadband value in millivolts. The array index corresponds to the index of the analog input (i.e.: AInMuteRange\[2\] refers to analog input 2).

The following table shows the input-output relation for this deadband adjustment block.

| abs(Input)     | Output |
|----------------|--------|
| ≤AInMuteRange  | 0      |
| \>AInMuteRange | Input  |
