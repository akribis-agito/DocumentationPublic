---
keyword: RegenCurr
summary: Read-only current flowing through the regeneration resistor.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 349
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RegenCurr

Read-only current flowing through the regeneration resistor.

## Overview

`RegenCurr` is a read-only status value that reports the current flowing through the regeneration resistor. It lets you monitor the power being dissipated by the regen circuit during braking, when the bus voltage rises above [RegenOn](RegenOn.md). It is not saved to flash.

## Examples

```text
ARegenCurr          ; read the present regen-resistor current
```

## See also

- [RegenOn](RegenOn.md), [RegenOff](RegenOff.md) — regen activation/deactivation thresholds
- [RegenUsed](RegenUsed.md) — external vs internal regen resistor
