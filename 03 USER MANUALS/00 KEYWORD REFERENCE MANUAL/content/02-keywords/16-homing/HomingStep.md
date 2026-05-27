---
keyword: HomingStep
summary: Read-only index of the last completed step in the homing sequence.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

Read-only index of the last completed step in the homing sequence.

## Overview

`HomingStep` is a read-only, axis-scoped status variable (not saved to flash) that reports the index of the last completed step in the homing sequence. Monitor it to track progress through a multi-step homing procedure defined by [HomingDef](HomingDef.md). It complements [HomingStat](HomingStat.md), which reports the overall status (in-progress step, success, or error code) of the run started by [HomingOn](HomingOn.md).

## Examples

```text
HomingStep?         ; index of the last completed homing step
```

## See also

- [HomingStat](HomingStat.md) — overall status and error codes of the homing run
- [HomingOn](HomingOn.md) — starts the homing process
- [HomingDef](HomingDef.md) — defines the steps being counted
