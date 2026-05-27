---
keyword: VelFiltOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 122
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
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
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
---
# VelFiltOn

**Definition:**

VelFiltOn is used to turn on/off the velocity filters. If VelFiltOn\[Index\] = 1, the filter is enabled. If VelFiltOn\[Index\] = 0, the filter is disabled (bypassed). The indices indicate the location/order of the velocity filter.

| Index | Descriptions      |
|-------|-------------------|
| 1     | Velocity filter 1 |
| 2     | Velocity filter 2 |
| 3     | Velocity filter 3 |
| 4     | Velocity filter 4 |
