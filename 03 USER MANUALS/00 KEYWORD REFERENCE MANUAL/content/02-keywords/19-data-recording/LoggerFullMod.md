---
keyword: LoggerFullMod
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 533
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
# LoggerFullMod

**Definition:**

LoggerFullMod sets the behavior of the continuous data logger when its buffer becomes full, selecting between overwrite (circular) or stop modes. It is a non-axis parameter saved to flash and can be changed at any time.

**See also:**

[LoggerOn](LoggerOn.md), [LoggerStatus](LoggerStatus.md), [LoggerGap](LoggerGap.md)
