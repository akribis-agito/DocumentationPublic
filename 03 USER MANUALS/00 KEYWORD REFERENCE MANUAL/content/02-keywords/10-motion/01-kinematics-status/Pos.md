---
keyword: Pos
summary: Main position feedback in user units; the position-loop feedback signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 2
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Pos

Main position feedback in user units; the position-loop feedback signal.

## Overview

`Pos` reports the main encoder feedback, expressed in main user units (configurable via `UsrUnits`). Because `Pos` is the position-loop feedback in non-gantry mode, its definition changes with the gantry mode and the dual-loop condition. It is the basis for the position error [PosErr](PosErr.md) and is related to the auxiliary feedback [AuxPos](AuxPos.md).

Although read-only, `Pos` can be preset to any value at any time via the [SetPosition](../03-kinematics-configuration/SetPosition.md) function (rather than writing `Pos` directly). Its value resets to `0` on power up.

## How it works

| Conditions | Default control (non-gantry mode) Dual-loop control (non-gantry mode) Gantry mode (regardless of dual-loop condition) | Pseudo dual-loop control (non-gantry mode) |
|---|---|---|
| Definition | Main encoder reading after the modulo operation block. **Unit: Main encoder count** | Auxiliary encoder reading after decoding but scaled up to main encoder unit.<br> $$Pos = AuxPos \bullet \frac{DualLoopFact}{65536}$$ **Unit: Main encoder count** |

## Examples

```text
Pos?                ; read the main position feedback
```

## See also

- [PosErr](PosErr.md) — position error (`PosRef - Pos`)
- [AuxPos](AuxPos.md) — auxiliary position feedback
- [SetPosition](../03-kinematics-configuration/SetPosition.md) — preset the position feedback
