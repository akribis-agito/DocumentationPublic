---
summary: Proposed long-long (64-bit signed integer) variant of GenData (availability unconfirmed).
keyword: GenDataLL
availability:
  standalone: []
  central-i:
  - v5
can_code: 775
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 101
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# GenDataLL

Proposed long-long (64-bit signed integer) variant of GenData (availability unconfirmed).

## Overview

`GenDataLL` is described as a general-purpose long-long (64-bit signed integer) variant of [GenData](GenData.md), intended to provide the same kind of shared storage — accessible by both the user program and the host — for extended-precision integer values.

> **Documentation pending:** `GenDataLL` was not found in the firmware parameter table. Its availability and attributes (array size, scope, range, flash, indexing) are unconfirmed and must be verified before use. As with the other array keywords in this family, any array access is expected to be 1-indexed (the first usable element is `GenDataLL[1]`, index 0 is reserved).

## See also

- [GenData](GenData.md) — 32-bit integer general-purpose array (confirmed)
- [GenDataD](GenDataD.md) — 64-bit double-precision integer variant
- [GenDataF](GenDataF.md) — floating-point variant
