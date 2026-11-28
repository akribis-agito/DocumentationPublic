---
keyword: GantryMode
summary: Selects the coordinate and yaw-reference behavior for a gantry pair.
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 916
availability:
- controller
- ci-master
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMode

Set the mode on the master (first) axis of an implemented motor pair, with gantry disabled and any transition complete. On AGM800 these pairs are A/B, C/D, E/F and G/H. Auxiliary ports I–L have no partner. On a three-axis controller only A/B form a pair.

| Value | Behavior on enabling gantry |
| --- | --- |
| 0 | Legacy coordinates. Firmware captures the master offset at engagement. |
| 1 | Symmetric linear/yaw coordinates. The yaw reference starts at the transformed yaw reference. |
| 2 | The same symmetric coordinates as mode 1. The yaw reference starts at zero to align the pair. |

In modes 1 and 2, set the two axes’ offsets independently before engagement. A nonzero mode written to the yaw axis or an axis without a pair gives error 8. A zero on those axes is accepted for parameter-file replay, subject to the transition check for an implemented pair. The setting is per axis and saved to flash. The default is 0. CAN code 916. [GantryOffset](../02-gantry-kinematic-feedback/GantryOffset.md)
