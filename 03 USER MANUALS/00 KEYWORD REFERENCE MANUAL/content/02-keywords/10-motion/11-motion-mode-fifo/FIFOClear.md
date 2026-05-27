---
keyword: FIFOClear
summary: Command function that empties the FIFO motion queue, discarding all entries.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`FIFOClear` empties the FIFO motion queue, discarding all queued entries in one operation. It cannot be issued while the axis is in motion. To discard a single entry rather than the whole queue, use [FIFORemove](FIFORemove.md).

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

A clear resets the queue to its initial empty state: the playback pointer returns to the first slot, the free-entry count returns to 128 (the full usable depth), and the active segment count-down, velocity and acceleration are zeroed — see the [FIFOStatus](FIFOStatus.md) elements. All stored type and value entries are cleared, so [FIFOType](FIFOType.md) and [FIFOValue](FIFOValue.md) read back as 0.

Because it discards the segment in progress, `FIFOClear` is intended for use before starting a motion or after one has ended, not during playback. To wind down a running motion gracefully, use [StopFIFO](StopFIFO.md) instead.

## Examples

```text
AFIFOClear=0         ; empty the queue (free count returns to 128)
```

## See also

- [FIFORemove](FIFORemove.md) — remove a single FIFO entry
- [FIFOStatus](FIFOStatus.md) — FIFO queue status
- [FIFOType](FIFOType.md) — full FIFO mode description
