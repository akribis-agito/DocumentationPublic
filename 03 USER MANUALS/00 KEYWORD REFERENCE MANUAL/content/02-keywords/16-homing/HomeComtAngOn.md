---
keyword: HomeComtAngOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 408
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomeComtAngOn

**Definition:**

HomeComtAngOn enables the automatic commutation angle capture feature during homing. When set to a non-zero value, the controller records the commutation angle at the home position into HomeComtAngWr, which can later be restored with HomeComtAngWr to avoid a homing sequence on subsequent power-ups. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[HomeComtAngWr](HomeComtAngWr.md), [HomeComtAngRd](HomeComtAngRd.md), [HomeStat](HomeStat.md)
