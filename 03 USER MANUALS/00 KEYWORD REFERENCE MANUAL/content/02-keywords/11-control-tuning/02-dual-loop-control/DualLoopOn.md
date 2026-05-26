---
keyword: DualLoopOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 269
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualLoopOn

**Definition:**

DualLoopOn is used to enable and configure dual-loop mode.

| DualLoopOn | Descriptions |
|---|---|
| 0 | Dual-loop mode is disabled (default control is used) |
| 1 | Dual-loop mode is enabled Velocity feedback is derived from AuxPos Position feedback is derived from Pos |
| 2 | Dual-loop mode is enabled Velocity feedback is derived from analog input’s tachometer input (AInMode[Index]=9) Position feedback is derived from Pos |
