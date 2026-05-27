---
keyword: FIFOValue
summary: Read-only array reporting the data value paired with each FIFO motion entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 280
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 129
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
# FIFOValue

Read-only array reporting the data value paired with each FIFO motion entry.

## Overview

`FIFOValue` reports the data value associated with each entry currently held in the FIFO motion queue. Each FIFO entry consists of a type, reported by [FIFOType](FIFOType.md), and a value, reported here. Together these two arrays describe the contents of the FIFO used by FIFO motion mode.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## Examples

```text
AFIFOValue[1]       ; query the value of the first FIFO entry
```

## See also

- [FIFOType](FIFOType.md) — type paired with each FIFO entry value; full FIFO mode description
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
