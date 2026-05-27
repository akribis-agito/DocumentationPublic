---
summary: Proposed long-long (64-bit signed integer) variant of GenData (availability unconfirmed).
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
