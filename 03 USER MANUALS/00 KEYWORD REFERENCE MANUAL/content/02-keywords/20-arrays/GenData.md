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

`GenData` is a general-purpose integer array that provides shared storage accessible by both the user program and the host. It is not linked to any controller feature, so it is well suited for use as user-program variables, as temporary variables in custom firmware functions, and for debugging. It is non-axis (a single shared array for the controller), readable and writable at any time, and saved to flash.

`GenData` is the 32-bit integer member of the general-data family: [GenDataD](GenDataD.md), [GenDataF](GenDataF.md) and [GenDataLL](GenDataLL.md) provide the same shared storage for other data types. For per-axis general storage that is feature-related, see [UserParam](UserParam.md). Values can be set directly with a normal write, or indirectly through the controller's indirect-write mechanism.

The array is 1-indexed: the first usable element is `GenData[1]`. With `array_size` of 1001, the highest usable index is `GenData[1000]` (index 0 is reserved and inaccessible).

## Examples

```text
AGenData[1]=100      ; store 100 in the first element
AGenData[1]         ; read the first element
AGenData[1000]=0     ; highest usable index
```

## See also

- [GenDataD](GenDataD.md) — 64-bit double-precision integer variant
- [GenDataF](GenDataF.md) — floating-point variant
- [GenDataLL](GenDataLL.md) — long-long (64-bit signed integer) variant
- [UserParam](UserParam.md) — per-axis feature-related general storage
