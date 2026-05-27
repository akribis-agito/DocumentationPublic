---
keyword: VBus
summary: Read-only amplifier DC bus voltage measurement, in millivolts.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 36
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VBus

Read-only amplifier DC bus voltage measurement, in millivolts.

## Overview

`VBus` reports the amplifier DC bus voltage measurement, in millivolts. It is a read-only status value that reflects the supply voltage available to the power stage. The same measurement is used by the bus-voltage protection, so a low or high reading here corresponds directly to the limits set by [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) and [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md). It is also the bus voltage referenced by the regeneration thresholds [RegenOn](../05-regeneration/RegenOn.md) and [RegenOff](../05-regeneration/RegenOff.md).

## Examples

```text
AVBus               ; read the present bus voltage (mV)
```

## See also

- [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) — maximum bus-voltage protection limit
- [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) — minimum bus-voltage protection limit
- [VLogic](VLogic.md) — logic-supply voltage reading
- [DCDC](DCDC.md) — internal logic-rail measurements
