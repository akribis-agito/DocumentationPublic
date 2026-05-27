---
keyword: HomingStep
summary: Read-only index of the last completed step in the homing sequence.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 385
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
# HomingStep

Read-only index of the homing step the engine has reached.

## Overview

`HomingStep` is a read-only, axis-scoped status variable (not saved to flash) that reports the step number the homing engine has reached in the sequence defined by [HomingDef](HomingDef.md). Monitor it to track progress through a multi-step homing procedure. It complements [HomingStat](HomingStat.md), which reports the overall status (in-progress step, success, or error code) of the run started by [HomingOn](HomingOn.md).

## How it works

The homing engine keeps an internal 1-based step pointer. Each control cycle it copies that pointer into `HomingStep`. When a step completes the pointer is incremented, so `HomingStep` moves to the next step to be processed; when homing ends it holds the step number that was reached at the end. While `HomingStat` is also reporting the active step, the two carry the same number; after homing ends, `HomingStat` switches to `100` (success) or a negative error code while `HomingStep` keeps the final step number.

The pointer is primed at `1` whenever homing is not running, so the first value seen after [HomingOn](HomingOn.md) is set is step 1.

## Examples

```text
AHomingStep         ; step number the homing engine has reached
```

## See also

- [HomingStat](HomingStat.md) — overall status and error codes of the homing run
- [HomingOn](HomingOn.md) — starts the homing process
- [HomingDef](HomingDef.md) — defines the steps being counted
