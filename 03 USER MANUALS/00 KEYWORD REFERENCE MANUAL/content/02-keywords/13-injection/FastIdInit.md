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

## Examples

```text
AFastIdInit          ; reset the PRBS sequence index
```

## See also

- [InjectType](InjectType.md) — selects the PRBS waveform
- [FastIdDownSam](FastIdDownSam.md) — PRBS generation downsampling factor (not reset by FastIdInit)
