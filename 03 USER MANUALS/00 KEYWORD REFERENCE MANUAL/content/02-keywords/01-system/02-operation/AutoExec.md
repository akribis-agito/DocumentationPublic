---
keyword: AutoExec
summary: When set, runs the user program automatically on power-up or restart.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 208
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
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
# AutoExec

When set, runs the user program automatically on power-up or restart.

## Overview

`AutoExec = 1` causes the controller to start executing the user program automatically on power-up or after a software restart. `AutoExec = 0` (default) leaves the program stopped until it is started explicitly.

Because `AutoExec` is saved to flash, run [Save](Save.md) before resetting so the setting persists across the power cycle.

## Examples

```text
AutoExec=1          ; run the user program automatically at startup
AutoExec?           ; query the current setting
Save                ; persist to flash, then Reset to apply
```

## See also

- [Save](Save.md) — persist parameters to flash
- [Reset](Reset.md) — software power cycle
