---
keyword: VelKi
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 103
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 20000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# VelKi

**Definition:**

VelKi is the integral gain in velocity position loop, applied onto the output of VelGain before entering integral block. The integral saturation value is controlled internally.

This keyword is applicable for gain scheduling. By default (no gain scheduling), the gain value of the first array element (VelKi\[1\]) is used for control. See [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) for more information on which array elements are used, depending on gain scheduling method.
