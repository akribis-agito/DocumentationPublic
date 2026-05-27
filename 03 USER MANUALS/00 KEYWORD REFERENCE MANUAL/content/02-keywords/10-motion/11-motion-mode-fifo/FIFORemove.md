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

`FIFORemove` removes an entry from the FIFO motion queue. It is the counterpart of the `FIFOPush*` functions that fill the FIFO, and is used to discard a queued entry without executing it. To empty the entire FIFO at once, use [FIFOClear](FIFOClear.md).

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
AFIFORemove=0        ; remove an entry from the FIFO
```

## See also

- [FIFOClear](FIFOClear.md) — empty the entire FIFO
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
- [FIFOType](FIFOType.md) — full FIFO mode description
