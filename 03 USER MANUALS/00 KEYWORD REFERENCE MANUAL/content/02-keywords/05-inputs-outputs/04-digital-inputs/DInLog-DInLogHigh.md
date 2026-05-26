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

$$
DInPort = DInPortBefore \oplus DInLog
$$
$$
DInPortHigh = DInPortHighBefore \oplus DInLogHigh
$$

**Example:** with `DInPortBefore = 15` (`…00001111`) and `DInLog = 6` (`…00000110`), the result is `DInPort = 9` (`…00001001`) — bits 1 and 2 are inverted (digital inputs 2 and 3).

## Notes

Typically used for limit switches for fail-safe reasons: configure so that a disconnected switch (input low) triggers a fault.

## See also

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — resulting input states
- [DInFilt](DInFilt.md) — debounce filter
- [DInMode](DInMode.md) — assign functions to inputs
