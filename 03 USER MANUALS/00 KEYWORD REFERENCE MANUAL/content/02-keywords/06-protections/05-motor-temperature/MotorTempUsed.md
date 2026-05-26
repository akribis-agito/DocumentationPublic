---
keyword: MotorTempUsed
summary: Selects the motor temperature-sensor type.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 398
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotorTempUsed

Selects the motor temperature-sensor type.

## Overview

`MotorTempUsed` selects the type of motor temperature sensor in use, which determines how [MotorTemp](MotorTemp.md) is read and whether [MaxMotorTemp](MaxMotorTemp.md) / [MotorTempOffset](MotorTempOffset.md) apply.

| Value | Sensor |
|-------|--------|
| 0 | None (or thermostat wired to a digital input) |
| 1 | PT100 |
| 2 | Thermostat (wired to the temperature-sensor input) |

## Examples

```text
MotorTempUsed=1     ; PT100 sensor
```

## See also

- [MotorTemp](MotorTemp.md) — measured temperature
- [MaxMotorTemp](MaxMotorTemp.md) — over-temperature limit (PT100)
- [MotorTempOffset](MotorTempOffset.md) — reading offset (PT100)
