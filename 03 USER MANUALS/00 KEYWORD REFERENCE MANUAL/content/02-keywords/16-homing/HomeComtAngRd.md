---
keyword: HomeComtAngRd
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 410
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
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
# HomeComtAngRd

**Definition:**

HomeComtAngRd is a read-only array that holds the commutation angle values recorded at the home position during a homing sequence when HomeComtAngOn is active. These values can be saved and used to restore the commutation angle on subsequent power-ups via HomeComtAngWr. It is an axis-related, read-only array that is not saved to flash.

**See also:**

[HomeComtAngOn](HomeComtAngOn.md), [HomeComtAngWr](HomeComtAngWr.md)
