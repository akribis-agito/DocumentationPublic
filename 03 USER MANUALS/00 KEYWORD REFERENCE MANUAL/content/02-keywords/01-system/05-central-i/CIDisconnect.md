---
keyword: CIDisconnect
summary: Command that terminates the active Central-i link on the selected axis port.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 505
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CIDisconnect

Command that terminates the active Central-i link on the selected axis port.

## Overview

`CIDisconnect` terminates the active Central-i link on the selected axis port. After it runs, the port stops real-time data exchange until a subsequent [CIConnect](CIConnect.md) is issued. It cannot be issued while the motor is on or in motion.

## Examples

```text
ACIDisconnect        ; tear down the Central-i link on the selected axis
```

## See also

- [CIConnect](CIConnect.md) — initiate the link
- [CIAutoConnect](CIAutoConnect.md) — connect automatically at power-up
- [CIStatus](CIStatus.md) — link state
