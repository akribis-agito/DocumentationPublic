---
keyword: ContCL
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 51
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
  - 10
  - 32000
  default: 32000
  scaling: 1.0
  implemented: final
overrides: {}
---
# ContCL

**Definition:**

ContCL refers to the continuous current limit of the amplifier. It is used to define amplifier behaviour in I2t power limitation scheme.

**Note:**

If ContCL is defined equal to or higher than peak current limit (PeakCL), controller will internally use the continuous current limit of PeakCL/2 instead. ContCL value will not be automatically updated.
