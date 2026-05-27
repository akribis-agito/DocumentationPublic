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

`MaxVBusTime` is the maximum time the bus voltage may remain outside the [MinVBus](MinVBus.md) / [MaxVBus](MaxVBus.md) limits before the axis is disabled. It adds tolerance for brief transients; for a hard, instantaneous ceiling use [MaxVBusAbs](MaxVBusAbs.md).

## Examples

```text
AMaxVBusTime=1000    ; allow brief out-of-range excursions before tripping
```

## See also

- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — the limits this delay applies to
- [MaxVBusAbs](MaxVBusAbs.md) — instantaneous trip (no delay)
