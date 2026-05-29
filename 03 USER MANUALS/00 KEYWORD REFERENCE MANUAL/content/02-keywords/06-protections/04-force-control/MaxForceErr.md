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
| Closed-loop force control | `MaxForceErr` | ConFlt code 1045 (force error too high) |
| [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0, or direct signal injection at the current-reference point | [MaxForceErrOL](MaxForceErrOL.md) | ConFlt code 1057 (open-loop force error too high) |
| Direct signal injection at the velocity-, position-, or **force-**reference point | `MaxForceErr` (force stays closed-loop) | ConFlt code 1045 |

Important: injecting **at the force-reference point** keeps the force-error limit on `MaxForceErr`, not `MaxForceErrOL` — only the position- and velocity-error limits switch to their open-loop counterparts in that case. The open-loop swap of the force limit happens only when [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) is non-zero, or when a direct signal-injection mode is active at the current-reference point ([InjectType](../../13-injection/InjectType.md) = a direct type and [InjectPoint](../../13-injection/InjectPoint.md) = current reference). Separately, if no analog force feedback is defined the loop faults with [ConFlt](../../07-status-and-faults/ConFlt.md) code 1046 (no force feedback).

### Edge cases

- **Motor off:** the force loop does not run, so the limit is not checked; the error is reset and re-initialised on the next motor-on.
- **No analog force feedback defined:** the loop faults with [ConFlt](../../07-status-and-faults/ConFlt.md) code 1046 the instant force control runs, regardless of how small the error is.
- **Mode dependency:** the check is part of the closed force-control loop. In modes that do not run that loop (e.g. current-control-only without force over PIV) the error is forced to zero and the limit cannot trip.
- **Clearing the fault:** ConFlt code 1045 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** force-error trips are not maskable through [ProtectMask](../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

## Examples

```text
AMaxForceErr[1]=2000   ; trip axis A if closed-loop force error exceeds 2000
AMaxForceErr           ; read the current limit
```

## See also

- [MaxForceErrOL](MaxForceErrOL.md) — open-loop force-error limit
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — the live force error being limited
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1045 (force error exceeds limit)
