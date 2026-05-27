---
keyword: PosFiltOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 124
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 2
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
# PosFiltOn

**Definition:**

PosFiltOn is used to turn on/off the position filters. If PosFiltOn\[Index\] = 1, the filter is enabled. If PosFiltOn\[Index\] = 0, the filter is disabled (bypassed). The indices indicate the location of the position filter.

| Index | Descriptions |
|---|---|
| 1 | Post-profiler filter It is used to filter the profiler’s output and will change the final PosRef value. |
| 2 | Position error filter It is used to filter the position error input, and generally applicable to dual-loop system. |
