---
keyword: FIFOPosTrgt
summary: Target position carried by the next FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 661
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
# FIFOPosTrgt

Target position carried by the next FIFO position segment.

## Overview

`FIFOPosTrgt` holds the target position for the FIFO position-tracking subsystem. Its value is taken as the segment data when [FIFOPosPush](FIFOPosPush.md) pushes a new position segment into the queue. The position can be shifted globally with [FIFOPosPosOf](FIFOPosPosOf.md). It is not saved to flash and can be changed at any time.

## Examples

```text
FIFOPosTrgt=100000  ; set the target position for the next FIFOPosPush
```

## See also

- [FIFOPosPush](FIFOPosPush.md) — push the segment using this target
- [FIFOPosPosOf](FIFOPosPosOf.md) — global position offset
- [FIFOPosStatus](FIFOPosStatus.md) — queue status
