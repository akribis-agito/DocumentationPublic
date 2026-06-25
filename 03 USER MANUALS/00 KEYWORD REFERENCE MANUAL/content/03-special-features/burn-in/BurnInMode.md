---
keyword: BurnInMode
summary: Enables the burn-in motion function, which continuously rotates the open-loop commutation angle to stress-test the system over extended periods.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 424
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# BurnInMode

**Definition:**

BurnInMode enables the burn-in motion function, which continuously rotates the open-loop commutation angle to stress-test the system over extended periods. It defaults to 0 (disabled) and is not enabled by a single write: enabling it requires a defined unlock sequence of values, and any out-of-sequence value resets it back to 0 (disabled). It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter and is not saved to flash.

When enabled, the controller marks commutation as established and rotates the commutation angle open-loop at the rate set by [BurnInFreq](BurnInFreq.md), independent of any commanded motion. Disabling burn-in (writing or resetting to 0) marks commutation as no longer valid on a brushless axis, so commutation must be re-established before normal closed-loop motion.

Burn-in motion drives an open-loop commutation angle only on brushless motor types ([MotorType](../../02-keywords/02-motor-and-amplifier/MotorType.md) configured as brushless). For brush/DC, voice-coil, stepper, and simulation types the burn-in function drives no commutation angle.

**See also:**

[BurnInFreq](BurnInFreq.md)
