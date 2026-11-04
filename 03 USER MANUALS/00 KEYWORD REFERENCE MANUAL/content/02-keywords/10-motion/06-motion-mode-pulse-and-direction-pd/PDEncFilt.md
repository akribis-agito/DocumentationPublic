---
keyword: PDEncFilt
summary: Reserved pulse-and-direction keyword; not implemented in current firmware.
availability:
- controller
- ci-master
can_code: 62
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# PDEncFilt

Reserved pulse-and-direction keyword; not implemented in current firmware.

## Overview

`PDEncFilt` is a reserved keyword. It is flagged as not implemented and has no read/write behaviour. It was intended as a noise filter for the P/D input, but that function was never implemented, so the keyword has no effect. The P/D input format itself is selected with [PDSubType](PDSubType.md).

> **Documentation pending:** This keyword is reserved and not implemented. Do not use it.

## See also

- [PDPos](PDPos.md) — the scaled P/D counter
- [PDEncDir](PDEncDir.md) — P/D accumulation direction
- [PDSubType](PDSubType.md) — selects the input signal format
