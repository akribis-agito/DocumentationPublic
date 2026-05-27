---
keyword: HomingStat
summary: Read-only status of the homing process, including step number and error codes.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

Read `HomingStat` to wait for homing to finish and to diagnose failures. It complements [HomingStep](HomingStep.md), which reports the last completed step, and is driven by the step definitions in [HomingDef](HomingDef.md).

## Status values

| HomingStat | Descriptions |
|----|----|
| 0 | No homing was done after power on or reset |
| Positive value (not 100) | Homing is in process. HomingStat value reflects the number of the currently processed step in the homing process. |
| -1 | The homing process failed and aborted due to wrong parameter at HomingDef array (the parameters related to each homing step are checked at the beginning of each step). |
| -2 | The homing process failed and aborted due to timeout during one of the homing steps. |
| -3 | The homing process failed and aborted due to unexpected motor off. During one of the homing steps, the axis was disabled due to some fault (reflected at the value of ConFlt) and the step could not be completed. |
| -4 | The homing process failed and aborted due to wrong motion reason. This means that the homing step which expects a given reason for end of motion (RLS, index, reached target…) encounters a different reason for end of motion. |
| -5 | The homing process failed and aborted due to wrong step type. This means that the homing process reached a step whose type (as defined in the HomingDef array) is not recognized. |
| -6 | The homing process failed and aborted due to axis in motion when starting a new step. |
| -7 | The homing process failed and aborted due to too many steps. This error will happen if the homing process reaches the last step defined in the HomingDef array, but the step’s instruction is not “End homing”. |
| -8 | The homing process failed and aborted due to unexpected limit. This error is relevant only when step’s instruction is “Check if axis is out of limit”. |
| 100 | The homing process has been successfully completed. |

The `-3` error reflects an axis fault during a step; the cause is reported by [ConFlt](../07-status-and-faults/ConFlt.md).

## Examples

```text
AHomingStat         ; 0 = not homed, >0 = step in progress, 100 = done, <0 = error
```

## See also

- [HomingOn](HomingOn.md) — starts the homing process this status tracks
- [HomingStep](HomingStep.md) — index of the last completed homing step
- [HomingDef](HomingDef.md) — defines the steps that produce these status values
- [ConFlt](../07-status-and-faults/ConFlt.md) — controller fault behind a `-3` (motor off) abort
