---
keyword: ForceFiltOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 741
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# ForceFiltOn

**Condition:**

ForceFiltOn is only used when ForcePIVOn = 0.

**Definition:**

ForceFiltOn is used to turn on/off the force filters. If ForceFiltOn\[Index\] = 1, the filter is enabled. If ForceFiltOn\[Index\] = 0, the filter is disabled (bypassed). The indices indicate the location/order of the force filter.

| Index | Descriptions   |
|-------|----------------|
| 1     | Force filter 1 |
| 2     | Force filter 2 |
