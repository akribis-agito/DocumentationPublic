---
keyword: ShapingFreq
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 152
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 32768000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ShapingFreq

**Definition:**

ShapingFreq is an array that stores the resonant frequencies (in Hz) of the vibration modes to be suppressed by the input shaper. Each element corresponds to one notch in the shaping filter, paired with the damping ratio in ShapingDamp. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[ShapingOn](ShapingOn.md), [ShapingDamp](ShapingDamp.md)
