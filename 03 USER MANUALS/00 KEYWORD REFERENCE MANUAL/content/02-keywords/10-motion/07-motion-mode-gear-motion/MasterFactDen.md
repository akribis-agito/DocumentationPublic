---
summary: Denominator of the gear ratio applied to the master-variable delta.
keyword: MasterFactDen
availability:
- controller
- ci-master
can_code: 632
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-11-23'
doc_revision: '2026.11'
---
# MasterFactDen

Denominator of the gear ratio applied to the master-variable delta.

## Overview

`MasterFactDen` is the denominator of the gear ratio in gear motion. Together with the numerator [MasterFact](MasterFact.md) it forms an exact rational ratio `MasterFact / MasterFactDen` that maps a change in the master variable (selected by [GearMaster](GearMaster.md)) to a change in [MasterPos](MasterPos.md), driving the follower's reference [PosRef](../01-kinematics-status/PosRef.md) (direct gear, [MotionMode](../02-motion-configuration/MotionMode.md) `= 5`) or target [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) (indirect gear, `MotionMode = 6`).

On legacy v4 gearing the denominator is fixed at 65536. Setting `MasterFactDen = 65536` on v5 preserves the old ratio for the same numerator. To use the intended 1:3 ratio, set the numerator to 1 and the denominator to 3.

On multi-axis firmware with the fractional tracking fix, direct slave mode also uses the reduced `MasterFact / MasterFactDen` ratio. Axis A carries the remainder as it follows changes in axis B’s reference. See [MotionMode10](MotionMode10.md).

## How it works

$$
\Delta_{\text{MasterPos}} = \frac{\text{MasterFact}}{\text{MasterFactDen}} \cdot \Delta_{\text{master variable}}
$$

### Exact, drift-free ratio

When the pair is set, the controller reduces `MasterFact` and `MasterFactDen` by their greatest common divisor. The denominator is always kept positive — the ratio's sign lives in `MasterFact`.

Each control cycle the controller then applies the ratio with a **quotient-and-remainder** scheme in extended-precision floating point: it carries the fractional part of the master change forward to the next cycle so that the accumulated follower motion equals `MasterFact / MasterFactDen × master change` with no long-term rounding drift, even for ratios that are not a clean multiple of 1/65536. This is the main advantage of the v5 numerator/denominator form over the v4 single-factor form.

### Migrating a saved ratio

In the host comparison at 2:5, legacy gearing rounded the factor down to 26214/65536. Over about 1.51 billion follower counts of positive travel the legacy follower ended 23,040 counts behind v5. The difference scales with net master travel and changes sign when travel reverses. Across the ratios tested, v5 stayed within half a count of the intended position. The separate velocity-feedforward comparison differed by at most one count. [Gearing migration study](https://github.com/akribis-agito/Firmware-Main/blob/b767c53b79d07e8b825c9889cfc4779867087f9c/docs/convergence/gearing_ffw_divergence_study.md)

### Worked example

A virtual-master rotary encoder reports 360 000 counts per revolution; the follower is geared at 7 follower units per 11 master units. Set `MasterFact = 7`, `MasterFactDen = 11`. If the master rotates at 360 000 counts/s (1 rev/s), `MasterPos` accumulates at `360000 × 7/11 ≈ 229 091` follower units/s. Per-cycle the controller scales the master change by `7/11` and carries the leftover fraction into the next cycle, so over any window of N cycles the accumulated follower change matches `7N/11` exactly.

The valid range is `1 … 16777215`; it must not be zero.

## Examples

```text
AMasterFactDen=65536 ; with MasterFact=65536 gives a 1:1 ratio (default)
AMasterFact=3        ; together with...
AMasterFactDen=7     ; ...gives an exact 3:7 ratio (follower moves 3 per 7 master units)
AMasterFactDen       ; read the gear-ratio denominator
```

## See also

- [MasterFact](MasterFact.md) — numerator of the gear ratio
- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [GearMaster](GearMaster.md) — selects the master variable
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (`= 5`) or indirect (`= 6`) gear motion
