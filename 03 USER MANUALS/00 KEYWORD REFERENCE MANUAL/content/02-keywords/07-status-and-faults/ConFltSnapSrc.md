---
keyword: ConFltSnapSrc
summary: Configures which parameters are captured into ConFltSnapVal on a fault.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 528
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
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
# ConFltSnapSrc

Configures which parameters are captured into ConFltSnapVal on a fault.

## Overview

`ConFltSnapSrc` selects which parameter values are captured (snapped) into [ConFltSnapVal](ConFltSnapVal.md) when a controller fault occurs. This lets you freeze the most relevant diagnostic data at the exact moment an axis faults, so you can inspect the system state afterwards rather than reading parameters that have since changed.

It is an axis-scoped array of 5 elements, read/write and saved to flash, so your snapshot configuration persists across power cycles. Each element holds the CAN code of the parameter to record; the captured values appear in the corresponding entries of the read-only [ConFltSnapVal](ConFltSnapVal.md) array.

## Examples

```text
AConFltSnapSrc[1]=33     ; capture the parameter with CAN code 33 (e.g. StatReg) first
AConFltSnapSrc[1]       ; query which parameter the first slot will capture
AConFltSnapSrc          ; query the whole 5-element snapshot source list
```

## See also

- [ConFltSnapVal](ConFltSnapVal.md) — the captured parameter values
- [ConFlt](ConFlt.md) — the fault code that triggers the snapshot
