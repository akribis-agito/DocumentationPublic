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

`ConFltSnapSrc` selects which parameters are captured (snapped) into [ConFltSnapVal](ConFltSnapVal.md) when a controller fault occurs. This lets you freeze the most relevant diagnostic data at the exact moment an axis faults, so you can inspect the system state afterwards rather than reading parameters that have since changed.

It is an axis-scoped array, read/write and saved to flash, so your snapshot configuration persists across power cycles. It provides **4 user-configurable slots**, at indices `[1]` through `[4]` (index `[0]` is unused so that indices start at 1). These four slots fill `ConFltSnapVal[1]…[4]`; the remaining `ConFltSnapVal` slots are filled automatically with a fixed set of system parameters that you do not configure here (see [ConFltSnapVal](ConFltSnapVal.md)).

## How it works

Each slot holds a **complex CAN code** that names the parameter to capture, not just a bare CAN code. The complex value encodes three fields:

| Bits | Field |
|---|---|
| 0–9 | CAN code of the parameter |
| 10–14 | Axis number (0 = A; ignored for non-axis parameters) |
| 16–31 | Array index (for array parameters; use 0 for scalars) |

For a scalar axis parameter on the current axis the complex code is just the plain CAN code, so `AConFltSnapSrc[1]=33` selects [StatReg](StatReg.md) (CAN code 33). Writing `0` to a slot disables it (its `ConFltSnapVal` entry stays at `-1`).

When you set `ConFltSnapSrc`, the firmware:

- Validates the complex code (the CAN code must exist, be a parameter rather than a command, and the axis/array index must be in range; otherwise the write is rejected with a snapshot-configuration error).
- Resolves and stores an internal pointer plus a scaling factor for each slot, so the capture at fault time is fast. If the selected parameter is scaled, the captured value is stored in raw (internal) units.
- **Resets all [ConFltSnapVal](ConFltSnapVal.md) entries to `-1`**, discarding any previously captured snapshot. Reconfigure the sources before the fault you want to diagnose, not after.

## Examples

```text
AConFltSnapSrc[1]=33     ; capture StatReg (CAN code 33) into ConFltSnapVal[1] at the next fault
AConFltSnapSrc[2]=0      ; disable the second slot
AConFltSnapSrc[1]       ; query which parameter the first slot will capture
AConFltSnapSrc          ; query the whole snapshot source list
```

## See also

- [ConFltSnapVal](ConFltSnapVal.md) — the captured values (slots 1–4 from here, plus fixed system parameters)
- [ConFlt](ConFlt.md) — the fault code that triggers the snapshot
- [StatReg](StatReg.md) — a common capture target (CAN code 33)
