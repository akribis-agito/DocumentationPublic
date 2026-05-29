---
keyword: DualStuckVel
summary: Maximum tolerated velocity difference between the two dual-loop feedbacks.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 157
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
  default: 40000
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualStuckVel

Maximum tolerated velocity difference between the two dual-loop feedbacks.

## Overview

`DualStuckVel` is the maximum absolute velocity difference tolerated between the two feedbacks in a dual-loop configuration, in count/s (counts referring to the main / position-loop feedback). If the difference exceeds this for [DualStuckTime](DualStuckTime.md) consecutive cycles, the axis is disabled — catching a slipped or broken coupling between the two encoders.

## How it works

The check runs each control sample, but **only when dual-loop is enabled** (`DualLoopOn` non-zero):

```text
if dual-loop is enabled
    if |Vel[2] - dual-loop speed| > DualStuckVel
        increment the dual-stuck counter
        if the dual-stuck counter has reached DualStuckTime
            turn the axis off and log the fault
    else
        reset the dual-stuck counter to 0
```

- The compared quantity is the absolute difference between the position-loop feedback velocity `Vel[2]` and the internally computed dual-loop speed (the velocity-loop feedback expressed in the same units). A healthy coupling keeps the two velocities close; a slipped, broken, or badly scaled coupling makes them diverge.
- While the difference exceeds `DualStuckVel`, an internal counter increments; any sample within tolerance resets it to `0`. The fault fires only on a continuous run of [DualStuckTime](DualStuckTime.md) samples.
- On trip the axis is turned off and [ConFlt](../../../07-status-and-faults/ConFlt.md) records ConFlt code 1049 (dual-loop stuck).

The default is `40000` count/s. Because the gate is `DualLoopOn`, this protection has no effect on single-loop axes.

### Edge cases

- **Motor off:** the dual-loop check does not run (the loop block runs only with the motor enabled); the internal counter is reset on motor-off.
- **`DualLoopOn = 0`:** the entire dual-stuck path is skipped — single-loop axes are never tripped by this protection regardless of value.
- **Mode dependency:** dual-loop stuck runs in every operation mode whenever `DualLoopOn` is non-zero (it is not bypassed by the current/force/auto-phasing modes that gate [motor-stuck](../motor-stuck-protection/00-overview.md)).
- **Range overflow:** writes outside `0…1300000000` are clamped to the keyword `range`.
- **Clearing the fault:** ConFlt code 1049 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the dual-loop-stuck trip is not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

## Examples

```text
ADualStuckVel[1]=40000   ; max tolerated feedback velocity mismatch (count/s)
ADualStuckVel[1]         ; read back the threshold
```

## See also

- [DualStuckTime](DualStuckTime.md) — how long the mismatch may persist
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1049 (dual-loop stuck)
