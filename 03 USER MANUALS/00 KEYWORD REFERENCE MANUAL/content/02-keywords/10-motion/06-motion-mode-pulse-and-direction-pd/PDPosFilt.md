---
keyword: PDPosFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 150
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
  - 4150
  - 2147483647
  default: 12800
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDPosFilt

**Condition:**

PDPosFilt is only used in the direct PD motion ([MotionMode](../../../02-keywords/10-motion/02-motion-configuration/MotionMode.md) = 3).

**Definition:**

PDPosFilt is the first order low-pass filter cut-off frequency, in terms of Hz/100, applied onto the change of PDPos since the start of motion. It is used to smoothen the generated position reference (instead of step change).

For example, if the required cut-off frequency is 250Hz, PDPosFilt should be 25000. By default, the cut-off frequency is 128Hz.
