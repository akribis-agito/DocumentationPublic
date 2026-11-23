---
keyword: MasterFact
summary: Numerator of the gear ratio applied to the master-variable delta.
availability:
- controller
- ci-master
can_code: 120
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
  - -16777215
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-11-23'
doc_revision: '2026.11'
---
# MasterFact

Numerator of the gear ratio applied to the master-variable delta.

## Overview

`MasterFact` is the numerator of the gear ratio applied to the change of the master variable in gear motion. It maps a change in the master (selected by [GearMaster](GearMaster.md)) to a change in [MasterPos](MasterPos.md), which in turn drives the follower's position reference [PosRef](../01-kinematics-status/PosRef.md) (direct gear, [MotionMode](../02-motion-configuration/MotionMode.md) `= 5`) or its target [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) (indirect gear, `MotionMode = 6`).

## How it works

### The ratio is normalised to 65536

`MasterFact` is a numerator relative to a base of 65536, so the default value `65536` gives a **1:1** ratio. In v4 it is applied directly, with no separate denominator term:

$$
\Delta_{\text{MasterPos}} = \frac{\text{MasterFact}}{65536} \cdot \Delta_{\text{master variable}}
$$

The scaled change is accumulated into `MasterPos` each cycle.

A negative `MasterFact` reverses the follower direction relative to the master. To set ratios that are not a clean multiple of 1/65536, use the numerator/denominator pair (v5) — see *Changes between versions*.

### Note on the separate direct-slave mode

On multi-axis firmware with the fractional tracking fix, direct slave mode also uses the reduced `MasterFact / MasterFactDen` ratio. Axis A carries the remainder as it follows changes in axis B’s reference. See [MotionMode10](MotionMode10.md).

## Examples

```text
AMasterFact=65536    ; 1:1 ratio (default)
AMasterFact=131072   ; follower moves 2 master units per master unit
AMasterFact=-65536   ; 1:1, reversed direction
AMasterFact          ; read current value
```

## Changes between versions

Legacy v4 gearing rounds the requested ratio to a multiple of 1/65536. Firmware using `MasterFact / MasterFactDen` carries the fractional remainder from one cycle to the next. At 1:3 the old factor was 21845/65536. With positive net master travel the legacy follower falls behind the v5 follower. Reversing net travel reverses the difference. A ratio that rounds upward gives the opposite result. See [MasterFactDen](MasterFactDen.md) for the measured differences and [MasterModRev](MasterModRev.md) to convert a saved wrap period.

## See also

- [MasterFactDen](MasterFactDen.md) — denominator of the gear ratio (v5)
- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [GearMaster](GearMaster.md) — selects the master variable
- [MasterFilt](MasterFilt.md) — low-pass filter on the geared reference (direct mode)
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (`= 5`) or indirect (`= 6`) gear motion
- [MotionMode10](MotionMode10.md) — separate direct-slave mode that also reads `MasterFact`
