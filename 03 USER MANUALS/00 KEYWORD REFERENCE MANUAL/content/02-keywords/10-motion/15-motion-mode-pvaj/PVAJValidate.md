---
keyword: PVAJValidate
summary: Checks a PVAJ list before it may be armed.
availability:
  standalone: []
  central-i:
  - v5
can_code: 881
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 3
  default: 0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
---
# PVAJValidate

Checks the [PVAJList](PVAJList.md) of this axis. A list must pass validation before [PVAJArm](PVAJArm.md) will accept it.

| Value | Checks performed |
|---|---|
| `1` | **Full** — header, range *and* continuity |
| `2` | **None** — force the list valid without checking. The trajectory becomes the user's responsibility |
| `3` | **Partial** — header and range only; continuity is not checked |

On success the axis moves to the *validated* state, visible in [PVAJStatus](PVAJStatus.md)`[1]`.

## What is checked

**Header** — `Len` within `1`–`8192`, `Gap` within `1`–`32`, `Mode` either `0` or `1`.

**Range** — every row's position within the position limits, velocity within [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md), acceleration within [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md).

**Continuity** — that consecutive rows agree, within [PVAJPosTol](PVAJPosTol.md) on position and [PVAJVelTol](PVAJVelTol.md) on velocity, with what the quintic between them implies.

## Errors

| Code | Meaning |
|---|---|
| `390` | list size (`Len`) out of range |
| `391` | gap out of range |
| `392` | mode is neither `0` nor `1` |
| `393` | a position lies outside the position limits |
| `394` | a velocity exceeds [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) |
| `395` | an acceleration exceeds [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md) |
| `396` | position continuity failed — check [PVAJPosTol](PVAJPosTol.md) |
| `397` | velocity continuity failed — check [PVAJVelTol](PVAJVelTol.md) |

A range failure is reported in preference to an earlier continuity failure, and the reported row is the one that failed.
