---
keyword: BoardTemp
summary: Read-only controller-board temperature (°C).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 397
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
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BoardTemp

Read-only controller-board temperature (°C).

## Overview

`BoardTemp` reports the temperature of the controller board, measured by the on-board sensor, in °C. It is read-only, not saved to flash, and available at all times. For the temperature of the power stage specifically, see [PwrTemp](PwrTemp.md).

## Examples

```text
BoardTemp?          ; controller board temperature (°C)
```

## See also

- [PwrTemp](PwrTemp.md) — power-stage temperature
- [MaxPwrTemp](MaxPwrTemp.md) — power-stage over-temperature limit
