---
keyword: PDPos
summary: Read-only scaled pulse-and-direction counter, accumulated every controller cycle.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 4
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
# PDPos

Read-only scaled pulse-and-direction counter, accumulated every controller cycle.

## Overview

`PDPos` is the pulse-and-direction counter that accumulates the number of pulses detected in each controller cycle, multiplied by the scaling factor and corrected for sign. It is the core feedback value of pulse-and-direction (P/D) decoding: in direct P/D motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 3) the change in `PDPos` since the start of motion drives the position reference, and in indirect P/D motion (`MotionMode` = 4) it drives the target position.

The scaling factor is the ratio of [PDFact](PDFact.md) (numerator) to [PDFactDen](PDFactDen.md) (denominator); the accumulation sign is set by [PDEncDir](PDEncDir.md). The accumulation (integration) occurs at every controller cycle so that no pulse-and-direction signal is lost. `PDPos` can be re-zeroed or preset using [SetPDPos](SetPDPos.md).

## How it works

When queried over a communication channel, `PDPos` is represented in pulse-direction user units. The conversion from internal counts is set by [PDUsrUnits](PDUsrUnits.md).

## Examples

```text
PDPos?              ; read the current scaled P/D counter (pulse-direction units)
```

## See also

- [PDVel](PDVel.md) — rate of change of `PDPos`
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — scaling-factor numerator/denominator
- [PDEncDir](PDEncDir.md) — accumulation direction (sign)
- [SetPDPos](SetPDPos.md) — preset/re-zero the counter
- [PDUsrUnits](PDUsrUnits.md) — query unit conversion
