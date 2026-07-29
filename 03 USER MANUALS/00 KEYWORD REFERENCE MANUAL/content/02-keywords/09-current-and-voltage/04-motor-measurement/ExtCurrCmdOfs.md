---
keyword: ExtCurrCmdOfs
summary: Per-phase offset, in mA, added to the phase current command before it is scaled onto the digital-SPI amplifier's DAC code.
availability:
  standalone: []
  central-i:
  - v5
can_code: 867
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -4000.0
  - 4000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-07-30'
doc_revision: '2026.07'
---
# ExtCurrCmdOfs

Per-phase offset, in mA, added to the phase current command before it is scaled onto the digital-SPI amplifier's DAC code.

## Overview

`ExtCurrCmdOfs` only matters on an axis driven by the **digital-SPI external amplifier** ([AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`) — on any other `AmpType`, including the built-in PWM stage, it has no effect. It is a per-phase offset, in milliamps, added to the phase current command for that external amplifier. The array is 1-indexed: `[1]` = Ia, `[2]` = Ib; index `0` is reserved and not used.

It is a per-axis parameter saved to flash. The value is a floating-point offset with a usable range of -4000.0 to 4000.0 mA and a default of 0. Use it to null a per-channel zero-current bias in the external amplifier's own analog/DAC stage — the trim a technician would otherwise have to dial in on the amplifier itself.

## How it works

The offset is added to the phase current command **before** the digital-SPI gain is applied — not to the resulting DAC code afterwards. That gain is set by [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.md) (`gain = 32768 / AAmpFullScale`, in counts per mA; see that page for the digital-SPI mode's derivation). Each control cycle, for phase index `i`:

```
codeBeforeMidCode = round( gain × (PhaseCurr[i] + ExtCurrCmdOfs[i]) )
ExtCurrCmdVal[i]  = codeBeforeMidCode + 32768                          ; saturated to 0…65535
```

where `32768` is the DAC's mid-code, representing 0 mA. The resulting code is reported by [ExtCurrCmdVal](ExtCurrCmdVal.md), the value actually sent to the amplifier.

![External-amplifier DAC command chain, per phase: the phase current command in mA has ExtCurrCmdOfs added to it in mA, then the sum is multiplied by the gain 32768 over AAmpFullScale in counts per mA, then 32768 (the DAC mid-code for zero current) is added, then the result is saturated to 0 through 65535. The final value is ExtCurrCmdVal, the DAC code sent to the amplifier. The offset is applied before the gain, in the same mA domain as the phase current, not after the gain as a raw count.](extcurrcmd-dac-chain.svg)

Because the offset is applied in the mA domain, its effect on the DAC code scales with the axis's gain. For example, with `AAmpFullScale` giving a gain of 8.0 counts/mA and a phase current command of 1000 mA:

- `ExtCurrCmdOfs[1] = 0`: code = round(8.0 × 1000) + 32768 = 40768
- `ExtCurrCmdOfs[1] = 250`: code = round(8.0 × (1000 + 250)) + 32768 = 42768

250 mA of offset moves the DAC code by exactly 2000 counts (250 × 8.0). This is the key difference from a raw DAC-count offset applied after the gain: here the same `ExtCurrCmdOfs` value shifts the code by a different amount on every axis, in proportion to that axis's `AAmpFullScale`, which is what makes it tunable in physical current units instead of in counts that depend on the gain setting.

> Applies to Central-i v5 only, and only when the axis is configured for the digital-SPI amplifier ([AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`).

## Examples

```text
AExtCurrCmdOfs[1]=250     ; add 250 mA to the Ia command before the gain
AExtCurrCmdOfs[2]=-100    ; add -100 mA to the Ib command before the gain
AExtCurrCmdOfs[1]         ; read the configured Ia offset
```

## See also

- [ExtCurrCmdVal](ExtCurrCmdVal.md) — the resulting DAC code this offset feeds into
- [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.md) — the gain applied after this offset
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — selects the digital-SPI amplifier mode (8) this keyword applies to
- [ExtCurrFBSca](ExtCurrFBSca.md) — scaling for the matching external current-feedback path
- [ComtStatus](../../15-commutation/ComtStatus.md) — status `-17`, phasing refused on an axis with an external amplifier
