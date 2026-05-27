---
keyword: ProgResetAll
summary: Stops all running threads and resets every pointer and stack.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 192
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# ProgResetAll

Stops all running threads and resets every pointer and stack.

## Overview

`ProgResetAll` stops any running user program threads and resets all the program pointers and stacks. It is the global form of [ProgReset](ProgReset.md): where `ProgReset` returns a single task to its initial state, `ProgResetAll` clears the entire interpreter state. Compare with [ProgHaltAll](ProgHaltAll.md), which only suspends threads without resetting them. It is a non-axis command and is not saved to flash.

## Examples

```text
ProgResetAll        ; stop all threads and reset all pointers and stacks
```

## See also

- [ProgReset](ProgReset.md) — reset a single task
- [ProgHaltAll](ProgHaltAll.md) — halt all threads without resetting
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
