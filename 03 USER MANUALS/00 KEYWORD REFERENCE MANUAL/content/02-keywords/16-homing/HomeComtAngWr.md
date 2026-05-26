---
keyword: HomeComtAngWr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 409
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomeComtAngWr

**Definition:**

HomeComtAngWr sets the commutation angle to be applied when the axis is initialised at its home position, bypassing a full homing sequence. Writing a previously captured angle (from HomeComtAngRd) allows the controller to resume commutation at the correct electrical angle without re-running homing. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[HomeComtAngOn](HomeComtAngOn.md), [HomeComtAngRd](HomeComtAngRd.md)
