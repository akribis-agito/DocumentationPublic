---
keyword: ConFltSnapVal
summary: Read-only snapshot of parameter values captured at the last fault.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 529
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 15
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - -2147483648
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ConFltSnapVal

Read-only snapshot of parameter values captured at the last fault.

## Overview

`ConFltSnapVal` holds the parameter values captured at the moment the last controller fault occurred, for the parameters you selected with [ConFltSnapSrc](ConFltSnapSrc.md). Reading it after a fault gives you a frozen picture of the system state at the instant the axis faulted, which is the key tool for diagnosing why a fault happened.

It is an axis-scoped, read-only array that is not saved to flash. The default element value is `-1`, indicating no value has been captured for that slot. Each captured value corresponds to the CAN code configured in the matching [ConFltSnapSrc](ConFltSnapSrc.md) slot.

## Examples

```text
AConFltSnapVal[1]   ; read the value captured for the first configured source
AConFltSnapVal      ; read the full captured snapshot
```

## See also

- [ConFltSnapSrc](ConFltSnapSrc.md) — selects which parameters are captured here
- [ConFlt](ConFlt.md) — the fault code that triggers the capture
