---
keyword: VelErr
summary: Velocity error (reference minus feedback), used for control and protection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 19
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
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# VelErr

Velocity error (reference minus feedback), used for control and protection.

## Overview

`VelErr` reports the error between the velocity reference and the velocity feedback, in main user units per second. It is the velocity-loop counterpart of the position error [PosErr](PosErr.md) and is used for velocity feedback control and motion protection.

`VelErr` is only reported when the axis is enabled, in a position or velocity operation mode, not in open-loop, and axis phasing is done; otherwise it reports `0`.

## How it works

1. Under individual (non-gantry) mode:

$$
VelErr = VelRef - Vel\lbrack 1\rbrack
$$

2. Under gantry mode:

$$
VelErr = VelRef - GantryVel
$$

## Examples

```text
AVelErr             ; read the current velocity error
```

## See also

- [VelRef](VelRef.md) — velocity-loop reference (the minuend)
- [Vel](Vel.md) — feedback velocity array (`Vel[1]` is the subtrahend in non-gantry mode)
- [PosErr](PosErr.md) — position error counterpart
