---
keyword: OpenLoopOn
summary: Opens the control loop at a chosen point (none, current, or voltage).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 144
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# OpenLoopOn

Opens the control loop at a chosen point (none, current, or voltage).

## Overview

`OpenLoopOn` opens the control loop at a chosen point, primarily for commissioning and diagnostics. When the loop is opened at the current reference, [OpenLoopCurr](OpenLoopCurr.md) supplies the reference; when opened at the voltage reference, [OpenLoopVolt](OpenLoopVolt.md) supplies it.

## How it works

| OpenLoopOn | Descriptions |
|---|---|
| 0 | **No open loop** All control loops are closed. |
| 1 | **Current open loop** Control loops are cut-off/opened at the current reference input (just before the current loop). |
| 2 | **Voltage open loop** Control loops are cut-off/opened at the voltage reference input (just before the space vector modulation for PWM drive). |

## Examples

```text
OpenLoopOn=1        ; current open loop, drive with OpenLoopCurr
OpenLoopOn=2        ; voltage open loop, drive with OpenLoopVolt
OpenLoopOn=0        ; close all loops (normal operation)
```

## See also

- [OpenLoopCurr](OpenLoopCurr.md) — current reference used when OpenLoopOn = 1
- [OpenLoopVolt](OpenLoopVolt.md) — voltage reference used when OpenLoopOn = 2
