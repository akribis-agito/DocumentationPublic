---
keyword: DoNothing
summary: No-op command used to check communication responsiveness.
availability:
  standalone:
  - v4
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

## How it works

When the controller receives `DoNothing` it changes nothing and immediately returns the standard "OK" acknowledgement. A host therefore confirms the link is alive purely from the fact that a reply came back.

The command also serves as the firmware's response to an "empty" message: if the controller receives only a carriage return (with or without an axis address and nothing else), it treats that input as `DoNothing` and acknowledges it, rather than reporting a syntax error. Pressing Enter on a bare terminal line is therefore harmless.

## Examples

```text
ADoNothing           ; issue a no-op; a normal acknowledgement confirms the link
```

## See also

- [About](../01-status/About.md) — host/diagnostic command
