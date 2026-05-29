---
keyword: MasterFact
summary: Numerator of the gear ratio applied to the master-variable delta.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

### Special unity-ratio case

A value of exactly `65536`, together with `MasterFilt = 64` and direct gear mode pointing at another axis's reference, enables the drift-free axis-to-axis gearbox described under [GearMaster](GearMaster.md).

## Examples

```text
AMasterFact=65536    ; 1:1 ratio (default)
AMasterFact=131072   ; follower moves 2 master units per master unit
AMasterFact=-65536   ; 1:1, reversed direction
AMasterFact          ; read current value
```

## Changes between versions

In **v4** the ratio is `MasterFact / 65536` (numerator only); there is no denominator in the accumulation. In **v5 (central-i)** the full rational ratio `MasterFact / MasterFactDen` is applied, carrying the fractional remainder, so non-integer ratios are exact and free of long-term drift; see [MasterFactDen](MasterFactDen.md). **v5 is central-i only.**

## See also

- [MasterFactDen](MasterFactDen.md) — denominator of the gear ratio (v5)
- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [GearMaster](GearMaster.md) — selects the master variable
- [MasterFilt](MasterFilt.md) — low-pass filter on the geared reference (direct mode)
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (`= 5`) or indirect (`= 6`) gear motion
