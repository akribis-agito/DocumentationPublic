---
keyword: PDVel
summary: Read-only rate of change of the scaled P/D counter PDPos, in P/D units per second.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 7
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: pd_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDVel

Read-only rate of change of the scaled P/D counter PDPos, in P/D units per second.

## Overview

`PDVel` is the rate of change of the scaled pulse-and-direction counter [PDPos](PDPos.md), expressed in pulse-direction units per second. It reports how fast the decoded P/D command is moving and is useful for monitoring the velocity of an incoming pulse-and-direction stream during direct ([MotionMode](../02-motion-configuration/MotionMode.md) = 3) or indirect (`MotionMode` = 4) P/D motion.

## How it works

`PDVel` is not differentiated from `PDPos` after the fact; it is taken directly from the **per-cycle scaled change** computed during P/D decoding. That change already carries the [PDFact](PDFact.md)/[PDFactDen](PDFactDen.md) scaling (including the sign of `PDFact`), the natural direction of the incoming pulse/direction stream, and the carried-forward fractional remainder, so `PDVel` matches `PDPos` in scaling and in stream direction. It does **not**, however, reflect the [PDEncDir](PDEncDir.md) inversion, which is applied to the `PDPos` accumulator only. It is the change per controller cycle expressed as a velocity.

In direct mode the velocity also feeds direction-dependent decisions (for example limit-switch handling and friction-compensation sign), so `PDVel` reflects the instantaneous P/D command rate.

Numerically, `PDVel` is the per-cycle change in `PDPos` multiplied by the fixed sample rate of **16,384 Hz** (the scaled change is taken over one ~61 us cycle and expressed per second). Because of this, when the incoming pulse rate is low you may see `PDVel` step between discrete values from one cycle to the next — for example, a steady one pulse per cycle (with `PDFact/PDFactDen = 1`) reads as about 16,384 units/s — rather than varying smoothly. The controller carries the fractional part of the scaled change forward between cycles, so over time `PDVel` resolves finer gradations than a single per-cycle step and tracks the true average rate.

Like `PDPos`, `PDVel` is an internal-count value converted to pulse-direction user units when queried over a communication channel — see [PDUsrUnits](PDUsrUnits.md).

## Examples

```text
APDVel              ; read the current P/D command velocity (pulse-direction units/s)
```

## See also

- [PDPos](PDPos.md) — the counter whose per-cycle delta `PDVel` reports
- [PDUsrUnits](PDUsrUnits.md) — query unit conversion
- [PDEncDir](PDEncDir.md) — inverts `PDPos` accumulation only; does not affect `PDVel`
