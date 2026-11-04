---
keyword: AutoGSavPer
summary: Sets the recurrence interval, in minutes, of the auto-gain update cycle.
availability:
- controller
- ci-master
products:
- agc300-et
- agc301-et
- agc301-et-bioxtreme
- agd155-af-2a06
- agd155-af-2a10
- agd200-et-2d01
- agd200-et-2d02
- agd200-et-2d05
- agd200-et-2d05-71
- agd301-et-2d01
- agd301-et-2d02
- agd301-et-2d05
- agd301-et-2d09
can_code: 366
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 1000
  default: 300
  scaling: 60.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGSavPer

**Definition:**

AutoGSavPer sets the recurrence interval, in minutes (the value is entered and displayed in minutes), of the auto-gain update cycle: while the algorithm is running it recomputes the gains and refreshes the AutoGStatus results no more often than once per this interval. In the full-auto modes (AutoGMode 1 and 3) the freshly computed gains are also written into the active control set at each update; in the semi-auto modes (AutoGMode 2 and 4) they are recomputed on this interval but applied only later with AutoGCopy. The default is 5 minutes. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGStatus](AutoGStatus.md), [AutoGCopy](AutoGCopy.md)
