---
keyword: AuxPos
summary: Auxiliary-encoder position feedback, in auxiliary user units.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 3
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AuxPos

Auxiliary-encoder position feedback, in auxiliary user units.

## Overview

`AuxPos` reports the auxiliary encoder feedback, expressed in auxiliary user units (configurable via `AuxUsrUnits`). It is the auxiliary-loop counterpart of the main position feedback [Pos](Pos.md) and feeds dual-loop control and pseudo dual-loop scaling. The auxiliary velocity [AuxVel](AuxVel.md) is derived from `AuxPos`.

Although `AuxPos` is writable, it can only be set to a desired value while the axis is disabled. Its value resets to `0` on power up.

## Examples

```text
AuxPos?             ; read the auxiliary encoder position
AuxPos=0            ; preset to zero (axis must be disabled)
```

## See also

- [AuxVel](AuxVel.md) — auxiliary velocity, derived from `AuxPos`
- [Pos](Pos.md) — main encoder position feedback
