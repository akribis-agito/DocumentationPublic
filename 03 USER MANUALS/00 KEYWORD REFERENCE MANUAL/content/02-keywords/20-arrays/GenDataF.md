---
summary: Proposed floating-point variant of GenData (availability unconfirmed).
---
# GenDataF

Proposed floating-point variant of GenData (availability unconfirmed).

## Overview

`GenDataF` is described as a general-purpose floating-point variant of [GenData](GenData.md), intended to provide the same kind of shared storage — accessible by both the user program and the host — for real-valued data.

> **Documentation pending:** `GenDataF` was not found in the firmware parameter table. Its availability and attributes (array size, scope, range, flash, indexing) are unconfirmed and must be verified before use. As with the other array keywords in this family, any array access is expected to be 1-indexed (the first usable element is `GenDataF[1]`, index 0 is reserved).

## See also

- [GenData](GenData.md) — 32-bit integer general-purpose array (confirmed)
- [GenDataD](GenDataD.md) — 64-bit double-precision integer variant
- [GenDataLL](GenDataLL.md) — long-long (64-bit signed integer) variant
