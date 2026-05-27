---
keyword: ModShort
summary: Selects the path of motion (normal, positive-only, negative-only, or shortest) for absolute PTP under modulo mode (not implemented in current firmware).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 149
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides:
  central-i.v5:
    access: rw
    units: none
    range:
    - 0
    - 3
    implemented: final
---
# ModShort

Selects the path of motion for absolute PTP under modulo mode.

## Overview

`ModShort` defines the path of motion taken in absolute point-to-point (PTP) motion when modulo mode is enabled (`ModRev ≠ 0`). It is used for general motion ([MotionMode](../../10-motion/02-motion-configuration/MotionMode.md) = 1 or 2) or during homing ([HomingDef](../../16-homing/HomingDef.md)[1, 11, …, 141] = 12). It complements [ModRev](ModRev.md), which enables modulo wrapping. Being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion.

> **Availability:** `ModShort` is implemented on **central-i v5 only** (range 0–3). On v4 (standalone and central-i) it is not implemented and has no effect — an absolute PTP move always goes to the literal target.

## How it works

`ModShort` is evaluated once when an absolute PTP target is commanded (no relative target). It rewrites the absolute target [AbsTrgt](../../10-motion/13-motion-mode-ptp/AbsTrgt.md) relative to the current reference before the move begins:

| Value | Description | Action |
|---|---|---|
| 0 | Axis moves to the target like a linear axis (taking additional revolution(s) if the absolute position delta is more than `ModRev`). | `AbsTrgt` unchanged — move to the literal target. |
| 1 | Negative direction only. If the target is higher than the current position, take the shortest negative-only path; otherwise move like a linear axis. | If `AbsTrgt` is above the current reference, subtract `ModRev` from `AbsTrgt`. |
| 2 | Positive direction only. If the target is lower than the current position, take the shortest positive-only path; otherwise move like a linear axis. | If `AbsTrgt` is below the current reference, add `ModRev` to `AbsTrgt`. |
| 3 | Shortest path. Does not take additional revolution(s) even if the absolute position delta is more than `ModRev`. | Compute `delta = (AbsTrgt − current reference + ModRev) mod ModRev`; if `delta ≤ ModRev/2` move `+delta`, else move `−(ModRev − delta)`. |

For value 3 the firmware folds the requested delta into one revolution and chooses the direction whose distance is at most half a revolution, so the axis never travels more than `ModRev/2` to reach the target.

## Examples

```text
AModShort=0          ; normal (linear-like) path
AModShort=3          ; shortest path
```

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Access | not implemented (no effect) | read/write, range 0–3 |

The path-selection logic exists only on the v5 firmware; it is absent on v4. **v5 is central-i only.**

## See also

- [ModRev](ModRev.md) — enables modulo mode that `ModShort` operates within
- [MotionMode](../../10-motion/02-motion-configuration/MotionMode.md) — motion mode in which `ModShort` applies
- [HomingDef](../../16-homing/HomingDef.md) — homing definition that can invoke `ModShort`
