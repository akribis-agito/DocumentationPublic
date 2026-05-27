---
keyword: Pos
summary: Main position feedback in user units; the position-loop feedback signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# Pos

Main position feedback in user units; the position-loop feedback signal.

## Overview

`Pos` reports the main encoder feedback in main user units (configurable via [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md)). It is the position-loop feedback signal in non-gantry mode, so it is the basis for the position error [PosErr](PosErr.md) (`PosErr = PosRef − Pos`) and is related to the auxiliary feedback [AuxPos](AuxPos.md).

Although read-only, `Pos` can be preset to any value at any time via [SetPosition](../03-kinematics-configuration/SetPosition.md) (do not write `Pos` directly). It resets to `0` on power-up.

## How it works

What `Pos` represents depends on the control configuration:

| Configuration | `Pos` definition |
|---------------|------------------|
| Default control, dual-loop control, or gantry mode (non-gantry except pseudo dual-loop) | Main encoder reading after the modulo block. Unit: main encoder count. |
| Pseudo dual-loop control (non-gantry) | Auxiliary encoder reading, decoded and scaled to main-encoder units: $$Pos = AuxPos \times \frac{DualLoopFact}{65536}$$ Unit: main encoder count. |

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer (`long`) | **64-bit integer (`long long`)** |
| Range | ±2,147,483,647 | ±2,251,799,813,685,247 (2⁵¹−1) |

In **v5** the position pipeline moved to **64-bit** calculations, so `Pos` is a 64-bit value with a far larger range (capped at 2⁵¹−1 because PCSuite records data in `double`). This lets a single axis accumulate far more travel without wrapping. **v5 is central-i only** — the standalone product is not supported on v5, so on standalone `Pos` remains the v4 32-bit value.

## Examples

```text
APos                ; read the main position feedback (axis A)
```

## See also

- [PosErr](PosErr.md) — position error (`PosRef − Pos`)
- [PosRef](PosRef.md) — position reference
- [AuxPos](AuxPos.md) — auxiliary position feedback
- [SetPosition](../03-kinematics-configuration/SetPosition.md) — preset the position feedback
