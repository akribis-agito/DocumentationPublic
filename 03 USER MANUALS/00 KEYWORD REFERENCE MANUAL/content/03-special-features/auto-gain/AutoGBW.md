---
keyword: AutoGBW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 358
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
  - 1
  - 2000
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
---
# AutoGBW

**Definition:**

AutoGBW sets the target closed-loop bandwidth in Hz for the automatic gain tuning algorithm. The tuner uses this value to compute the desired servo gains that achieve the specified bandwidth. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGMode](AutoGMode.md), [AutoGJm](AutoGJm.md), [AutoGKt](AutoGKt.md)
