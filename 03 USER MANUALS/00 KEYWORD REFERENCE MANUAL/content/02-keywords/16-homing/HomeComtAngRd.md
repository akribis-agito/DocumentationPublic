---
keyword: HomeComtAngRd
summary: Read-only array of commutation angles captured at the home position.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 410
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomeComtAngRd

Read-only array of commutation angles captured at the home position.

## Overview

`HomeComtAngRd` is a read-only array holding the commutation angle recorded at the index position during a homing run. Each value is an electrical angle expressed in units of 0.01°, so the range 0–35999 covers a full electrical revolution (0–359.99°). Index `[1]` and `[2]` are used; element `[0]` does not exist (the array is 1-indexed). The capture happens whether or not [HomeComtAngOn](HomeComtAngOn.md) is enabled, so this array can be read to discover the commutation angle that corresponds to the mechanical home, which can then be saved into [HomeComtAngWr](HomeComtAngWr.md). It is an axis-scoped, read-only array that is not saved to flash.

## How it works

When the homing step that ends on the index position completes, the controller copies the live commutation angle into both `HomeComtAngRd[1]` and `HomeComtAngRd[2]`. If [HomeComtAngOn](HomeComtAngOn.md) is non-zero, the controller then forces the live commutation to the value in [HomeComtAngWr](HomeComtAngWr.md) and refreshes `HomeComtAngRd[1]` to that applied value. The result is:

| Element | Contents after the index step |
|---|---|
| `HomeComtAngRd[1]` | The commutation angle now in effect: the angle measured at the index, or — if [HomeComtAngOn](HomeComtAngOn.md) is enabled — the applied [HomeComtAngWr](HomeComtAngWr.md) value. |
| `HomeComtAngRd[2]` | The commutation angle that was measured at the index, before any apply. |

When [HomeComtAngOn](HomeComtAngOn.md) is `0`, both elements hold the angle measured at the index. To learn the angle to store for a given home, run a homing sequence and read `HomeComtAngRd[2]`.

## Examples

```text
AHomeComtAngRd[1]   ; commutation angle currently in effect (0.01° units)
AHomeComtAngRd[2]   ; commutation angle measured at the index
AHomeComtAngRd      ; read the full captured-angle array
```

## See also

- [HomeComtAngOn](HomeComtAngOn.md) — enables capture-and-apply into this array
- [HomeComtAngWr](HomeComtAngWr.md) — the stored angle applied when enabled
- [ComtAng](../15-commutation/ComtAng.md) — the live commutation angle, in the same 0.01° units
