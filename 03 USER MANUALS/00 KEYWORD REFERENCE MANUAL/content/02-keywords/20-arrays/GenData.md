---
keyword: GenData
summary: General-purpose, non-axis 32-bit integer array for shared user/host storage.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 237
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 1001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GenData

General-purpose, non-axis 32-bit integer array for shared user/host storage.

## Overview

`GenData` is a general-purpose 32-bit signed integer array that provides shared storage accessible by both the user program and the host. It is not linked to any controller feature, so it is well suited for use as user-program variables, as temporary variables in custom functions, and for debugging. It is non-axis (a single array shared across the controller), readable and writable at any time, and saved to flash so its contents survive a power cycle once the parameters are stored.

`GenData` is the 32-bit integer member of the general-data family: [GenDataF](GenDataF.md) (32-bit floating-point), [GenDataD](GenDataD.md) (64-bit double-precision floating-point) and [GenDataLL](GenDataLL.md) (64-bit signed integer) provide the same kind of shared storage for the other data types. For per-axis storage that the controller also uses internally for certain features, see [UserParam](UserParam.md). Values can be set directly with a normal write, or indirectly through the controller's indirect-write mechanism.

![General-purpose array families: the GenData row holds the four non-axis variants (GenData int32, GenDataF float32, GenDataD float64, GenDataLL int64) recommended for user programs, and the UserParam row holds the four per-axis variants (UserParam, UserParamF, UserParamD, UserParamLL) some of whose entries are reserved internally](array-family-types.svg)

Each element holds a 32-bit signed integer, so the value range is -2147483648 to 2147483647 and the default is 0. The array is 1-indexed: the first usable element is `GenData[1]` (index 0 is reserved and inaccessible). The number of usable elements depends on the controller model: typically 1000, with 5000 on larger controllers and up to 10000 on models with double-flash storage.

## Examples

```text
AGenData[1]=100      ; store 100 in the first element
AGenData[1]         ; read the first element
AGenData[1000]=0     ; highest usable index on a 1000-element model
```

## See also

- [GenDataD](GenDataD.md) — 64-bit double-precision floating-point variant
- [GenDataF](GenDataF.md) — 32-bit single-precision floating-point variant
- [GenDataLL](GenDataLL.md) — long-long (64-bit signed integer) variant
- [UserParam](UserParam.md) — per-axis feature-related general storage
