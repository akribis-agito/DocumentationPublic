---
keyword: AccelFact
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 168
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
  - 40
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccelFact

**Definition:**

AccelFact is a scaling factor applied to the Accel value, allowing the effective acceleration to be adjusted by a ratio without changing the base Accel parameter. The actual acceleration used for motion is Accel multiplied by AccelFact. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[Accel](Accel.md), [Decel](Decel.md), [Speed](Speed.md)
