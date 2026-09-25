---
keyword: PVAJList
summary: The PVAJ trajectory table - header plus up to 8192 position/velocity/acceleration/jerk rows.
availability:
  standalone: []
  central-i:
  - v5
can_code: 880
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 32772
  data_type: double
  ok_in_motion: true
  ok_motor_on: true
  units: none
  default: 0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
---
# PVAJList

The trajectory table executed by the PVAJ motion modes ([MotionMode](../02-motion-configuration/MotionMode.md) = 22 or 23). See the [PVAJ overview](00-overview.md) for how the modes fit together.

## Layout

Indexes are 1-based, as for every array keyword.

| Index | Contents |
|---|---|
| `[1]` | **Len** — number of rows in the list, `1`–`8192` |
| `[2]` | **Gap** — control ticks between consecutive rows, `1`–`32` |
| `[3]` | **Mode** — `0` absolute, `1` relative to the position at `Begin` |
| `[4]`, `[5]`, `[6]`, `[7]` | row 1: position, velocity, acceleration, jerk |
| `[8]` … | row 2, and so on in strides of four |

The last usable index is therefore **32771** — `J` of row 8192.

Values are held as doubles. Position is in counts, velocity in counts/second, acceleration in counts/second², jerk in counts/second³.

## Writing the list

Writing **any** element returns the axis to the *not validated* state, so a list must be re-validated ([PVAJValidate](PVAJValidate.md)) and re-armed ([PVAJArm](PVAJArm.md)) after any change. Because [PVAJArm](PVAJArm.md) snapshots the list, a new one may be written while a motion is still executing — the running motion is unaffected.

## Flash

`PVAJList` is saved to flash only on a product whose parameter region is large enough to hold it (14 MB); elsewhere it is **not** flash-saved. A 3 MB row against a smaller parameter region would make *every* `SaveFile` fail with a full-flash error, not merely lose the PVAJ list.

## Errors

The range and continuity of the list are checked by [PVAJValidate](PVAJValidate.md), not on write; see that page for the codes.
