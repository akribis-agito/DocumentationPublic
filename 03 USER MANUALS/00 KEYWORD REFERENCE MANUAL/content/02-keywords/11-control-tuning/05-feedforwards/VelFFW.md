---
keyword: VelFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 108
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
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 0
    - 1000000000
---
# VelFFW

**Definition:**

VelFFW is the velocity feedforward gain applied onto the first derivative of position reference (dPosRef). The velocity feedforward is scaled before the final summation.

This keyword is applicable for gain scheduling. By default (no gain scheduling), the gain value of the first array element (VelFFW\[1\]) is used for control. See [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) for more information on which array elements are used, depending on gain scheduling method.
