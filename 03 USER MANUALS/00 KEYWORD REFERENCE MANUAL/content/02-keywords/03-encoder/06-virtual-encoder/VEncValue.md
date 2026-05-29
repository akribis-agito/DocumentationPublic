---
keyword: VEncValue
summary: Read-only accumulated count emitted by the virtual encoder, tracking the scaled source signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 623
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncValue

Read-only accumulated count emitted by the virtual encoder, tracking the scaled source signal.

## Overview

`VEncValue` is the running count that the virtual encoder has emitted on its encoder-emulation output. The virtual encoder is an encoder-**signal generator**: when enabled with [VEncOn](VEncOn.md), it drives a quadrature or pulse/direction output that follows a selected source variable. `VEncValue` mirrors the number of edges generated so far, so it tracks the source ([VEncSrc](VEncSrc.md)) after the source-to-output scaling [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) is applied.

It is read-only, per-axis, and not saved to flash. It is **not** the axis's own feedback position ([Pos](../../10-motion/01-kinematics-status/Pos.md)) — it is the accounting of the generated output signal. It powers up at 0.

## How it works

Each control cycle, while [VEncOn](VEncOn.md) = 1, the generator:

1. Reads the source variable selected by [VEncSrc](VEncSrc.md) and scales it by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md).
2. Runs a tracking controller plus feed-forward and emits the appropriate number of output edges this cycle.
3. Adds those emitted edges to `VEncValue`.

When the virtual encoder is first turned on, `VEncValue` is initialised to the current scaled source value, so it starts aligned with the source rather than at an arbitrary offset. If the source wraps under modulo and [VEncModRev](VEncModRev.md) is set, `VEncValue` is stepped by one scaled span at the wrap so it stays continuous. Because the output is closed-loop tracked, `VEncValue` follows the scaled source with minimal lag rather than being a free-running counter.

## Examples

```text
AVEncValue           ; read the count emitted by the virtual encoder
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source variable the output tracks
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — source-to-output scaling ratio
- [VEncModRev](VEncModRev.md) — source modulo span used to keep `VEncValue` continuous
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — the axis's own feedback position (distinct from `VEncValue`)
