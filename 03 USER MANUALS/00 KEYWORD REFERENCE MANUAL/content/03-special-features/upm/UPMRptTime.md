---
keyword: UPMRptTime
summary: Sets the recording "tail" of the UPM repetitive compensation algorithm, in milliseconds.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 561
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 65536
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# UPMRptTime

**Definition:**

UPMRptTime sets the recording "tail" of the UPM repetitive compensation algorithm, in milliseconds: the extra time, after the motion itself has ended, during which the controller keeps recording the position error and current reference of the learning cycle. When a repetitive motion starts, this tail value is loaded as a countdown; the countdown decrements only while the axis is no longer in motion, and when it expires the first learning cycle stops and the recorded cycle length is fixed at the number of samples captured up to that point. A longer tail therefore captures more of the post-motion settling into the learned correction. The default is 0 (no tail), and the value ranges from 0 ms up to 1000 ms, further limited by the space available in the repetitive-compensation storage arrays. The value is held internally in control samples and converted to/from the millisecond value you set. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter saved to flash.

**See also:**

[UPMRptOn](UPMRptOn.md), [UPMRptCalc](UPMRptCalc.md), [UPMRptMotion](UPMRptMotion.md)
