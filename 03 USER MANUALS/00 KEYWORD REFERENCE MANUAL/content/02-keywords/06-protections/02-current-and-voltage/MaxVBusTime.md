---
keyword: MaxVBusTime
summary: How long bus voltage may stay outside the MinVBus/MaxVBus limits before tripping.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 93
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
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVBusTime

How long bus voltage may stay outside the MinVBus/MaxVBus limits before tripping.

## Overview

`MaxVBusTime` is the time the bus voltage may remain above the [MaxVBus](MaxVBus.md) limit before the axis is disabled. It adds tolerance for brief transients; for a hard, instantaneous ceiling use [MaxVBusAbs](MaxVBusAbs.md).

## How it works

The firmware keeps an over-voltage timer (`glMaxVBusCounter`). On each periodic bus check, if `VBus ≥ MaxVBus` the timer is accumulated, otherwise it is reset to 0. When the timer reaches `MaxVBusTime` while still over the limit, the [MaxVBus](MaxVBus.md) trip fires ([ConFlt](../../07-status-and-faults/ConFlt.md) = `1008`). With the default `MaxVBusTime = 0` the over-voltage trip is effectively immediate on the next check.

> **Note:** the firmware uses this same counter mechanism only for the *over*-voltage ([MaxVBus](MaxVBus.md)) path. The under-voltage ([MinVBus](MinVBus.md)) trip and the absolute ceiling ([MaxVBusAbs](MaxVBusAbs.md)) act without this delay.

## Examples

```text
AMaxVBusTime=1000    ; allow brief over-voltage excursions before tripping
```

## See also

- [MaxVBus](MaxVBus.md) — the over-voltage limit this delay applies to
- [MinVBus](MinVBus.md) — under-voltage limit (no delay)
- [MaxVBusAbs](MaxVBusAbs.md) — instantaneous trip (no delay)
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1008 raised when the delay expires
