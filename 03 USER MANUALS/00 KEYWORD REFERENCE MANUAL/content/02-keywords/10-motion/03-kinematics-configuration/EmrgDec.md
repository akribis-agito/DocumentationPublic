---
keyword: EmrgDec
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 140
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# EmrgDec

**Definition:**

EmrgDec sets the emergency deceleration rate applied when a Stop or fault condition is triggered during motion. It is typically set higher than the normal Decel value so the axis stops as quickly as possible. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[Decel](Decel.md), [Accel](Accel.md), [Abort](../04-motion-command/Abort.md)
