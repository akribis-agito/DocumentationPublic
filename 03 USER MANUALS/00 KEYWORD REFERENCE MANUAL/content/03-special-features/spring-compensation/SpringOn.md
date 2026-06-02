---
keyword: SpringOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 592
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# SpringOn

**Definition:**

SpringOn enables the spring compensation feature, which injects a position-dependent feedforward current into the control loop to counteract elastic restoring forces acting on the load. It is an axis-related parameter and is not saved to flash; it can be changed at any time.

SpringOn accepts the values 0 to 2 and defaults to 0. The compensation is gated on a simple nonzero test, so any nonzero value (1 or 2) enables it identically; there is no difference in behavior between the two enabled values. Because the parameter is not saved to flash, it reverts to 0 (disabled) at power-up and must be set again to re-enable. It may be changed while the axis is in motion.

**See also:**

[SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md), [SpringTable](SpringTable.md), [SpringPosFFW](SpringPosFFW.md)
