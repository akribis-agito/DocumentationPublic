---
keyword: PlantModel
summary: Array of identified plant-model coefficients used by auto-tuning and velocity filter design.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 558
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 81
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# PlantModel

Array of identified plant-model coefficients used by auto-tuning and velocity filter design.

## Overview

`PlantModel` stores the identified plant-model coefficients used by the auto-tuning and velocity filter design algorithms. The coefficients describe the mechanical transfer function of the axis as determined by the identification procedure (see [CalcIden](CalcIden.md) and [IdenResults](IdenResults.md)). It is an axis-related array saved to flash and can be changed at any time.

## Examples

```text
APlantModel         ; read all identified plant-model coefficients
APlantModel[1]      ; read the first coefficient
```

## See also

- [CalcIden](CalcIden.md) — runs the sine-sweep calculation
- [IdenResults](IdenResults.md) — raw input/output relations feeding the model
