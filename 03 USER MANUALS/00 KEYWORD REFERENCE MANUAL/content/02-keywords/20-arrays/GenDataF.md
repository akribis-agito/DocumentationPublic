---
summary: General-purpose, non-axis 32-bit single-precision floating-point array for shared user/host storage.
keyword: GenDataF
availability:
  standalone: []
  central-i:
  - v5
can_code: 719
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 101
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# GenDataF

General-purpose, non-axis 32-bit single-precision floating-point array for shared user/host storage.

## Overview

`GenDataF` is the 32-bit single-precision floating-point member of the general-data array family. It is a general-purpose, non-axis array that provides the same kind of shared storage as [GenData](GenData.md) — accessible by both the user program and the host, not linked to any controller feature, and saved to flash — but holds real (single-precision floating-point) values rather than 32-bit integers. Use it for fractional values where single precision is sufficient; for greater precision use the double-precision [GenDataD](GenDataD.md).

It is readable and writable at any time, including while in motion and with the motor on. Values can be set directly with a normal write or through the controller's indirect-write mechanism. The array is 1-indexed: the first usable element is `GenDataF[1]` (index 0 is reserved and inaccessible), and there are 100 usable elements.

## Examples

```text
AGenDataF[1]=1.5    ; store a single-precision value
AGenDataF[1]        ; read the first element
```

## See also

- [GenData](GenData.md) — 32-bit integer general-purpose array
- [GenDataD](GenDataD.md) — 64-bit double-precision floating-point variant
- [GenDataLL](GenDataLL.md) — long-long (64-bit signed integer) variant
