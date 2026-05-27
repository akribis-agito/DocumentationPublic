---
keyword: LoggerFullMod
summary: Selects logger behavior when its buffer fills (overwrite or stop).
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

Selects logger behavior when its buffer fills (overwrite or stop).

## Overview

`LoggerFullMod` sets the behavior of the continuous data logger when its buffer becomes full, selecting between an overwrite (circular) mode and a stop mode. This determines whether long-running logging keeps the most recent samples or freezes at the first full buffer. It is a non-axis parameter saved to flash and can be changed at any time. It works together with [LoggerOn](LoggerOn.md), [LoggerGap](LoggerGap.md), and is observed through [LoggerStatus](LoggerStatus.md).

> **Documentation pending:** the mapping of the two values (range `0`–`1`) to the overwrite/circular and stop modes is not specified in the source material.

## Examples

```text
LoggerFullMod?      ; query the current buffer-full mode
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerStatus](LoggerStatus.md) — logger run state and buffer fill
- [LoggerGap](LoggerGap.md) — logger sampling interval
