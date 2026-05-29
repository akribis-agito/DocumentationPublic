---
summary: General-purpose, non-axis 64-bit double-precision floating-point array for shared user/host storage.
keyword: GenDataD
availability:
  standalone: []
  central-i:
  - v5
can_code: 773
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 101
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GenDataD

General-purpose, non-axis 64-bit double-precision floating-point array for shared user/host storage.

## Overview

`GenDataD` is the 64-bit double-precision floating-point member of the general-data array family. It is a general-purpose, non-axis array that provides the same kind of shared storage as [GenData](GenData.md) — accessible by both the user program and the host, not linked to any controller feature, and saved to flash — but holds real (double-precision floating-point) values rather than 32-bit integers. Use it where the user program or host needs to store fractional values or magnitudes beyond the range or precision of an integer.

It is readable and writable at any time, including while in motion and with the motor on. Values are set with a normal write. The host-side indirect-write mechanism (`IndirectArray` / `IndirectIndex` / `IndirectValue` with `IndirectDo`) cannot target this array; it writes only the 32-bit integer [GenData](GenData.md). Within a user program, an element can still be addressed with a computed (run-time) index — see [Addressing](GenData.md#addressing). The array is 1-indexed: the first usable element is `GenDataD[1]` (index 0 is reserved and inaccessible), and there are 100 usable elements.

## Examples

```text
AGenDataD[1]=3.14159265358979   ; store a double-precision value
AGenDataD[1]                    ; read the first element
```

## See also

- [GenData](GenData.md) — 32-bit integer general-purpose array
- [GenDataF](GenDataF.md) — 32-bit single-precision floating-point variant
- [GenDataLL](GenDataLL.md) — long-long (64-bit signed integer) variant
