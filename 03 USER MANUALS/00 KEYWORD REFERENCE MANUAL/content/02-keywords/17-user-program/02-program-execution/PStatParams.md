---
keyword: PStatParams
summary: Lists the parameters included in each periodic statistics transmission.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 483
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatParams

Lists the parameters included in each periodic statistics transmission.

## Overview

`PStatParams` specifies which controller parameters are included in each periodic program-status transmission (up to **20 entries**, indices `[1]`–`[20]`). Each element identifies one parameter to sample and send at the interval set by [PStatInterval](PStatInterval.md), over the port chosen by [PStatPort](PStatPort.md), whenever streaming is enabled by [PStatOn](PStatOn.md). It is a non-axis array and is saved to flash (default `0`).

## How it works

Each element holds a [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) that names the exact parameter to stream — the same encoding used by the snapshot and event-trigger sources:

| Bits | Field |
|---|---|
| 0–9 | CAN code of the parameter |
| 10–14 | Axis number (0 = A; ignored for non-axis parameters) |
| 16–31 | Array index (for array parameters; use 0 for scalars) |

For a scalar parameter on axis A the complex code is just the plain CAN code. An entry of `0` is skipped, so leave unused slots at `0`. When you set `PStatParams`, the controller validates every non-zero entry; if any entry names a parameter that cannot be resolved, the configuration is rejected — [PStatOn](PStatOn.md) reads back a negative (error) value and the offending entry is cleared. Each transmission carries the current value of every valid entry, in index order.

## Examples

```text
APStatParams[1]=<complex CAN code of parameter to stream>    ; first streamed parameter
APStatParams[2]=0    ; leave the second slot unused
APStatParams         ; read the whole streamed-parameter list
```

## See also

- [PStatOn](PStatOn.md) — enable/disable periodic statistics streaming
- [PStatPort](PStatPort.md) — communication port used for streaming
- [PStatInterval](PStatInterval.md) — interval between transmissions
