---
keyword: VEncModRev
summary: Modulo span (counts per revolution) of the virtual-encoder source, so the generator stays continuous across source roll-over.
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
---
# VEncModRev

Modulo span (counts per revolution) of the virtual-encoder source, so the generator stays continuous across source roll-over.

## Overview

`VEncModRev` tells the virtual encoder how large the source signal's modulo span is, so that when the source ([VEncSrc](VEncSrc.md)) wraps from the top of its range back to zero (or vice-versa), the generated output does not jump. The virtual encoder is an encoder-**signal generator** (it emits a quadrature or pulse/direction signal that tracks a source variable), not a feedback input; see [VEncOn](VEncOn.md). `VEncModRev` exists purely to keep that generated signal continuous when the chosen source itself runs in modulo.

It is a per-axis parameter saved to flash, can be changed while the motor is on (but not in motion), and is `0` by default, which **disables** the wrap handling. The usable range is `0` to `2,000,000,000`.

## How it works

`VEncModRev` is the number of source counts in one full modulo cycle of the source — i.e. the source's counts-per-revolution. Set it to match the [ModRev](../04-modulo-mode/ModRev.md) span of whatever variable [VEncSrc](VEncSrc.md) points at.

Each control cycle the generator compares the new source value with the previous one:

- If `VEncModRev = 0`, no wrap handling is done; the source is assumed never to roll over.
- If `VEncModRev ≠ 0` and the source changes by more than **half** of `VEncModRev` in a single cycle, the change is treated as a roll-over (not a real jump). The generator shifts its internal tracking by one full span and steps the generated count [VEncValue](VEncValue.md) by the scaled equivalent of one span, so the emitted signal continues smoothly instead of producing a large burst of edges.

The scaled span is computed from `VEncModRev` together with the output scaling [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md), so the wrap compensation is applied in the same units as the generated output.

## Examples

```text
AVEncModRev=0            ; default: source never wraps, no roll-over handling
AVEncModRev=131072       ; source runs modulo 131072 counts/rev; keep output continuous on wrap
AVEncModRev               ; read the configured modulo span
```

## See also

- [VEncSrc](VEncSrc.md) — source variable whose modulo span this describes
- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncValue](VEncValue.md) — the generated output count that is kept continuous across wraps
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — source-to-output scaling ratio
- [ModRev](../04-modulo-mode/ModRev.md) — modulo span of the axis feedback (a typical source)
