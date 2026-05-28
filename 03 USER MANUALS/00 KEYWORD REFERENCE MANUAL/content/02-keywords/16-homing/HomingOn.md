---
keyword: HomingOn
summary: Starts and reports the active homing process for the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 340
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomingOn

Starts and reports the active homing process for the axis.

## Overview

`HomingOn` is the trigger for the built-in homing process. It is cleared to `0` on power-on or reset. Writing `1` starts the homing sequence defined in [HomingDef](HomingDef.md), with progress and any error reported by [HomingStat](HomingStat.md). The controller clears `HomingOn` back to `0` automatically when the process finishes — whether it completed successfully or was aborted by an error.

Because it cannot be written while the axis is in motion, `HomingOn` is set to begin a homing run from a stationary state. Together with [HomingDef](HomingDef.md) (the step definitions) and [HomingStat](HomingStat.md) (the status), it forms the core of the homing interface.

## How it works

The homing engine runs inside the control interrupt, once per controller cycle, while `HomingOn == 1`:

1. **Rising edge (just set to 1).** The current kinematics — [Speed](../10-motion/03-kinematics-configuration/Speed.md), acceleration, deceleration, emergency deceleration and the jerk mode — are copied into internal "mirror" variables, and jerk mode is forced off for the duration of homing. Each homing step then overwrites the kinematics with the values from its [HomingDef](HomingDef.md) parameters. The internal step pointer is set to step 1 and the "first cycle in step" flag is raised.
2. **Each cycle.** The engine executes the current step (see [HomingDef](HomingDef.md) for the per-step behaviour) and republishes the step number to [HomingStat](HomingStat.md) and [HomingStep](HomingStep.md).
3. **Completion.** Reaching an "End homing" step sets `HomingOn` back to `0` and `HomingStat` to `100`. Any failure (timeout, unexpected motor-off, in-motion, wrong end-of-motion reason, etc.) also clears `HomingOn` to `0` and writes the matching negative error code to `HomingStat`.
4. **Falling edge (just cleared).** The mirrored kinematics (Speed, accel, decel, emergency decel) are restored, so a homing run leaves the axis's normal motion settings unchanged.

While `HomingOn` is `0`, the engine keeps the internal pointer primed at step 1 so the next write of `1` always starts from the beginning.

## Examples

```text
AHomingOn=1          ; start the homing process defined by HomingDef
AHomingOn           ; 1 while homing is active, cleared to 0 when done
```

## See also

- [HomingDef](HomingDef.md) — defines the homing steps that run
- [HomingStat](HomingStat.md) — reports progress and error status of the run
- [HomingStep](HomingStep.md) — the homing step number the engine has reached
