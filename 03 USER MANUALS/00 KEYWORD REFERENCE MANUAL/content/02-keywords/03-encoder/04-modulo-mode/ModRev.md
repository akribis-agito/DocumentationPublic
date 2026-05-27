---
keyword: ModRev
summary: Modulo divisor; wraps the feedback (and references) to the range [0, ModRev-1] when non-zero.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 70
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: user
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ModRev

Modulo divisor; wraps the feedback (and references) to the range [0, ModRev-1] when non-zero.

## Overview

`ModRev` defines the divisor used in the modulo operation. When non-zero, modulo mode wraps the feedback position to the range $[0,\ ModRev - 1]$, which lets a rotary axis move in one direction indefinitely without the feedback exceeding the numerical limit. When `ModRev=0`, modulo operation is disabled. Being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion. The shortest-path behaviour in PTP motion is selected by [ModShort](ModShort.md).

When the feedback (generally [Pos](../../10-motion/01-kinematics-status/Pos.md)) undergoes the modulo operation, the position reference ([PosRef](../../10-motion/01-kinematics-status/PosRef.md)) and the target position ([AbsTrgt](../../10-motion/13-motion-mode-ptp/AbsTrgt.md)) also undergo the modulo operation to ensure continuity in position control. Modulo operation also applies to position before mapping (PosBeforeMap), pulse-direction position (PDPos), and gear motion position (MasterPos).

## How it works

| ModRev value | Description |
|:--:|:--|
| 0 | Modulo operation is disabled. |
| ≠ 0 | Modulo operation is enabled, with feedback wrapped to the range $[0,\ ModRev - 1]$. |

## Examples

The table shows the modulo operation output for a `ModRev` of 3000:

| Modulo operation input (after error mapping) | ModRev value | Modulo operation output |
|:--:|:--:|:--:|
| 3050 | 3000 | 50 |
| 3000 | 3000 | 0 |
| 0 | 3000 | 0 |
| -40 | 3000 | 2960 |

```text
AModRev=3000         ; wrap feedback to [0, 2999]
AModRev=0            ; disable modulo mode
```

## See also

- [ModShort](ModShort.md) — shortest-path selection for PTP motion under modulo mode
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position that is wrapped
- [PosRef](../../10-motion/01-kinematics-status/PosRef.md) / [AbsTrgt](../../10-motion/13-motion-mode-ptp/AbsTrgt.md) — references that also wrap for continuity
