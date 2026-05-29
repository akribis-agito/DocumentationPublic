---
keyword: MaxForceErrOL
summary: Maximum allowable force error in open-loop force control; exceeding it faults.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 591
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
  default: 50000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxForceErrOL

Maximum allowable force error in open-loop force control; exceeding it faults.

## Overview

`MaxForceErrOL` is the maximum allowable force error in **open-loop** force-control mode (OL = open loop). It is the open-loop counterpart of [MaxForceErr](MaxForceErr.md), with a deliberately larger default (50000 vs 2000) because the force error is naturally greater when the loop is open. It is axis-scoped, saved to flash, and may be changed at any time including during motion (range 0…327680).

## How it works

The force loop applies a single active force-error limit to `|ForceErr|`; the drive swaps that limit to `MaxForceErrOL` for open-loop force operation, and to [MaxForceErr](MaxForceErr.md) for normal closed-loop control. The open-loop limit is selected when:

- [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) is non-zero, **or**
- a **direct** signal-injection mode is active **at the current-reference injection point** ([InjectType](../../13-injection/InjectType.md) = a direct injection type and [InjectPoint](../../13-injection/InjectPoint.md) = current reference).

Important wrong-state note: injecting **at the force-reference injection point** does **not** swap force to `MaxForceErrOL` — the force loop is still closed in that case, so `MaxForceErr` stays in force and a trip raises ConFlt code 1045. Only the position- and velocity-error limits switch to their open-loop counterparts during force-reference injection. Similarly, injection at the velocity- or position-reference point keeps force on `MaxForceErr`. See [MaxForceErr](MaxForceErr.md) for the full mapping.

When the limit is exceeded in this state, the loop disables the axis and [ConFlt](../../07-status-and-faults/ConFlt.md) shows ConFlt code 1057 (open-loop force error too high), distinguishing it from the closed-loop ConFlt code 1045. Writing the keyword re-evaluates which limit is active, so the change takes effect immediately.

### Edge cases

- **Motor off:** the force loop does not run; the open-loop limit is not checked.
- **Closed-loop operation:** with [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) = 0 and no direct current-reference injection, this limit is inactive — the trip uses [MaxForceErr](MaxForceErr.md) (ConFlt code 1045) instead.
- **Range overflow:** writes outside `0…327680` are clamped to the keyword range; the in-force internal limit is updated immediately on write.
- **Clearing the fault:** ConFlt code 1057 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** open-loop force-error trips are not maskable through [ProtectMask](../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

## Examples

```text
AMaxForceErrOL[1]=50000   ; trip axis A if open-loop force error exceeds 50000
AMaxForceErrOL            ; read the current limit
```

## See also

- [MaxForceErr](MaxForceErr.md) — closed-loop force-error limit
- [OpenLoopOn](../../08-axis-operation/01-general-keywords/OpenLoopOn.md) — selects open-loop operation
- [InjectType](../../13-injection/InjectType.md) / [InjectPoint](../../13-injection/InjectPoint.md) — signal injection that also selects this limit
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1057 (open-loop force error exceeds limit)
