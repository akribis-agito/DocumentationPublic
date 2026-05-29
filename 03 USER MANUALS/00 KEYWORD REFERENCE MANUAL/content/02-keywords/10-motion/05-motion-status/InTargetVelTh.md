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

In current/force mode the feedback velocity is tested each cycle:

$$
|\text{Vel}[1]| \le \text{InTargetVelTh}
$$

The behaviour differs from the position-mode check in one important way: the comparison is re-evaluated **every cycle and is not latched**. If `|Vel[1]| > InTargetVelTh` the controller forces `InTargetStat = 2` and zeroes the dwell counter; if it is within the window the counter advances toward `InTargetTime` and `InTargetStat` latches to 4 — but should the velocity later exceed the threshold again, the status immediately drops back to 2. The window maximum is the maximum speed and the default is `1000` (user velocity units). It is saved to flash.

The dwell-counter mechanic is the same as for the position-based settling check; see the timing diagram on the [InTargetTol](InTargetTol.md) page (substitute `|Vel[1]|` for `|PosErr|` and `InTargetVelTh` for `InTargetTol`). The key difference is that in current/force mode the resulting state-4 latch is *not sticky* — it falls back to 2 the instant the velocity leaves the window.

## Examples

```text
AInTargetVelTh=1000  ; velocity window in user units/s (default)
AInTargetVelTh      ; read current value
```

### Edge cases

- **Motor off:** value held; `InTargetStat = 0` so no check is made.
- **Out-of-range write:** the parameter system clamps to `0`–`1.3 × 10⁹`; negative values are rejected.
- **Simulation mode (`MotorType` = 5):** `Vel[1]` reflects the simulated reference; the check runs normally.
- **ModRev wrap:** the wrap preserves `ΔPos`, so `|Vel[1]|` does not spike at the wrap.
- **Active fault:** axis disabled, `InTargetStat = 0`.
- **Other motion modes:** the velocity-based settling applies only when `OperationMode` is current (1) or force (4); in position/velocity mode [InTargetTol](InTargetTol.md) is used instead.
- **`InTargetVelTh = 0`:** requires exact-zero velocity — unreachable on a physical axis with any disturbance.
- **Not sticky:** value 4 in current/force mode drops back to 2 as soon as the velocity exceeds the threshold again — unlike position/velocity mode, which latches.

## See also

- [InTargetStat](InTargetStat.md) — settling state gated by this window
- [InTargetTime](InTargetTime.md) — minimum dwell time inside the window
- [InTargetTol](InTargetTol.md) — position settling window (position/velocity control)
- [Vel](../01-kinematics-status/Vel.md) — `Vel[1]` is the signal compared against this window
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — selects current/force-based settling
