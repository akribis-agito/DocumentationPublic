---
summary: Proposed 64-bit double-precision integer variant of GenData (availability unconfirmed).
keyword: GenDataD
availability:
  standalone: []
  central-i:
  - v5
can_code: 773
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 101
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# GenDataD

Proposed 64-bit double-precision integer variant of GenData (availability unconfirmed).

## Overview

`GenDataD` is described as a general-purpose double-precision integer (64-bit) variant of [GenData](GenData.md), intended to provide the same kind of shared storage — accessible by both the user program and the host — for large integer values.

> **Documentation pending:** `GenDataD` was not found in the firmware parameter table. Its availability and attributes (array size, scope, range, flash, indexing) are unconfirmed and must be verified before use. As with the other array keywords in this family, any array access is expected to be 1-indexed (the first usable element is `GenDataD[1]`, index 0 is reserved).

## See also

- [GenData](GenData.md) — 32-bit integer general-purpose array (confirmed)
- [GenDataF](GenDataF.md) — floating-point variant
- [GenDataLL](GenDataLL.md) — long-long (64-bit signed integer) variant
