---
summary: Proposed 64-bit double-precision integer variant of GenData (availability unconfirmed).
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
