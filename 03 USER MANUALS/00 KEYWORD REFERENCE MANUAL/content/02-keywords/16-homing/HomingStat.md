---
keyword: HomingStat
summary: Read-only status of the homing process, including step number and error codes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 342
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomingStat

Read-only status of the homing process, including step number and error codes.

## Overview

`HomingStat` reports the live status of the homing process started by [HomingOn](HomingOn.md). While homing runs it holds the number of the step currently being processed; on completion it reports either success (`100`) or a negative error code describing why the process aborted. When a homing step fails, the process is aborted, `HomingOn` is cleared, and `HomingStat` is set to the matching error code below.

Read `HomingStat` to wait for homing to finish and to diagnose failures. It is driven by the step definitions in [HomingDef](HomingDef.md). While the process is active, `HomingStat` and [HomingStep](HomingStep.md) carry the same value — the current step number; they differ only at the end, where `HomingStat` switches to `100` or a negative error code while `HomingStep` retains the step number that was reached.

## How it works

Each control cycle, the homing engine publishes the current step number into `HomingStat` before executing that step. If the step completes normally the engine advances and the next step's number appears. If a step detects an error condition it clears [HomingOn](HomingOn.md) to `0` and overwrites `HomingStat` with the negative code for that condition (see the table). An "End homing" step sets `HomingStat` to `100`.

The per-step error checks include: the axis was unexpectedly already in motion when a step started (`-6`); the motor was disabled mid-step, e.g. by a fault (`-3`); the step's timeout elapsed (`-2`); a motion ended for a reason other than the one the step required (`-4`); the sequence ran past the last step without an "End homing" instruction (`-7`); and several step-specific conditions listed below.

## Status values

| HomingStat | Descriptions |
|----|----|
| 0 | No homing was done after power on or reset. |
| Positive value (not 100) | Homing is in process. The value is the number of the step currently being processed. |
| -1 | Aborted due to a wrong parameter in the HomingDef array (parameters of each step are checked at the start of that step). |
| -2 | Aborted due to timeout during one of the homing steps (the step's "maximum time" parameter elapsed). |
| -3 | Aborted due to unexpected motor off. During a step the axis was disabled (e.g. by a fault reflected in ConFlt) and the step could not complete. |
| -4 | Aborted due to wrong motion reason. A step that expects a specific end-of-motion reason (RLS, FLS, index, reached target, home change…) saw a different reason. |
| -5 | Aborted due to wrong step type. The sequence reached a step whose instruction value is not a recognized type. |
| -6 | Aborted because the axis was in motion when a new step started. |
| -7 | Aborted due to too many steps — the sequence reached the last possible step without an "End homing" instruction. |
| -8 | Aborted due to an unexpected limit. Relevant only to the "Check if axis is out of limit" step. |
| -9 | Aborted because the conditions for SetPosition were not met. Relevant to the "Set position" and the two "Move to hard stop" steps. |
| -10 | Aborted due to a not-allowed motion mode requested by the "write to MotionMode" step. |
| -11 | Aborted due to a not-allowed map type requested by the "write to MapType" step. |
| -12 | Aborted because phasing (commutation initialization) was not yet done when an "Enable the motor" step ran. |
| 100 | The homing process completed successfully. |

The `-3` error reflects an axis fault during a step; the cause is reported by [ConFlt](../07-status-and-faults/ConFlt.md). The `-9` error refers to the preconditions of [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md).

## Examples

```text
AHomingStat         ; 0 = not homed, >0 = step in progress, 100 = done, <0 = error
```

## See also

- [HomingOn](HomingOn.md) — starts the homing process this status tracks
- [HomingStep](HomingStep.md) — the current homing step number
- [HomingDef](HomingDef.md) — defines the steps that produce these status values
- [ConFlt](../07-status-and-faults/ConFlt.md) — controller fault behind a `-3` (motor off) abort
- [SetPosition](../10-motion/03-kinematics-configuration/SetPosition.md) — preconditions behind a `-9` abort
