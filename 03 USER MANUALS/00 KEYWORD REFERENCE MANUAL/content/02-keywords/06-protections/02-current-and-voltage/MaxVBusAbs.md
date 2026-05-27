---
keyword: MaxVBusAbs
summary: Absolute bus-voltage ceiling; exceeding it disables the axis instantly.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 94
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
# MaxVBusAbs

Absolute bus-voltage ceiling; exceeding it disables the axis instantly.

## Overview

`MaxVBusAbs` is the maximum allowable absolute bus voltage. If the bus voltage exceeds `MaxVBusAbs`, the axis is **instantaneously** disabled and an error is reported to the fault register `ConFlt`. This is the no-delay counterpart to [MaxVBus](MaxVBus.md), which tolerates excess for up to [MaxVBusTime](MaxVBusTime.md).

## Examples

```text
AMaxVBusAbs=90000    ; instantaneous over-voltage ceiling (mV)
```

## See also

- [MaxVBus](MaxVBus.md) — time-delayed over-voltage limit
- [MaxVBusTime](MaxVBusTime.md) — delay used by MaxVBus / MinVBus
