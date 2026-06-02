---
keyword: Print
summary: User-program statement that outputs a text string to the host.
availability:
  standalone: []
  central-i:
  - v5
can_code: 827
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# Print

User-program statement that outputs a text string to the host.

## Overview

`Print` outputs a text string from a running user program to the communication channel, for status or debug messages while the program executes. It is a non-axis function and is not saved to flash. It is available on Central-i (v5) only; on a standalone controller a `Print` request returns a "not supported" error.

## How it works

`Print` is intended to be used from within a user program rather than as a direct host command. When the program is compiled, each printed string literal is stored in the program memory; at run time the `Print` statement passes the address of that string and the firmware streams the text out over the communication channel that is servicing the program. Execution continues with the next program line after the text has been queued.

Because the message is emitted on the active communication channel, it appears in the host tool that is connected to the controller — making `Print` useful for tracing program flow, reporting intermediate values, or signalling that a particular branch was reached. It does not affect motion or any keyword value.

## Examples

```text
; inside a user program
Print "Homing complete"      ; emit a status message to the host
Print "Entering phase 2"     ; trace which branch the program took
```

## See also

- [ProgRun](ProgRun.md) — start a user program
- [ProgStat](ProgStat.md) — user-program run status
