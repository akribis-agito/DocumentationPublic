---
keyword: MapErrOffset
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 411
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapErrOffset

**Definition:**

MapErrOffset holds a temporary position-error offset that is added to the map correction during an active offset ramping operation. It reflects the current correction offset being applied and is cleared when the ramp completes. It is an axis-related parameter, not saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapErrOffRamp](MapErrOffRamp.md), [MapErrOnStep](MapErrOnStep.md), [MapType](MapType.md)
