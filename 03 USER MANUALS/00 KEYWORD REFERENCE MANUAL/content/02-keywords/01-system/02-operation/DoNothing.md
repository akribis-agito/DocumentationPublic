---
keyword: DoNothing
summary: No-op command used to check communication responsiveness.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 239
attributes:
  access: ro
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
  implemented: final
overrides: {}
---
# DoNothing

No-op command used to check communication responsiveness.

## Overview

`DoNothing` performs no action. Its only purpose is to give the host a harmless command to send when it needs to confirm that the controller is present and responding — effectively a communication "ping." It is safe to issue at any time, including while the motor is on or in motion.

## Examples

```text
ADoNothing           ; issue a no-op; a normal acknowledgement confirms the link
```

## See also

- [About](../01-status/About.md) — host/diagnostic command
