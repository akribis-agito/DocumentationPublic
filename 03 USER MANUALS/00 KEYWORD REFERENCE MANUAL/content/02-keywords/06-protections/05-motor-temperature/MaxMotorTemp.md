---
keyword: MaxMotorTemp
summary: Maximum allowable motor temperature (PT100 sensor); exceeding it faults.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 399
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
  - 10
  - 150
  default: 80
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxMotorTemp

Maximum allowable motor temperature (PT100 sensor); exceeding it faults.

## Overview

`MaxMotorTemp` is the maximum allowable motor temperature, in °C. If the measured [MotorTemp](MotorTemp.md) exceeds this limit, the controller raises a fault to protect the motor.

> **Condition:** only applicable with a PT100 temperature sensor — i.e. [MotorTempUsed](MotorTempUsed.md) `== 1`.

## Examples

```text
AMaxMotorTemp=80     ; trip if motor temperature exceeds 80 °C
```

## See also

- [MotorTemp](MotorTemp.md) — measured motor temperature
- [MotorTempUsed](MotorTempUsed.md) — sensor-type selection
- [MotorTempOffset](MotorTempOffset.md) — reading offset (cable compensation)
