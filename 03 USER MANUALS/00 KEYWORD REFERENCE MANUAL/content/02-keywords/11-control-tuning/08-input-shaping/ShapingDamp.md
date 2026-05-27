---
keyword: ShapingDamp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 153
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
  - 1
  - 65535
  default: 32768
  scaling: 1.0
  implemented: final
overrides: {}
---
# ShapingDamp

**Definition:**

ShapingDamp is an array that stores the damping ratios for each resonance mode defined in ShapingFreq. Each element is the damping ratio (0 to 1) of the corresponding frequency, used by the input shaper to compute the impulse amplitudes. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[ShapingOn](ShapingOn.md), [ShapingFreq](ShapingFreq.md)
