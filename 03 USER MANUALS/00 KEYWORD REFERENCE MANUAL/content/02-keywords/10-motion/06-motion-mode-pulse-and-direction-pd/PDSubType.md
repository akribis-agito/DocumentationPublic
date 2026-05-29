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

`PDSubType` selects how the controller interprets the two input lines, so that [PDPos](PDPos.md) accumulates correctly for the connected master. There are two formats: classic pulse-and-direction (one pulse line + one direction line) and A-quad-B incremental (two quadrature lines). It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

## How it works

`PDSubType` sets the input format the controller uses to decode the two input lines into the per-cycle pulse count (see [PDPos](PDPos.md)).

| Value | Input format | Description |
|---|---|---|
| 0 | **Pulse and Direction** (default) | One line carries step pulses, the other carries the direction level. Each pulse advances the counter; the direction line sets the sign. |
| 1 | **AqB Incremental** | Two 90°-out-of-phase quadrature channels (A and B), as from an incremental encoder. The decoder derives both count and direction from the phase relationship. |

The range is 0–1; no other formats are defined. The format is configured per axis. Whichever format is selected, both input lines are first cleaned by the per-axis hardware debounce set by [DInFilt](../../05-inputs-outputs/04-digital-inputs/DInFilt.md) — see *Input filtering and maximum rate* below. That debounce is the only setting that conditions the raw input edges; [PDFiltFact](PDFiltFact.md) (derived from [PDPosFilt](PDPosFilt.md)) is a separate, direct-mode low-pass applied later to the position reference and never touches the incoming edges.

### How each format is decoded

- **Pulse + direction (0):** the counter changes once on each **rising edge** of the (filtered) pulse line; the direction line is sampled and sets whether that change is +1 or -1. Only rising edges are counted.
- **A-quad-B (1):** the two channels are decoded by their phase relationship; **every** A/B transition advances the counter and the lead/lag order of A versus B sets the sign, so one quadrature cycle (one full line of the encoder) produces four counts.

### Input filtering and maximum rate

Both input lines pass through the same hardware debounce, whose strength is set per axis by [DInFilt](../../05-inputs-outputs/04-digital-inputs/DInFilt.md) (0-15). A level change on either line is accepted only after it has been held stable for `DInFilt + 1` consecutive filter-clock periods, so a larger `DInFilt` lengthens the settle time and lowers the highest pulse rate the input can resolve. The exact settle time and rate ceiling depend on the product's internal filter-clock rate; for headroom, keep the incoming pulse rate well below the point where each high/low half of a pulse is shorter than the debounce settle time, and use the lowest `DInFilt` that still rejects your noise.

## Examples

```text
APDSubType=0         ; pulse + direction input (default)
APDSubType=1         ; A-quad-B (quadrature) input
```

## See also

- [PDPos](PDPos.md) — counter populated according to the selected decode format
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — input scaling factor applied after decode
- [SetPDPos](SetPDPos.md) — preset/re-zero the P/D counter
