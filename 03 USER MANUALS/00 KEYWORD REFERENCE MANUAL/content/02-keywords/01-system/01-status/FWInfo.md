---
keyword: FWInfo
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 312
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FWInfo

**Definition:**

FWInfo is a read-only command that returns a block of firmware version and build information for the controller. It is used by the host software to identify the firmware revision currently running on the device.

**See also:**

[Identity](Identity.md), [About](About.md)
