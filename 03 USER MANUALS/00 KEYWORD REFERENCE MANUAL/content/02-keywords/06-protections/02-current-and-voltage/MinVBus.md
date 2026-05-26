---
keyword: MinVBus
summary: Minimum allowed bus voltage; sustained shortfall disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 89
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
  - 11000
  - 90000
  default: 11000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MinVBus

Minimum allowed bus voltage; sustained shortfall disables the axis.

## Overview

`MinVBus` is the minimum allowed bus voltage, in mV. If the actual bus voltage stays below this limit for longer than [MaxVBusTime](MaxVBusTime.md), the axis is disabled and an error code is reported to the fault register `ConFlt`. This guards against brown-out / supply-loss conditions.

## Examples

```text
MinVBus=18000       ; 18 V minimum bus voltage (mV)
```

## See also

- [MaxVBus](MaxVBus.md) — maximum bus voltage
- [MaxVBusTime](MaxVBusTime.md) — out-of-range time before tripping
