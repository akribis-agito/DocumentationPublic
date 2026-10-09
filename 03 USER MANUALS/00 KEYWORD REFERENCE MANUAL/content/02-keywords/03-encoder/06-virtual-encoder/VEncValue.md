---
keyword: VEncValue
summary: Read-only virtual-encoder tracking count in the scaled source reference frame.
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# VEncValue

Read-only virtual-encoder tracking count in the scaled source reference frame.

## Overview

`VEncValue` is the virtual encoder's internal tracking count. It includes output increments, reference initialization and modulo adjustments. With [VEncOn](VEncOn.md) enabled, the generator drives a quadrature or pulse/direction output that follows [VEncSrc](VEncSrc.md) scaled by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md).

It is read-only, per-axis, and not saved to flash. It is **not** the axis's own feedback position ([Pos](../../10-motion/01-kinematics-status/Pos.md)) — it is the accounting of the generated output signal. It powers up at 0.

## How it works

Each control cycle, while [VEncOn](VEncOn.md) = 1, the generator:

1. Reads the source variable selected by [VEncSrc](VEncSrc.md) and scales it by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md).
2. Runs a tracking controller plus feed-forward and emits the appropriate number of output edges this cycle.
3. Updates `VEncValue` from its tracked output increments.

When the virtual encoder is first turned on, `VEncValue` is initialized to the current scaled source value. A detected wrap under [VEncModRev](VEncModRev.md) adjusts it by one scaled span.

In firmware containing [Firmware-Main #1103](https://github.com/akribis-agito/Firmware-Main/issues/1103), source/scale writes and source steps above one-sample capacity also reset the tracking reference. The capacity check follows modulo compensation. A reset can change `VEncValue` without emitting the corresponding edges. See [VEncOn](VEncOn.md) for subsequent tracking and retained motor-on protection.

## Examples

```text
AVEncValue           ; read the virtual-encoder tracking count
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source variable the output tracks
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — source-to-output scaling ratio
- [VEncModRev](VEncModRev.md) — source modulo span used for wrap compensation
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — the axis's own feedback position (distinct from `VEncValue`)
