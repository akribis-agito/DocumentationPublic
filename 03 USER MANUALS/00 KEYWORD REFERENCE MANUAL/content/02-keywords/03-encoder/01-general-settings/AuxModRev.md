---
keyword: AuxModRev
summary: Modulo revolution divisor for the auxiliary encoder (not implemented in current firmware).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 71
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: aux_user_units
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# AuxModRev

Modulo revolution divisor for the auxiliary encoder (not implemented in current firmware).

## Overview

`AuxModRev` is the modulo revolution divisor for the auxiliary encoder, the auxiliary-encoder counterpart of [ModRev](../04-modulo-mode/ModRev.md) for the main encoder. When set to a non-zero value it is intended to wrap the auxiliary encoder position to the range $[0, AuxModRev - 1]$. It is an axis-scope parameter saved to flash and cannot be changed while the motor is on or in motion.

> **Availability:** `AuxModRev` is flagged `not_implemented` in the current firmware. The parameter is defined and stored, but the control loop does not act on it — the per-cycle modulo wrap acts on the main encoder ([Pos](../../10-motion/01-kinematics-status/Pos.md)) only. Setting `AuxModRev` therefore has no effect on the auxiliary feedback ([AuxPos](../../10-motion/01-kinematics-status/AuxPos.md)). Modulo mode is currently supported on the main encoder only; contact Agito if auxiliary-encoder modulo is required.

## Examples

```text
AAuxModRev          ; query the configured auxiliary modulo divisor
```

## See also

- [ModRev](../04-modulo-mode/ModRev.md) — main-encoder modulo divisor (the implemented counterpart)
- [AuxPos](../../10-motion/01-kinematics-status/AuxPos.md) — auxiliary encoder feedback position
