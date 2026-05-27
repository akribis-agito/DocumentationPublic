---
summary: Denominator of the gear ratio applied to the master-variable delta.
keyword: MasterFactDen
availability:
  standalone: []
  central-i:
  - v5
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
---
# MasterFactDen

Denominator of the gear ratio applied to the master-variable delta.

## Overview

`MasterFactDen` is the denominator of the gear ratio in gear motion. Together with the numerator [MasterFact](MasterFact.md) it forms an exact rational ratio `MasterFact / MasterFactDen` that maps a change in the master variable (selected by [GearMaster](GearMaster.md)) to a change in [MasterPos](MasterPos.md), driving the follower's reference [PosRef](../01-kinematics-status/PosRef.md) (direct gear, [MotionMode](../02-motion-configuration/MotionMode.md) `= 5`) or target [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) (indirect gear, `MotionMode = 6`).

`MasterFactDen` exists **only on v5 (central-i)**. On v4 there is no denominator: the ratio is `MasterFact / 65536` (see [MasterFact](MasterFact.md)). The default `65536` therefore reproduces the v4 1:1 ratio when `MasterFact = 65536`.

## How it works

$$
\mathrm{\Delta}_{MasterPos} = \frac{MasterFact}{MasterFactDen} \bullet \mathrm{\Delta}_{master\ variable}
$$

### Exact, drift-free ratio

When the pair is set, the firmware reduces `MasterFact` and `MasterFactDen` by their greatest common divisor and precomputes the reciprocal of the denominator (`develop:CommonC/SpecialFuncs.c:5306`, `:5399`). The denominator is always kept positive — the ratio's sign lives in `MasterFact`.

Each control cycle the gearing macro then applies the ratio with a **quotient-and-remainder** scheme in `long double`: it carries the fractional part of the master change forward to the next cycle (`gldMasterPosPreFactFloatPoint`) so that the accumulated follower motion equals `MasterFact / MasterFactDen × master change` with no long-term rounding drift, even for ratios that are not a clean multiple of 1/65536 (`develop:CommonIncludes/AG300_CTL01ControlInterrupt.h`). This is the main advantage of the v5 numerator/denominator form over the v4 single-factor form.

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
