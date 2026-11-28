---
keyword: PVAJList
summary: PVAJ trajectory table with a header and up to 16 Orbit FR or 8192 standard rows.
availability:
- ci-master
can_code: 880
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 32772
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-11-24'
doc_revision: '2026.11'
---
# PVAJList

The trajectory table executed by the PVAJ motion modes ([MotionMode](../02-motion-configuration/MotionMode.md) = 22 or 23). See the [PVAJ overview](00-overview.md) for how the modes fit together.

## Layout

Indexes are 1-based, as for every array keyword.

| Index | Contents |
|---|---|
| `[1]` | **Len** — number of rows in the list, `1`–`8192` (`1`–`16` on Orbit FR) |
| `[2]` | **Gap** — control ticks between consecutive rows, `1`–`32` |
| `[3]` | **Mode** — `0` absolute, `1` relative to the position at `Begin` |
| `[4]`, `[5]`, `[6]`, `[7]` | row 1: position, velocity, acceleration, jerk |
| `[8]` … | row 2, and so on in strides of four |

The last usable index is **32771** on standard firmware or **67** on Orbit FR, the jerk entry of the final row.

Values are held as doubles. Position is in counts, velocity in counts/second, acceleration in counts/second², jerk in counts/second³.

## Writing the list

Writing **any** element returns the axis to the *not validated* state, so a list must be re-validated ([PVAJValidate](PVAJValidate.md)) and re-armed ([PVAJArm](PVAJArm.md)) after any change. Because [PVAJArm](PVAJArm.md) snapshots the list, a new one may be written while a motion is still executing — the running motion is unaffected.

## Flash

The double-flash firmware saves `PVAJList`. This includes the 16-row list on Orbit FR. On products with a smaller parameter allocation, the list is volatile.

## Errors

The range and continuity of the list are checked by [PVAJValidate](PVAJValidate.md), not on write; see that page for the codes.

## Orbit FR

On an Orbit FR AGM800 this list has 16 data rows. Including the three header entries, usable indices run from 1 through 67. The ordinary 8192-row layout has last index 32771.
