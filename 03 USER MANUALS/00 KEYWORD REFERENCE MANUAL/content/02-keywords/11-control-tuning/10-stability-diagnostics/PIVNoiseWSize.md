---
keyword: PIVNoiseWSize
summary: "Length, in milliseconds, of the sliding window over which the PIV noise statistic is computed."
availability:
  standalone: []
  central-i:
  - v5
can_code: 800
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# PIVNoiseWSize

Length, in milliseconds, of the sliding window over which the PIV noise statistic is computed.

## Overview

`PIVNoiseWSize` sets how long a window of recent samples the PIV noise detector ([PIVNoiseDtct](PIVNoiseDtct.md)) averages over when measuring the spread of the current reference at standstill. It is specified in milliseconds. A longer window smooths the statistic and rejects brief transients, at the cost of slower response to a sustained noise problem; a shorter window reacts faster but is noisier itself.

The window length is given in milliseconds and is internally clamped to the range the controller supports; values from about 5 ms to 125 ms are accepted, with 30 ms a typical setting. The detector also requires the axis to remain at a commanded standstill for somewhat longer than one window before it acts on the statistic, so longer windows lengthen the settling time the axis must observe before noise can be reported.

This keyword is available from v5 (central-i) only.

## How it works

The controller converts the millisecond value into a sample count at the control-loop rate and uses it as the length of the sliding window for the spread (variance) computation. The resulting count is clamped to the controller's supported window size, so very small or very large millisecond values are limited to the usable range rather than rejected.

Because changing the window size resizes the internal buffer, this keyword cannot be changed while the axis is in motion or while the motor is on. Set it before enabling the detector. It is saved to flash.

## Examples

```text
APIVNoiseWSize=30     ; 30 ms window (typical)
APIVNoiseWSize=125    ; longest window: smoothest statistic, slowest to react
APIVNoiseWSize[1]     ; read back the configured window length in ms
```

## See also

- [PIVNoiseDtct](PIVNoiseDtct.md) — enable the PIV noise detector
- [PIVNoiseSTD](PIVNoiseSTD.md) — PIV noise spread threshold
- [PIVNoiseStat](PIVNoiseStat.md) — PIV noise detector status array
