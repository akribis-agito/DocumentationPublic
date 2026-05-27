---
keyword: ModShort
summary: Selects the path of motion (normal, positive-only, negative-only, or shortest) for absolute PTP under modulo mode (not implemented in current firmware).
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# ModShort

Selects the path of motion for absolute PTP under modulo mode.

## Overview

`ModShort` defines the path of motion taken in absolute point-to-point (PTP) motion when modulo mode is enabled (`ModRev ≠ 0`). It is used for general motion ([MotionMode](../../10-motion/02-motion-configuration/MotionMode.md) = 1 or 2) or during homing ([HomingDef](../../16-homing/HomingDef.md)[1, 11, …, 141] = 12). It complements [ModRev](ModRev.md), which enables modulo wrapping. Being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion.

> **Documentation pending:** `ModShort` is flagged `not_implemented` in the current firmware. Confirm availability before use.

## How it works

| Value | Description |
|---|---|
| 0 | Axis moves to the target like a linear axis (taking additional revolution(s) if the absolute position delta is more than `ModRev`). |
| 1 | Axis moves to the target in the negative direction only. If the target is higher than the current position, the axis takes the shortest negative-only path to the target. Otherwise it moves like a linear axis (additional revolution(s) if the delta exceeds `ModRev`). |
| 2 | Axis moves to the target in the positive direction only. If the target is lower than the current position, the axis takes the shortest positive-only path to the target. Otherwise it moves like a linear axis (additional revolution(s) if the delta exceeds `ModRev`). |
| 3 | Axis moves to the target by the shortest path. It does not take additional revolution(s) even if the absolute position delta is more than `ModRev`. |

## Examples

```text
ModShort=0          ; normal (linear-like) path
ModShort=3          ; shortest path
```

## See also

- [ModRev](ModRev.md) — enables modulo mode that `ModShort` operates within
- [MotionMode](../../10-motion/02-motion-configuration/MotionMode.md) — motion mode in which `ModShort` applies
- [HomingDef](../../16-homing/HomingDef.md) — homing definition that can invoke `ModShort`
