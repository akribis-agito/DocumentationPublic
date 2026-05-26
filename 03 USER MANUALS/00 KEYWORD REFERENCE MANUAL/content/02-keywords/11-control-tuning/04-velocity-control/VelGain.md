---
keyword: VelGain
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 102
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
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VelGain

**Definition:**

VelGain is the proportional gain in veloicty loop, applied onto the VelErr.

This keyword is applicable for gain scheduling. By default (no gain scheduling), the gain value of the first array element (VelGain\[1\]) is used for control. See [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) for more information on which array elements are used, depending on gain scheduling method.
