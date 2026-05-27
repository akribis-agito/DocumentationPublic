---
keyword: FIFORemove
summary: Command function that removes the last entry pushed into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 289
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
# FIFORemove

Command function that removes the last entry pushed into the FIFO motion queue.

## Overview

`FIFORemove` removes the most recently pushed entry from the tail of the FIFO motion queue — the last entry added by a `FIFOPush*` function. It is used to discard a queued entry before it is played, without disturbing the rest of the queue. To empty the entire queue at once, use [FIFOClear](FIFOClear.md). Unlike `FIFOClear`, `FIFORemove` may be issued during FIFO motion.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

A remove frees one entry at the tail of the queue, incrementing the free-entry count reported by [FIFOStatus](FIFOStatus.md) (index 2). It has no effect if the queue is already empty.

During an active FIFO motion the entry currently being played cannot be removed: if only that one segment remains queued, the remove is ignored. This protects the segment in progress. When the axis is not running a FIFO motion, the tail entry is removed as long as the queue holds at least one entry.

## Examples

```text
AFIFORemove=0        ; discard the most recently pushed entry
```

## See also

- [FIFOClear](FIFOClear.md) — empty the entire FIFO
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
- [FIFOType](FIFOType.md) — full FIFO mode description
