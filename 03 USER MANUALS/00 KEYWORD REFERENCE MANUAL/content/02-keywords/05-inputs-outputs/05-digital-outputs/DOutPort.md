---
keyword: DOutPort
summary: Bit-packed manual state of the digital outputs (before DOutLog inversion).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 211
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutPort

Bit-packed manual state of the digital outputs (before DOutLog inversion).

## Overview

`DOutPort` holds the manual state of the digital outputs as a bitfield (0-based bit positions: bit 0 = output 1). Each bit: `1` = on, `0` = off. It is the value *before* any [DOutLog](DOutLog.md) inversion.

`DOutPort` is writable only when the output is under manual control — that is, [DOutSelect](DOutSelect.md)`[x] = 0` **and** [DOutMode](DOutMode.md)`[x] = 0`. It is not saved to flash, so manual states must be re-applied after power-up.

## Examples

`DOutPort = 6` (binary `…0110`) turns outputs 2 and 3 on, all others off.

## Notes

1. `DOutPort = DOutPort | Bitword` is the usual way to set specific bits, but it is **not atomic** (read–modify–write): another process writing `DOutPort` in between can be overwritten. Prefer the atomic [DOutPortSBit/CBit/TBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) operations.
2. Not saved to flash.
3. The final physical state may be inverted by [DOutLog](DOutLog.md).

## See also

- [DOutPortSBit-DOutPortCBit-DOutPortTBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) — atomic set/clear/toggle
- [DOutLog](DOutLog.md) — output logic inversion
- [DOutSelect](DOutSelect.md) / [DOutMode](DOutMode.md) — must both be 0 to write DOutPort
