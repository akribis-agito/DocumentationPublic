---
keyword: VEncSrc
summary: Selects the source signal used to generate the virtual encoder position.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 614
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncSrc

Selects the source signal used to generate the virtual encoder position.

## Overview

`VEncSrc` selects the internal variable that the virtual encoder tracks. The selected variable is scaled by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md), emitted in the format set by [VEncType](VEncType.md), and (for pulse/direction) timed with [VEncDelay](VEncDelay.md), to produce the generated encoder signal when the virtual encoder is enabled ([VEncOn](VEncOn.md) = 1). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## How it works

`VEncSrc` is **not a small enumerated list** — it is an encoded *keyword command code* combining a keyword, its axis, and array index. The controller resolves it at configuration time to the corresponding internal variable and its data type (32-bit/64-bit integer, float, or double). Each control cycle the virtual encoder reads that variable, so any readable controller variable can be the source — for example another axis's position [Pos](../../10-motion/01-kinematics-status/Pos.md) or reference [PosRef](../../10-motion/01-kinematics-status/PosRef.md).

If the chosen source itself wraps under modulo ([ModRev](../04-modulo-mode/ModRev.md)), the firmware detects the wrap (a jump greater than half the source's modulo span) and compensates the tracking memories so the generated output stays continuous.

The numeric value to write for a given source is the keyword's command code; obtain it from PCSuite or the keyword reference rather than guessing.

## Examples

```text
AVEncSrc            ; query the configured virtual encoder source code
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncType](VEncType.md) — output signal format
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — scaling ratio numerator / denominator
- [Pos](../../10-motion/01-kinematics-status/Pos.md) / [PosRef](../../10-motion/01-kinematics-status/PosRef.md) — typical source variables
