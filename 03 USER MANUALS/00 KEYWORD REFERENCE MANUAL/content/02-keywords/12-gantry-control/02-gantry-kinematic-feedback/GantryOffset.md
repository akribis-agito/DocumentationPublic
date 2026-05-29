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

The offset is captured at the `0 → 1` transition as the difference of the **shaped, filtered** position references on the two members (i.e. after smoothing / shaping / filtering, the value the position loop will actually track):

```text
AGantryOffset = APosRef - BPosRef
```

It is then folded into the gantry feedbacks every cycle while gantry is on:

```text
AGantryFdbk = (APos + BPos + AGantryOffset) / 2
BGantryFdbk = (APos - BPos - AGantryOffset)
```

Reading `GantryOffset` on any axis other than the master (`A`, or `C`/`E`/`G` on v5) has no use and always returns `0`.

## Examples

```text
AGantryOffset      ; read the captured A/B offset
```

### Edge cases

- **Gantry off** ([GantryOn](../01-general-variables/GantryOn.md) = 0) — the offset is held at its last captured value (or `0` if gantry has never engaged); it is not recomputed.
- **Captured per engagement** — every `0 → 1` transition re-snaps the offset. If the load drifts while gantry is off, the next engagement captures the new mechanical relationship and the yaw loop again starts from zero.
- **Read-only** — writes are rejected.
- **Wrong axis** — only the master-axis storage is meaningful; reads on other axes return `0`.
- **Pre-engagement value** — the offset captured at the `0 → 1` transition is taken from [PosRef](../../10-motion/01-kinematics-status/PosRef.md) (the shaped/filtered position reference), not from [Pos](../../10-motion/01-kinematics-status/Pos.md), so a stationary axis (where reference equals feedback) sees `Pos[A] - Pos[B]`; a moving axis with non-zero tracking error sees the shaped-reference difference instead.
- **Platform** — v5 widens the storage to 64-bit and supports multiple gantry pairs ([GantryOn](../01-general-variables/GantryOn.md) on A / C / E / G).

## See also

- [GantryFdbk](GantryFdbk.md) — gantry feedbacks that apply this offset
- [GantryOn](../01-general-variables/GantryOn.md) — captures the offset on the 0→1 transition
