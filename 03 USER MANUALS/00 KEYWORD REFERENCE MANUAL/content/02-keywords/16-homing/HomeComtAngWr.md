---
keyword: HomeComtAngWr
summary: Sets the commutation angle applied at the home position to skip a homing sequence.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 409
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# HomeComtAngWr

Sets the commutation angle applied at the home position to skip a homing sequence.

## Overview

`HomeComtAngWr` holds the commutation angle that the commutation-angle homing feature applies at the home/index position. The value is an electrical angle in units of 0.01° (range 0–35999 = 0–359.99°). Set it to an angle previously read from [HomeComtAngRd](HomeComtAngRd.md), so that after homing the controller resumes commutation at the correct electrical angle. It is an axis-scoped parameter saved to flash, so the value persists across power cycles, and it cannot be written while the axis is in motion.

This keyword only has an effect when [HomeComtAngOn](HomeComtAngOn.md) is non-zero. With the feature disabled, `HomeComtAngWr` is simply a stored value that is neither applied during homing nor on direct writes.

## How it works

`HomeComtAngWr` is applied in two situations, both gated by [HomeComtAngOn](HomeComtAngOn.md):

- **During homing.** When the homing step that ends on the index completes and [HomeComtAngOn](HomeComtAngOn.md) is non-zero, the controller sets the live commutation angle ([ComtAng](../15-commutation/ComtAng.md)) directly to `HomeComtAngWr` and recomputes the internal commutation offset from it. Because the axis is sitting on the index, this is a direct assignment.

- **On a direct write.** When you write `HomeComtAngWr` while [HomeComtAngOn](HomeComtAngOn.md) is non-zero, the controller computes the difference between the new value and the angle currently held in [HomeComtAngRd](HomeComtAngRd.md)`[1]`, converts that delta to encoder counts, and shifts the commutation offset by it (wrapping within one electrical cycle). [HomeComtAngRd](HomeComtAngRd.md)`[1]` is then updated to the new value. Writing is permitted only when the axis is not in motion, so the angle is well-defined during the adjustment.

The conversion uses the axis's electrical cycle length, so the same 0.01° value maps correctly regardless of pole count and encoder resolution.

## Examples

```text
AHomeComtAngOn=1      ; enable the feature first
AHomeComtAngWr=12000  ; apply 120.00 electrical degrees as the home commutation angle
AHomeComtAngWr       ; read the configured commutation angle (0.01° units)
```

## See also

- [HomeComtAngRd](HomeComtAngRd.md) — source of the captured angle to write here
- [HomeComtAngOn](HomeComtAngOn.md) — must be enabled for this value to take effect
- [ComtAng](../15-commutation/ComtAng.md) — the live commutation angle this value sets
