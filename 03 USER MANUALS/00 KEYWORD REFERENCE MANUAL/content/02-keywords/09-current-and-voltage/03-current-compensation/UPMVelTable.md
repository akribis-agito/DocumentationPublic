---
keyword: UPMVelTable
summary: Per-commutation-angle current compensation table for brushless motors (e.g. cogging compensation).
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# UPMVelTable

Per-commutation-angle current compensation table for brushless motors (e.g. cogging compensation).

## Overview

`UPMVelTable` is a parameter array that provides commutation-angle-dependent motor current compensation, for example to compensate cogging. It is only used when [MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 or 4 (brushless motor). See [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md) for its application point.

## How it works

All array elements default to 0 (no compensation). Each index represents the corresponding commutation angle ([ComtAng](../../15-commutation/ComtAng.md)) in 1-degree increments. For example, `UPMVelTable[54]` is the current compensation value applied when ComtAng = 54 degrees.

## Examples

```text
AUPMVelTable[54]=300 ; compensation applied at commutation angle 54 degrees
AUPMVelTable[1]=0    ; no compensation at the first angle entry
```

## See also

- [ComtAng](../../15-commutation/ComtAng.md) — commutation angle that indexes this table
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — must be 3 or 4 (brushless) for this to apply
- [CurrRefOffset](CurrRefOffset.md) — motor-side current offset
