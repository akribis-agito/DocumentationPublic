---
keyword: PDEncFilt
summary: Reserved pulse-and-direction keyword; not implemented in current firmware.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 62
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# PDEncFilt

Reserved pulse-and-direction keyword; not implemented in current firmware.

## Overview

`PDEncFilt` is a reserved keyword. It is marked as not implemented and is slated for removal from firmware.

> **Documentation pending:** This keyword is reserved and not implemented. Do not use it.

## See also

- [PDPos](PDPos.md) — the scaled P/D counter
- [PDEncDir](PDEncDir.md) — P/D accumulation direction
