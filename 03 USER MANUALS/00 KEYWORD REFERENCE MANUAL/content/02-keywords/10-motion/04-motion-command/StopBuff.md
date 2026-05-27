---
keyword: StopBuff
summary: Stops spline-buffer (Buff) motion, halting playback and decelerating to rest.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 550
attributes:
  access: ro
  scope: axis
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
# StopBuff

Stops spline-buffer (Buff) motion, halting playback and decelerating to rest.

## Overview

`StopBuff` is a command that stops motion in spline-buffer (Buff) mode: it halts the spline playback and decelerates the axis to rest. It is the buffer-mode counterpart to the general [Stop](Stop.md) command. The buffer playback state can be observed through [BuffStatus](../12-motion-mode-spline-buffer/BuffStatus.md). It can be issued during motion. It is an axis-related command function.

## Examples

```text
StopBuff            ; stop spline-buffer playback
```

## See also

- [Stop](Stop.md) — general controlled stop
- [BuffStatus](../12-motion-mode-spline-buffer/BuffStatus.md) — spline-buffer playback status
