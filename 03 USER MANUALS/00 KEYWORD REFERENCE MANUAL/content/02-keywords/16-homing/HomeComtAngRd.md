---
keyword: HomeComtAngRd
summary: Read-only array of commutation angles captured at the home position.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Read-only array of commutation angles captured at the home position.

## Overview

`HomeComtAngRd` is a read-only array (3 elements) holding the commutation-angle values recorded at the home position during a homing sequence while [HomeComtAngOn](HomeComtAngOn.md) is active. Each value is an electrical angle in the range 0–35999. A recorded value can be noted and later written to [HomeComtAngWr](HomeComtAngWr.md) to restore the commutation angle on subsequent power-ups, avoiding a repeat homing sequence. It is an axis-scoped, read-only array that is not saved to flash.

## Examples

```text
AHomeComtAngRd[1]   ; read the first captured commutation angle
AHomeComtAngRd      ; read the full captured-angle array
```

## See also

- [HomeComtAngOn](HomeComtAngOn.md) — enables capture into this array
- [HomeComtAngWr](HomeComtAngWr.md) — writes a stored angle back to restore commutation
