---
keyword: LAmpVBus
summary: Read-only bus-voltage measurements of the built-in linear amplifier (AmpType = 4).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 253
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 3
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
# LAmpVBus

Read-only bus-voltage measurements of the built-in linear amplifier (AmpType = 4).

## Overview

`LAmpVBus` reports the bus-voltage measurements of the built-in linear amplifier, in millivolts, as a read-only array. It is only used when [AmpType](../../02-motor-and-amplifier/AmpType.md) = 4 (a reserved setting). For the standard switching-amplifier bus voltage, see [VBus](VBus.md).

> **Note:** `AmpType` = 4 is a reserved setting; this reading applies only to products with a built-in linear amplifier.

## Examples

```text
ALAmpVBus[1]        ; read the first linear-amplifier bus voltage (mV)
```

## See also

- [VBus](VBus.md) — switching-amplifier DC bus voltage reading
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — amplifier type selection
