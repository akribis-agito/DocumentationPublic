---
keyword: PwrTemp
summary: Read-only power-stage temperature (°C).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 38
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
  default: 25
  scaling: 1.0
  implemented: final
overrides: {}
---
# PwrTemp

Read-only power-stage temperature (°C).

## Overview

`PwrTemp` reports the temperature, in °C, measured on the power-generating part of the product (the power stage). It is read-only. The protection limit for this temperature is [MaxPwrTemp](MaxPwrTemp.md).

## Examples

```text
PwrTemp?            ; power-stage temperature (°C)
```

## See also

- [MaxPwrTemp](MaxPwrTemp.md) — power-stage over-temperature limit
- [BoardTemp](BoardTemp.md) — controller-board temperature
