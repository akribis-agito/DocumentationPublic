---
keyword: HallsValue
summary: Read-only raw Hall-sensor state, reported as a 3-bit value (bits CBA).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 383
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 6
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HallsValue

Read-only raw Hall-sensor state, reported as a 3-bit value (bits CBA).

## Overview

`HallsValue` reports the current raw Hall-sensor state. The three Hall input signals from the motor are combined into a single integer, with the signals occupying bits C, B and A (bit 2 = C, bit 1 = B, bit 0 = A), to indicate the current electrical sector for commutation. The six valid (legal) combinations correspond to the values 1–6; this state is used together with [HallsAngle](HallsAngle.md) to derive the commutation angle in Hall-based commutation, and an illegal combination is flagged by [ComtStatus](ComtStatus.md). It is axis-scope, read-only, and not saved to flash, so it can be read at any time.

## Examples

```text
AHallsValue         ; query the current raw Hall state (1-6)
```

## See also

- [HallsAngle](HallsAngle.md) — electrical angle mapped to each Hall state
- [HallOnlyFilt](HallOnlyFilt.md) — filter for the Hall-based commutation angle
- [ComtMode](ComtMode.md) — selects the commutation method
- [ComtStatus](ComtStatus.md) — reports illegal Hall sequence errors
