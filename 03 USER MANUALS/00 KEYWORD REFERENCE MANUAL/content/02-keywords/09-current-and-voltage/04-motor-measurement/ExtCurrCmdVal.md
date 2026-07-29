---
keyword: ExtCurrCmdVal
summary: Read-only array reporting the actual DAC code sent to the digital-SPI external amplifier, per phase.
availability:
  standalone: []
  central-i:
  - v5
can_code: 868
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
  - -1
  - 65536
  default: 32768
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-07-30'
doc_revision: '2026.07'
---
# ExtCurrCmdVal

Read-only array reporting the actual DAC code sent to the digital-SPI external amplifier, per phase.

## Overview

`ExtCurrCmdVal` only carries a live value on an axis driven by the **digital-SPI external amplifier** ([AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`) — on any other `AmpType` it is unused. It is a read-only, per-phase array reporting the DAC code the controller is actually sending to the amplifier, in raw counts. The array is 1-indexed: `[1]` = Ia, `[2]` = Ib; index `0` is reserved and not used.

It is a diagnostic value, not a control: being read-only and not saved to flash, it can be read at any time and exists purely so an integrator can confirm what the controller sent, e.g. when the amplifier's own trim is suspect. Writing it is rejected with a read-only error.

## How it works

Each control cycle, for phase index `i`, the controller computes

```
codeBeforeMidCode = round( gain × (PhaseCurr[i] + ExtCurrCmdOfs[i]) )
ExtCurrCmdVal[i]  = codeBeforeMidCode + 32768                          ; saturated to 0…65535
```

where `gain = 32768 / AAmpFullScale` (counts/mA) and `32768` is the DAC's mid-code (0 mA at zero phase current and zero offset). See [ExtCurrCmdOfs](ExtCurrCmdOfs.md) for the full offset-before-gain derivation and a worked example.

`ExtCurrCmdVal` saturates: if the computed code would fall outside the DAC's 0–65535 range it is clamped to the nearest end, it does not wrap. The value is what is actually written to the amplifier's SPI/DAC register, so it reflects any clamping that occurred, even if the unclamped calculation would have gone further.

> Applies to Central-i v5 only, and only when the axis is configured for the digital-SPI amplifier ([AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`).

## Examples

```text
AExtCurrCmdVal[1]       ; read the DAC code currently sent for Ia
AExtCurrCmdVal[2]       ; read the DAC code currently sent for Ib
AExtCurrCmdVal[1]=100   ; rejected: ExtCurrCmdVal is read-only
```

## See also

- [ExtCurrCmdOfs](ExtCurrCmdOfs.md) — the per-phase mA offset that feeds into this code, with the full command chain and a worked example
- [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.md) — the gain applied between the offset and this code
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — selects the digital-SPI amplifier mode (8) this keyword applies to
- [ComtStatus](../../15-commutation/ComtStatus.md) — status `-17`, phasing refused on an axis with an external amplifier
