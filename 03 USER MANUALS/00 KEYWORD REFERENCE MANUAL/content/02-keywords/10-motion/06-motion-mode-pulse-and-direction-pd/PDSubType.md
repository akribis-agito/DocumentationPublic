---
keyword: PDSubType
summary: Selects the pulse-and-direction input signal format (e.g. step/direction vs. CW/CCW).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 421
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDSubType

Selects the pulse-and-direction input signal format (e.g. step/direction vs. CW/CCW).

## Overview

`PDSubType` selects how the FPGA decoder interprets the two input lines, so that [PDPos](PDPos.md) accumulates correctly for the connected master. There are two formats: classic pulse-and-direction (one pulse line + one direction line) and A-quad-B incremental (two quadrature lines). It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## How it works

The decode happens in the FPGA, not in software. When `PDSubType` is written, the special function `SpPDSubType` (`SpecialFuncs.c:3959`) writes the per-axis bits into the FPGA's pulse-and-direction settings register (`FPGA_PULSE_AND_DIRECTION_SETTINGS`, `0x0012`); the firmware then just reads the resulting signed pulse delta each cycle (see [PDPos](PDPos.md)).

| Value | Input format | Description |
|---|---|---|
| 0 | **Pulse and Direction** (default) | One line carries step pulses, the other carries the direction level. Each pulse advances the counter; the direction line sets the sign. |
| 1 | **AqB Incremental** | Two 90°-out-of-phase quadrature channels (A and B), as from an incremental encoder. The decoder derives both count and direction from the phase relationship. |

The range is 0–1; no other formats are defined. On multi-axis controllers each axis's bit is packed into the same register (axis A in bit 0, B in bit 1, C in bit 2), so `SpPDSubType` rewrites the combined word whenever any axis changes (`SpecialFuncs.c:3965`–`3972`).

## Examples

```text
APDSubType=0         ; pulse + direction input (default)
APDSubType=1         ; A-quad-B (quadrature) input
```

## See also

- [PDPos](PDPos.md) — counter populated according to the selected decode format
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — input scaling factor applied after decode
- [SetPDPos](SetPDPos.md) — preset/re-zero the P/D counter
