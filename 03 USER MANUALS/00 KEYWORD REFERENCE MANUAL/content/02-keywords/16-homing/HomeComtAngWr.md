---
keyword: HomeComtAngWr
summary: Sets the commutation angle applied at the home position to skip a homing sequence.
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

Sets the commutation angle applied at the home position to skip a homing sequence.

## Overview

`HomeComtAngWr` sets the commutation angle (electrical angle, 0–35999) to apply when the axis is initialised at its home position, bypassing a full homing sequence. Writing a previously captured angle — read from [HomeComtAngRd](HomeComtAngRd.md) after a capture enabled by [HomeComtAngOn](HomeComtAngOn.md) — lets the controller resume commutation at the correct electrical angle without re-running homing. It is an axis-scoped parameter saved to flash, so the value persists across power cycles, and it cannot be changed while the axis is in motion.

## Examples

```text
AHomeComtAngWr=12000 ; apply this commutation angle at the home position
AHomeComtAngWr      ; read the configured commutation angle
```

## See also

- [HomeComtAngRd](HomeComtAngRd.md) — source of the captured angle to write here
- [HomeComtAngOn](HomeComtAngOn.md) — enables capturing the angle during homing
