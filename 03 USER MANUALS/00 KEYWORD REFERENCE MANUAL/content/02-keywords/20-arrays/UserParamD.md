---
summary: Proposed per-axis 64-bit double-precision integer variant of UserParam (availability unconfirmed).
---
# UserParamD

Proposed per-axis 64-bit double-precision integer variant of UserParam (availability unconfirmed).

## Overview

`UserParamD` is described as an axis-related double-precision integer (64-bit) variant of [UserParam](UserParam.md), intended to provide the same kind of per-axis storage — accessible by both the user program and the host — for large integer values.

> **Documentation pending:** `UserParamD` was not found in the firmware parameter table. Its availability and attributes (array size, scope, range, flash, indexing) are unconfirmed and must be verified before use. As with the other array keywords in this family, any array access is expected to be 1-indexed (the first usable element is `UserParamD[1]`, index 0 is reserved). Because the user-parameter arrays are feature-related, some entries may be reserved internally — see [UserParam](UserParam.md).

## See also

- [UserParam](UserParam.md) — 32-bit integer per-axis array (confirmed)
- [UserParamF](UserParamF.md) — floating-point variant
- [UserParamLL](UserParamLL.md) — long-long (64-bit signed integer) variant
