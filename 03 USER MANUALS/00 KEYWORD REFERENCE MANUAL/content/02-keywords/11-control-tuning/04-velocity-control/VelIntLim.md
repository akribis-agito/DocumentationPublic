---
keyword: VelIntLim
summary: Limits the velocity controller’s integral current contribution for each gain-schedule set.
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 915
availability:
- controller
- ci-master
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 2147483647
  scaling: 1.0
  implemented: final
overrides: {}
---
# VelIntLim

Each element sets the maximum magnitude in mA for the velocity-loop integral contribution on the selected axis. The same limit applies in both directions. With the default of 2147483647, the controller adds no integral-current clamp. A setting of zero clamps this contribution to zero.

Set the element for each gain set you use. Fixed scheduling selects the value for the active set; interpolated scheduling blends the two corresponding limits. This applies to ordinary and gantry scheduling. Read `ScheduleGains[7]` to see the limit in effect. This per-axis setting is available on the integrated standalone and Central-i products and is saved to flash. CAN code 915.

For example, `AVelIntLim[1]=1500` sets a 1,500 mA limit in A-axis gain set 1. [ScheduleGains](../01-general-keywords/ScheduleGains.md)
