---
keyword: PosUnitGrp
summary: "Read-only list of the keywords that belong to the position unit group."
availability:
  standalone: []
  central-i:
  - v5
can_code: 802
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 40
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosUnitGrp

Read-only list of the keywords that belong to the position unit group.

## Overview

`PosUnitGrp` reports which keywords make up the **position** unit group of the global engineering-units feature. These are the position-related keywords whose values are reinterpreted together when the position engineering unit is changed through [PosUnitFct](PosUnitFct.md) and [PosUnitUnt](PosUnitUnt.md). The list is fixed by the firmware; reading it lets you confirm exactly which keywords a position-unit change affects.

This keyword is available from central-i v5 only.

## How it works

`PosUnitGrp` is a read-only, non-axis array. The firmware fills it with the identities of the position-group member keywords; each element identifies one member keyword. The array is 1-indexed: element [1] is the first member and element [0] is reserved and not used.

The position group contains the following keywords:

| Index | Member keyword |
|---|---|
| 1 | Pos |
| 2 | PosErr |
| 3 | PosRef |
| 4 | MasterPos |
| 5 | IndexPos |
| 6 | ModRev |
| 7 | RevPLim |
| 8 | FwdPLim |
| 9 | MaxPosErr |
| 10 | InjectPosAmp |
| 11 | AbsTrgt |
| 12 | RelTrgt |
| 13 | SetPosition |
| 14 | PosBeforeMap |
| 15 | AccShapeDist |
| 16 | RefOffsetStep |
| 17 | SchedulePos |
| 18 | InTargetTol |
| 19 | PosPosTh |
| 20 | CurrPosErrTh |
| 21 | SpeedChgPos |
| 22 | Targets |
| 23 | MaxPosErrOL |
| 24 | EncAbsVal |
| 25 | CurrPosTh |
| 26 | ModeSwitchPos |
| 27 | BuffPos |
| 28 | ForcePosErrTh |
| 29 | SpringPLow |
| 30 | SpringPHigh |
| 31 | RetractTarget |
| 32 | GantryFdbk |
| 33 | GantryOffset |
| 34 | FIFOPosTrgt |
| 35 | FIFOPosPosOf |
| 36 | DualEncSwapOn |
| 37 | DualEncRange |
| 38 | SpringTableGp |
| 39 | CompTbleGap |

The highest usable index is one less than the array size.

## Examples

```text
APosUnitGrp[1]      ; read the first member of the position unit group
APosUnitGrp[9]      ; read the member at index 9
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [PosUnitFct](PosUnitFct.md) — position scale factor
- [PosUnitUnt](PosUnitUnt.md) — position unit label
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [VelUnitGrp](VelUnitGrp.md) · [AccUnitGrp](AccUnitGrp.md) · [FrcUnitGrp](FrcUnitGrp.md) — the other quantity groups
