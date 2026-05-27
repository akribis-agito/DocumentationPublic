---
keyword: PosErr
summary: Position error (reference minus feedback), used for control and protection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 18
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosErr

Position error (reference minus feedback), used for control and protection.

## Overview

`PosErr` reports the error between the position reference and the position feedback, in main user units. It is the primary position-loop control and protection signal, and the settling check that drives [InTargetStat](../05-motion-status/InTargetStat.md) compares `abs(PosErr)` against [InTargetTol](../05-motion-status/InTargetTol.md).

`PosErr` is only reported when the axis is enabled, in a position operation mode, not in open-loop, and axis phasing is done; otherwise it reports `0`. It is used for position feedback control, motion protection, homing and operation-mode switching.

## How it works

1. Under individual (non-gantry) mode:

$$
PosErr = PosRef - Pos
$$

2. Under gantry mode:

$$
PosErr = PosRef - GantryFdbk
$$

## Examples

```text
APosErr             ; read the current position error
```

## See also

- [PosRef](PosRef.md) — position reference (the minuend)
- [Pos](Pos.md) — position feedback (the subtrahend in non-gantry mode)
- [InTargetTol](../05-motion-status/InTargetTol.md) — settling window compared against `PosErr`
