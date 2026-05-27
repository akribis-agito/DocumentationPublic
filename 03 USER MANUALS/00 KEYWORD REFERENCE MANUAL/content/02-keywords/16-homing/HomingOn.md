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

## Examples

```text
AHomingOn=1          ; start the homing process defined by HomingDef
AHomingOn           ; 1 while homing is active, cleared to 0 when done
```

## See also

- [HomingDef](HomingDef.md) — defines the homing steps that run
- [HomingStat](HomingStat.md) — reports progress and error status of the run
- [HomingStep](HomingStep.md) — index of the last completed step
