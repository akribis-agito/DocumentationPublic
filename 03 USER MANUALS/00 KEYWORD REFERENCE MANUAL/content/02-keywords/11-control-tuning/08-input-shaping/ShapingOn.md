---
keyword: ShapingOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 151
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ShapingOn

**Definition:**

ShapingOn enables or disables the input shaping (command filtering) feature on the axis. When set to a non-zero value, the motion reference is convolved with an impulse sequence defined by ShapingFreq and ShapingDamp to suppress resonant vibration. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[ShapingFreq](ShapingFreq.md), [ShapingDamp](ShapingDamp.md)
