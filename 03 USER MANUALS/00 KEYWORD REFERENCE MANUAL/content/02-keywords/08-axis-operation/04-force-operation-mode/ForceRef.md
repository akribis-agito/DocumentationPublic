---
keyword: ForceRef
summary: Filtered force reference used in the force control loop.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 581
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
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# ForceRef

Filtered force reference used in the force control loop.

## Overview

`ForceRef` is the filtered force reference used in the force control loop. It follows the source defined by [ForceCmdSrc](ForceCmdSrc.md) (analog input or the [ForceCmdVal](ForceCmdVal.md) table). The force loop drives the feedback [Force](Force.md) toward this reference, with the difference reported as [ForceErr](ForceErr.md).

Please refer to [Control tuning – Force control](../../../02-keywords/06-protections/04-force-control/00-overview.md) for more information on the filter.

## Examples

```text
AForceRef           ; read the filtered force reference
```

## See also

- [ForceCmdSrc](ForceCmdSrc.md) — selects the reference source
- [Force](Force.md) — force feedback the loop tracks
- [ForceErr](ForceErr.md) — ForceRef minus Force
