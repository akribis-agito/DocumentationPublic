---
keyword: VEncModRev
summary: Modulo span (counts per revolution) used to compensate virtual-encoder source wraps.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 629
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 830
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# VEncModRev

Modulo span (counts per revolution) used to compensate virtual-encoder source wraps.

## Overview

`VEncModRev` supplies the span used to compensate a wrap of the source ([VEncSrc](VEncSrc.md)). The virtual encoder generates a quadrature or pulse/direction signal that tracks that source; see [VEncOn](VEncOn.md).

It is a per-axis parameter saved to flash, can be changed while the motor is on (but not in motion), and is `0` by default, which **disables** the wrap handling. The usable range is `0` to `2,000,000,000`.

## How it works

`VEncModRev` is the number of source counts in one full modulo cycle of the source — i.e. the source's counts-per-revolution. Set it to match the [ModRev](../04-modulo-mode/ModRev.md) span of whatever variable [VEncSrc](VEncSrc.md) points at.

Each control cycle the generator compares the new source value with the previous one:

- If `VEncModRev = 0`, no wrap handling is done; the source is assumed never to roll over.
- If `VEncModRev ≠ 0` and the source changes by more than **half** of `VEncModRev` in a single cycle, the generator compensates a roll-over by shifting its tracking memories and [VEncValue](VEncValue.md) by one scaled span.

In firmware containing [Firmware-Main #1103](https://github.com/akribis-agito/Firmware-Main/issues/1103), the source-step capacity check follows this compensation. If the compensated step exceeds one-sample capacity, tracking restarts at the new reference and that step is discarded. With the motor on, fault **1066** remains. See [VEncOn](VEncOn.md).

The scaled span is computed from `VEncModRev` together with the output scaling [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md), so the wrap compensation is applied in the same units as the generated output.

## Examples

```text
AVEncModRev=0            ; default: source never wraps, no roll-over handling
AVEncModRev=131072       ; compensate source wraps at 131072 counts/rev
AVEncModRev               ; read the configured modulo span
```

## See also

- [VEncSrc](VEncSrc.md) — source variable whose modulo span this describes
- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncValue](VEncValue.md) — the virtual-encoder tracking count
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — source-to-output scaling ratio
- [ModRev](../04-modulo-mode/ModRev.md) — modulo span of the axis feedback (a typical source)
