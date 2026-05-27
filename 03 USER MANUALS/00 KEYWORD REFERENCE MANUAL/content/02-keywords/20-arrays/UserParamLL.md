---
summary: Proposed per-axis long-long (64-bit signed integer) variant of UserParam (availability unconfirmed).
keyword: UserParamLL
availability:
  standalone: []
  central-i:
  - v5
can_code: 774
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
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
# UserParamLL

Proposed per-axis long-long (64-bit signed integer) variant of UserParam (availability unconfirmed).

## Overview

`UserParamLL` is the 64-bit signed integer (long-long) member of the user-parameter array family. It is an axis-related array that provides the same kind of per-axis storage as [UserParam](UserParam.md) — accessible by both the user program and the host, and saved to flash — but holds 64-bit integers, for whole-number values that do not fit in the 32-bit range of [UserParam](UserParam.md).

Like the rest of the user-parameter family, these arrays are feature-related: some entries may be used internally by controller features (the controller guarantees an entry is not shared by more than one feature at a time), so for free scratch storage in the user program, custom functions or debugging, prefer the general-data arrays such as [GenDataLL](GenDataLL.md). It is readable and writable at any time, including while in motion and with the motor on. The array is 1-indexed: the first usable element is `UserParamLL[1]` (index 0 is reserved and inaccessible); the number of usable elements is model-dependent (typically 20, fewer on smaller models). The value range spans the controller's 64-bit position word (-2251799813685248 to 2251799813685247).

## Examples

```text
AUserParamLL[1]=5000000000   ; store a large 64-bit integer
AUserParamLL[1]              ; read the first element
```

## See also

- [UserParam](UserParam.md) — 32-bit integer per-axis array (confirmed)
- [UserParamD](UserParamD.md) — 64-bit double-precision integer variant
- [UserParamF](UserParamF.md) — floating-point variant
