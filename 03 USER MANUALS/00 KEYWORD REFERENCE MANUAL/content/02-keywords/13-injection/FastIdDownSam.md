---
keyword: FastIdDownSam
summary: Downsampling factor that sets the PRBS new-value generation rate.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 541
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 3
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# FastIdDownSam

Downsampling factor that sets the PRBS new-value generation rate.

## Overview

`FastIdDownSam` sets the downsampling factor for the PRBS (pseudorandom binary sequence) generation rate. It applies only when [InjectType](InjectType.md) selects PRBS injection (`InjectType = 6 or 7`). A larger value slows the rate at which new binary values are produced relative to the controller cycle rate. The PRBS sequence index can be reset with [FastIdInit](FastIdInit.md).

## How it works

$$
\text{Rate of generation of new binary value}\ [\text{Hz}] = \frac{\text{Controller cycle rate}\ [\text{Hz}]}{2^{\text{FastIdDownSam}}}
$$

Each PRBS bit is held at the output for $2^{\text{FastIdDownSam}}$ controller cycles before the next bit is taken from the sequence, so the factor stretches the sequence in time without changing its bit pattern. The allowed values give the following rates:

| Value | Controller cycles per PRBS bit |
|-------|--------------------------------|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 (default) |

For example, with `FastIdDownSam = 1`, a new binary value is produced every 2 controller cycles. Changing this factor takes effect for subsequent bits; [FastIdInit](FastIdInit.md) restarts the sequence from its first bit but leaves this factor unchanged.

## Examples

```text
AFastIdDownSam=1     ; new value every 2 controller cycles
AFastIdDownSam=3     ; new value every 8 controller cycles (default)
AFastIdDownSam      ; query the current downsampling factor
```

> **Note:** this value is not reset by PCSuite.

## See also

- [InjectType](InjectType.md) — selects the PRBS waveform
- [FastIdInit](FastIdInit.md) — resets the PRBS sequence index
