---
keyword: MotorTemp
summary: Read-only measured motor temperature (flagged not implemented in current firmware).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 400
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
  - -40
  - 150
  default: 25
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# MotorTemp

Read-only measured motor temperature (flagged not implemented in current firmware).

## Overview

`MotorTemp` reports the measured motor temperature from an attached sensor (°C). It is read-only, axis-related, and not saved to flash.

> **Not implemented:** `MotorTemp` is flagged `NOT_IMPLEMENTED` in the current firmware parameter table. Confirm hardware/sensor support with Agito before relying on it.

## See also

- [MaxMotorTemp](MaxMotorTemp.md) — over-temperature limit
- [MotorTempUsed](MotorTempUsed.md) — sensor-type selection
- [MotorTempOffset](MotorTempOffset.md) — reading offset
