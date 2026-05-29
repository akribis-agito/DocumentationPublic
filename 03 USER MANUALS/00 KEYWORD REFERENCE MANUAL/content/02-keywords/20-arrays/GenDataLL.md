---
summary: General-purpose, non-axis 64-bit signed integer array for shared user/host storage.
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
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GenDataLL

General-purpose, non-axis 64-bit signed integer array for shared user/host storage.

## Overview

`GenDataLL` is the 64-bit signed integer (long-long) member of the general-data array family. It is a general-purpose, non-axis array that provides the same kind of shared storage as [GenData](GenData.md) — accessible by both the user program and the host, not linked to any controller feature, and saved to flash — but holds 64-bit integers, for whole-number values that do not fit in the 32-bit range of [GenData](GenData.md).

It is readable and writable at any time, including while in motion and with the motor on. Values can be set directly with a normal write or through the controller's indirect-write mechanism. The array is 1-indexed: the first usable element is `GenDataLL[1]` (index 0 is reserved and inaccessible), and there are 100 usable elements. The value range spans the controller's 64-bit position word (-2251799813685248 to 2251799813685247).

## Examples

```text
AGenDataLL[1]=1000000000000   ; store a large 64-bit integer
AGenDataLL[1]                 ; read the first element
```

## See also

- [GenData](GenData.md) — 32-bit integer general-purpose array
- [GenDataD](GenDataD.md) — 64-bit double-precision floating-point variant
- [GenDataF](GenDataF.md) — 32-bit single-precision floating-point variant
