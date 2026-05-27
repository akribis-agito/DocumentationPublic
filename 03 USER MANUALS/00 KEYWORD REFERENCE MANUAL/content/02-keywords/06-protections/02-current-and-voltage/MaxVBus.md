---
keyword: MaxVBus
summary: Maximum allowed bus voltage; sustained excess disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 92
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVBus

Maximum allowed bus voltage; sustained excess disables the axis.

## Overview

`MaxVBus` is the maximum allowed bus voltage, in mV. If the actual bus voltage exceeds this limit for longer than [MaxVBusTime](MaxVBusTime.md), the axis is disabled and an error code is reported to the fault register `ConFlt`. For an instantaneous (no delay) over-voltage trip, see [MaxVBusAbs](MaxVBusAbs.md).

## Examples

```text
AMaxVBus=80000       ; 80 V maximum bus voltage (mV)
```

## See also

- [MinVBus](MinVBus.md) — minimum bus voltage
- [MaxVBusTime](MaxVBusTime.md) — out-of-range time before tripping
- [MaxVBusAbs](MaxVBusAbs.md) — instantaneous over-voltage trip
