---
keyword: ForceInTTime
summary: Minimum dwell time within the settling window before force control is settled.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 733
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 163840
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceInTTime

Minimum dwell time within the settling window before force control is settled.

## Overview

`ForceInTTime` defines the minimum time, in milliseconds, that the force error ([ForceErr](ForceErr.md)) must continuously stay within the settling window ([ForceInTTol](ForceInTTol.md)) before the axis is considered settled in [ForceInTStat](ForceInTStat.md). It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2.

## How it works

The internal dwell counter is active only while [ForceInTStat](ForceInTStat.md) = 3. Each cycle the controller tests `|ForceErr| <= ForceInTTol`; if true it increments the counter, otherwise it re-zeroes it. Once the counter reaches `ForceInTTime` the axis is considered settled (`ForceInTStat` = 4) and the settling condition is no longer checked for that command entry.

A value of `0` means the axis is declared settled as soon as `ForceErr` first enters the window (no dwell required).

## Examples

```text
AForceInTTime=50     ; require 50 ms within the settling window
```

## See also

- [ForceInTTol](ForceInTTol.md) — the settling window
- [ForceInTStat](ForceInTStat.md) — in-target status driven by this timer
- [ForceErr](ForceErr.md) — error checked against the window
