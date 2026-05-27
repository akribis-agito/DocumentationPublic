---
keyword: ECAMInterp
summary: Reserved internal ECAM keyword (not implemented).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 308
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# ECAMInterp

Reserved internal ECAM keyword (not implemented).

## Overview

`ECAMInterp` is a reserved internal keyword in the ECAM motion group. Its valid range is fixed at `[0, 0]`.

> **Documentation pending:** `ECAMInterp` is currently reserved and not implemented (`implemented: not_implemented`). No user-facing behaviour is defined.

## See also

- [Motion mode – Electronic cam (ECAM)](00-overview.md) — ECAM motion overview
