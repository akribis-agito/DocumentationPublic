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

`PDVel` is not differentiated from `PDPos` after the fact; it is taken directly from the **per-cycle scaled delta** computed during P/D decoding. The controller derives `PDVel` from that cycle's scaled 32.32 delta by shifting it down into the reference rate (a right shift of `32 − 14`). Because the delta already carries the [PDFact](PDFact.md)/[PDFactDen](PDFactDen.md) scaling, the [PDEncDir](PDEncDir.md) sign, and the carried-forward fractional remainder, `PDVel` reflects the same scaling and direction as `PDPos`. It is the change per control cycle expressed at the reference's 50.14 rate, i.e. an internal velocity in counts per second.

`PDVel` is used internally as well as for monitoring: in direct mode the profiler copies it into its velocity estimate so direction-dependent decisions (e.g. limit-switch handling, friction-compensation sign) work, and the by-pulses gain-scheduling mode switches control sets whenever `PDVel` is non-zero.

Like `PDPos`, `PDVel` is an internal-count value converted to pulse-direction user units when queried over a communication channel — see [PDUsrUnits](PDUsrUnits.md).

## Examples

```text
APDVel              ; read the current P/D command velocity (pulse-direction units/s)
```

## See also

- [PDPos](PDPos.md) — the counter whose per-cycle delta `PDVel` reports
- [PDUsrUnits](PDUsrUnits.md) — query unit conversion
- [PDEncDir](PDEncDir.md) — sets the sign that `PDVel` inherits
