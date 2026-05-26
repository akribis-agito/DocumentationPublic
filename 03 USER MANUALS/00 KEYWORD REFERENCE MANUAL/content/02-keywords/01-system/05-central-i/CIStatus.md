---
keyword: CIStatus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 508
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 8
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
# CIStatus

**Definition:**

CIStatus is a read-only axis-related array that reports the current state of the Central-i port for the selected axis, including connection status, error flags, and link quality indicators. It is updated in real time and does not require a specific motion or motor state.

**See also:**

[CIGlobalStat](CIGlobalStat.md), [CIConnect](CIConnect.md), [CIIdentity](CIIdentity.md)
