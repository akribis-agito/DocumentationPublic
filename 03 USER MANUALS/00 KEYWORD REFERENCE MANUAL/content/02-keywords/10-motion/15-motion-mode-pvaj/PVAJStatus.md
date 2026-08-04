---
keyword: PVAJStatus
summary: PVAJ state, current row and rows remaining.
availability:
  standalone: []
  central-i:
  - v5
can_code: 883
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  default: 0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
---
# PVAJStatus

Read-only report of where this axis stands in the PVAJ cycle.

| Index | Contents |
|---|---|
| `[1]` | **State** — see below |
| `[2]` | **Current row**, 1-based, while executing |
| `[3]` | **Rows remaining** until the list completes |

## State

| Value | State | Reached by |
|---|---|---|
| `0` | not validated | power-on, or any write to [PVAJList](PVAJList.md) |
| `1` | validated | [PVAJValidate](PVAJValidate.md) succeeded |
| `2` | armed | [PVAJArm](PVAJArm.md) `= 1` |
| `3` | executing | `Begin` in [MotionMode](../02-motion-configuration/MotionMode.md) `22` or `23` |

Completing a motion returns the axis to *not validated*, because completion disarms it and the list would have to be validated again for a further run.
