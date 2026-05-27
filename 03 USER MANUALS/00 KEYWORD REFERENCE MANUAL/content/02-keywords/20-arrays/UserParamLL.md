---
summary: Proposed per-axis long-long (64-bit signed integer) variant of UserParam (availability unconfirmed).
---
# UserParamLL

Proposed per-axis long-long (64-bit signed integer) variant of UserParam (availability unconfirmed).

## Overview

`UserParamLL` is described as an axis-related long-long (64-bit signed integer) variant of [UserParam](UserParam.md), intended to provide the same kind of per-axis storage — accessible by both the user program and the host — for extended-precision integer values.

> **Documentation pending:** `UserParamLL` was not found in the firmware parameter table. Its availability and attributes (array size, scope, range, flash, indexing) are unconfirmed and must be verified before use. As with the other array keywords in this family, any array access is expected to be 1-indexed (the first usable element is `UserParamLL[1]`, index 0 is reserved). Because the user-parameter arrays are feature-related, some entries may be reserved internally — see [UserParam](UserParam.md).

## See also

- [UserParam](UserParam.md) — 32-bit integer per-axis array (confirmed)
- [UserParamD](UserParamD.md) — 64-bit double-precision integer variant
- [UserParamF](UserParamF.md) — floating-point variant
