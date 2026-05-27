---
summary: Per-axis, feature-related 64-bit double-precision floating-point array for shared user/host storage.
keyword: UserParamD
availability:
  standalone: []
  central-i:
  - v5
can_code: 772
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# UserParamD

Per-axis, feature-related 64-bit double-precision floating-point array for shared user/host storage.

## Overview

`UserParamD` is the 64-bit double-precision floating-point member of the user-parameter array family. It is an axis-related array that provides the same kind of per-axis storage as [UserParam](UserParam.md) — accessible by both the user program and the host, and saved to flash — but holds real (double-precision floating-point) values rather than 32-bit integers.

Like the rest of the user-parameter family, these arrays are feature-related: some entries may be used internally by controller features (the controller guarantees an entry is not shared by more than one feature at a time), so for free scratch storage in the user program, custom functions or debugging, prefer the general-data arrays such as [GenDataD](GenDataD.md). It is readable and writable at any time, including while in motion and with the motor on. The array is 1-indexed: the first usable element is `UserParamD[1]` (index 0 is reserved and inaccessible); the number of usable elements is model-dependent (typically 20, fewer on smaller models).

## Examples

```text
AUserParamD[1]=2.5  ; store a double-precision value
AUserParamD[1]      ; read the first element
```

## See also

- [UserParam](UserParam.md) — 32-bit integer per-axis array
- [UserParamF](UserParamF.md) — 32-bit single-precision floating-point variant
- [UserParamLL](UserParamLL.md) — long-long (64-bit signed integer) variant
