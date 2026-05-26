---
keyword: CiMuxSel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 552
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CiMuxSel

**Definition:**

CiMuxSel is an axis-related array (three elements per axis) that selects which physical port is routed through the Central-i multiplexer for each axis. Together with [CiMuxDir](CiMuxDir.md) it determines the complete multiplexer configuration. The setting is saved to flash.

**See also:**

[CiMuxDir](CiMuxDir.md), [CIConnect](CIConnect.md)
