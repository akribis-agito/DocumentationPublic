---
keyword: DOutLog
summary: Per-output logic inversion (XOR) applied to the final digital-output state.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`DOutLog` inverts the logic of selected digital outputs, as a bitfield (0-based: bit 0 = output 1). Each bit: `0` = default, `1` = inverted. The inversion is applied after [DOutPort](DOutPort.md) (and after any hardware/software function), producing the final output word that drives the physical outputs.

## How it works

Every control cycle, just before writing the physical pins, the output word is XORed with `DOutLog`:

$$
\text{Final output word} = \text{DOutPort} \oplus \text{DOutLog}
$$

A `1` bit in `DOutLog` inverts that output; a `0` bit passes it through unchanged. The result is what the hardware discrete-output stage receives. On products with selectable sink/source pins, the final word is computed first, then split by [DOutType](DOutType.md) into the sink and source drivers — so polarity is applied **before** the sink/source routing.

**Example:** with `DOutPort = 7` (`…0111`) and `DOutLog = 3` (`…0011`), the final output word is `4` (`…0100`) — bits 0 and 1 (outputs 1 and 2) are inverted.

## Notes

1. `DOutLog` is applied to the final word, so it inverts outputs regardless of how the underlying `DOutPort` bit was set — manual writes, [DOutPortSBit/CBit/TBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md), or a [DOutMode](DOutMode.md) software function all see the same inversion.
2. It does not affect outputs routed to a *hardware* function via [DOutSelect](DOutSelect.md) (events, P/D, UserPWM), which bypass the `DOutPort`/`DOutLog` word in hardware.
3. Saved to flash, so polarity persists across power cycles.

### Edge cases

- **Hardware-function outputs** — bits where [DOutSelect](DOutSelect.md) is non-zero **bypass** `DOutLog`; polarity for those pins is set in the hardware function itself.
- **Bits beyond the product's output count** — stored in the 32-bit word but have no pin to affect.
- **Motor on/off** — independent of `MotorOn`; inversion runs every cycle.
- **Mode independence** — independent of [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md).
- **Read-back** — reads the inversion mask; combine with `DOutPort` to compute the final pin level.
- **Save** — flash-saveable; reapplied at boot.

## See also

- [DOutPort](DOutPort.md) — pre-inversion output state (the operand XORed with DOutLog)
- [DOutType](DOutType.md) — sink/source routing applied after the XOR
- [DOutMode](DOutMode.md) — software functions also pass through this inversion
