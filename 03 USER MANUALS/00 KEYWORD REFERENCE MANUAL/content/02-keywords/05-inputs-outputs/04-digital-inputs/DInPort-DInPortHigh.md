---
summary: Bit-packed state of the digital inputs after debounce and logic inversion (DInPort = inputs 1–32, DInPortHigh = 33–64).
---
# DInPort / DInPortHigh

Bit-packed state of the digital inputs after debounce and logic inversion.

## Overview

`DInPort` reflects the state of digital inputs 1–32; `DInPortHigh` covers inputs 33–64 on products with more than 32 inputs. Each input is one **bit** (0-based bit position: bit 0 = input 1), and the value shown is after the [DInFilt](DInFilt.md) debounce and any [DInLog](DInLog-DInLogHigh.md) inversion. Both are read-only and not saved to flash. See the [digital-input signal path](00-overview.md).

| Bit value | State |
|-----------|-------|
| 0 | Off |
| 1 | On |

## How it works

Every control cycle the debounced input word(s) are read from hardware and the [DInLog](DInLog-DInLogHigh.md) inversion mask is XORed in before the result is stored, so what you read already reflects both the debounce and the polarity setting:

$$
\text{DInPort} = (\text{debounced inputs}) \oplus \text{DInLog}
$$
$$
\text{DInPortHigh} = (\text{debounced inputs 33–64}) \oplus \text{DInLogHigh}
$$

The previous cycle's value is retained before the update, which is how the function dispatch (see [DInMode](DInMode.md)) detects rising and falling edges. On a Central-i master the words instead come from the remote unit's synchronized I/O mirror, but the XOR-with-`DInLog` step is identical.

`DInPort` is refreshed every control cycle at the controller's loop rate; the underlying raw signal is sampled and debounced far faster in hardware (see [DInFilt](DInFilt.md)).

## Examples

```text
ADInPort              ; read inputs 1–32 as a bitfield
ADInPortHigh          ; read inputs 33–64
```

If `DInPortHigh = 18` (binary `…0001 0010`), bits 1 and 4 are set — so digital inputs **34** and **37** are on.

## Notes

For a bi-directional I/O configured as an output (see [BiDirConfig](../01-general-keywords/BiDirConfig.md)), `DInPort`/`DInPortHigh` can be read back to check the output's state.

## See also

- [DInLog-DInLogHigh](DInLog-DInLogHigh.md) — per-input logic inversion
- [DInFilt](DInFilt.md) — debounce filter
- [DInMode](DInMode.md) — assign functions to inputs
