---
keyword: FastIdInit
summary: Resets the PRBS sequence index to the first pre-defined binary value.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 540
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
# FastIdInit

Resets the PRBS sequence index to the first pre-defined binary value.

## Overview

`FastIdInit` resets the PRBS (pseudorandom binary sequence) index back to the first pre-defined binary value, so injection restarts from the beginning of the sequence. It applies only when [InjectType](InjectType.md) selects PRBS injection (`InjectType = 6 or 7`). It does not reset the PRBS downsampling factor [FastIdDownSam](FastIdDownSam.md).

## How it works

The PRBS waveform is read from a fixed table of 8192 bits (a maximal-length sequence). The controller walks this table one bit at a time, taking the most-significant bit of the current 16-bit word first and stepping down to the least-significant bit before advancing to the next word. `FastIdInit` returns this read position to the very first bit (the most-significant bit of the first word) and clears the downsampling counter, so the next PRBS injection produces exactly the same bit pattern from the start. Issuing it lets repeated identification runs use an identical excitation, which is required when their results are to be compared or averaged. The downsampling factor [FastIdDownSam](FastIdDownSam.md), which sets how fast the table is consumed, is left unchanged.

## Examples

```text
AFastIdInit          ; reset the PRBS sequence index
```

## See also

- [InjectType](InjectType.md) — selects the PRBS waveform
- [FastIdDownSam](FastIdDownSam.md) — PRBS generation downsampling factor (not reset by FastIdInit)
