---
keyword: AutoExec
summary: When set, runs the user program automatically on power-up or restart.
availability:
  standalone:
  - v4
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

## How it works

`AutoExec` is a single flag (range 0–1) read once during start-up, after the firmware has loaded parameters from flash and initialized the stored user program. At that point the controller auto-starts the program **only if both** conditions hold:

| Condition | Requirement |
|-----------|-------------|
| `AutoExec` | Equals 1 |
| User program present | A valid user program is stored in flash |

When both are true the program is launched on the user-program execution thread, starting from its first instruction — exactly as if a [ProgRun](../../17-user-program/02-program-execution/ProgRun.md) had been issued. If no program is stored, `AutoExec = 1` has no effect. The flag is read only at start-up, so changing it at run time does not start or stop a program until the next power-up or [Reset](Reset.md).

Unlike the other keywords in this section, `AutoExec` is a stored parameter rather than a command: it can be read or written at any time, including while the motor is on or in motion.

## Examples

```text
AAutoExec=1          ; run the user program automatically at startup
AAutoExec            ; read the current setting
ASave                ; persist to flash; then AReset to apply
```

## See also

- [Save](Save.md) — persist this flag to flash so it survives a power cycle
- [Reset](Reset.md) — software power cycle that re-reads `AutoExec` on restart
- [ProgRun](../../17-user-program/02-program-execution/ProgRun.md) — start the user program manually
