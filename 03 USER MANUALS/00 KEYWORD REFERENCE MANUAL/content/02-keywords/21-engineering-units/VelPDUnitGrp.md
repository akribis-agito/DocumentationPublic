---
keyword: VelPDUnitGrp
summary: Read-only list of the pulse-and-direction velocity keywords that share the P/D velocity user-unit scaling and label.
availability:
  standalone: []
  central-i:
  - v5
can_code: 823
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
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
# VelPDUnitGrp

Read-only list of the pulse-and-direction velocity keywords that share the P/D velocity user-unit scaling and label.

## Overview

When Global User Units is enabled for an axis ([UserUnitsEn](UserUnitsEn.md) = 1), each physical quantity is presented to the host with a per-quantity scale factor and a free-text unit label. `VelPDUnitGrp` is the membership list for the **pulse-and-direction (P/D) velocity** quantity: it tells the host which keywords are scaled together by [VelPDUnitFct](VelPDUnitFct.md) and labeled by [VelPDUnitUnt](VelPDUnitUnt.md).

It is the P/D counterpart of the main-feedback [VelUnitGrp](VelUnitGrp.md), and applies to the pulse-and-direction velocity [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md).

`VelPDUnitGrp` is read-only and fixed: the controller populates it at startup, so you read it to discover the group, you do not edit it.

## How it works

The keyword is a non-axis array. Each populated element holds one member of the P/D velocity unit group. Arrays are 1-indexed; element [0] does not exist. The array has a reserved slot, so with `array_size` 2 the highest usable index is 1.

| Index | Member keyword |
|-------|----------------|
| [1]   | PDVel (pulse-and-direction velocity) |

Each element returns the internal command code of the member keyword (range 0–1023). A value of 0 means the slot is unused.

This grouping is consumed by the host display/units layer; it does not change the internal control computation. The scale factor and label for these keywords come from [VelPDUnitFct](VelPDUnitFct.md) and [VelPDUnitUnt](VelPDUnitUnt.md).

Global User Units and the embedded P/D scaling [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) are mutually exclusive on the same axis. If `UserUnitsEn` is on and `PDUsrUnits` is also set to a non-default scaling, accessing a member of this group reports a conflict.

This keyword is available from v5 (central-i) only.

## Examples

```text
AVelPDUnitGrp[1]    ; read the member command code of the P/D velocity group
```

## See also

- [VelPDUnitFct](VelPDUnitFct.md) — scale factor for the P/D velocity quantity
- [VelPDUnitUnt](VelPDUnitUnt.md) — unit label for the P/D velocity quantity
- [VelUnitGrp](VelUnitGrp.md) — main-feedback velocity unit group
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
- [PDVel](../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md) — pulse-and-direction velocity
