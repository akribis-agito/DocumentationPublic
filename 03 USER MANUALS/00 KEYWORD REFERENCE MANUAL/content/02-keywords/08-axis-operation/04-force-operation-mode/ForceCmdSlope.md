---
keyword: ForceCmdSlope
summary: Ramp rate (unit/s) toward each force-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 569
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdSlope

Ramp rate (unit/s) toward each force-command table entry.

## Overview

`ForceCmdSlope` defines the slope for the transition from the present raw [ForceRef](ForceRef.md) value to the active [ForceCmdVal](ForceCmdVal.md) entry, in units per second. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2. The holding timer [ForceCmdCntr](ForceCmdCntr.md) only begins counting from 0 once the ramp completes. Each table entry has its own slope (array indexed 1 to 20, paired with the [ForceCmdVal](ForceCmdVal.md) of the same index).

## How it works

While the raw reference has not yet reached the target value, the generator steps it toward the target by `ForceCmdSlope[ForceCmdIndex] * Ts` each control cycle, where `Ts` is the cycle period (`AG300_CTL01ControlLoops.c:1332`):

$$
\Delta ForceRef\ \lbrack unit\rbrack\  = \ ForceCmdSlope\ \times\ T_{s}
$$

During the ramp the firmware sets [ForceInTStat](ForceInTStat.md) to 2 (ramping) and holds [ForceCmdCntr](ForceCmdCntr.md) at 0 (`AG300_CTL01ControlLoops.c:1336`). The step is clamped so the reference does not overshoot the target [ForceCmdVal](ForceCmdVal.md). Only when the raw reference exactly equals the target does the holding timer start and the in-target dwell begin. Because `ForceCmdSlope` has a minimum value of 1, the ramp is always finite (a value cannot be applied as an instantaneous step).

## Examples

```text
AForceCmdSlope[3]=700 ; ramp into entry 3 at 700 units/s
```

## See also

- [ForceCmdVal](ForceCmdVal.md) — target force values
- [ForceCmdHTime](ForceCmdHTime.md) — holding times per entry
- [ForceCmdCntr](ForceCmdCntr.md) — timer that starts after the ramp
