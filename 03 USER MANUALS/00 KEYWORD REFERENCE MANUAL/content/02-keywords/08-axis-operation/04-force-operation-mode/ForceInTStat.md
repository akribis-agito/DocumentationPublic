---
keyword: ForceInTStat
summary: In-target status of force control for the user-defined reference table.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 735
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceInTStat

In-target status of force control for the user-defined reference table.

## Overview

`ForceInTStat` reports the in-target (force-settled) status of force control when a user-defined force reference array is used. It is the force-mode counterpart of the position/velocity [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md), and it reuses the same `IN_TARGET_STATUS_*` constants (`AG300_CTL01ParamsCommon.h:1920`). It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2, and it tracks progress from motor enable through ramping to settling within [ForceInTTol](ForceInTTol.md) for at least [ForceInTTime](ForceInTTime.md).

## How it works

| ForceInTStat | Constant | Descriptions |
|----|----|----|
| 0 | `IN_TARGET_STATUS_MOTOR_OFF` | Motor is disabled. Set when the axis turns off (`AG300_CTL01ControlInterrupt.h:571`). |
| 1 | `IN_TARGET_STATUS_MOTOR_ON` | Motor is enabled, no force command settling yet. Set on motor-on (`AG300_CTL01Funcs.c:17273`). |
| 2 | `IN_TARGET_STATUS_IN_MOTION` | Raw force reference is ramping toward the target value ([ForceCmdVal](ForceCmdVal.md)) at [ForceCmdSlope](ForceCmdSlope.md) (`AG300_CTL01ControlLoops.c:1330`). |
| 3 | `IN_TARGET_STATUS_WAITING_TARGET_TIME` | Raw reference has reached the target value; the force feedback is settling within the [ForceInTTol](ForceInTTol.md) window around the target and the [ForceInTTime](ForceInTTime.md) dwell is pending (`AG300_CTL01ControlLoops.c:1170`). |
| 4 | `IN_TARGET_STATUS_TARGET_REACHED` | Force feedback has stayed within `ForceInTTol` of the target for at least `ForceInTTime` (`AG300_CTL01ControlLoops.c:1186`). |

The state machine advances inside the force-command generator (`AG300_CTL01ControlLoops.c:1160`):

- **2 → 3:** the moment the raw reference equals the target [ForceCmdVal](ForceCmdVal.md), the firmware leaves the ramping state, switches to state 3, and clears the dwell counter (`glForceInTrgtCounter`).
- **within 3:** each cycle, if `|ForceErr| <= ForceInTTol` the dwell counter increments; if `ForceErr` leaves the window the counter is re-zeroed (`AG300_CTL01ControlLoops.c:1200`). This means state 3 covers both "settling" and "settled but waiting for the dwell".
- **3 → 4:** once the dwell counter reaches [ForceInTTime](ForceInTTime.md), the status latches to 4 and the [ForceSamples](ForceSamples.md) timings are recorded.

Once state 4 is reached the settling condition is **no longer checked** for that entry, so it is effectively latched until the force command changes (the raw reference ramps to a new [ForceCmdVal](ForceCmdVal.md), returning to state 2) or the motor is disabled (state 0). This mirrors the sticky behaviour of [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md) = 4 in position control.

> **Note:** `ForceInTStat` reflects the table source only. With the analog source ([ForceCmdSrc](ForceCmdSrc.md) = 0) there is no defined target to settle on, so the in-target detection is not run.

## Examples

```text
AForceInTStat       ; 4 = settled in target, 2 = still ramping
```

## See also

- [ForceInTTol](ForceInTTol.md) — settling window
- [ForceInTTime](ForceInTTime.md) — required dwell time within the window
- [ForceSamples](ForceSamples.md) — measured move/settle timings (recorded when state reaches 4)
- [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md) — position/velocity/current in-target status (same state values)
