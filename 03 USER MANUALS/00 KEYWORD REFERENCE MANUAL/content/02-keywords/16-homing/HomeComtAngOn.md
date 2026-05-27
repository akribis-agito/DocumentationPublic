---
keyword: HomeComtAngOn
summary: Enables capture of the commutation angle at the home position during homing.
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

Enables capture of the commutation angle at the home position during homing.

## Overview

`HomeComtAngOn` enables the automatic commutation-angle capture feature during homing. When set to a non-zero value, the controller records the commutation angle at the home position into the read-only [HomeComtAngRd](HomeComtAngRd.md) array. A captured value can later be written to [HomeComtAngWr](HomeComtAngWr.md) so commutation is restored at the correct electrical angle on subsequent power-ups, avoiding a full homing sequence. It is an axis-scoped parameter, not saved to flash, and can be changed at any time.

## Examples

```text
AHomeComtAngOn=1     ; capture the commutation angle at home during homing
AHomeComtAngOn      ; 0 = disabled, 1 = enabled
```

## See also

- [HomeComtAngRd](HomeComtAngRd.md) — read-only array holding the captured angle(s)
- [HomeComtAngWr](HomeComtAngWr.md) — writes a stored angle back to restore commutation
- [HomeStat](HomeStat.md) — homing status bit-field
