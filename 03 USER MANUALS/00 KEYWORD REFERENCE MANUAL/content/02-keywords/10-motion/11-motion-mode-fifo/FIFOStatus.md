---
keyword: FIFOStatus
summary: Read-only array reporting the status of the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 282
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOStatus

Read-only array reporting the status of the FIFO motion queue.

## Overview

`FIFOStatus` is a read-only array that reports the current state of the FIFO motion queue, such as how many entries it holds and whether it is empty or full. It is used to monitor the FIFO while pushing segments with the `FIFOPush*` functions and while executing FIFO motion.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

> **Documentation pending:** The meaning of each individual element of the `FIFOStatus` array was not available in the source reference. Verify element assignments against current firmware before relying on specific indices.

## Examples

```text
FIFOStatus[1]?      ; query the first status element
```

## See also

- [FIFOType](FIFOType.md) — full FIFO mode description
- [FIFOValue](FIFOValue.md) — value of each FIFO entry
- [StopFIFO](StopFIFO.md) — end the current segment as the last one
