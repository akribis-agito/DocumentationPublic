---
summary: Proposed per-axis floating-point variant of UserParam (availability unconfirmed).
keyword: UserParamF
availability:
  standalone: []
  central-i:
  - v5
can_code: 718
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# UserParamF

Proposed per-axis floating-point variant of UserParam (availability unconfirmed).

## Overview

`UserParamF` is described as an axis-related floating-point variant of [UserParam](UserParam.md), intended to provide the same kind of per-axis storage — accessible by both the user program and the host — for real-valued data.

> **Documentation pending:** `UserParamF` was not found in the firmware parameter table. Its availability and attributes (array size, scope, range, flash, indexing) are unconfirmed and must be verified before use. As with the other array keywords in this family, any array access is expected to be 1-indexed (the first usable element is `UserParamF[1]`, index 0 is reserved). Because the user-parameter arrays are feature-related, some entries may be reserved internally — see [UserParam](UserParam.md).

## See also

- [UserParam](UserParam.md) — 32-bit integer per-axis array (confirmed)
- [UserParamD](UserParamD.md) — 64-bit double-precision integer variant
- [UserParamLL](UserParamLL.md) — long-long (64-bit signed integer) variant
