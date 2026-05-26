---
keyword: ForcePIVOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 622
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
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForcePIVOn

**Definition:**

ForcePIVOn is used to define the force control structure, as follows.

| Value | Force control structure |
|-------|-------------------------|
| 0     | Standard force control  |
| 1     | Force-over-PIV control  |

Please refer to [Control tuning – Force control](../../../02-keywords/06-protections/04-force-control/00-overview.md) for more information.
