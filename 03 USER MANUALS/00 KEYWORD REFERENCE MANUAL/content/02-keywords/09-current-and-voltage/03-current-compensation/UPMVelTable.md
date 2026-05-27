---
keyword: UPMVelTable
summary: Per-commutation-angle current compensation table for brushless motors (e.g. cogging compensation).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 628
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 361
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -20000
  - 20000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# UPMVelTable

Per-commutation-angle current compensation table for brushless motors (e.g. cogging compensation).

## Overview

`UPMVelTable` is a parameter array that provides commutation-angle-dependent motor current compensation, for example to compensate cogging. It is only used when [MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4 (linear or rotary brushless motor — the firmware classifies both as a brushless motor type). See [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md) for its application point.

## How it works

The compensation is applied in the current control loop while the motor is enabled and commutation (auto-phasing) is complete. Two conditions must hold for the table to be used:

1. The motor is a brushless type (so a commutation angle exists — brush motors have no commutation angle).
2. The anti-cogging feature is enabled by its on/off flag (`UPMVelOn` ≠ 0).

When enabled, each control cycle the firmware reads the present commutation angle ([ComtAng](../../15-commutation/ComtAng.md)), converts it from radians to degrees and rounds to the nearest whole degree, then uses that as the array index. The value found there is **added** to the current reference:

$$
CurrRef \mathrel{+}= UPMVelTable[\,\mathrm{round}(ComtAng_{deg})\,]
$$

So `UPMVelTable[54]` is the current compensation value applied when the commutation angle rounds to 54 degrees. The table holds one entry per whole degree over a full electrical cycle (0–360 degrees); it is 1-indexed, so the valid compensation entries begin at index `1`. All array elements default to 0 (no compensation).

The added term is in the same units as the current reference ([CurrRef](../02-motor-variables/CurrRef.md)). On central-i v5 the table and reference are floating-point; on v4 they are integer. The indexing and the conditions for application are identical across versions.

## Examples

```text
AUPMVelTable[54]=300 ; compensation applied at commutation angle 54 degrees
AUPMVelTable[1]=0    ; no compensation at the first angle entry
```

## See also

- [ComtAng](../../15-commutation/ComtAng.md) — commutation angle that indexes this table
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — must be 3 or 4 (brushless) for this to apply
- [CurrRefOffset](CurrRefOffset.md) — motor-side current offset
