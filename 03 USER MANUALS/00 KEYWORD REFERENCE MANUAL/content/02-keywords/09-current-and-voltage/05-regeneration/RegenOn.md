---
keyword: RegenOn
summary: DC bus-voltage threshold (mV) above which the regeneration resistor is activated.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 95
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
# RegenOn

DC bus-voltage threshold (mV) above which the regeneration resistor is activated.

## Overview

`RegenOn` sets the DC bus-voltage threshold above which the regeneration (braking-resistor) circuit is activated. When the bus voltage [VBus](../01-system-variables/VBus.md) rises above this level during deceleration, the controller switches on the regen resistor to dissipate the excess energy. Setting `RegenOn` higher than [RegenOff](RegenOff.md) provides hysteresis to prevent rapid switching. It is saved to flash and can be changed at any time.

## Examples

```text
ARegenOn=80000       ; activate regen above 80 V (mV)
```

## See also

- [RegenOff](RegenOff.md) — deactivation threshold (provides hysteresis)
- [RegenCurr](RegenCurr.md) — measured regen-resistor current
- [RegenUsed](RegenUsed.md) — external vs internal regen resistor
- [VBus](../01-system-variables/VBus.md) — bus voltage compared against this threshold
