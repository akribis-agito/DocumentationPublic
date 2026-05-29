---
keyword: PosAuxUnitGrp
summary: Read-only list of the auxiliary-encoder position keywords that share the auxiliary position user-unit scaling and label.
availability:
  standalone: []
  central-i:
  - v5
can_code: 814
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 5
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
# PosAuxUnitGrp

Read-only list of the auxiliary-encoder position keywords that share the auxiliary position user-unit scaling and label.

## Overview

When the Global User Units feature is enabled for an axis ([UserUnitsEn](UserUnitsEn.md) = 1), each physical quantity (position, velocity, acceleration, force, and the auxiliary/pulse-and-direction variants) is presented to the host with a per-quantity scale factor and a free-text unit label. `PosAuxUnitGrp` is the membership list for the **auxiliary-encoder position** quantity: it tells the host which keywords are scaled together by [PosAuxUnitFct](PosAuxUnitFct.md) and labeled by [PosAuxUnitUnt](PosAuxUnitUnt.md).

It is the auxiliary-encoder counterpart of the main-feedback [PosUnitGrp](PosUnitGrp.md), and applies to the auxiliary feedback position [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) and the other auxiliary position-type values derived from it.

`PosAuxUnitGrp` is read-only and fixed: the controller populates it at startup, so you read it to discover the group, you do not edit it.

## How it works

The keyword is a non-axis array. Each populated element holds one member of the auxiliary position unit group. Arrays are 1-indexed; element [0] does not exist. The array has a reserved slot, so with `array_size` 5 the highest usable index is 4.

| Index | Member keyword |
|-------|----------------|
| [1]   | AuxPos (auxiliary feedback position) |
| [2]   | AuxIndexPos (auxiliary index-capture position) |
| [3]   | AuxModRev (auxiliary modulo per revolution) |
| [4]   | AuxEncAbsVal (auxiliary absolute-encoder value) |

Each element returns the internal command code of the member keyword (range 0–1023). A value of 0 means the slot is unused.

This grouping is consumed by the host display/units layer; it does not change the internal control computation. The scale factor and label for these keywords come from [PosAuxUnitFct](PosAuxUnitFct.md) and [PosAuxUnitUnt](PosAuxUnitUnt.md).

Global User Units and the embedded auxiliary scaling [AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) are mutually exclusive on the same axis. If `UserUnitsEn` is on and `AuxUsrUnits` is also set to a non-default scaling, accessing a member of this group reports a conflict.

This keyword is available from v5 (central-i) only.

## Examples

```text
APosAuxUnitGrp[1]    ; read the first member command code of the auxiliary position group
APosAuxUnitGrp[4]    ; read the fourth member command code
```

## See also

- [PosAuxUnitFct](PosAuxUnitFct.md) — scale factor for the auxiliary position quantity
- [PosAuxUnitUnt](PosAuxUnitUnt.md) — unit label for the auxiliary position quantity
- [PosUnitGrp](PosUnitGrp.md) — main-feedback position unit group
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
- [AuxPos](../10-motion/01-kinematics-status/AuxPos.md) — auxiliary feedback position
