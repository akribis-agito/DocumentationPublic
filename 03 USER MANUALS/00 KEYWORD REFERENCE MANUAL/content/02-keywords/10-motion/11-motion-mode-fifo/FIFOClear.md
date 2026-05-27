---
keyword: FIFOClear
summary: Command function that empties the FIFO motion queue, discarding all entries.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 290
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# FIFOClear

Command function that empties the FIFO motion queue, discarding all entries.

## Overview

`FIFOClear` empties the FIFO motion queue, discarding all queued entries. It cannot be issued while the axis is in motion. To remove a single entry rather than the whole queue, use [FIFORemove](FIFORemove.md).

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
AFIFOClear=0         ; empty the FIFO queue
```

## See also

- [FIFORemove](FIFORemove.md) — remove a single FIFO entry
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
- [FIFOType](FIFOType.md) — full FIFO mode description
