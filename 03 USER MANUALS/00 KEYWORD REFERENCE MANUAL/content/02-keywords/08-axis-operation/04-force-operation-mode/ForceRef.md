---
keyword: ForceRef
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# ForceRef

**Definition:**

ForceRef is the filtered force reference used in the force control loop. It follows the source defined by [ForceCmdSrc](../../../02-keywords/08-axis-operation/04-force-operation-mode/ForceCmdSrc.md) (analog input or ForceCmdVal table).

Please refer to [Control tuning – Force control](../../../02-keywords/06-protections/04-force-control/00-overview.md) for more information on the filter.
