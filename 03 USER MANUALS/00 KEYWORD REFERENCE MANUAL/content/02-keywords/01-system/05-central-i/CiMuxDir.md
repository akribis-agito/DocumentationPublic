---
keyword: CiMuxDir
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 551
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4095
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CiMuxDir

**Definition:**

CiMuxDir is a non-axis parameter that controls the direction of the Central-i multiplexer — i.e., which physical port the shared CI bus is currently routed to. Together with [CiMuxSel](CiMuxSel.md) it allows one controller to share its Central-i interface across multiple ports. The setting is saved to flash.

**See also:**

[CiMuxSel](CiMuxSel.md), [CIConnect](CIConnect.md)
