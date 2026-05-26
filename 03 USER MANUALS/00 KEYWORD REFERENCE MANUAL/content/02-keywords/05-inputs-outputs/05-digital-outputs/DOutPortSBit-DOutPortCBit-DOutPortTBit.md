---
summary: Atomic set / clear / toggle of individual DOutPort bits, one output per array index.
---
# DOutPortSBit / DOutPortCBit / DOutPortTBit

Atomic set / clear / toggle of individual DOutPort bits.

## Overview

These three array keywords change individual bits of [DOutPort](DOutPort.md) atomically — avoiding the read-modify-write race of writing `DOutPort` directly:

- `DOutPortSBit[i]` — **sets** the bit for output *i*
- `DOutPortCBit[i]` — **clears** the bit for output *i*
- `DOutPortTBit[i]` — **toggles** the bit for output *i*

The array index is the output number (1-based: index 1 → DOutPort bit 0 → output 1).

| Index | Changes DOutPort bit # | Output |
|-------|------------------------|--------|
| 1 | 0 | Output 1 |
| 2 | 1 | Output 2 |
| 3 | 2 | Output 3 |
| … | … | … |

## Examples

Starting from `DOutPort = 6` (`0b0110`):

| Command | Operation | Result |
|---------|-----------|--------|
| `DOutPortSBit[4]` | set bit 3 | 14 (`0b1110`) |
| `DOutPortCBit[2]` | clear bit 1 | 4 (`0b0100`) |
| `DOutPortTBit[3]` | toggle bit 2 | 2 (`0b0010`) |

## See also

- [DOutPort](DOutPort.md) — the underlying output bitfield
- [DOutLog](DOutLog.md) — output logic inversion
