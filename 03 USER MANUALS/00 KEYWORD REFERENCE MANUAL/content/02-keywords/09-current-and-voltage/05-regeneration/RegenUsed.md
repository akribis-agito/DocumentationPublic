---
keyword: RegenUsed
summary: Selects whether an external or internal regeneration resistor is used.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 378
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RegenUsed

Selects whether an external or internal regeneration resistor is used.

## Overview

`RegenUsed` selects whether the controller uses an external or internal regeneration resistor, configuring the regen circuit to match the hardware. Because it is a hardware-configuration setting, it cannot be changed while the axis is in motion or the motor is on. It is saved to flash. The thresholds [RegenOn](RegenOn.md)/[RegenOff](RegenOff.md) control when whichever resistor is selected switches in and out.

## Examples

```text
ARegenUsed=1         ; use the selected regen resistor (default)
ARegenUsed          ; read the present setting
```

## See also

- [RegenOn](RegenOn.md), [RegenOff](RegenOff.md) — regen activation/deactivation thresholds
- [RegenCurr](RegenCurr.md) — measured regen-resistor current
