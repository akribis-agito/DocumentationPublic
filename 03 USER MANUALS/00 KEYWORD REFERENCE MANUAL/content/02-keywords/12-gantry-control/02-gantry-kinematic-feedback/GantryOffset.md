---
keyword: GantryOffset
summary: Gantry axis offset, captured or written according to GantryMode.
availability:
- controller
- ci-master
can_code: 653
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-11-24'
doc_revision: '2026.11'
---
# GantryOffset

In `GantryMode=0`, engaging gantry captures the master offset from the difference between the two shaped, filtered position references. This value is read-only in legacy mode and is recalculated at the next engagement.

In modes 1 and 2 the master and yaw axes use their respective offsets. Write each value while gantry is disabled and the transition is complete. Writes are rejected while gantry is active or a transition is pending. The reported values use position units and are not saved to flash.

For example, `AGantryOffset` reads the master offset of pair A/B and `BGantryOffset` reads its yaw offset. [GantryMode](../01-general-variables/GantryMode.md)
