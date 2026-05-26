---
keyword: StopBuff
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

**Definition:**

StopBuff is a command that stops motion in spline-buffer (Buff) mode. It halts the spline playback and decelerates the axis to rest. It is an axis-related command function that can be issued during motion.

**See also:**

[Stop](Stop.md), [BuffStatus](../12-motion-mode-spline-buffer/BuffStatus.md)
