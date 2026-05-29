---
summary: Per-input logic inversion (XOR) for the digital inputs (DInLog = inputs 1–32, DInLogHigh = 33–64).
---
# DInLog / DInLogHigh

Per-input logic inversion (XOR) for the digital inputs.

## Overview

`DInLog` inverts the logic of selected digital inputs 1–32; `DInLogHigh` does the same for inputs 33–64. Each input is one bit; a set bit inverts that input via an XOR applied before the state is stored in [DInPort](DInPort-DInPortHigh.md).

| Bit value | Logic |
|-----------|-------|
| 0 | Default |
| 1 | Inverted |

## How it works

The inversion is applied each control cycle at the moment the raw input word is read from hardware — the debounced hardware word is XORed with the `DInLog` mask before it is stored, so [DInPort](DInPort-DInPortHigh.md) (and every function that reads it) already sees the inverted polarity:

$$
\text{DInPort} = (\text{debounced inputs}) \oplus \text{DInLog}
$$
$$
\text{DInPortHigh} = (\text{debounced inputs 33–64}) \oplus \text{DInLogHigh}
$$

**Example:** with the debounced inputs reading `15` (`…00001111`) and `DInLog = 6` (`…00000110`), the result is `DInPort = 9` (`…00001001`) — bits 1 and 2 are inverted (digital inputs 2 and 3).

Because the inversion happens before edge detection and the [DInMode](DInMode.md) function dispatch, inverting a limit-switch or fault input flips the active sense of that function too. On a Central-i master the valid range of each `DInLog` is constrained to the bits corresponding to the remote device's actual digital-input count, so only those bits are writable.

## Notes

Typically used for limit switches for fail-safe reasons: configure so that a disconnected switch (input low) triggers a fault.

### Edge cases

- **Central-i remote bit count** — only bits corresponding to the remote's actual digital-input count are writable; extra bits are masked off.
- **`DInLogHigh` on small platforms** — products without inputs 33–64 ignore `DInLogHigh`; the keyword exists for software portability.
- **Applied before edge detection** — inverting a limit / fault input flips the active sense of the matching [DInMode](DInMode.md) function.
- **Motor on/off** — independent of `MotorOn`; inversion runs every cycle.
- **Save** — flash-saveable; persistent across reboots.

## See also

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — resulting input states (after this XOR)
- [DInFilt](DInFilt.md) — debounce filter (applied in hardware, before this inversion)
- [DInMode](DInMode.md) — assign functions to inputs (which see the inverted polarity)
