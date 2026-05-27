---
keyword: MaxPwrTemp
summary: Maximum allowed power-stage temperature (°C); exceeding it triggers protection.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 90
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
  - 20
  - 80
  default: 65
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPwrTemp

Maximum allowed power-stage temperature (°C); exceeding it triggers protection.

## Overview

`MaxPwrTemp` is the maximum allowed temperature, in °C, for the power-generating components of the product. When [PwrTemp](PwrTemp.md) approaches or exceeds this limit, the controller's over-temperature protection acts to prevent damage.

## Examples

```text
AMaxPwrTemp=65       ; power-stage over-temperature limit (°C)
```

## See also

- [PwrTemp](PwrTemp.md) — measured power-stage temperature
- [BoardTemp](BoardTemp.md) — controller-board temperature
