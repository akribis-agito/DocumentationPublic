---
keyword: DOutLog
summary: Per-output logic inversion (XOR) applied to the final digital-output state.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 212
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutLog

Per-output logic inversion (XOR) applied to the final digital-output state.

## Overview

`DOutLog` inverts the logic of selected digital outputs, as a bitfield (0-based: bit 0 = output 1). Each bit: `0` = default, `1` = inverted. The inversion is applied after [DOutPort](DOutPort.md) (and after any hardware/software function), producing the internal `DOutPortFinal` that drives the physical outputs.

## How it works

$$
DOutPortFinal = DOutPort \oplus DOutLog
$$

**Example:** with `DOutPort = 7` (`…0111`) and `DOutLog = 3` (`…0011`), `DOutPortFinal = 4` (`…0100`) — bits 0 and 1 (outputs 1 and 2) are inverted.

## Notes

`DOutLog` also applies to outputs assigned a hardware or software function, not just manual outputs.

## See also

- [DOutPort](DOutPort.md) — pre-inversion output state
- [DOutType](DOutType.md) — sink/source mode
