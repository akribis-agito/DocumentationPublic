---
keyword: AutoGStatus
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 357
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 51
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGStatus

**Definition:**

AutoGStatus is a read-only array (indexes 1 to 50) that reports the working values of the automatic gain tuning process for the axis. Its locations expose the latest results and intermediate quantities, including the estimated inertia ratio, the estimation-quality figure, the computed gains (position gain, velocity gain, velocity integral gain, and acceleration feedforward gain), the time of the most recent calculation, the time remaining until the next scheduled update (in minutes), a flag indicating that valid tuning results are present, and internal sample counters used by the algorithm. It is an axis-related status variable and is not saved to flash.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGMode](AutoGMode.md), [AutoGCopy](AutoGCopy.md)
