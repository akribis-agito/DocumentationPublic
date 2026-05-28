---
keyword: PeakTime
summary: Maximum time allowed at peak current; sets the I²t time constant.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 53
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
  - 1
  - 3000
  default: 500
  scaling: 1.0
  implemented: final
overrides: {}
---
# PeakTime

Maximum time allowed at peak current; sets the I²t time constant.

## Overview

`PeakTime` defines, in **milliseconds**, the time the drive may sustain a step from zero up to the peak current ([PeakCL](PeakCL.md)) before the I²t limitation engages. Together with [ContCL](ContCL.md) and [PeakCL](PeakCL.md) it sets the time constant τ of the I²t protection.

## How it works

The firmware solves for the filter time constant so that a worst-case step to `PeakCL` reaches the continuous threshold `ContCL²` after exactly `PeakTime`:

$$
\frac{1}{\tau} = \frac{\ln\!\left(1 - \dfrac{ContCL^{2}}{PeakCL^{2}}\right)}{-\,PeakTime \times 0.001}
$$

A larger `PeakTime` gives a longer τ — the motor is allowed to dwell at peak current for longer before the limitation (or trip) occurs. See [ContCL](ContCL.md) for the full mechanism.

![I-squared filtered response charging from zero toward PeakCL squared and reaching ContCL squared exactly at PeakTime; the engage and release thresholds are marked](i2t-curve.svg)

> **Worked example:** with `ContCL = 2000` mA, `PeakCL = 4000` mA and `PeakTime = 1000` ms, the firmware sets τ so that a step from zero to 4 A reaches the `ContCL²` threshold after exactly 1 s. If `MotorCurr` is held at 4 A from `t = 0`, the I²t limitation engages at `t ≈ 1 s` and clamps the command to `ContCL`. The limit releases once `I²_filt` drops below `0.90 × ContCL²` (10 % hysteresis).

> **Note (Central-i):** for some remote amplifier sub-types the firmware clamps `PeakTime` to 1500 ms internally.

If the motor's trip time is rated at a trip current different from the peak current, compute the equivalent peak-current time from the motor's trip-curve formula before setting `PeakTime`.

## Examples

```text
APeakTime=500        ; 500 ms allowed at peak current
```

## See also

- [ContCL](ContCL.md) — continuous current limit (and I²t diagram)
- [PeakCL](PeakCL.md) — peak current limit
