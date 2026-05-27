---
keyword: InTargetVelTh
summary: Velocity settling window (Vel[1]) used to declare target reached in current/force control.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 292
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetVelTh

Velocity settling window (Vel[1]) used to declare target reached in current/force control.

## Overview

In current or force control operation mode ([OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) `= 1` or `4`), `InTargetVelTh` is the velocity settling window that the absolute feedback velocity [Vel](../01-kinematics-status/Vel.md) `[1]` must stay within for [InTargetTime](InTargetTime.md) before [InTargetStat](InTargetStat.md) signals that the target is reached (`InTargetStat = 4`). For position/velocity control the position-based window [InTargetTol](InTargetTol.md) is used instead.

## How it works

In current/force mode the profiler tests the feedback velocity each cycle:

$$
|Vel[1]| \le InTargetVelTh
$$

The behaviour differs from the position-mode check in one important way (`AG300_CTL01Profiler.c:10349–10365`): the comparison is re-evaluated **every cycle and is not latched**. If `|Vel[1]| > InTargetVelTh` the firmware forces `InTargetStat = 2` and zeroes the dwell counter; if it is within the window the counter advances toward `InTargetTime` and `InTargetStat` latches to 4 — but should the velocity later exceed the threshold again, the status immediately drops back to 2. The window maximum is `MAX_SPEED` and the default is `1000` (user velocity units, `INTARGETVELTH_DFLT`). It is saved to flash.

## Examples

```text
AInTargetVelTh=1000  ; velocity window in user units/s (default)
AInTargetVelTh      ; read current value
```

## See also

- [InTargetStat](InTargetStat.md) — settling state gated by this window
- [InTargetTime](InTargetTime.md) — minimum dwell time inside the window
- [InTargetTol](InTargetTol.md) — position settling window (position/velocity control)
- [Vel](../01-kinematics-status/Vel.md) — `Vel[1]` is the signal compared against this window
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — selects current/force-based settling
