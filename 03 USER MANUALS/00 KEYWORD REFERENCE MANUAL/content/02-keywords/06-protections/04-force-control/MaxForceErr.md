---
keyword: MaxForceErr
summary: Maximum allowable force error in closed-loop force control; exceeding it faults.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 585
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
  - 327680
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxForceErr

Maximum allowable force error in closed-loop force control; exceeding it faults.

## Overview

`MaxForceErr` is the maximum allowable force error in **closed-loop** force-control mode. If the magnitude of the force error (commanded − measured force) exceeds this threshold, the controller disables the axis with a fault. It is axis-scoped, saved to flash, and may be changed at any time including during motion (range 0…327680, default 2000). For the open-loop equivalent, see [MaxForceErrOL](MaxForceErrOL.md).

## How it works

In the force control loop the drive forms the force error from the filtered force reference and the measured force, then tests its absolute value against the active force-error limit:

```text
ForceErr = (filtered force reference) − (measured force)
if (|ForceErr| > active force-error limit)
    → disable axis, append to ErrLog
```

The fault code raised depends on whether the loop is currently closed or open:

| Situation | Limit used | ConFlt code shown |
|-----------|------------|-------------------|
| Closed-loop force control | `MaxForceErr` | 1045 (force error too high) |
| Open-loop / injection at the force reference | [MaxForceErrOL](MaxForceErrOL.md) | 1057 (open-loop force error too high) |

The active force-error limit is set to `MaxForceErr` for normal closed-loop operation and switched to [MaxForceErrOL](MaxForceErrOL.md) when open-loop or signal injection is engaged at the force-reference point. Separately, if no analog force feedback is defined the loop faults with [ConFlt](../../07-status-and-faults/ConFlt.md) code 1046 (no force feedback).

## Examples

```text
AMaxForceErr[1]=2000   ; trip axis A if closed-loop force error exceeds 2000
AMaxForceErr           ; read the current limit
```

## See also

- [MaxForceErrOL](MaxForceErrOL.md) — open-loop force-error limit
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — the live force error being limited
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1045 (force error exceeds limit)
