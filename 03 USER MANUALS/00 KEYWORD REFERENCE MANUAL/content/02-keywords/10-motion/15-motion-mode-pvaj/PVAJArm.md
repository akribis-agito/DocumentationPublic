---
keyword: PVAJArm
summary: Snapshots a validated PVAJ list and makes the axis eligible for Begin.
availability:
  standalone: []
  central-i:
  - v5
can_code: 882
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
---
# PVAJArm

`PVAJArm = 1` **arms** the axis: the validated [PVAJList](PVAJList.md) is copied into an internal snapshot and the axis becomes eligible for `Begin` in a PVAJ motion mode. `PVAJArm = 0` disarms it.

Because arming takes a snapshot, a new list may be uploaded and validated while a motion is still executing — the running motion continues from the copy it started with.

Completing a motion **disarms** the axis, so each run needs its own `PVAJArm = 1`.

## Errors

| Code | Meaning |
|---|---|
| `398` | the list is not validated — call [PVAJValidate](PVAJValidate.md) first |
| `399` | the axis is executing a PVAJ motion; it can be neither armed nor disarmed until that motion ends |

Disarming an executing axis is refused rather than honoured: the interpolator would otherwise be left running off a snapshot that no longer belongs to anything.
