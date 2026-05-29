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

`Pos` is the main position feedback and, in normal (non-gantry) operation, the **position-loop feedback signal** — so it is the basis for the position error [PosErr](PosErr.md) (`PosErr = PosRef − Pos`). It is reported in user units (set by [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md)); the internal pipeline (mapping, modulo) operates in main-encoder counts.

`Pos` is read-only but is not simply "the encoder." It is the **output of a feedback pipeline** and is reshaped by several mechanisms (simulation, error mapping, modulo, dual-loop, gantry) described below. It resets to `0` on power-up and can be **preset** with [SetPosition](../03-kinematics-configuration/SetPosition.md) (do not write `Pos` directly); with an absolute encoder it is initialised from the absolute reading at startup.

## How it works

### Feedback pipeline

Each control cycle `Pos` is produced from the decoded main-encoder reading in stages:

```text
main encoder ─► (decode) ─► PosBeforeMap ─► [error mapping] ─► [modulo ModRev] ─► Pos
```

[PosBeforeMap](../../04-error-mapping/PosBeforeMap.md) holds the value **before** correction (for diagnostics). With no error map and no modulo, `Pos` equals the decoded encoder reading.

### Simulation mode

When the axis runs in **simulation** (`MotorType` = simulation) there is no physical encoder: the controller sets the feedback equal to the reference, so **`Pos` follows `PosRef` exactly**. Error mapping is deliberately skipped in simulation to avoid creating a feedback loop with the motor-off behaviour that forces `PosRef = Pos`. This lets you dry-run motion programs without hardware.

### Motor-off behaviour

While the motor is off, the controller forces `PosRef = Pos`, so the reference tracks the live feedback. This guarantees zero position error at the instant the motor is enabled, preventing a jump.

### Error mapping

When an encoder error map is active ([MapType](../../04-error-mapping/MapType.md) = 1D/2D/3D), `Pos = PosBeforeMap + correction`, with the correction interpolated from the map table. The correction is **ramped in/out** so engaging or changing the map does not produce a position step.

### Modulo (continuous rotary) — ModRev

If [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0, `Pos` is kept within `[0, ModRev)`. When the reading would cross a boundary (`Pos ≥ ModRev` going positive, or `Pos < 0` going negative) the controller subtracts/adds `ModRev` from `Pos` **and shifts the entire reference frame by the same amount** — `PosRef`, the shaped/filtered references, [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md), `PDPos`, and the gear master position all move together — so the following error is preserved across the wrap and the axis can rotate continuously. The wrap is applied only when the jerk buffer is clear of pre-wrap values, and it assumes no more than half a modulus distance of travel per control cycle. For a stepper open-loop motor the wrap edge is detected on the reference rather than on `Pos` (there is no closed-loop feedback to compare). See also [ModShort](../../03-encoder/04-modulo-mode/ModShort.md) for shortest-path targeting.

### Edge cases

- **Motor off:** `Pos` continues to track the encoder reading (so an external push moves `Pos`); the controller forces `PosRef = Pos` so [PosErr](PosErr.md) stays zero.
- **Simulation mode (`MotorType` = 5):** `Pos` is forced to equal `PosRef` (no physical encoder).
- **Active fault:** the encoder pipeline keeps updating `Pos`; the loop is shut down but the feedback remains valid for inspecting the stopped position.
- **Out-of-range write:** `Pos` is read-only — write attempts are rejected by the parameter system. Use [SetPosition](../03-kinematics-configuration/SetPosition.md) to preset.
- **ModRev wrap during a jerk-buffered move:** the wrap is held until `glNumberOfWrongValuesInJerkBufferBecauseOfModulus` clears, so back-and-forth motion near the wrap edge can momentarily skip a wrap; this is benign.
- **Dual-loop:** in pseudo dual-loop `Pos` is the scaled [AuxPos](AuxPos.md); in true dual-loop and in gantry the position loop uses `Pos`/[GantryFdbk](../../12-gantry-control/02-gantry-kinematic-feedback/GantryFdbk.md) and `Pos` still reads the main encoder.

### Dual-loop and gantry

What `Pos` represents also depends on the loop configuration:

| Configuration | `Pos` definition |
|---------------|------------------|
| Default, dual-loop, or gantry (all except pseudo dual-loop) | Decoded main-encoder reading (post-mapping/modulo). |
| Pseudo dual-loop (non-gantry) | Auxiliary encoder, scaled to main-encoder units: $$\text{Pos} = \text{AuxPos} \cdot \frac{\text{DualLoopFact}}{65536}$$ |

In gantry mode the position loop uses [GantryFdbk](../../12-gantry-control/02-gantry-kinematic-feedback/GantryFdbk.md) (the common-mode position) rather than a single-axis `Pos`.

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Data type | 32-bit integer (`long`) | **64-bit integer (`long long`)** |
| Range | ±2,147,483,647 | ±2,251,799,813,685,247 (2⁵¹−1) |

In **v5** the position pipeline moved to **64-bit** calculations, so `Pos` is a 64-bit value with a far larger range (capped at 2⁵¹−1 because PCSuite records data in `double`), allowing far more accumulated travel without wrapping. **v5 is central-i only** — the standalone product is not supported on v5, so on standalone `Pos` remains the v4 32-bit value.

## Examples

```text
APos                ; read axis A's main position feedback
```

## See also

- [PosRef](PosRef.md) — position reference; [PosErr](PosErr.md) — `PosRef − Pos`
- [PosBeforeMap](../../04-error-mapping/PosBeforeMap.md) — feedback before error-mapping correction
- [AuxPos](AuxPos.md) — auxiliary feedback (used in pseudo dual-loop)
- [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) / [ModShort](../../03-encoder/04-modulo-mode/ModShort.md) — modulo (continuous-rotation) mode
- [MapType](../../04-error-mapping/MapType.md) — encoder error mapping
- [SetPosition](../03-kinematics-configuration/SetPosition.md) — preset the feedback
- [GantryFdbk](../../12-gantry-control/02-gantry-kinematic-feedback/GantryFdbk.md) — gantry common-mode position
- [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — user-unit scaling
