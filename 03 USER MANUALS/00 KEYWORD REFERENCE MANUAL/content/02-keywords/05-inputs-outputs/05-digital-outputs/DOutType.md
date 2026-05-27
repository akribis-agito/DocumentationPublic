---
keyword: DOutType
summary: Per-output sink/source mode for single-ended digital outputs (bitfield).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 209
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
# DOutType

Per-output sink/source mode for single-ended digital outputs (bitfield).

## Overview

`DOutType` configures each digital output for sink or source mode, as a bitfield (0-based: bit 0 = output 1). Each bit: `0` = sink, `1` = source. It applies only to single-ended (open-collector) outputs that have a configurable sink/source stage — see the individual product manual. Differential outputs and outputs without a configurable stage ignore their `DOutType` bit.

| Bit value | Mode |
|-----------|------|
| 0 | Sink |
| 1 | Source |

## How it works

`DOutType` decides which physical driver carries each output. The control interrupt first builds the final output word (`DOutPort XOR DOutLog`), then routes only the open-collector bits by type:

- **Sink driver** gets the bits where `DOutType = 0`: `(~DOutType) & DOutPortFinal` (masked to the open-collector outputs).
- **Source driver** gets the bits where `DOutType = 1`: `DOutType & DOutPortFinal` (same mask).

So an output bit only drives current through the driver its type selects; the other driver sees `0` for that bit. When you change `DOutType`, the firmware also writes the FPGA source-control register (on a standalone controller) or sends the new type word to the remote unit (on central-i) so the hardware stage matches immediately.

`DOutType` is the same setting shown as sink/source selection on the single-ended digital-output signal path in the [digital-outputs overview](00-overview.md).

## Examples

```text
ADOutType=9          ; binary …1001 — outputs 1 and 4 source mode; rest sink
ADOutType            ; read the present sink/source configuration
```

## See also

- [DOutPort](DOutPort.md) / [DOutLog](DOutLog.md) — produce the word that is split by type
- [DOutSelect](DOutSelect.md) / [DOutMode](DOutMode.md) — output function assignment
