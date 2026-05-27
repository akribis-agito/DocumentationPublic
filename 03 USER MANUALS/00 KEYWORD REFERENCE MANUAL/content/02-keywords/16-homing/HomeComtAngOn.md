---
keyword: HomeComtAngOn
summary: Enables capture of the commutation angle at the home position during homing.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 408
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
overrides: {}
---
# HomeComtAngOn

Enables capture of the commutation angle at the home position during homing.

## Overview

`HomeComtAngOn` is the master enable for the commutation-angle homing feature. The commutation angle ([ComtAng](../15-commutation/ComtAng.md)) is the electrical angle the controller uses to commutate the motor; this feature lets a known mechanical home position re-establish that angle without re-running a full phasing/homing search.

`HomeComtAngOn` controls two related actions:

- During a homing run, when the axis arrives at the recorded index position, the commutation angle present there is captured into [HomeComtAngRd](HomeComtAngRd.md), and — only if `HomeComtAngOn` is non-zero — the commutation is then forced to the value stored in [HomeComtAngWr](HomeComtAngWr.md).
- When the user writes [HomeComtAngWr](HomeComtAngWr.md) directly, the commutation variables are adjusted by the delta — again only if `HomeComtAngOn` is non-zero.

It is an axis-scoped parameter, not saved to flash, and can be changed at any time.

## How it works

The capture/apply runs inside the homing step that ends on the index position ("Move to index position", and likewise "Move to lock position"). When that step finishes:

1. The current commutation angle is copied into [HomeComtAngRd](HomeComtAngRd.md)`[1]` and `[2]` regardless of `HomeComtAngOn`.
2. If `HomeComtAngOn != 0`, the controller sets [ComtAng](../15-commutation/ComtAng.md) to the value in [HomeComtAngWr](HomeComtAngWr.md), recomputes the internal commutation offset from it, and refreshes [HomeComtAngRd](HomeComtAngRd.md)`[1]` to the applied value.

If `HomeComtAngOn` is `0`, the angle present at the index is still captured into [HomeComtAngRd](HomeComtAngRd.md) for inspection, but the live commutation is left unchanged.

| HomeComtAngOn | Behaviour |
|---|---|
| 0 | Capture-only: [HomeComtAngRd](HomeComtAngRd.md) is updated at the index, commutation is not altered. |
| 1 | Capture-and-apply: as above, then [ComtAng](../15-commutation/ComtAng.md) is forced to [HomeComtAngWr](HomeComtAngWr.md); direct writes to [HomeComtAngWr](HomeComtAngWr.md) also adjust live commutation. |

## Examples

```text
AHomeComtAngOn=1     ; enable capture-and-apply of the commutation angle at home
AHomeComtAngOn      ; 0 = disabled, 1 = enabled
```

## See also

- [HomeComtAngRd](HomeComtAngRd.md) — read-only array holding the captured angle(s)
- [HomeComtAngWr](HomeComtAngWr.md) — the angle applied when this is enabled
- [ComtAng](../15-commutation/ComtAng.md) — the live commutation angle this feature sets
