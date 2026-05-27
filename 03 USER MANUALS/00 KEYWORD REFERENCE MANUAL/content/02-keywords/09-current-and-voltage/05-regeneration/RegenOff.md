---
keyword: RegenOff
summary: DC bus-voltage threshold (mV) below which the regeneration resistor is deactivated.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 96
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
# RegenOff

DC bus-voltage threshold (mV) below which the regeneration resistor is deactivated.

## Overview

`RegenOff` sets the DC bus-voltage threshold below which the regeneration circuit is deactivated. Once the bus voltage [VBus](../01-system-variables/VBus.md) drops below this level, the controller switches off the regen resistor. Setting `RegenOff` lower than [RegenOn](RegenOn.md) provides hysteresis to prevent rapid switching. It is saved to flash and can be changed at any time.

## Examples

```text
ARegenOff=75000      ; deactivate regen below 75 V (mV)
```

## See also

- [RegenOn](RegenOn.md) — activation threshold (provides hysteresis)
- [RegenCurr](RegenCurr.md) — measured regen-resistor current
- [RegenUsed](RegenUsed.md) — external vs internal regen resistor
- [VBus](../01-system-variables/VBus.md) — bus voltage compared against this threshold
