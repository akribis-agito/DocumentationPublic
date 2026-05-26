---
keyword: LoggerGap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 531
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
  - 1
  - 1000000
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
---
# LoggerGap

**Definition:**

LoggerGap sets the sampling interval of the continuous data logger in servo cycles, controlling how frequently data is captured relative to the control loop rate. It is a non-axis parameter saved to flash and can be changed at any time.

**See also:**

[LoggerOn](LoggerOn.md), [LoggerParams](LoggerParams.md), [LoggerFullMod](LoggerFullMod.md)
