---
keyword: GantryOffset
summary: Read-only initial A/B position offset captured when gantry mode is switched on.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 653
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
# GantryOffset

Read-only initial A/B position offset captured when gantry mode is switched on.

## Overview

`GantryOffset` is a read-only parameter. `AGantryOffset` is calculated once when `AGantryOn` is switched by the user from `0` to `1`. It captures the initial difference between the two ends' position references so that this standing offset is removed from the differential ([GantryFdbk](GantryFdbk.md)) calculation. Without it, the difference between the two motors at the moment gantry mode engages would appear as a large yaw error and the controller would try to force the beam square with a step; folding the captured offset in lets the yaw feedback start from a clean zero (see the common/differential explanation under [GantryOn](../01-general-variables/GantryOn.md)). It is held unchanged for as long as gantry mode stays on and is recomputed on the next `0`→`1` transition. Reported in user units; on central-i v5 it is a 64-bit value.

## How it works

The offset is captured as:

```text
AGantryOffset = APosRef - BPosRef
```

It is then folded into the gantry feedbacks:

```text
AGantryFdbk = (APos + BPos + AGantryOffset) / 2
BGantryFdbk = (APos - BPos - AGantryOffset)
```

Reading `GantryOffset` on any axis other than the master `A` has no use and always returns `0`.

## Examples

```text
AGantryOffset      ; read the captured A/B offset
```

## See also

- [GantryFdbk](GantryFdbk.md) — gantry feedbacks that apply this offset
- [GantryOn](../01-general-variables/GantryOn.md) — captures the offset on the 0→1 transition
