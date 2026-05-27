---
keyword: PDVel
summary: Read-only rate of change of the scaled P/D counter PDPos, in P/D units per second.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

Like `PDPos`, `PDVel` is an internal-count value that is converted to pulse-direction user units when queried over a communication channel. See [PDUsrUnits](PDUsrUnits.md) for the query conversion.

## Examples

```text
APDVel              ; read the current P/D command velocity (pulse-direction units/s)
```

## See also

- [PDPos](PDPos.md) — the counter whose derivative `PDVel` reports
- [PDUsrUnits](PDUsrUnits.md) — query unit conversion
